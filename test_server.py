"""
测试我的第一个MCP Server - 正确协议版
"""
import subprocess
import json
import sys

def send_jsonrpc_messages(messages, timeout=10):
    """发送多条JSON-RPC消息"""
    proc = subprocess.Popen(
        [sys.executable, "my_first_server.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=r"C:\Users\Administrator\.openclaw\workspace\mcp-servers"
    )
    
    # 发送所有消息
    for msg in messages:
        request_json = json.dumps(msg) + "\n"
        proc.stdin.write(request_json.encode())
        proc.stdin.flush()
    
    proc.stdin.close()
    stdout = proc.stdout.read().decode()
    proc.wait(timeout=timeout)
    
    return stdout

# MCP协议需要先初始化
print("=" * 60)
print("MCP Server 测试")
print("=" * 60)

# 发送初始化 + 工具列表请求
messages = [
    # Initialize
    {
        "jsonrpc": "2.0",
        "id": 0,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "test", "version": "1.0.0"}
        }
    },
    # 通知初始化完成
    {
        "jsonrpc": "2.0",
        "method": "notifications/initialized",
        "params": {}
    },
    # 列出工具
    {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/list"
    }
]

stdout = send_jsonrpc_messages(messages)
print("Server响应:")
print(stdout[:2000])

# 测试调用工具
print("\n" + "=" * 60)
print("测试工具调用")
print("=" * 60)

messages2 = [
    # Initialize
    {
        "jsonrpc": "2.0",
        "id": 0,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "test", "version": "1.0.0"}
        }
    },
    {
        "jsonrpc": "2.0",
        "method": "notifications/initialized",
        "params": {}
    },
    # 调用add工具
    {
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/call",
        "params": {
            "name": "add",
            "arguments": {"a": 10, "b": 25}
        }
    }
]

stdout2 = send_jsonrpc_messages(messages2)
print("add(10, 25) 响应:")
print(stdout2[:2000])
