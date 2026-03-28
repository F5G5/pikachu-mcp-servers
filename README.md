# ⚡ Pikachu MCP Servers

> 皮卡丘的MCP服务器集合 - 让AI连接真实世界！⚡

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![FastMCP](https://img.shields.io/badge/FastMCP-3.1.1-green.svg)](https://gofastmcp.com/)

## 🎯 简介

这是一个开源的MCP (Model Context Protocol) 服务器集合，提供实用工具服务。快速让AI助手获得连接外部世界的能力！

**特点：**
- 🔌 真实API集成（天气、新闻、搜索）
- 🛠️ 开箱即用，无需API Key
- 📝 代码简洁，易于学习和二次开发
- 🚀 支持OpenClaw、Claude Desktop等MCP客户端

## 📦 服务器列表

### 🌤️ pikachu-weather (天气服务器) 
连接真实天气API

| 工具 | 功能 | 数据来源 |
|:---|:---|:---|
| `get_current_weather(city)` | 实时天气 | wttr.in |
| `get_weather_forecast(city, days)` | 天气预报 | wttr.in |
| `get_air_quality(city)` | 空气质量 | 内置数据 |
| `calculate(a, b, operation)` | 计算器 | 代码实现 |
| `currency_converter(amount, from, to)` | 货币换算 | open.er-api.com |
| `get_news(keyword)` | 最新新闻 | 模拟数据 |
| `world_time(city)` | 世界时间 | 系统时区 |

### 📰 pikachu-news (新闻服务器)
实时获取全网热点新闻

| 工具 | 功能 | 数据来源 |
|:---|:---|:---|
| `get_tech_news()` | 科技新闻 | Hacker News API |
| `get_zhihu_hot()` | 知乎热榜 | 知乎API |
| `get_douyin_hot()` | 抖音热榜 | 模拟数据 |
| `get_weibo_hot()` | 微博热榜 | 微博API |
| `search_news(keyword, limit)` | 新闻搜索 | DuckDuckGo |

### 🔍 pikachu-search (搜索服务器)
多功能搜索与查询

| 工具 | 功能 | 数据来源 |
|:---|:---|:---|
| `web_search(query, num_results)` | 网页搜索 | DuckDuckGo |
| `wikipedia_lookup(keyword)` | 维基百科 | Wikipedia API |
| `github_search(keyword)` | GitHub仓库 | 模拟数据 |
| `unit_converter(value, from, to)` | 单位换算 | 内置算法 |
| `quick_math(expression)` | 数学计算 | Python eval |

### 🧮 pikachu-first (基础服务器)
基础工具集合

| 工具 | 功能 |
|:---|:---|
| `add(a, b)` | 加法 |
| `subtract(a, b)` | 减法 |
| `multiply(a, b)` | 乘法 |
| `divide(a, b)` | 除法 |
| `get_weather(city)` | 天气查询 |
| `reverse_text(text)` | 反转文字 |
| `count_words(text)` | 统计字数 |

## 🚀 快速开始

### 前置要求
- Python 3.10+
- FastMCP

### 安装依赖

```bash
# 克隆仓库
git clone https://github.com/F5G5/pikachu-mcp-servers.git
cd pikachu-mcp-servers

# 安装FastMCP
pip install fastmcp

# 或使用uv（推荐）
uv pip install fastmcp --system
```

### 配置到 OpenClaw

在 `openclaw.json` 中添加:

```json
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
      },
      "pikachu-search": {
        "command": "python",
        "args": ["/path/to/search_server.py"]
      }
    }
  }
}
```

### 配置到 Claude Desktop

在 `~/.claude_desktop_config.json` 中添加:

```json
{
  "mcpServers": {
    "pikachu-weather": {
      "command": "python",
      "args": ["/absolute/path/to/weather_server.py"]
    }
  }
}
```

## 📖 使用示例

```
你: 查一下北京现在的天气
AI: [调用 get_current_weather] -> 北京当前晴，25°C

你: 获取最新科技新闻
AI: [调用 get_tech_news] -> Hacker News TOP 10

你: 搜索"Python教程"
AI: [调用 web_search] -> 相关结果列表
```

## 🛠️ 开发自己的MCP Server

### 基础模板

```python
from fastmcp import FastMCP

mcp = FastMCP("我的Server")

@mcp.tool()
def my_tool(param: str) -> str:
    """工具描述"""
    # 你的逻辑
    return result

if __name__ == "__main__":
    mcp.run()
```

### 关键注解

```python
@mcp.tool(
    annotations={
        "readOnlyHint": True,      # 只读操作
        "idempotentHint": True,    # 幂等操作
        "destructiveHint": False,   # 非破坏性
    }
)
```

## 📂 项目结构

```
pikachu-mcp-servers/
├── README.md              # 本文件
├── weather_server.py      # 天气服务
├── news_server.py         # 新闻服务
├── search_server.py       # 搜索服务
├── my_first_server.py     # 基础工具
└── test_*.py              # 测试脚本
```

## 🤝 贡献

欢迎提交Issue和Pull Request！

1. Fork 本仓库
2. 创建新分支 (`git checkout -b feature/amazing`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送分支 (`git push origin feature/amazing`)
5. 创建Pull Request

## 📄 许可证

MIT License - 随意使用，但请保留署名！

## 🙏 支持

如果对你有帮助，请:
- ⭐ Star 这个项目
- 🐛 提交Bug
- 📢 分享给需要的人

---

**皮卡皮卡～⚡ 让AI连接真实世界！**
