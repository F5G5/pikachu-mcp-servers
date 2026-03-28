#!/usr/bin/env python3
"""快速测试MCP Server"""
import subprocess
import json
import sys

def test_mcp():
    proc = subprocess.Popen(
        [sys.executable, "my_first_server.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=r"C:\Users\Administrator\.openclaw\workspace\mcp-servers"
    )
    
    # MCP初始化
    init_msg = json.dumps({
        "jsonrpc": "2.0",
        "id": 0,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "test", "version": "1.0.0"}
        }
    }) + "\n"
    
    notif_msg = json.dumps({
        "jsonrpc": "2.0",
        "method": "notifications/initialized",
        "params": {}
    }) + "\n"
    
    list_msg = json.dumps({
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/list"
    }) + "\n"
    
    # 发送消息
    proc.stdin.write(init_msg.encode())
    proc.stdin.write(notif_msg.encode())
    proc.stdin.write(list_msg.encode())
    proc.stdin.close()
    
    # 读取响应
    output = proc.stdout.read().decode('utf-8', errors='replace')
    proc.wait(timeout=5)
    
    return output

if __name__ == "__main__":
    print("Testing MCP Server...")
    result = test_mcp()
    
    # 解析JSON响应
    lines = result.strip().split('\n')
    for line in lines:
        try:
            data = json.loads(line)
            if 'result' in data and 'tools' in data['result']:
                tools = data['result']['tools']
                print(f"\nOK Server响应正常!")
                print(f"发现 {len(tools)} 个工具：")
                for t in tools:
                    print(f"  - {t['name']}: {t['description']}")
                break
        except json.JSONDecodeError:
            continue
    else:
        print(f"响应内容：{result[:500]}")
