"""
============================================
第3课：列表、元组、字典、集合
============================================
Python 的四种核心容器类型，用于存储和操作多个数据。
数据分析中大量使用这些结构来组织和处理数据。
"""

# ==================== 一、列表 (list) ====================

print("=== 列表 (list) ===")

# 列表用方括号 [] 定义，可以存放不同类型的元素
fruits = ["苹果", "香蕉", "橘子", "葡萄"]
print(f"原始列表: {fruits}")

# 1. 访问与切片（和字符串一样）
print(f"fruits[0]   = '{fruits[0]}'")       # 第一个元素
print(f"fruits[-1]  = '{fruits[-1]}'")      # 最后一个元素
print(f"fruits[1:3] = {fruits[1:3]}")       # 切片：索引 1~2

# 2. 修改列表（列表可变）
fruits[0] = "草莓"                # 修改元素
print(f"修改后: {fruits}")

# 3. 常用方法
fruits.append("芒果")              # 末尾追加
print(f"append('芒果'): {fruits}")

fruits.insert(1, "西瓜")           # 指定位置插入
print(f"insert(1, '西瓜'): {fruits}")

fruits.remove("香蕉")              # 删除第一个匹配项
print(f"remove('香蕉'): {fruits}")

popped = fruits.pop()              # 弹出末尾元素
print(f"pop() 弹出: '{popped}', 剩余: {fruits}")

# 4. 排序
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()                     # 原地升序排序
print(f"sort() 排序: {numbers}")

numbers.sort(reverse=True)         # 降序
print(f"降序排列: {numbers}")

# 5. 列表长度与存在性检查
print(f"列表长度: {len(fruits)}")
print(f"'苹果' 在列表中吗? {'苹果' in fruits}")


# ==================== 二、元组 (tuple) ====================

print("\n=== 元组 (tuple) ===")

# 元组用圆括号 () 定义，创建后不可修改（不可变）
point = (3, 5)
print(f"坐标点: {point}")
print(f"x = {point[0]}, y = {point[1]}")

# 元组可以不加括号（逗号是关键）
colors = "红", "绿", "蓝"
print(f"颜色元组: {colors}")

# 元组拆包 —— 非常实用的特性
x, y = point      # 将元组中的值分别赋给 x 和 y
print(f"拆包: x={x}, y={y}")

# 交换两个变量的值（元组拆包的妙用）
a, b = 10, 20
a, b = b, a
print(f"交换后: a={a}, b={b}")

# 元组不可变（没有 append、remove 等方法）
# tuple[0] = 99  ← 这行会报错！元组不能被修改


# ==================== 三、字典 (dict) ====================

print("\n=== 字典 (dict) ===")

# 字典用花括号 {} 定义，存储键值对，类似现实中的"字典"查词
# 在数据分析中，字典常用于表示一条记录
student = {
    "name": "小红",
    "age": 20,
    "score": 95.5,
    "city": "北京"
}
print(f"学生信息: {student}")

# 1. 访问字典
print(f"姓名: {student['name']}")       # 通过键获取值
print(f"年龄: {student.get('age')}")     # get() 方法，键不存在返回 None
print(f"性别: {student.get('gender', '未知')}")  # 不存在时提供默认值

# 2. 修改和添加
student["score"] = 98.0           # 修改已有键的值
student["gender"] = "女"          # 添加新的键值对
print(f"更新后: {student}")

# 3. 删除
del student["city"]               # 删除指定键值对
removed = student.pop("gender")   # 删除并返回值
print(f"删除 'gender'='{removed}', 剩余: {student}")

# 4. 遍历字典
print("\n遍历字典:")
for key, value in student.items():
    print(f"  {key} → {value}")

# 只遍历键或值
print(f"所有键: {list(student.keys())}")
print(f"所有值: {list(student.values())}")


# ==================== 四、集合 (set) ====================

print("\n=== 集合 (set) ===")

# 集合用花括号 {} 定义，元素无序且不重复
# 常用于：去重、集合运算（交并差）
unique_numbers = {1, 2, 2, 3, 3, 3, 4}
print(f"集合（自动去重）: {unique_numbers}")  # {1, 2, 3, 4}

# 列表去重
scores = [85, 90, 85, 75, 90, 100]
unique_scores = list(set(scores))
print(f"列表去重: {scores} → {unique_scores}")

# 集合运算
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(f"集合 A: {a}")
print(f"集合 B: {b}")
print(f"交集 A & B: {a & b}")      # 两者都有的元素
print(f"并集 A | B: {a | b}")      # 所有元素（去重）
print(f"差集 A - B: {a - b}")      # 在 A 不在 B 的元素


# ==================== 五、实战：学生成绩管理 ====================

print("\n=== 实战：学生成绩管理 ===")

# 用列表嵌套字典来表示数据（类似表格）
students = [
    {"name": "小明", "chinese": 85, "math": 92, "english": 78},
    {"name": "小红", "chinese": 92, "math": 88, "english": 95},
    {"name": "小刚", "chinese": 78, "math": 95, "english": 82},
]

# 计算每个学生的总分和平均分
print(f"{'姓名':<6}{'语文':<6}{'数学':<6}{'英语':<6}{'总分':<6}{'平均分':<6}")
print("-" * 42)

for s in students:
    total = s["chinese"] + s["math"] + s["english"]
    avg = total / 3
    print(f"{s['name']:<6}{s['chinese']:<6}{s['math']:<6}"
          f"{s['english']:<6}{total:<6}{avg:<6.1f}")

# 找出数学最高分
math_scores = [s["math"] for s in students]   # 列表推导式（后面会详细学）
top_math = max(math_scores)
top_student = [s["name"] for s in students if s["math"] == top_math]
print(f"\n数学最高分: {top_math} 分，由 {top_student} 获得")


# ==================== 练习区 ====================

# 练习1：创建一个包含 5 个城市名称的列表，在末尾追加一个新城市，然后删除第2个城市

# 练习2：有一个字典 {"apple": 5, "banana": 3, "orange": 8}，打印所有商品名和数量

# 练习3：两个列表 list1 = [1, 2, 3, 4, 5] 和 list2 = [4, 5, 6, 7, 8]，
#        找出它们的共同元素（交集）
#        提示：转成集合用 & 运算
