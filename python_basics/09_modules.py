"""
============================================
第9课：模块与包
============================================
把代码按功能拆分成多个文件，各司其职，方便管理和复用。
"""

# ==================== 一、import 的多种方式 ====================

print("=== import 的多种方式 ===")

# 方式1：导入整个模块
import math
print(f"math.pi = {math.pi}")
print(f"math.sqrt(16) = {math.sqrt(16)}")

# 方式2：导入特定函数/变量
from math import sqrt, pi
print(f"直接使用 sqrt(25) = {sqrt(25)}")
print(f"直接使用 pi = {pi}")

# 方式3：导入所有内容（不推荐，可能引起命名冲突）
# from math import *

# 方式4：起别名
import datetime as dt
today = dt.date.today()
print(f"今天的日期: {today}")

from math import sqrt as square_root
print(f"别名 square_root(100) = {square_root(100)}")


# ==================== 二、标准库常用模块 ====================

print("\n=== Python 标准库常用模块 ===")

# 1. random —— 随机数
import random
print(f"随机整数 [1, 10]: {random.randint(1, 10)}")
print(f"随机小数 [0, 1):  {random.random():.4f}")
print(f"随机选择: {random.choice(['苹果', '香蕉', '橘子'])}")

# 2. datetime —— 日期时间
from datetime import datetime, timedelta
now = datetime.now()
print(f"当前时间: {now}")
print(f"格式化:   {now.strftime('%Y年%m月%d日 %H:%M:%S')}")

# 3. os —— 操作系统接口
import os
print(f"当前工作目录: {os.getcwd()}")
print(f"环境变量 PATH: {os.environ.get('PATH', 'N/A')[:50]}...")

# 4. sys —— Python 解释器信息
import sys
print(f"Python 版本: {sys.version}")
print(f"系统平台: {sys.platform}")

# 5. json —— JSON 数据处理（数据分析中非常常用）
import json
data = {"name": "小明", "age": 25, "scores": [85, 92, 78]}
json_str = json.dumps(data, ensure_ascii=False, indent=2)
print(f"Python 对象 → JSON:\n{json_str}")

parsed = json.loads(json_str)
print(f"JSON → Python 对象: {parsed}")
print(f"读取 name: {parsed['name']}")

# 6. collections —— 高级容器类型
from collections import Counter, defaultdict

# Counter：计数
words = ["苹果", "香蕉", "苹果", "橘子", "香蕉", "苹果"]
counter = Counter(words)
print(f"Counter 计数: {counter}")
print(f"最常见的: {counter.most_common(2)}")

# defaultdict：带默认值的字典
grouped = defaultdict(list)
fruits = [
    ("水果", "苹果"), ("水果", "香蕉"),
    ("蔬菜", "白菜"), ("蔬菜", "萝卜"),
    ("水果", "橘子"),
]
for category, item in fruits:
    grouped[category].append(item)
print(f"defaultdict 分组: {dict(grouped)}")


# ==================== 三、自定义模块（演示） ====================

print("\n=== 自定义模块 ===")

# 创建一个简单的工具模块（实际会写在一个单独的 .py 文件中）
# 这里用一个字符串来演示模块的概念

"""
# 假如我们在同一目录下创建 my_utils.py 文件：

# my_utils.py 内容如下：
def greet(name):
    return f"你好，{name}！"

def average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

PI = 3.14159

# 然后在另一个文件中可以这样使用：
# from my_utils import greet, average
# print(greet("小明"))
# print(average([1, 2, 3, 4, 5]))
"""

print("✅ 模块的概念：一个 .py 文件就是一个模块")
print("✅ 包的概念：一个包含 __init__.py 的文件夹就是一个包")


# ==================== 四、if __name__ == '__main__' ====================

print("\n=== if __name__ == '__main__' ===")

# 这个模式让一个 .py 文件既可以作为模块导入，也可以直接运行
# 当你直接运行脚本时，__name__ 是 '__main__'
# 当你导入模块时，__name__ 是模块名

def helper_function():
    return "这是一个辅助函数"

def main():
    """当前文件的主函数"""
    print("当前文件被直接运行！")
    print(f"__name__ = {__name__}")
    print("这里可以放测试代码或程序入口")

if __name__ == "__main__":
    # 只有在直接运行此文件时才会执行
    main()
    print("\n在其他文件中 import 本文件时，这部分代码不会执行")


# ==================== 五、实战：用标准库完成数据分析 ====================

print("\n=== 实战：成绩统计工具 ===")

import statistics
from collections import Counter

# 模拟成绩数据
exam_scores = [85, 92, 78, 95, 60, 88, 72, 85, 90, 85]

# 统计信息
mean = statistics.mean(exam_scores)        # 平均值
median = statistics.median(exam_scores)    # 中位数
mode = statistics.mode(exam_scores)        # 众数
stdev = statistics.stdev(exam_scores)      # 标准差

print(f"成绩数据: {exam_scores}")
print(f"平均分: {mean:.1f}")
print(f"中位数: {median}")
print(f"众数:   {mode}")
print(f"标准差: {stdev:.2f}")

# 成绩分布
score_counter = Counter(exam_scores)
print(f"各分数出现次数: {dict(score_counter)}")

# 等级统计
grades = {"优秀(≥90)": 0, "良好(≥80)": 0, "及格(≥60)": 0, "不及格(<60)": 0}
for s in exam_scores:
    if s >= 90:
        grades["优秀(≥90)"] += 1
    elif s >= 80:
        grades["良好(≥80)"] += 1
    elif s >= 60:
        grades["及格(≥60)"] += 1
    else:
        grades["不及格(<60)"] += 1

print(f"\n成绩分布:")
for grade, count in grades.items():
    bar = "█" * count
    print(f"  {grade}: {bar} {count}人")


# ==================== 练习区 ====================

# 练习1：用 random 模块，模拟抛硬币 100 次，统计正面和反面出现的次数
# 提示：random.choice(["正面", "反面"])

# 练习2：用 datetime 模块，计算你的出生日期到今天一共过了多少天
# 提示：(今天 - 出生日期).days

# 练习3：用 json 模块，创建一个嵌套的 Python 字典，
#        转为 JSON 字符串并保存到文件，然后再读取回来
