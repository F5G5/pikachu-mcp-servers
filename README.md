# ⚡ Pikachu MCP Servers

> 让AI连接真实世界 - 开源MCP工具集合！⚡

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![FastMCP](https://img.shields.io/badge/FastMCP-3.1.1-green.svg)](https://gofastmcp.com/)
[![Stars](https://img.shields.io/github/stars/F5G5/pikachu-mcp-servers?style=social)](https://github.com/F5G5/pikachu-mcp-servers)

> 🎯 8个MCP服务器 | 40+工具 | 完全免费开源

---

## 🚀 快速开始

```bash
# 克隆仓库
git clone https://github.com/F5G5/pikachu-mcp-servers.git
cd pikachu-mcp-servers

# 安装依赖
pip install fastmcp

# 配置到OpenClaw
# 在 openclaw.json 的 mcp.servers 中添加配置

# 重启OpenClaw
openclaw gateway restart
```

---

## 📦 服务器列表 (8个)

### 🌤️ pikachu-weather | 天气服务

| 工具 | 功能 | 数据源 |
|:---|:---|:---|
| `get_current_weather(city)` | 实时天气 | wttr.in |
| `get_weather_forecast(city, days)` | 天气预报 | wttr.in |
| `get_air_quality(city)` | 空气质量 | 内置 |
| `calculate(a, b, op)` | 计算器 | - |
| `currency_converter(amount, from, to)` | 货币换算 | open.er-api |
| `world_time(city)` | 世界时间 | 系统 |

### 📰 pikachu-news | 新闻服务

| 工具 | 功能 | 数据源 |
|:---|:---|:---|
| `get_tech_news()` | 科技新闻 | Hacker News |
| `get_zhihu_hot()` | 知乎热榜 | 知乎API |
| `get_douyin_hot()` | 抖音热榜 | 内置 |
| `get_weibo_hot()` | 微博热榜 | 微博API |
| `search_news(keyword, limit)` | 新闻搜索 | DuckDuckGo |

### 🔍 pikachu-search | 搜索服务

| 工具 | 功能 | 数据源 |
|:---|:---|:---|
| `web_search(query, num)` | 网页搜索 | DuckDuckGo |
| `wikipedia_lookup(keyword)` | 维基百科 | Wikipedia API |
| `github_search(keyword)` | GitHub仓库 | 内置 |
| `unit_converter(v, from, to)` | 单位换算 | 内置 |
| `quick_math(expression)` | 数学计算 | Python |

### 📱 pikachu-social | 社交媒体

| 工具 | 功能 |
|:---|:---|
| `generate_social_content(platform, topic, tone)` | 多平台内容生成 |
| `hashtag_generator(keywords, count)` | 热门标签 |
| `thread_generator(topic, style, sections)` | Thread长文 |
| `emoji_fy(text)` | Emoji美化 |

### ⏰ pikachu-productivity | 效率工具

| 工具 | 功能 |
|:---|:---|
| `pomodoro_timer(minutes)` | 番茄钟 |
| `task_planner(tasks, hours)` | 智能任务规划 |
| `daily_review()` | 每日复盘模板 |
| `weekly_planner()` | 周计划生成器 |
| `focus_session(work, break)` | 深度工作时段 |
| `quick_break(type)` | 快速休息建议 |

### 💻 pikachu-devtools | 开发工具

| 工具 | 功能 |
|:---|:---|
| `json_formatter(json)` | JSON格式化 |
| `json_minifier(json)` | JSON压缩 |
| `url_encoder(text)` | URL编码/解码 |
| `base64_tool(text, op)` | Base64编码/解码 |
| `hash_generator(text, algo)` | Hash生成 |
| `regex_tester(pattern, string)` | 正则测试 |
| `color_converter(color)` | 颜色转换 |
| `timestamp_converter(ts, type)` | 时间戳转换 |
| `http_status_check(code)` | HTTP状态码 |

### 🧮 pikachu-first | 基础工具

| 工具 | 功能 |
|:---|:---|
| `add(a, b)` | 加法 |
| `subtract(a, b)` | 减法 |
| `multiply(a, b)` | 乘法 |
| `divide(a, b)` | 除法 |
| `reverse_text(text)` | 反转文字 |
| `count_words(text)` | 统计字数 |

### 💎 pikachu-pro | Pro版

| 工具 | 功能 |
|:---|:---|
| `get_weather_pro(city, hourly)` | 高级天气 |
| `get_stock_price(symbol)` | 股票行情 |
| `get_crypto_price(coin)` | 加密货币 |
| `get_ai_news()` | AI行业新闻 |
| `analyze_seo(title, desc, kw)` | SEO分析 |
| `generate_password(len, special)` | 密码生成 |

---

## 📊 工具统计

| 类别 | 数量 |
|:---|---:|
| 天气/环境 | 8 |
| 新闻/内容 | 10 |
| 社交媒体 | 4 |
| 效率工具 | 6 |
| 开发工具 | 9 |
| 基础工具 | 6 |
| **总计** | **43+** |

---

## 🎯 使用示例

```
你: 查一下北京天气
AI: 调用 get_current_weather("北京") → 返回天气信息

你: 帮我写一条Twitter推广AI工具
AI: 调用 generate_social_content("twitter", "AI工具", "friendly")

你: 25分钟番茄钟
AI: 调用 pomodoro_timer(25) → 启动专注计时

你: JSON格式化
AI: 调用 json_formatter(json_string) → 格式化结果
```

---

## 📂 项目结构

```
pikachu-mcp-servers/
├── weather_server.py      # 天气服务
├── news_server.py         # 新闻服务  
├── search_server.py       # 搜索服务
├── social_server.py       # 社交媒体
├── productivity_server.py # 效率工具
├── devtools_server.py     # 开发工具
├── my_first_server.py     # 基础工具
├── pro_server.py          # Pro版
├── install.sh             # Linux/macOS安装
├── install.ps1            # Windows安装
├── TUTORIAL_ZH.md         # 中文教程
├── PROMOTION.md           # 推广文案
└── README.md              # 本文件
```

---

## 🤝 贡献

欢迎提交Issue和Pull Request！

1. Fork本仓库
2. 创建新分支
3. 提交代码
4. 发起PR

---

## 📄 许可证

MIT License - 随意使用！

---

## 🙏 支持

- ⭐ 给仓库Star
- 🐛 提交Bug
- 📢 分享给朋友

**GitHub**: https://github.com/F5G5/pikachu-mcp-servers
**Pro版**: https://github.com/F5G5/pikachu-mcp-pro

---

*皮卡皮卡～⚡ 让AI更强大！*
