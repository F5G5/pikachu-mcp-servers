#!/bin/bash
# Pikachu MCP Servers 一键安装脚本

set -e

echo "⚡ 皮卡丘MCP服务器一键安装"
echo "================================"

# 检测操作系统
OS="$(uname -s)"
if [[ "$OS" == "Darwin" ]]; then
    echo "检测到: macOS"
    PYTHON="python3"
elif [[ "$OS" == "Linux" ]]; then
    echo "检测到: Linux"
    PYTHON="python3"
else
    echo "检测到: Windows (使用PowerShell)"
    PYTHON="python"
fi

# 检查Python
if ! command -v $PYTHON &> /dev/null; then
    echo "❌ 未找到Python，请先安装Python 3.10+"
    exit 1
fi

echo "✅ Python版本: $($PYTHON --version)"

# 检查pip
if ! $PYTHON -m pip --version &> /dev/null; then
    echo "📦 安装pip..."
    $PYTHON -m ensurepip --default-pip
fi

# 安装FastMCP
echo "📦 安装FastMCP..."
$PYTHON -m pip install fastmcp -q

echo "✅ 安装完成！"
echo ""
echo "================================"
echo "📋 下一步：配置到OpenClaw"
echo "================================"
echo ""
echo "1. 打开 OpenClaw 配置文件"
echo "   Linux/Mac: ~/.openclaw/openclaw.json"
echo "   Windows: %USERPROFILE%\\.openclaw\\openclaw.json"
echo ""
echo '2. 在 "mcp": { "servers": {} } 中添加:'
echo ''
cat << 'EOF'
{
  "mcp": {
    "servers": {
      "pikachu-weather": {
        "command": "python",
        "args": ["/path/to/weather_server.py"]
      },
      "pikachu-news": {
        "command": "python",
        "args": ["/path/to/news_server.py"]
      }
    }
  }
}
EOF
echo ""
echo "3. 重启OpenClaw"
echo ""
echo "================================"
echo "🎉 享受皮卡丘的服务吧！"
echo "================================"
