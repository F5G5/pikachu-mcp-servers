"""
皮卡丘效率工具MCP Server ⚡
时间管理、任务规划、效率提升
"""
from fastmcp import FastMCP
import json
import re
from datetime import datetime, timedelta

mcp = FastMCP("皮卡丘效率服务")

@mcp.tool()
def pomodoro_timer(minutes: int = 25) -> str:
    """番茄钟计时器"""
    if minutes not in [15, 25, 45, 60]:
        minutes = 25
    
    session = {
        15: "短时专注",
        25: "标准番茄",
        45: "深度工作",
        60: "马拉松"
    }
    
    start = datetime.now()
    end = start + timedelta(minutes=minutes)
    
    return f"""🍅 番茄钟启动！

{'='*40}
📊 时长: {minutes}分钟 ({session[minutes]})
⏰ 开始: {start.strftime('%H:%M:%S')}
⏰ 结束: {end.strftime('%H:%M:%S')}
⏱️  提醒: {end.strftime('%H:%M')}

💡 建议:
- 手机静音/免打扰
- 关闭无关窗口
- 只做一件事
- 完成后休息5-10分钟

🎯 专注模式启动！"""

@mcp.tool()
def task_planner(tasks: str, available_hours: float = 4.0) -> str:
    """智能任务规划"""
    task_list = [t.strip() for t in tasks.split('\n') if t.strip()]
    
    if not task_list:
        return "⚠️ 请输入任务列表，每行一个任务"
    
    total_tasks = len(task_list)
    
    # 估算每个任务时间（简单平均分配）
    time_per_task = available_hours / total_tasks
    
    result = f"""📋 智能任务规划

{'='*40}
📊 总任务: {total_tasks}个
⏰ 可用时间: {available_hours}小时
⏱️ 每任务约: {time_per_task:.1f}小时

{'='*40}"""
    
    for i, task in enumerate(task_list, 1):
        priority = "🔴 高" if i <= total_tasks // 3 else ("🟡 中" if i <= total_tasks * 2 // 3 else "🟢 低")
        start_time = datetime.now() + timedelta(hours=(i-1) * time_per_task)
        end_time = start_time + timedelta(hours=time_per_task)
        result += f"""
{i}. {priority} {task}
   ⏰ {start_time.strftime('%H:%M')} - {end_time.strftime('%H:%M')}
"""
    
    result += f"""
{'='*40}
💡 执行建议:
1. 先做标记🔴的任务
2. 45分钟后休息5分钟
3. 按顺序执行，不要跳任务
4. 完成一项划掉一项"""
    
    return result

@mcp.tool()
def daily_review() -> str:
    """每日复盘模板"""
    today = datetime.now().strftime('%Y-%m-%d')
    
    return f"""📝 每日复盘 - {today}

{'='*40}

✅ 今日完成:

1. 
2. 
3. 


❌ 未完成:

1. 
2. 


💡 今日收获:

1. 
2. 


🤔 明日改进:

1. 
2. 


📊 今日评分: ⭐⭐⭐⭐⭐

💬 备注:


{'='*40}
💡 复盘要点:
- 记录具体完成的事
- 分析未完成的原因
- 总结可复用的经验
- 制定可执行的改进计划"""

@mcp.tool()
def weekly_planner() -> str:
    """周计划生成器"""
    today = datetime.now()
    week_start = today - timedelta(days=today.weekday())
    
    days = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    
    result = f"""📅 周计划 - {week_start.strftime('%Y-%m-%d')} 起

{'='*40}"""
    
    for i, day in enumerate(days):
        is_weekend = i >= 5
        work_hours = 2 if is_weekend else 6
        
        result += f"""
{days[i]} ({week_start.strftime('%Y-%m-%d')})
📊 可用时间: {work_hours}小时
🎯 重点任务:
   1. 
   2. 
"""
        week_start += timedelta(days=1)
    
    result += f"""
{'='*40}
💡 周计划建议:
- 周一: 制定目标，分解任务
- 周二-周四: 专注执行
- 周五: 检查进度，调整计划
- 周六: 灵活安排/休息
- 周日: 下周规划"""
    
    return result

@mcp.tool()
def smart_reminder(task: str, priority: str = "medium", deadline: str = "") -> str:
    """智能提醒生成"""
    priority_levels = {
        "high": "🔴 高优先级",
        "medium": "🟡 中优先级", 
        "low": "🟢 低优先级"
    }
    
    p = priority_levels.get(priority.lower(), priority_levels["medium"])
    
    reminder = f"""⏰ 任务提醒已设置！

{'='*40}
📌 任务: {task}
{p}
"""
    
    if deadline:
        reminder += f"⏱️ 截止: {deadline}\n"
    
    actions = []
    
    if "重要" in task or priority == "high":
        actions.append("🚨 立即处理，不要拖延")
    if "学习" in task or "读" in task:
        actions.append("📚 预留专注时间，关闭干扰")
    if "运动" in task or "健身" in task:
        actions.append("👟 准备好装备")
    if "会议" in task or "面试" in task:
        actions.append("📋 提前5分钟准备")
    if "提交" in task or "deadline" in task.lower():
        actions.append("⚠️ 设置多个提前提醒")
    
    if actions:
        reminder += f"\n💡 建议:\n"
        for a in actions:
            reminder += f"   {a}\n"
    
    return reminder

@mcp.tool()
def focus_session(work_minutes: int = 90, break_minutes: int = 20) -> str:
    """深度工作专注时段"""
    if work_minutes < 25:
        work_minutes = 25
    if work_minutes > 180:
        work_minutes = 180
    
    start = datetime.now()
    end = start + timedelta(minutes=work_minutes)
    break_end = end + timedelta(minutes=break_minutes)
    
    cycles = work_minutes // 90
    
    return f"""🎯 深度工作时段启动！

{'='*40}
⏰ 开始: {start.strftime('%H:%M:%S')}
⏰ 结束: {end.strftime('%H:%M:%S')}
⏱️ 专注时长: {work_minutes}分钟
🔄 建议循环: {cycles}个90分钟

⏸️ 休息时段:
   {end.strftime('%H:%M')} - {break_end.strftime('%H:%M')} ({break_minutes}分钟)

{'='*40}
🎧 建议:
- 听白噪音/纯音乐
- 手机静音+免打扰
- 戴耳机表示"忙碌中"
- 准备一杯水

🌟 深度工作技巧:
1. 单一任务，不多任务切换
2. 设定明确的目标
3. 记录任何打断你的事
4. 完成后记录成果

🎯 开始计时，专注！"""

@mcp.tool()
def quick_break(suggestion_type: str = "any") -> str:
    """快速休息建议"""
    breaks = {
        "eye": [
            "👀 眼保健操 - 闭眼转圈各10次",
            "👀 20-20-20法则：看20英尺外的东西20秒",
            "👀 眨眼1分钟，防止干眼"
        ],
        "body": [
            "🧘 站立拉伸 - 双手举过头顶，保持30秒",
            "🏃 原地跑步5分钟",
            "💪 俯卧撑10个+深蹲20个"
        ],
        "mind": [
            "🧠 冥想5分钟，专注于呼吸",
            "🎵 听一首喜欢的歌，闭眼放松",
            "☕ 泡杯茶/咖啡，享受片刻"
        ],
        "any": [
            "🚽 去趟洗手间，活动一下",
            "💧 倒杯水，补充水分",
            "👀 离开屏幕，看看窗外",
            "🧘 站起来伸个懒腰",
            "📱 快速浏览社交媒体5分钟",
            "☕ 泡杯咖啡/茶"
        ]
    }
    
    import random
    
    pool = breaks.get(suggestion_type.lower(), breaks["any"])
    tip = random.choice(pool)
    
    return f"""☕ 休息时间到！

{'='*40}
💡 建议:
{tip}

⏱️ 建议时长: 5-15分钟

{'='*40}
💡 休息原则:
- 不要刷短视频（越刷越累）
- 不要看工作消息
- 离开工作区
- 让大脑真正放松"""

if __name__ == "__main__":
    mcp.run()
