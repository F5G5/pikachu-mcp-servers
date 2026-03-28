# 🎓 皮卡丘MCP服务器 - 零基础入门教程

> 从零开始，5分钟学会使用MCP服务器！⚡

## 📚 目录

1. [什么是MCP？](#什么是mcp)
2. [为什么需要MCP服务器？](#为什么需要mcp服务器)
3. [准备工作](#准备工作)
4. [安装步骤](#安装步骤)
5. [配置OpenClaw](#配置openclaw)
6. [使用方法](#使用方法)
7. [常见问题](#常见问题)

---

## 🤔 什么是MCP？

**MCP = Model Context Protocol（模型上下文协议）**

简单来说，MCP就是AI的"USB接口"！就像USB让电脑连接各种设备一样，MCP让AI连接各种外部工具和数据。

```
传统AI:
你 → AI（只能回答，不能做事）

MCP加持:
你 → AI → MCP服务器 → 真实世界（天气、新闻、搜索...）
```

## 💡 为什么需要MCP服务器？

| 能力 | 没有MCP | 有MCP |
|:---|:---:|:---:|
| 查天气 | ❌ | ✅ |
| 搜新闻 | ❌ | ✅ |
| 搜索网页 | ❌ | ✅ |
| 股票行情 | ❌ | ✅ |
| 单位换算 | ❌ | ✅ |

---

## 🛠️ 准备工作

### 需要什么？

1. **Python 3.10+**
   - 下载: https://www.python.org/downloads/
   - 安装时勾选 "Add Python to PATH"

2. **OpenClaw** 或 **Claude Desktop**
   - OpenClaw: https://openclaw.ai
   - Claude Desktop: https://claude.ai/desktop

### 检查Python

打开终端/命令提示符，输入：

```bash
python --version
```

看到类似 `Python 3.10.x` 或更高版本就OK！

---

## 📦 安装步骤

### 方法一：一键安装（推荐）

#### Windows
```powershell
# 以管理员身份打开PowerShell，运行:
irm https://raw.githubusercontent.com/F5G5/pikachu-mcp-servers/main/install.ps1 | iex
```

#### Linux / macOS
```bash
curl -fsSL https://raw.githubusercontent.com/F5G5/pikachu-mcp-servers/main/install.sh | bash
```

### 方法二：手动安装

```bash
# 1. 克隆仓库
git clone https://github.com/F5G5/pikachu-mcp-servers.git
cd pikachu-mcp-servers

# 2. 安装FastMCP
pip install fastmcp

# 3. 或者用uv（更快）
uv pip install fastmcp --system
```

---

## ⚙️ 配置OpenClaw

### 1. 打开配置文件

**Windows:**
```
C:\Users\你的用户名\.openclaw\openclaw.json
```

**Linux/Mac:**
```
~/.openclaw/openclaw.json
```

### 2. 添加服务器配置

在配置文件中找到或创建 `mcp` 部分：

```json
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
      },
      "pikachu-search": {
        "command": "python",
        "args": ["C:/path/to/search_server.py"],
        "cwd": "C:/path/to"
      }
    }
  }
}
```

**注意**: 把 `C:/path/to` 改成你实际的文件夹路径！

### 3. 重启OpenClaw

```bash
openclaw gateway restart
```

---

## 🎮 使用方法

配置完成后，直接对话使用！

### 示例对话

```
你: 查一下北京现在的天气
皮卡丘: [调用天气API] → 📍 北京当前天气
   🌡️ 温度: 25°C
   🌤️ 天气: 晴
   💧 湿度: 45%
   🌬️ 风速: 12 km/h

你: 获取最新科技新闻
皮卡丘: [调用新闻API] → 🔥 Hacker News TOP 10...

你: 搜索"Python教程"
皮卡丘: [调用搜索API] → 相关结果列表...

你: 帮我计算 123 + 456
皮卡丘: [调用计算器] → 123 + 456 = 579
```

---

## 🔧 配置Claude Desktop

如果你用的是Claude Desktop（非OpenClaw）：

### 1. 打开配置

**macOS:**
```
~/Library/Application Support/Claude/claude_desktop_config.json
```

**Windows:**
```
%APPDATA%\Claude\claude_desktop_config.json
```

### 2. 添加配置

```json
{
  "mcpServers": {
    "pikachu-weather": {
      "command": "python",
      "args": ["C:/绝对路径/weather_server.py"]
    }
  }
}
```

### 3. 重启Claude Desktop

---

## ❓ 常见问题

### Q: 提示"找不到python"？

**Windows**: 确保Python已添加到系统PATH，或使用完整路径：
```json
"command": "C:/Users/你的用户名/AppData/Local/Programs/Python/Python310/python.exe"
```

### Q: Server启动失败？

检查：
1. FastMCP是否安装: `pip show fastmcp`
2. Python版本是否 >= 3.10: `python --version`
3. 文件路径是否正确

### Q: 如何卸载？

从配置文件中删除对应server配置即可。不需要卸载FastMCP（其他程序可能也在用）。

---

## 🚀 下一步

- ⭐ 给仓库Star！
- 🐛 提交Bug/建议: https://github.com/F5G5/pikachu-mcp-servers/issues
- 💰 升级Pro版: https://afdian.net/@pikachu_mcp

---

**皮卡皮卡～有问题尽管问！⚡**
