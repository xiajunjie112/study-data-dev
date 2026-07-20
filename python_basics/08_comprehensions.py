"""
============================================
第8课：推导式与高阶函数
============================================
Python 的特色语法，让代码更简洁、更高效。
这是在数据分析代码中随处可见的技巧。
"""

# ==================== 一、列表推导式（温故知新） ====================

print("=== 列表推导式 ===")

# 基本形式：[表达式 for 变量 in 可迭代对象]
# 加上条件：[表达式 for 变量 in 可迭代对象 if 条件]

# 例1：生成平方数
squares = [x**2 for x in range(1, 11)]
print(f"1~10的平方: {squares}")

# 例2：带条件筛选
evens = [x for x in range(20) if x % 2 == 0]
print(f"0~19的偶数: {evens}")

# 例3：嵌套循环（扁平化矩阵）
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"矩阵扁平化: {flattened}")

# 例4：字符串处理
words = ["hello", "world", "python", "data"]
upper_words = [word.upper() for word in words if len(word) > 4]
print(f"长度>4的大写单词: {upper_words}")


# ==================== 二、字典推导式 ====================

print("\n=== 字典推导式 ===")

# 语法：{键:值 for 变量 in 可迭代对象}

# 例1：数字 → 平方
square_dict = {x: x**2 for x in range(1, 6)}
print(f"数字→平方字典: {square_dict}")

# 例2：交换键值
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(f"交换键值: {swapped}")

# 例3：带条件过滤
scores = {"小明": 85, "小红": 92, "小刚": 60, "小美": 45}
passed = {name: score for name, score in scores.items() if score >= 60}
print(f"及格的同学: {passed}")


# ==================== 三、集合推导式 ====================

print("\n=== 集合推导式 ===")

# 语法：{表达式 for 变量 in 可迭代对象} —— 自动去重

# 提取字符串中所有元音字母
text = "Hello Python Data Analysis"
vowels = {c.lower() for c in text if c.lower() in "aeiou"}
print(f"字符串中的元音字母: {vowels}")

# 给列表元素加 1 并去重
nums = [1, 2, 2, 3, 3, 3, 4]
unique_plus_one = {x + 1 for x in nums}
print(f"加1去重: {unique_plus_one}")


# ==================== 四、lambda 表达式 ====================

print("\n=== lambda 表达式 ===")

# lambda 参数: 返回值 —— 匿名函数，用于简短的逻辑

# 基本用法
add = lambda a, b: a + b
print(f"lambda add(3, 5) = {add(3, 5)}")

# sorted() 与 lambda
students = [
    ("小明", 85),
    ("小红", 92),
    ("小刚", 78),
    ("小美", 95),
]

# 按分数排序（升序）
sorted_by_score = sorted(students, key=lambda s: s[1])
print(f"按分数升序: {sorted_by_score}")

# 按分数排序（降序）
sorted_desc = sorted(students, key=lambda s: s[1], reverse=True)
print(f"按分数降序: {sorted_desc}")


# ==================== 五、map() & filter() & reduce() ====================

print("\n=== map / filter / reduce ===")

# 1. map(func, iterable) —— 对每个元素应用函数
numbers = [1, 2, 3, 4, 5]

doubled = list(map(lambda x: x * 2, numbers))
print(f"map 翻倍: {doubled}")

# 等价于列表推导式
doubled2 = [x * 2 for x in numbers]
print(f"推导式翻倍: {doubled2}")

# 2. filter(func, iterable) —— 筛选满足条件的元素
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"filter 偶数: {evens}")

# 等价于列表推导式
evens2 = [x for x in numbers if x % 2 == 0]

# 3. reduce(func, iterable) —— 累积运算
# 注意：reduce 需要从 functools 导入
from functools import reduce

total = reduce(lambda a, b: a + b, numbers)   # 相当于 ((1+2)+3)+4+5
print(f"reduce 求和: {total}")

# 用 reduce 计算阶乘
factorial = reduce(lambda a, b: a * b, range(1, 6))  # 5! = 120
print(f"reduce 5! = {factorial}")


# ==================== 六、列表推导式 vs map/filter ====================

print("\n=== 列表推导式 vs map/filter ===")

# 实际项目中列表推导式更常用，也更可读
# 但 map/filter 在函数式编程中仍有价值

# 复杂一点的例子
data = [
    {"name": "iPhone", "price": 6999},
    {"name": "iPad", "price": 3499},
    {"name": "MacBook", "price": 9999},
    {"name": "AirPods", "price": 1299},
]

# 筛选出价格 > 3000 的产品名
expensive_products = [
    item["name"]
    for item in data
    if item["price"] > 3000
]
print(f"价格 > 3000 的产品: {expensive_products}")


# ==================== 七、实战：链式操作 ====================

print("\n=== 实战：链式操作 ===")

# 模拟一个数据分析中的常见场景
raw_scores = ["85", "92", "78", "不合格", "95", "88", "100", "65"]

# 任务：将字符串列表转为数字，过滤掉无效数据，然后计算平均分
# 链式写法：
valid_scores = [
    int(s) for s in raw_scores        # 转为整数
    if s.isdigit()                     # 只保留纯数字
]

print(f"原始数据: {raw_scores}")
print(f"有效分数: {valid_scores}")
print(f"平均分: {sum(valid_scores) / len(valid_scores):.1f}")

# 用 map/filter 实现
valid_scores2 = list(
    filter(lambda x: x >= 0,
           map(lambda s: int(s) if s.isdigit() else -1, raw_scores))
)
print(f"map/filter 方式: {valid_scores2}")


# ==================== 练习区 ====================

# 练习1：用列表推导式生成 0~50 之间所有能被 3 整除的数

# 练习2：有一个数字列表 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]，
#        用列表推导式生成每个数的平方，只保留平方大于 20 的结果

# 练习3：有两个列表 names = ["小明","小红","小刚"] 和
#        scores = [85, 92, 78]，用字典推导式生成姓名→分数的字典

# 练习4：用 reduce 计算 1×2×3×...×10（即 10 的阶乘）
