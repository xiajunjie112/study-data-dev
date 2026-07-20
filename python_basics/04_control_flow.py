"""
============================================
第4课：条件判断与循环
============================================
控制流让程序能做决策和重复执行，
是编程逻辑的核心。
"""

# ==================== 一、if / elif / else 条件判断 ====================

print("=== 条件判断 ===")

# 基本结构
score = 85

if score >= 90:
    grade = "优秀"
elif score >= 80:
    grade = "良好"
elif score >= 70:
    grade = "中等"
elif score >= 60:
    grade = "及格"
else:
    grade = "不及格"

print(f"分数: {score} → 等级: {grade}")

# 条件判断中的"真值"—— Python 中很多值可以当作布尔值使用
# 以下值被视为 False：
#   False, 0, 0.0, ""(空字符串), [](空列表), {}(空字典), None
print("\n真值测试:")
for val in [0, 1, "", "Hello", [], [1, 2], None]:
    if val:        # 等价于 if bool(val) == True
        print(f"  ✅ True: {repr(val)}")
    else:
        print(f"  ❌ False: {repr(val)}")

# 多条件组合
age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("\n✅ 可以入场（年满18岁且有票）")
else:
    print("\n❌ 无法入场")

# 条件表达式（三元运算符）—— 简单 if-else 的简写
x = 10
result = "正数" if x > 0 else "非正数"
print(f"\n条件表达式: {x} 是 {result}")


# ==================== 二、for 循环 ====================

print("\n=== for 循环 ===")

# 1. 遍历列表
fruits = ["苹果", "香蕉", "橘子"]
print("遍历水果列表:")
for fruit in fruits:
    print(f"  - {fruit}")

# 2. 使用 range() —— 生成数字序列
print("\nrange(5):")
for i in range(5):           # 0, 1, 2, 3, 4
    print(f"  i = {i}")

print("\nrange(1, 10, 2):")    # 起始1，结束9，步长2
for i in range(1, 10, 2):    # 1, 3, 5, 7, 9
    print(f"  i = {i}")

# 3. 遍历字典
student = {"name": "小红", "age": 20, "score": 95}
print("\n遍历字典:")
for key, value in student.items():
    print(f"  {key}: {value}")

# 4. enumerate() —— 同时获取索引和值
print("\nenumerate 遍历:")
for idx, fruit in enumerate(fruits):
    print(f"  索引 {idx} → {fruit}")


# ==================== 三、while 循环 ====================

print("\n=== while 循环 ===")

# while 循环在条件为 True 时持续执行
count = 0
while count < 5:
    print(f"  第 {count + 1} 次循环")
    count += 1        # 必须更新条件变量，否则会无限循环！

# break —— 跳出整个循环
print("\nbreak 示例:")
for i in range(10):
    if i == 5:
        print(f"  遇到 {i}，跳出循环！")
        break
    print(f"  i = {i}")

# continue —— 跳过本次循环，继续下一次
print("\ncontinue 示例（跳过偶数）:")
for i in range(10):
    if i % 2 == 0:       # 如果 i 是偶数
        continue          # 跳过，不打印
    print(f"  i = {i}")

# else 子句 —— 循环正常结束（没有被 break）时执行
print("\nfor-else 示例:")
for i in range(3):
    print(f"  i = {i}")
else:
    print("  循环正常结束！")


# ==================== 四、嵌套循环 ====================

print("\n=== 嵌套循环 ===")

# 打印九九乘法表
print("九九乘法表:")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i*j:2d}", end="  ")
    print()    # 换行


# ==================== 五、列表推导式（简洁的循环） ====================

print("\n=== 列表推导式 ===")

# 传统写法：生成 0~9 的平方
squares = []
for i in range(10):
    squares.append(i ** 2)
print(f"传统写法: {squares}")

# 列表推导式 —— 一行搞定
squares2 = [i ** 2 for i in range(10)]
print(f"推导式:   {squares2}")

# 带条件的列表推导式
evens = [i for i in range(20) if i % 2 == 0]
print(f"0~19中的偶数: {evens}")

# 字符串处理
names = [" 小明 ", "小红", " 小刚 "]
cleaned = [name.strip() for name in names]
print(f"去除空格: {cleaned}")


# ==================== 六、实战：数据筛选与统计 ====================

print("\n=== 实战：数据筛选与统计 ===")

# 模拟一组温度数据（单位：℃）
temperatures = [23.5, 18.2, 31.8, 27.1, 15.6, 29.4, 22.0, 35.2, 19.8, 26.7]

print(f"温度数据: {temperatures}")

# 找出所有超过 30℃ 的高温天
hot_days = [t for t in temperatures if t > 30]
print(f"高温天（>30℃）: {hot_days}")

# 计算平均温度
avg_temp = sum(temperatures) / len(temperatures)
print(f"平均温度: {avg_temp:.1f}℃")

# 温度等级分类
for temp in temperatures:
    if temp >= 30:
        level = "🔥 高温"
    elif temp >= 20:
        level = "☀️ 舒适"
    else:
        level = "❄️ 偏冷"
    print(f"  {temp:5.1f}℃ → {level}")


# ==================== 练习区 ====================

# 练习1：用 for 循环计算 1 到 100 的总和
# 提示：用 range(1, 101)

# 练习2：有一组分数 [65, 78, 92, 45, 88, 56, 73, 95]，
#        用列表推导式筛选出所有及格（>=60）的分数

# 练习3：用嵌套循环打印一个 5×5 的矩阵，每个元素为行号×列号
# 预期输出：
#   1  2  3  4  5
#   2  4  6  8 10
#   3  6  9 12 15
#   4  8 12 16 20
#   5 10 15 20 25
