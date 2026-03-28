# Pikachu MCP Servers 一键安装脚本 (Windows PowerShell)

Write-Host "⚡ 皮卡丘MCP服务器一键安装" -ForegroundColor Yellow
Write-Host "================================" -ForegroundColor Yellow

# 检查Python
$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonCmd) {
    $pythonCmd = Get-Command python3 -ErrorAction SilentlyContinue
}
if (-not $pythonCmd) {
    Write-Host "❌ 未找到Python，请先安装Python 3.10+" -ForegroundColor Red
    Write-Host "下载地址: https://www.python.org/downloads/" -ForegroundColor Cyan
    exit 1
}

Write-Host "✅ Python版本: $(python --version)" -ForegroundColor Green

# 安装FastMCP
Write-Host "📦 安装FastMCP..." -ForegroundColor Cyan
python -m pip install fastmcp -q

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ 安装完成！" -ForegroundColor Green
} else {
    Write-Host "❌ 安装失败，请手动运行: python -m pip install fastmcp" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "================================" -ForegroundColor Yellow
Write-Host "📋 下一步：配置到OpenClaw" -ForegroundColor Yellow
Write-Host "================================" -ForegroundColor Yellow
Write-Host ""
Write-Host "1. 打开配置文件:" -ForegroundColor White
Write-Host "   $env:USERPROFILE\.openclaw\openclaw.json" -ForegroundColor Gray
Write-Host ""
Write-Host '2. 在 "mcp": { "servers": {} } 中添加:' -ForegroundColor White
Write-Host ""

$configJson = @'
{
  "mcp": {
    "servers": {
      "pikachu-weather": {
        "command": "python",
        "args": ["C:/path/to/weather_server.py"],
        "cwd": "C:/path/to"
      },
      "pikachu-news": {
        "command": "python",
        "args": ["C:/path/to/news_server.py"],
        "cwd": "C:/path/to"
      }
    }
  }
}
'@
Write-Host $configJson -ForegroundColor Gray
Write-Host ""
Write-Host "3. 重启OpenClaw" -ForegroundColor White
Write-Host ""
Write-Host "================================" -ForegroundColor Yellow
Write-Host "🎉 享受皮卡丘的服务吧！" -ForegroundColor Yellow
Write-Host "================================" -ForegroundColor Yellow
