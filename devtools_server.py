"""
皮卡丘开发者工具MCP Server ⚡
代码格式化、API测试、版本比较等开发工具
"""
from fastmcp import FastMCP
import json
import re
import hashlib
import base64
from urllib.parse import urlencode, urlparse, parse_qs
from datetime import datetime

mcp = FastMCP("皮卡丘开发工具")

@mcp.tool()
def json_formatter(json_string: str) -> str:
    """JSON格式化"""
    try:
        parsed = json.loads(json_string)
        formatted = json.dumps(parsed, indent=2, ensure_ascii=False)
        return f"""📄 JSON格式化结果

{'='*40}
✅ 格式正确！

输出:
{formatted}

{'='*40}
📊 统计:
- 层级深度: {len(str(parsed).splitlines())}行
- 键数量: {len(parsed) if isinstance(parsed, dict) else len(parsed)}"""
    except json.JSONDecodeError as e:
        return f"""❌ JSON格式错误

{'='*40}
错误位置: 第{e.lineno}行, 第{e.colno}列
错误信息: {e.msg}

提示: 检查引号、逗号、花括号是否匹配"""

@mcp.tool()
def json_minifier(json_string: str) -> str:
    """JSON压缩"""
    try:
        parsed = json.loads(json_string)
        minified = json.dumps(parsed, separators=(',', ':'))
        return f"""📄 JSON压缩结果

{'='*40}
✅ 压缩成功！

压缩后:
{minified}

{'='*40}
📊 压缩统计:
- 原始大小: {len(json_string)}字节
- 压缩后: {len(minified)}字节
- 节省: {len(json_string) - len(minified)}字节
- 压缩率: {(1 - len(minified)/len(json_string))*100:.1f}%"""
    except json.JSONDecodeError as e:
        return f"❌ JSON格式错误: {e}"

@mcp.tool()
def url_encoder(text: str) -> str:
    """URL编码/解码"""
    from urllib.parse import quote, unquote
    
    encoded = quote(text)
    decoded = unquote(text)
    
    return f"""🔗 URL编码/解码

{'='*40}
原文:
{text}

URL编码:
{encoded}

URL解码:
{decoded}

{'='*40}
💡 用途:
- URL中包含特殊字符
- 传递中文参数
- API请求参数处理"""

@mcp.tool()
def base64_tool(text: str, operation: str = "encode") -> str:
    """Base64编码/解码"""
    try:
        if operation == "encode":
            encoded = base64.b64encode(text.encode('utf-8')).decode('utf-8')
            return f"""📦 Base64编码

{'='*40}
原文:
{text}

编码结果:
{encoded}"""
        else:
            decoded = base64.b64decode(text.encode('utf-8')).decode('utf-8')
            return f"""📦 Base64解码

{'='*40}
原文:
{text}

解码结果:
{decoded}"""
    except Exception as e:
        return f"❌ 操作失败: {str(e)}\n\n可能原因：解码的字符串不是有效的Base64"

@mcp.tool()
def hash_generator(text: str, algorithm: str = "sha256") -> str:
    """生成Hash值"""
    text_bytes = text.encode('utf-8')
    
    algorithms = {
        "md5": hashlib.md5,
        "sha1": hashlib.sha1,
        "sha256": hashlib.sha256,
        "sha512": hashlib.sha512
    }
    
    algo = algorithms.get(algorithm.lower(), hashlib.sha256)
    result = algo(text_bytes).hexdigest()
    
    return f"""🔐 Hash生成

{'='*40}
算法: {algorithm.upper()}
原文: {text}

Hash值:
{result}

{'='*40}
💡 用途:
- MD5: 校验文件完整性（非安全用途）
- SHA1: 兼容性场景
- SHA256: 推荐的安全场景
- SHA512: 高安全要求"""

@mcp.tool()
def regex_tester(pattern: str, test_string: str) -> str:
    """正则表达式测试"""
    try:
        matches = re.findall(pattern, test_string)
        match_objs = re.finditer(pattern, test_string)
        
        result = f"""🔍 正则表达式测试

{'='*40}
模式: {pattern}
测试字符串: {test_string}

{'='*40}"""
        
        if matches:
            result += f"\n✅ 匹配成功！共找到{len(matches)}个匹配：\n\n"
            for i, m in enumerate(matches, 1):
                result += f"  {i}. '{m}'"
                if isinstance(m, str) and len(m) > 0:
                    # 找到在原字符串中的位置
                    for pos in [i.start() for i in re.finditer(re.escape(m), test_string)]:
                        result += f" (位置 {pos})"
                result += "\n"
            
            # 显示捕获组
            match_obj_list = list(re.finditer(pattern, test_string))
            if any(m.groups() for m in match_obj_list):
                result += "\n📌 捕获组:\n"
                for i, mo in enumerate(match_obj_list[:5], 1):
                    if mo.groups():
                        result += f"  匹配{i}: {mo.groups()}\n"
        else:
            result += "\n❌ 未找到匹配"
        
        return result
        
    except re.error as e:
        return f"❌ 正则表达式错误: {e}"

@mcp.tool()
def color_converter(color: str) -> str:
    """颜色格式转换"""
    color = color.strip().lower()
    
    # 解析颜色
    hex_pattern = r'^#?([a-f0-9]{6}|[a-f0-9]{3})$'
    rgb_pattern = r'rgb\s*\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)'
    
    try:
        if re.match(hex_pattern, color):
            # HEX转RGB
            if len(color) == 4:
                color = '#' + ''.join([c*2 for c in color.lstrip('#')])
            r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
            hex_color = color if color.startswith('#') else '#' + color
        elif re.match(rgb_pattern, color):
            # RGB转HEX
            match = re.match(rgb_pattern, color)
            r, g, b = int(match.group(1)), int(match.group(2)), int(match.group(3))
            hex_color = f'#{r:02x}{g:02x}{b:02x}'
        else:
            return f"❌ 不支持的颜色格式: {color}\n\n支持格式:\n- HEX: #FF0000 或 FF0000\n- RGB: rgb(255, 0, 0)"
        
        # HSL转换
        r, g, b = r/255, g/255, b/255
        cmax = max(r, g, b)
        cmin = min(r, g, b)
        delta = cmax - cmin
        
        if delta == 0:
            h = 0
        elif cmax == r:
            h = 60 * (((g - b) / delta) % 6)
        elif cmax == g:
            h = 60 * (((b - r) / delta) + 2)
        else:
            h = 60 * (((r - g) / delta) + 4)
        
        l = (cmax + cmin) / 2
        s = 0 if delta == 0 else delta / (1 - abs(2*l - 1))
        
        h, s, l = int(h), int(s*100), int(l*100)
        
        return f"""🎨 颜色转换

{'='*40}
HEX: {hex_color.upper()}
RGB: rgb({r}, {g}, {b})
HSL: hsl({h}, {s}%, {l}%)

{'='*40}
预览: [{' '*20}]

💡 CSS使用:
  color: {hex_color};
  background-color: {hex_color};;

📋 取色工具:
- Chrome: 开发者工具 > Elements > 颜色选择器
- VS Code: Color Picker插件"""

    except Exception as e:
        return f"❌ 转换失败: {e}"

@mcp.tool()
def timestamp_converter(timestamp: str = "", format_type: str = "unix_to_datetime") -> str:
    """时间戳转换"""
    now = datetime.now()
    
    if format_type == "now":
        return f"""⏰ 当前时间

{'='*40}
📅 日期时间: {now.strftime('%Y-%m-%d %H:%M:%S')}
🕐 Unix时间戳: {int(now.timestamp())}
📅 ISO格式: {now.isoformat()}

{'='*40}
💡 常用格式:
- %Y-%m-%d %H:%M:%S
- %Y/%m/%d %H:%M
- %Y年%m月%d日"""
    
    try:
        if timestamp.isdigit():
            ts = int(timestamp)
            if ts < 10000000000:
                ts *= 1000  # 秒转毫秒
            dt = datetime.fromtimestamp(ts / 1000)
        else:
            dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            ts = int(dt.timestamp() * 1000)
        
        return f"""⏰ 时间戳转换

{'='*40}
📅 日期时间: {dt.strftime('%Y-%m-%d %H:%M:%S')}
🕐 Unix时间戳: {ts}
🕐 秒级时间戳: {ts // 1000}
📅 ISO格式: {dt.isoformat()}
📅 北京时间: {dt.strftime('%Y年%m月%d日 %H时%M分%S秒')}

{'='*40}
💡 使用场景:
- API返回的时间通常是毫秒级时间戳
- JavaScript: Date.now()
- Python: int(time.time() * 1000)
- MySQL: UNIX_TIMESTAMP()"""
        
    except Exception as e:
        return f"❌ 转换失败: {e}\n\n请输入有效的时间戳（毫秒或秒）或日期时间字符串"

@mcp.tool()
def http_status_check(code: int) -> str:
    """HTTP状态码查询"""
    status_codes = {
        200: ("✅ OK", "请求成功"),
        201: ("✅ Created", "资源创建成功"),
        204: ("✅ No Content", "请求成功，无返回内容"),
        301: ("↔️ Moved Permanently", "永久重定向"),
        302: ("↔️ Found", "临时重定向"),
        304: ("✅ Not Modified", "使用缓存"),
        400: ("❌ Bad Request", "请求语法错误"),
        401: ("🔐 Unauthorized", "需要认证"),
        403: ("🔐 Forbidden", "权限不足"),
        404: ("❌ Not Found", "资源不存在"),
        405: ("❌ Method Not Allowed", "不支持的请求方法"),
        429: ("⚠️ Too Many Requests", "请求过于频繁"),
        500: ("💥 Internal Server Error", "服务器内部错误"),
        502: ("💥 Bad Gateway", "网关错误"),
        503: ("⚠️ Service Unavailable", "服务不可用"),
        504: ("⚠️ Gateway Timeout", "网关超时"),
    }
    
    if code in status_codes:
        symbol, desc = status_codes[code]
        category = "成功" if code < 300 else "重定向" if code < 400 else "客户端错误" if code < 500 else "服务端错误"
        
        return f"""🌐 HTTP状态码: {code}

{'='*40}
{symbol} {desc}
📊 类别: {category}

{'='*40}
💡 故障排查:
{"- 检查URL是否正确" if code == 404 else ""}
{"- 检查请求头和权限" if code == 401 else ""}
{"- 联系服务器管理员" if code >= 500 else ""}
{"- 降低请求频率" if code == 429 else ""}"""
    else:
        return f"""❌ 未知状态码: {code}

{'='*40}
常见状态码范围:
- 1xx: 信息响应
- 2xx: 成功
- 3xx: 重定向
- 4xx: 客户端错误
- 5xx: 服务端错误"""

if __name__ == "__main__":
    mcp.run()
