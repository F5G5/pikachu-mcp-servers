"""
皮卡丘新闻MCP Server ⚡
实时获取最新新闻
"""
from fastmcp import FastMCP
import urllib.request
import json
from datetime import datetime

mcp = FastMCP("皮卡丘新闻服务")

@mcp.tool()
def get_tech_news() -> str:
    """获取最新科技新闻"""
    try:
        # 使用 Hacker News API
        url = "https://hacker-news.firebaseio.com/v0/topstories.json"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            story_ids = json.loads(response.read().decode())[:10]
        
        news = "🔥 最新科技新闻 (Hacker News)\n"
        news += "=" * 40 + "\n\n"
        
        for i, story_id in enumerate(story_ids, 1):
            story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
            req = urllib.request.Request(story_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10) as r:
                story = json.loads(r.read().decode())
            
            title = story.get('title', 'No title')
            score = story.get('score', 0)
            news_url = story.get('url', f"https://news.ycombinator.com/item?id={story_id}")
            by = story.get('by', 'unknown')
            
            news += f"{i}. {title}\n"
            news += f"   ⬆️ {score} | 👤 {by}\n"
            news += f"   🔗 {news_url}\n\n"
        
        return news
    except Exception as e:
        return f"获取失败: {str(e)}\n\n备选：可以尝试搜索其他关键词"

@mcp.tool()
def get_zhihu_hot() -> str:
    """获取知乎热榜"""
    try:
        url = "https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit=10"
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json'
        })
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
        
        news = "💬 知乎热榜\n"
        news += "=" * 40 + "\n\n"
        
        items = data.get('data', [])[:10]
        for i, item in enumerate(items, 1):
            title = item.get('target', {}).get('title', '无标题')
            metric = item.get('target', {}).get('metrics', {}).get('member_count', 0)
            news += f"{i}. {title}\n"
            news += f"   👁️ {metric} 浏览\n\n"
        
        return news
    except Exception as e:
        return f"获取失败: {str(e)}"

@mcp.tool()
def search_news(keyword: str, limit: int = 5) -> str:
    """搜索新闻"""
    # 使用 DuckDuckGo 搜索API
    try:
        from urllib.parse import quote
        url = f"https://api.duckduckgo.com/?q={quote(keyword)}&format=json&no_redirect=1"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
        
        results = data.get('RelatedTopics', [])[:limit]
        
        news = f"🔍 关于「{keyword}」的新闻\n"
        news += "=" * 40 + "\n\n"
        
        for i, item in enumerate(results, 1):
            title = item.get('Text', '无标题')
            url = item.get('FirstURL', '')
            news += f"{i}. {title}\n"
            if url:
                news += f"   🔗 {url}\n\n"
        
        return news
    except Exception as e:
        return f"搜索失败: {str(e)}"

@mcp.tool()
def get_douyin_hot() -> str:
    """获取抖音热榜（模拟数据）"""
    # 抖音API需要特殊权限，使用模拟数据
    hot_topics = [
        ("1", "AI绘画工具大火，创作者经济新机遇", "152.3万热度"),
        ("2", "春季穿搭指南，显瘦显高秘籍", "98.7万热度"),
        ("3", "00后创业故事，从0到百万粉", "87.2万热度"),
        ("4", "新能源汽车续航实测，结果意外", "76.5万热度"),
        ("5", "美食探店|藏在巷子里的老字号", "65.8万热度"),
    ]
    
    result = "📱 抖音热榜 TOP5\n"
    result += "=" * 40 + "\n\n"
    
    for rank, title, hot in hot_topics:
        result += f"🔥 第{rank}名\n"
        result += f"   {title}\n"
        result += f"   {hot}\n\n"
    
    result += f"⏰ 更新时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    return result

@mcp.tool()
def get_weibo_hot() -> str:
    """获取微博热榜"""
    try:
        url = "https://weibo.com/ajax/side/hotSearch"
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Referer': 'https://weibo.com'
        })
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
        
        result = "🌟 微博热榜\n"
        result += "=" * 40 + "\n\n"
        
        hotgo = data.get('data', {}).get('hotgo', [])[:10]
        for i, item in enumerate(hotgo, 1):
            word = item.get('word', '未知')
            num = item.get('num', 0)
            result += f"{i}. {word}\n"
            result += f"   🔥 {num:,} 热度\n\n"
        
        return result
    except Exception as e:
        return f"获取失败: {str(e)}\n\n微博API可能需要登录"

if __name__ == "__main__":
    mcp.run()
