"""
============================================
第10课：综合练习与下一步
============================================
用前面学到的知识完成一个综合任务，
以及了解学完基础后该往哪个方向走。
"""

# ==================== 前置准备 ====================

# 先确保导入我们会用到的模块
import json
import random
import os

print("=" * 60)
print("🎯 Python 基础综合练习")
print("=" * 60)


# ==================== 任务1：简易记账本 ====================

print("\n" + "=" * 60)
print("📝 任务1：简易记账本")
print("=" * 60)

def run_account_book():
    """
    一个简单的记账程序：
    - 可以记录收入和支出
    - 可以查看总余额
    - 数据可以保存到文件
    """
    account_file = "account_book.json"
    
    # 加载已有的记账数据
    if os.path.exists(account_file):
        with open(account_file, "r", encoding="utf-8") as f:
            records = json.load(f)
    else:
        records = []
    
    # 这里模拟交互，实际运行时会循环等待输入
    # 我们直接演示添加几条记录
    sample_records = [
        {"type": "收入", "category": "工资", "amount": 5000, "date": "2024-01-15"},
        {"type": "支出", "category": "餐饮", "amount": 35, "date": "2024-01-15"},
        {"type": "支出", "category": "交通", "amount": 12, "date": "2024-01-16"},
        {"type": "收入", "category": "兼职", "amount": 800, "date": "2024-01-20"},
        {"type": "支出", "category": "购物", "amount": 299, "date": "2024-01-21"},
    ]
    
    records.extend(sample_records)
    
    # 保存到文件
    with open(account_file, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
    
    # 统计
    total_income = sum(r["amount"] for r in records if r["type"] == "收入")
    total_expense = sum(r["amount"] for r in records if r["type"] == "支出")
    balance = total_income - total_expense
    
    print(f"✅ 记账数据已保存到 {account_file}")
    print(f"总记录数: {len(records)} 条")
    print(f"总收入:   {total_income:>8.2f} 元")
    print(f"总支出:   {total_expense:>8.2f} 元")
    print(f"当前余额: {balance:>8.2f} 元")
    
    # 按类别统计
    categories = {}
    for r in records:
        cat = r["category"]
        if cat not in categories:
            categories[cat] = {"收入": 0, "支出": 0}
        categories[cat][r["type"]] += r["amount"]
    
    print(f"\n各类别统计:")
    for cat, amounts in sorted(categories.items()):
        print(f"  {cat}: 收入 {amounts['收入']:>8.2f}  支出 {amounts['支出']:>8.2f}")

run_account_book()


# ==================== 任务2：猜数字游戏 ====================

print("\n" + "=" * 60)
print("🎮 任务2：猜数字游戏")
print("=" * 60)

def guess_number_game():
    """
    猜数字游戏：
    - 系统随机生成一个 1~100 的数字
    - 玩家每次猜一个数，系统提示"大了"或"小了"
    - 猜中后显示猜的次数
    """
    print("我想到了一个 1~100 之间的数字，你来猜猜看！")
    
    target = random.randint(1, 100)
    attempts = 0
    # 模拟几次猜测过程
    guesses = [50, 75, 62, 68, 65]  # 模拟的猜测序列
    
    for guess in guesses:
        attempts += 1
        if guess < target:
            print(f"  第{attempts}次: 猜 {guess} → 小了 📈")
        elif guess > target:
            print(f"  第{attempts}次: 猜 {guess} → 大了 📉")
        else:
            print(f"  🎉 第{attempts}次: 猜 {guess} → 猜中了！太棒了！")
            return
    
    print(f"\n😅 正确答案是 {target}，你还需要继续努力哦！")

guess_number_game()


# ==================== 任务3：文本分析器 ====================

print("\n" + "=" * 60)
print("📊 任务3：文本分析器")
print("=" * 60)

from collections import Counter

def text_analyzer(text):
    """
    分析一段文本，返回各项统计信息
    """
    print(f"原始文本: \"{text}\"\n")
    
    # 基本统计
    char_count = len(text)                     # 总字符数（含空格）
    char_no_space = len(text.replace(" ", "")) # 不含空格字符数
    word_count = len(text.split())             # 单词数
    
    print(f"📏 基本统计:")
    print(f"  总字符数（含空格）: {char_count}")
    print(f"  总字符数（不含空格）: {char_no_space}")
    print(f"  单词数: {word_count}")
    
    # 字母频率统计
    letters = [c.lower() for c in text if c.isalpha()]
    letter_freq = Counter(letters)
    
    print(f"\n📈 字母出现频率（Top 5）:")
    for letter, count in letter_freq.most_common(5):
        print(f"  '{letter}': {count} 次")
    
    # 句子统计
    sentences = [s.strip() for s in text.replace("!", ".").replace("?", ".").split(".") if s.strip()]
    print(f"\n📝 句子数量: {len(sentences)}")
    for i, s in enumerate(sentences, 1):
        print(f"  第{i}句: \"{s}\"")
    
    return {
        "char_count": char_count,
        "word_count": word_count,
        "sentence_count": len(sentences),
        "letter_freq": letter_freq,
    }

# 测试文本分析器
sample_text = "Hello World! Python is amazing. I love data analysis. Let's learn together!"
result = text_analyzer(sample_text)


# ==================== 任务4：小型数据管道 ====================

print("\n" + "=" * 60)
print("🔄 任务4：小型数据管道 — 综合运用")
print("=" * 60)

def data_pipeline():
    """
    模拟一个完整的数据处理流程：
    原始数据 → 清洗 → 转换 → 统计 → 输出报告
    """
    # 第1步：模拟原始数据
    print("第1步：获取原始数据 🛢️")
    raw_data = [
        " 张三, 25 , 北京, 工程师 ",
        "李四, 30, 上海, 数据科学家",
        "  王五, 28, 广州, 分析师  ",
        "赵六, 35, 深圳, 经理",
    ]
    print(f"  收到 {len(raw_data)} 条记录")
    
    # 第2步：数据清洗
    print("\n第2步：数据清洗 🧹")
    cleaned = []
    for line in raw_data:
        parts = [p.strip() for p in line.split(",")]
        if len(parts) == 4:
            record = {
                "name": parts[0],
                "age": int(parts[1]),
                "city": parts[2],
                "job": parts[3],
            }
            cleaned.append(record)
    print(f"  清洗后有效数据: {len(cleaned)} 条")
    
    # 第3步：数据转换
    print("\n第3步：数据转换 🔄")
    for r in cleaned:
        r["age_group"] = "青年" if r["age"] < 30 else "中年"
    print("  已添加年龄分组信息")
    
    # 第4步：统计分析
    print("\n第4步：统计分析 📊")
    cities = Counter(r["city"] for r in cleaned)
    jobs = Counter(r["job"] for r in cleaned)
    avg_age = sum(r["age"] for r in cleaned) / len(cleaned)
    
    print(f"  年龄范围: {min(r['age'] for r in cleaned)} ~ {max(r['age'] for r in cleaned)}")
    print(f"  平均年龄: {avg_age:.1f}")
    print(f"  城市分布: {dict(cities)}")
    print(f"  职位分布: {dict(jobs)}")
    
    # 第5步：输出报告
    print("\n第5步：生成报告 📋")
    report_lines = ["人员信息报告", "=" * 30]
    for r in cleaned:
        report_lines.append(
            f"  {r['name']} | {r['age']}岁 | {r['city']} | {r['job']} | {r['age_group']}"
        )
    report = "\n".join(report_lines)
    print(report)
    
    # 保存报告
    with open("data_report.txt", "w", encoding="utf-8") as f:
        f.write(report)
    print(f"\n✅ 报告已保存到 data_report.txt")

data_pipeline()


# ==================== 下一步学习方向 ====================

print("\n" + "=" * 60)
print("🧭 下一步学习方向")
print("=" * 60)

print("""
✅ 已完成：Python 基础语法
   • 变量与数据类型      • 字符串操作
   • 列表/元组/字典/集合   • 条件判断与循环
   • 函数                • 文件读写
   • 异常处理            • 推导式与高阶函数
   • 模块与标准库

🎯 推荐下一步（按学习路线）:
   1️⃣ NumPy —— 数值计算基础
   2️⃣ pandas —— 数据分析核心
   3️⃣ Matplotlib + Seaborn —— 数据可视化
   4️⃣ SQL —— 数据库查询与分析
   5️⃣ 统计基础 —— 描述性统计、假设检验
   6️⃣ 实战项目：探索性数据分析（EDA）

📂 项目文件结构:
   python_basics/
   ├── 01_variables_and_types.py    ← 变量与类型
   ├── 02_strings.py                ← 字符串
   ├── 03_collections.py            ← 容器类型
   ├── 04_control_flow.py           ← 控制流
   ├── 05_functions.py              ← 函数
   ├── 06_file_io.py                ← 文件读写
   ├── 07_exceptions.py             ← 异常处理
   ├── 08_comprehensions.py         ← 推导式与高阶函数
   ├── 09_modules.py                ← 模块与标准库
   └── 10_next_steps.py             ← 综合练习与下一步

💡 学习建议:
   • 每个文件都可以直接运行：python 文件名.py
   • 先看注释理解概念，再看示例代码
   • 修改代码中的值，观察输出变化
   • 完成每个文件末尾的练习题
   • 把所有文件的末尾练习做完，基础就扎实了
""")
