"""
我的第一个MCP Server - 皮卡丘出品 ⚡
功能：计算器和天气预报
"""

from fastmcp import FastMCP

# 创建MCP服务器
mcp = FastMCP("皮卡丘的服务器")

# ============ 计算器工具 ============

@mcp.tool()
def add(a: int, b: int) -> int:
    """加法计算器"""
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """减法计算器"""
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """乘法计算器"""
    return a * b

@mcp.tool()
def divide(a: int, b: int) -> str:
    """除法计算器"""
    if b == 0:
        return "错误：除数不能为0！"
    return f"{a / b:.2f}"

# ============ 天气查询工具 ============

@mcp.tool()
def get_weather(city: str) -> str:
    """获取天气信息（模拟）"""
    # 这里可以用真实API，但先模拟
    weather_data = {
        "北京": "☀️ 晴，25°C",
        "上海": "🌧️ 小雨，18°C",
        "深圳": "🌤️ 多云，28°C",
        "杭州": "🌤️ 晴，22°C",
    }
    return weather_data.get(city, f"❓ 未知城市 {city}，请输入北京/上海/深圳/杭州")

@mcp.tool()
def get_forecast(city: str, days: int) -> str:
    """获取天气预报"""
    forecasts = {
        "北京": ["☀️ 晴 25°C", "⛅ 多云 23°C", "🌧️ 小雨 20°C"],
        "上海": ["🌧️ 小雨 18°C", "🌧️ 中雨 16°C", "⛅ 多云 19°C"],
        "深圳": ["🌤️ 多云 28°C", "☀️ 晴 30°C", "🌤️ 多云 29°C"],
        "杭州": ["🌤️ 晴 22°C", "☀️ 晴 24°C", "⛅ 多云 21°C"],
    }
    data = forecasts.get(city, None)
    if not data:
        return f"❓ 未知城市 {city}"
    
    result = [f"📍 {city} 天气预报："]
    for i, d in enumerate(data[:days], 1):
        result.append(f"  第{i}天：{d}")
    return "\n".join(result)

# ============ 文字工具 ============

@mcp.tool()
def reverse_text(text: str) -> str:
    """反转文字"""
    return text[::-1]

@mcp.tool()
def count_words(text: str) -> dict:
    """统计文字"""
    words = text.split()
    return {
        "字数": len(text),
        "词数": len(words),
        "英文词数": len([w for w in words if w.isalpha()]),
    }

if __name__ == "__main__":
    # 启动服务器（通过stdio传输）
    mcp.run()
