# ⚡ Pikachu MCP Servers

皮卡丘的MCP服务器集合 - AI工具即服务！

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 简介

这是一个MCP (Model Context Protocol) 服务器集合，提供实用工具服务。

## 📦 服务器列表

### 🧮 pikachu-first (计算器服务器)
基础计算器 + 文字处理工具

**工具:**
- `add(a, b)` - 加法
- `subtract(a, b)` - 减法  
- `multiply(a, b)` - 乘法
- `divide(a, b)` - 除法
- `get_weather(city)` - 天气查询(模拟)
- `get_forecast(city, days)` - 天气预报(模拟)
- `reverse_text(text)` - 反转文字
- `count_words(text)` - 统计字数

### 🌤️ pikachu-weather (天气服务器)
连接真实API的天气服务

**工具:**
- `get_current_weather(city)` - 实时天气 (wttr.in API)
- `get_weather_forecast(city, days)` - 天气预报
- `get_air_quality(city)` - 空气质量
- `calculate(a, b, operation)` - 计算器
- `currency_converter(amount, from, to)` - 货币换算
- `get_news(keyword)` - 最新新闻
- `world_time(city)` - 世界时间

## 🚀 快速开始

### 前置要求
- Python 3.10+
- uv (推荐) 或 pip

### 安装

```bash
# 克隆仓库
git clone https://github.com/YOUR_USERNAME/pikachu-mcp-servers.git
cd pikachu-mcp-servers

# 安装依赖
pip install fastmcp

# 或使用uv
uv pip install fastmcp --system
```

### 配置到 Claude Desktop

在 `~/.claude.json` 中添加:

```json
{
  "mcpServers": {
    "pikachu-first": {
      "command": "python",
      "args": ["path/to/pikachu-first.py"]
    },
    "pikachu-weather": {
      "command": "python", 
      "args": ["path/to/weather_server.py"]
    }
  }
}
```

### 配置到 OpenClaw

在 `openclaw.json` 中添加:

```json
{
  "mcp": {
    "servers": {
      "pikachu-first": {
        "command": "python",
        "args": ["C:/path/to/pikachu-first.py"]
      },
      "pikachu-weather": {
        "command": "python",
        "args": ["C:/path/to/weather_server.py"]
      }
    }
  }
}
```

## 📖 使用示例

```
你: 用pikachu-weather的get_current_weather查一下北京天气
AI: [调用工具，返回北京实时天气]

你: 用calculate计算 100 + 200
AI: 100 + 200 = 300
```

## 🛠️ 开发

```bash
# 本地测试
python pikachu-first.py

# 运行测试
python test_server.py
```

## 📄 许可证

MIT License - 随意使用，但请保留署名！

## 🙏 支持

如果对你有帮助，请:
- ⭐ Star 这个项目
- �Sponsor 支持开发者
- 📢 分享给需要的人

---

皮卡皮卡～⚡
