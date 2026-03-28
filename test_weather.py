"""测试天气Server"""
import subprocess
import json
import sys
import os

def test_server(script_name, tool_name, params):
    proc = subprocess.Popen(
        [sys.executable, script_name],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=r"C:\Users\Administrator\.openclaw\workspace\mcp-servers",
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

    output = proc.stdout.read().decode('utf-8', errors='replace')
    proc.wait(timeout=10)
    return output

# 测试天气查询
print("=" * 50)
print("Test: get_current_weather(Beijing)")
print("=" * 50)
result = test_server("weather_server.py", "get_current_weather", {"city": "Beijing"})
print(result[:800])

print("\n" + "=" * 50)
print("Test: get_weather_forecast(Shanghai, 3)")
print("=" * 50)
result = test_server("weather_server.py", "get_weather_forecast", {"city": "Shanghai", "days": 3})
print(result[:800])
