# ⚡ Pikachu MCP Servers

> 让AI连接真实世界 - 开源MCP工具集合！⚡

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![FastMCP](https://img.shields.io/badge/FastMCP-3.1.1-green.svg)](https://gofastmcp.com/)
[![Stars](https://img.shields.io/github/stars/F5G5/pikachu-mcp-servers?style=social)](https://github.com/F5G5/pikachu-mcp-servers)

> 🎯 **14个MCP服务器** | **70+工具** | **MIT开源**

---

## 🚀 快速开始

```bash
# 克隆仓库
git clone https://github.com/F5G5/pikachu-mcp-servers.git
cd pikachu-mcp-servers

# 安装依赖
pip install fastmcp

# 配置到OpenClaw - 在openclaw.json添加配置
openclaw gateway restart
```

---

## 📦 服务器列表

### 🌤️ 天气服务
| 工具 | 功能 |
|:---|:---|
| `get_current_weather(city)` | 实时天气 |
| `get_weather_forecast(city, days)` | 天气预报 |
| `get_air_quality(city)` | 空气质量 |
| `calculate(a, b, op)` | 计算器 |
| `currency_converter(amount, from, to)` | 货币换算 |
| `world_time(city)` | 世界时间 |

### 📰 新闻服务
| 工具 | 功能 |
|:---|:---|
| `get_tech_news()` | 科技新闻 |
| `get_zhihu_hot()` | 知乎热榜 |
| `get_douyin_hot()` | 抖音热榜 |
| `get_weibo_hot()` | 微博热榜 |
| `search_news(keyword, limit)` | 新闻搜索 |

### 🔍 搜索服务
| 工具 | 功能 |
|:---|:---|
| `web_search(query, num)` | 网页搜索 |
| `wikipedia_lookup(keyword)` | 维基百科 |
| `github_search(keyword)` | GitHub仓库 |
| `unit_converter(v, from, to)` | 单位换算 |
| `quick_math(expression)` | 数学计算 |

### 📱 社交媒体
| 工具 | 功能 |
|:---|:---|
| `generate_social_content(platform, topic, tone)` | 内容生成 |
| `hashtag_generator(keywords, count)` | 标签生成 |
| `thread_generator(topic, style, sections)` | 长文生成 |
| `emoji_fy(text)` | Emoji美化 |

### ⏰ 效率工具
| 工具 | 功能 |
|:---|:---|
| `pomodoro_timer(minutes)` | 番茄钟 |
| `task_planner(tasks, hours)` | 任务规划 |
| `daily_review()` | 每日复盘 |
| `weekly_planner()` | 周计划 |
| `focus_session(work, break)` | 专注时段 |
| `quick_break(type)` | 快速休息 |

### 💻 开发工具
| 工具 | 功能 |
|:---|:---|
| `json_formatter(json)` | JSON格式化 |
| `json_minifier(json)` | JSON压缩 |
| `url_encoder(text)` | URL编码 |
| `base64_tool(text, op)` | Base64 |
| `hash_generator(text, algo)` | Hash生成 |
| `regex_tester(pattern, string)` | 正则测试 |
| `color_converter(color)` | 颜色转换 |
| `timestamp_converter(ts, type)` | 时间戳 |
| `http_status_check(code)` | HTTP状态码 |

---

## 📊 Pro版服务器 (付费)

完整Pro版仓库: [github.com/F5G5/pikachu-mcp-pro](https://github.com/F5G5/pikachu-mcp-pro)

### 🗄️ 数据库
| 工具 | 功能 |
|:---|:---|
| `sqlite_connect(db_path)` | 连接SQLite |
| `sqlite_execute(query)` | 执行SQL |
| `sqlite_create_table(name, columns)` | 创建表 |
| `sqlite_insert(table, data)` | 插入数据 |
| `csv_to_sqlite(csv, table)` | CSV导入 |
| `export_to_csv(query, output)` | 导出CSV |

### 📧 邮件服务
| 工具 | 功能 |
|:---|:---|
| `configure_email(host, port, user, pass)` | 配置SMTP |
| `send_email(to, subject, body)` | 发送邮件 |
| `send_html_email(to, subject, html)` | HTML邮件 |
| `send_email_template(to, tmpl, data)` | 模板邮件 |
| `batch_send_email(recipients, subject, body)` | 批量发送 |

### 🤖 AI服务
| 工具 | 功能 |
|:---|:---|
| `configure_ai(openai, anthropic, gemini)` | 配置AI密钥 |
| `ai_chat(model, message, system)` | AI对话 |
| `ai_translate(text, target, source)` | AI翻译 |
| `ai_summarize(text, max_length)` | AI摘要 |
| `ai_code_review(code, language)` | 代码审查 |
| `ai_sentiment(text)` | 情感分析 |

### 📁 文件处理
| 工具 | 功能 |
|:---|:---|
| `read_csv(file_path, max_rows)` | 读取CSV |
| `write_csv(file, data, columns)` | 写入CSV |
| `append_csv(file, row)` | 追加CSV |
| `csv_stats(file)` | CSV统计 |
| `filter_csv(file, condition)` | CSV筛选 |
| `csv_to_json(csv, output)` | CSV转JSON |
| `json_to_csv(json, output)` | JSON转CSV |

### ☁️ 云服务
| 工具 | 功能 |
|:---|:---|
| `ping(url)` | URL连通性 |
| `http_request(method, url, headers, body)` | HTTP请求 |
| `download_file(url, path)` | 下载文件 |
| `upload_to_url(file, url)` | 上传文件 |
| `register_webhook(name, url, secret)` | 注册Webhook |
| `trigger_webhook(hook_id, payload)` | 触发Webhook |
| `url_shorten(long_url)` | 短链接 |
| `check_health(url)` | 健康检查 |

### 📈 系统监控
| 工具 | 功能 |
|:---|:---|
| `system_info()` | 系统信息 |
| `cpu_info()` | CPU详情 |
| `memory_info()` | 内存详情 |
| `disk_info()` | 磁盘信息 |
| `network_info()` | 网络信息 |
| `process_list(top)` | 进程列表 |
| `battery_info()` | 电池信息 |
| `service_status(name)` | 服务状态 |

---

## 📊 工具统计

| 类型 | 免费版 | Pro版 | 总计 |
|:---|:---:|:---:|:---:|
| 天气/环境 | 6 | - | 6 |
| 新闻/内容 | 5 | - | 5 |
| 社交媒体 | 4 | - | 4 |
| 效率工具 | 6 | - | 6 |
| 开发工具 | 9 | - | 9 |
| 数据库 | - | 9 | 9 |
| 邮件 | - | 6 | 6 |
| AI | - | 7 | 7 |
| 文件处理 | - | 10 | 10 |
| 云服务 | - | 8 | 8 |
| 系统监控 | - | 8 | 8 |
| **总计** | **30** | **48** | **78+** |

---

## 🎯 使用示例

```
你: 查一下北京天气
AI: 调用 get_current_weather("北京")

你: 帮我写Twitter推广AI工具
AI: 调用 generate_social_content("twitter", "AI工具")

你: 分析这个CSV文件
AI: 调用 read_csv("data.csv")

你: 系统性能怎么样
AI: 调用 system_info() + cpu_info() + memory_info()

你: 发送邮件给test@example.com
AI: 调用 configure_email + send_email
```

---

## 📂 项目结构

```
pikachu-mcp-servers/          # 免费版 (MIT)
├── weather_server.py
├── news_server.py
├── search_server.py
├── social_server.py
├── productivity_server.py
├── devtools_server.py
├── my_first_server.py
└── README.md

pikachu-mcp-pro/             # Pro版 ($9.9/月)
├── database_server.py
├── email_server.py
├── ai_server.py
├── file_server.py
├── cloud_server.py
├── monitor_server.py
├── pro_server.py
└── README.md
```

---

## 💰 价格

| 版本 | 价格 | 服务器 | 工具 |
|:---|:---:|:---:|:---:|
| 免费版 | $0 | 7个 | 30+ |
| Pro版 | $9.9/月 | 全部14个 | 78+ |

**获取Pro版**: [爱发电](https://afdian.net/@pikachu_mcp) | [GitHub Sponsors](https://github.com/sponsors/F5G5)

---

## 🤝 贡献

欢迎提交Issue和PR！

---

## 📄 许可证

MIT License

---

**GitHub**: https://github.com/F5G5/pikachu-mcp-servers
**Pro版**: https://github.com/F5G5/pikachu-mcp-pro

*皮卡皮卡～⚡ 让AI更强大！*
