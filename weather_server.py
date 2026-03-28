"""
皮卡丘天气MCP Server v2.0 - 连接真实API ⚡
"""
from fastmcp import FastMCP
import urllib.request
import json
from datetime import datetime

mcp = FastMCP("皮卡丘天气服务")

# ============ 天气查询工具 ============

@mcp.tool()
def get_current_weather(city: str) -> str:
    """获取当前天气（使用真实API）"""
    try:
        # 使用 wttr.in API（免费无需key）
        url = f"https://wttr.in/{city}?format=j1"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
        
        current = data['current_condition'][0]
        weather_desc = current['weatherDesc'][0]['value']
        temp_C = current['temp_C']
        humidity = current['humidity']
        wind_speed = current['windspeedKmph']
        wind_dir = current['winddir16Point']
        
        result = f"""📍 {city} 当前天气
🌡️ 温度: {temp_C}°C
🌤️ 天气: {weather_desc}
💧 湿度: {humidity}%
🌬️ 风速: {wind_speed} km/h ({wind_dir})

⏰ 查询时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"""
        
        return result
    except Exception as e:
        return f"查询失败: {str(e)}\n\n支持的格式：城市名（英文），如: Beijing, Shanghai, Shenzhen"

@mcp.tool()
def get_weather_forecast(city: str, days: int = 3) -> str:
    """获取天气预报（真实API）"""
    try:
        url = f"https://wttr.in/{city}?format=j1"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
        
        result = f"📍 {city} 天气预报\n"
        result += "=" * 30 + "\n"
        
        for i in range(min(days, 3)):
            day_data = data['weather'][i]
            date = day_data['date']
            max_temp = day_data['maxtempC']
            min_temp = day_data['mintempC']
            desc = day_data['hourly'][4]['weatherDesc'][0]['value']  # 中午天气
            
            day_names = ['今天', '明天', '后天']
            result += f"\n📅 {day_names[i]} ({date})"
            result += f"\n   🌡️ {min_temp}°C ~ {max_temp}°C"
            result += f"\n   🌤️ {desc}\n"
        
        return result
    except Exception as e:
        return f"查询失败: {str(e)}"

@mcp.tool()
def get_air_quality(city: str) -> str:
    """获取空气质量（模拟）"""
    # wttr.in没有空气质量，用模拟数据
    air_data = {
        "北京": {"aqi": 158, "level": "中度污染", "pm25": 95},
        "上海": {"aqi": 72, "level": "良好", "pm25": 38},
        "深圳": {"aqi": 45, "level": "优", "pm25": 22},
        "广州": {"aqi": 65, "level": "良", "pm25": 32},
        "成都": {"aqi": 120, "level": "轻度污染", "pm25": 68},
        "杭州": {"aqi": 58, "level": "良", "pm25": 28},
    }
    
    data = air_data.get(city)
    if data:
        return f"""🏭 {city} 空气质量
AQI: {data['aqi']}
等级: {data['level']}
PM2.5: {data['pm25']} μg/m³"""
    else:
        return f"暂不支持{city}的空气质量查询"

# ============ 实用工具 ============

@mcp.tool()
def calculate(a: float, b: float, operation: str) -> str:
    """计算器 - 支持加减乘除"""
    ops = {
        "+": a + b,
        "-": a - b,
        "*": a * b,
        "/": a / b if b != 0 else "错误：除数为0"
    }
    result = ops.get(operation, "未知操作")
    return f"{a} {operation} {b} = {result}"

@mcp.tool()
def currency_converter(amount: float, from_currency: str, to_currency: str) -> str:
    """货币换算（使用真实汇率API）"""
    try:
        # 使用 exchangerate-api 免费端点
        url = f"https://open.er-api.com/v6/latest/{from_currency.upper()}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
        
        rate = data['rates'].get(to_currency.upper())
        if rate:
            result = amount * rate
            return f"""💱 货币换算
{amount} {from_currency.upper()} = {result:.2f} {to_currency.upper()}
汇率: 1 {from_currency.upper()} = {rate:.4f} {to_currency.upper()}"""
        else:
            return f"不支持的货币: {to_currency}"
    except Exception as e:
        return f"查询失败: {str(e)}"

@mcp.tool()
def get_news(keyword: str = "technology") -> str:
    """获取最新新闻标题（使用NewsAPI模拟）"""
    # 使用公共RSS源
    news_topics = {
        "technology": "科技",
        "business": "商业",
        "sports": "体育",
        "entertainment": "娱乐",
        "science": "科学"
    }
    
    topic = news_topics.get(keyword.lower(), "科技")
    
    # 模拟新闻（实际项目可用NewsAPI）
    news = f"""📰 {topic} 最新消息
{'='*30}
1. AI技术持续突破，多行业应用加速落地
2. 新能源汽车销量同比增长45%
3. 电商平台推出新一轮促销活动
4. 远程办公工具需求持续增长
5. 量子计算研究取得重大进展
{'='*30}
来源: 综合整理 | {datetime.now().strftime('%Y-%m-%d')}"""
    
    return news

@mcp.tool()
def world_time(city: str) -> str:
    """查询世界各地时间"""
    time_zones = {
        "北京": "Asia/Shanghai",
        "上海": "Asia/Shanghai", 
        "东京": "Asia/Tokyo",
        "纽约": "America/New_York",
        "伦敦": "Europe/London",
        "巴黎": "Europe/Paris",
        "悉尼": "Australia/Sydney",
        "洛杉矶": "America/Los_Angeles",
        "迪拜": "Asia/Dubai",
        "新加坡": "Asia/Singapore"
    }
    
    from datetime import datetime
    import time
    
    tz = time_zones.get(city)
    if tz:
        import os
        os.environ['TZ'] = tz
        time.tzset()
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S %Z')
        return f"🌍 {city} 当前时间:\n{now}"
    else:
        return f"暂不支持查询{city}的时间"

if __name__ == "__main__":
    mcp.run()
