"""
皮卡丘搜索MCP Server ⚡
多功能搜索工具
"""
from fastmcp import FastMCP
import urllib.request
import json
from urllib.parse import quote
from datetime import datetime

mcp = FastMCP("皮卡丘搜索服务")

@mcp.tool()
def web_search(query: str, num_results: int = 5) -> str:
    """网页搜索"""
    try:
        # 使用 DuckDuckGo Instant Answer API
        url = f"https://api.duckduckgo.com/?q={quote(query)}&format=json&no_redirect=1"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
        
        result = f"🔍 搜索: {query}\n"
        result += "=" * 50 + "\n\n"
        
        # Related topics
        topics = data.get('RelatedTopics', [])[:num_results]
        for i, topic in enumerate(topics, 1):
            text = topic.get('Text', '')
            topic_url = topic.get('FirstURL', '')
            if text:
                result += f"{i}. {text}\n"
                if topic_url:
                    result += f"   🔗 {topic_url}\n"
                result += "\n"
        
        if not topics:
            result += "未找到相关结果\n"
        
        return result
    except Exception as e:
        return f"搜索失败: {str(e)}"

@mcp.tool()
def bing_search(query: str) -> str:
    """Bing搜索（模拟）"""
    # Bing需要API Key，使用模拟结果
    result = f"🔍 Bing搜索: {query}\n"
    result += "=" * 50 + "\n\n"
    
    # 模拟Bing搜索结果格式
    mock_results = [
        ("【官方】" + query + " - 最新资讯", "https://example.com/1", "这是关于" + query + "的官方信息来源..."),
        (query + "完整指南 (2024)", "https://example.com/2", "本文详细介绍" + query + "的相关知识和使用方法..."),
        (query + "常见问题解答", "https://example.com/3", "以下是关于" + query + "最常见的问题..."),
    ]
    
    for i, (title, url, desc) in enumerate(mock_results, 1):
        result += f"{i}. {title}\n"
        result += f"   {desc}\n"
        result += f"   🔗 {url}\n\n"
    
    result += f"⚠️ 注意：这是演示数据，真实Bing搜索需要API Key\n"
    return result

@mcp.tool()
def wikipedia_lookup(keyword: str) -> str:
    """维基百科查询"""
    try:
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{quote(keyword)}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
        
        title = data.get('title', keyword)
        extract = data.get('extract', '未找到结果')
        wiki_url = data.get('content_urls', {}).get('desktop', {}).get('page', '')
        
        result = f"📚 维基百科: {title}\n"
        result += "=" * 50 + "\n\n"
        result += f"{extract}\n\n"
        if wiki_url:
            result += f"🔗 {wiki_url}"
        
        return result
    except Exception as e:
        return f"查询失败: {str(e)}\n\n可能没有对应的维基百科页面"

@mcp.tool()
def github_search(keyword: str) -> str:
    """GitHub仓库搜索（模拟）"""
    # GitHub API需要token，简化处理
    result = f"🐙 GitHub搜索: {keyword}\n"
    result += "=" * 50 + "\n\n"
    
    result += f"热门仓库:\n\n"
    result += f"1. awesome-{keyword.lower().replace(' ', '-')}\n"
    result += f"   ⭐ 10.2k | 🔀 2.3k\n"
    result += f"   精选资源列表\n\n"
    result += f"2. {keyword.lower().replace(' ', '-')}-sdk\n"
    result += f"   ⭐ 3.4k | 🔀 567\n"
    result += f"   官方SDK\n\n"
    result += f"3. {keyword.lower().replace(' ', '-')}-tutorial\n"
    result += f"   ⭐ 1.2k | 🔀 234\n"
    result += f"   入门教程\n\n"
    
    result += f"🔗 https://github.com/search?q={quote(keyword)}\n"
    result += f"⚠️ 需要GitHub API Key获取真实数据"
    
    return result

@mcp.tool()
def unit_converter(value: float, from_unit: str, to_unit: str) -> str:
    """单位换算"""
    conversions = {
        # 长度
        ("km", "miles"): 0.621371,
        ("miles", "km"): 1.60934,
        ("m", "feet"): 3.28084,
        ("feet", "m"): 0.3048,
        ("cm", "inches"): 0.393701,
        ("inches", "cm"): 2.54,
        # 重量
        ("kg", "lbs"): 2.20462,
        ("lbs", "kg"): 0.453592,
        ("g", "oz"): 0.035274,
        ("oz", "g"): 28.3495,
        # 温度
        ("c", "f"): lambda c: c * 9/5 + 32,
        ("f", "c"): lambda f: (f - 32) * 5/9,
    }
    
    key = (from_unit.lower(), to_unit.lower())
    
    result = f"🔄 单位换算\n"
    result += "=" * 50 + "\n\n"
    
    if key in conversions:
        rate = conversions[key]
        if callable(rate):
            converted = rate(value)
        else:
            converted = value * rate
        
        result += f"{value} {from_unit} = {converted:.4f} {to_unit}"
    else:
        result += f"不支持的换算: {from_unit} -> {to_unit}\n\n"
        result += "支持的换算:\n"
        result += "- 长度: km↔miles, m↔feet, cm↔inches\n"
        result += "- 重量: kg↔lbs, g↔oz\n"
        result += "- 温度: c↔f"
    
    return result

@mcp.tool()
def quick_math(expression: str) -> str:
    """快速数学计算"""
    try:
        # 安全计算（仅支持基本运算）
        allowed = set("0123456789+-*/.() ")
        if all(c in allowed for c in expression):
            result = eval(expression)
            return f"🧮 计算结果\n\n{expression} = {result}"
        else:
            return "⚠️ 只支持数字和 + - * / ( ) 操作符"
    except Exception as e:
        return f"计算错误: {str(e)}"

if __name__ == "__main__":
    mcp.run()
