"""Test all MCP Servers"""
import subprocess
import json
import sys
import os

def test_server(script_path, tool_name, params, timeout=15):
    try:
        proc = subprocess.Popen(
            [sys.executable, script_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=os.path.dirname(script_path),
            env={**os.environ, 'PYTHONIOENCODING': 'utf-8'}
        )
        
        messages = [
            {"jsonrpc": "2.0", "id": 0, "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "test", "version": "1.0.0"}}},
            {"jsonrpc": "2.0", "method": "notifications/initialized", "params": {}},
            {"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {"name": tool_name, "arguments": params}}
        ]
        
        for msg in messages:
            proc.stdin.write((json.dumps(msg) + "\n").encode('utf-8'))
            proc.stdin.flush()
        proc.stdin.close()
        
        stdout, _ = proc.communicate(timeout=timeout)
        output = stdout.decode('utf-8', errors='replace')
        
        for line in output.strip().split('\n'):
            try:
                resp = json.loads(line)
                if 'result' in resp:
                    return "PASS", resp['result']
                if 'error' in resp:
                    return "ERROR", str(resp['error'])
            except:
                continue
        return "NO_RESULT", output[:200]
        
    except subprocess.TimeoutExpired:
        proc.kill()
        return "TIMEOUT", ""
    except Exception as e:
        return "CRASH", str(e)

def list_tools(script_path):
    try:
        proc = subprocess.Popen(
            [sys.executable, script_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=os.path.dirname(script_path),
            env={**os.environ, 'PYTHONIOENCODING': 'utf-8'}
        )
        
        messages = [
            {"jsonrpc": "2.0", "id": 0, "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "test", "version": "1.0.0"}}},
            {"jsonrpc": "2.0", "method": "notifications/initialized", "params": {}},
            {"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
        ]
        
        for msg in messages:
            proc.stdin.write((json.dumps(msg) + "\n").encode('utf-8'))
            proc.stdin.flush()
        proc.stdin.close()
        
        stdout, _ = proc.communicate(timeout=10)
        
        for line in stdout.decode('utf-8', errors='replace').strip().split('\n'):
            try:
                resp = json.loads(line)
                if 'result' in resp and 'tools' in resp['result']:
                    return [t['name'] for t in resp['result']['tools']]
            except:
                continue
        return []
    except:
        return []

BASE_DIR = r"C:\Users\Administrator\.openclaw\workspace\mcp-servers"
PRO_DIR = r"C:\Users\Administrator\.openclaw\workspace\mcp-servers-pro"

servers = [
    ("my_first_server.py", BASE_DIR, [("add", {"a": 5, "b": 3})]),
    ("weather_server.py", BASE_DIR, [("get_current_weather", {"city": "Beijing"}), ("calculate", {"a": 10, "b": 5, "operation": "+"})]),
    ("news_server.py", BASE_DIR, [("get_douyin_hot", {})]),
    ("search_server.py", BASE_DIR, [("quick_math", {"expression": "2+2"})]),
    ("social_server.py", BASE_DIR, [("hashtag_generator", {"keywords": ["tech"], "count": 3})]),
    ("productivity_server.py", BASE_DIR, [("daily_review", {})]),
    ("devtools_server.py", BASE_DIR, [("hash_generator", {"text": "hello", "algorithm": "md5"})]),
]

print("=" * 60)
print("Pikachu MCP Server Test")
print("=" * 60)

results = []
for filename, dir_path, tests in servers:
    script_path = os.path.join(dir_path, filename)
    if not os.path.exists(script_path):
        print(f"\n[FILE NOT FOUND] {filename}")
        continue
    
    print(f"\n[FILE] {filename}")
    print("-" * 40)
    
    tools = list_tools(script_path)
    print(f"   Tools: {', '.join(tools[:5])}{'...' if len(tools) > 5 else ''}")
    
    for tool_name, params in tests:
        status, result = test_server(script_path, tool_name, params, timeout=10)
        print(f"   [{status}] {tool_name}")
        if status == "PASS":
            preview = str(result)[:80] if result else ""
            if preview:
                print(f"      -> {preview}...")
        results.append((filename, tool_name, status))

print("\n" + "=" * 60)
print("RESULTS SUMMARY")
print("=" * 60)

passed = sum(1 for _, _, s in results if s == "PASS")
total = len(results)

for fname, tool, status in results:
    icon = "OK" if status == "PASS" else "FAIL" if status == "CRASH" else "TMOUT" if status == "TIMEOUT" else "WARN"
    print(f"[{icon}] {fname}: {tool}")

print(f"\nPassed: {passed}/{total}")
if passed < total:
    print("Some tests failed - needs fix!")
