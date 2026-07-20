"""
============================================
第1课：变量与数据类型
============================================
Python 中的变量不需要声明类型，直接赋值即可。
常见数据类型：整数(int)、浮点数(float)、字符串(str)、布尔型(bool)、空值(None)
"""

# ==================== 一、变量赋值 ====================

# Python 使用 = 来给变量赋值
name = "小明"       # 字符串类型
age = 25            # 整数类型
height = 1.75       # 浮点数类型
is_student = True   # 布尔类型

# 用 print() 打印变量的值
print("=== 变量赋值 ===")
print(name)         # 输出：小明
print(age)          # 输出：25
print(height)       # 输出：1.75
print(is_student)   # 输出：True

# 变量可以被重新赋值为不同类型的值（动态类型）
age = "二十五岁"    # 原来 age 是整数，现在变成了字符串
print(f"age 变成了字符串: {age}")


# ==================== 二、常用数据类型 ====================

print("\n=== 数据类型示例 ===")

# 1. 整数 (int)
a = 10
b = -5
c = 0
print(f"整数: a={a}, b={b}, c={c}")

# 2. 浮点数 (float) —— 带小数点的数字
pi = 3.14159
temperature = -2.5
print(f"浮点数: pi={pi}, 温度={temperature}")

# 3. 字符串 (str) —— 用单引号或双引号包围
greeting = "你好，世界！"
quote = 'Python 是一门优雅的语言'
multiline = """这是一个
包含多行文本的
多行字符串"""
print(f"字符串: {greeting}")
print(f"多行字符串:\n{multiline}")

# 4. 布尔型 (bool) —— 只有 True 和 False
is_raining = False
is_sunny = True
print(f"布尔值: is_raining={is_raining}, is_sunny={is_sunny}")

# 5. 空值 (None) —— 表示"没有值"或"空"
result = None
print(f"空值: result={result}")


# ==================== 三、类型检查与转换 ====================

print("\n=== 类型检查与转换 ===")

# type() 函数可以查看变量的类型
print(f"type(10)  -> {type(10)}")            # <class 'int'>
print(f"type(3.14) -> {type(3.14)}")          # <class 'float'>
print(f"type('Hi') -> {type('Hi')}")          # <class 'str'>
print(f"type(True) -> {type(True)}")          # <class 'bool'>

# 类型转换
x = "100"
y = int(x)       # 字符串 → 整数
z = float(x)     # 字符串 → 浮点数
print(f"int('100') = {y}, float('100') = {z}")

# 常用的类型转换函数
print(int(3.9))     # 浮点数 → 整数（向下取整），输出：3
print(float(5))     # 整数 → 浮点数，输出：5.0
print(str(123))     # 整数 → 字符串，输出："123"
print(bool(1))      # 1 转换为 True，0 转换为 False


# ==================== 四、基本运算 ====================

print("\n=== 基本运算 ===")

# 算术运算
x, y = 10, 3
print(f"x={x}, y={y}")
print(f"加法 x + y = {x + y}")       # 13
print(f"减法 x - y = {x - y}")       # 7
print(f"乘法 x * y = {x * y}")       # 30
print(f"除法 x / y = {x / y}")       # 3.333...（结果是浮点数）
print(f"整除 x // y = {x // y}")     # 3（向下取整）
print(f"取余 x %% y = {x % y}")       # 1
print(f"乘方 x ** y = {x ** y}")     # 1000

# 字符串运算
s1 = "Hello"
s2 = "World"
print(f"字符串拼接: {s1 + ' ' + s2}")    # Hello World
print(f"字符串重复: {'Ha' * 3}")          # HaHaHa

# 比较运算（结果都是布尔值）
print(f"10 > 3 : {10 > 3}")     # True
print(f"10 == 3: {10 == 3}")    # False（注意：== 是比较，= 是赋值）
print(f"10 != 3: {10 != 3}")    # True


# ==================== 五、f-string 格式化输出 ====================

print("\n=== f-string 格式化输出 ===")

# f-string 是 Python 3.6+ 最推荐的字符串格式化方式
name = "小红"
score = 95.5
print(f"姓名：{name}，分数：{score}")

# 控制小数位数
pi = 3.1415926535
print(f"π ≈ {pi:.2f}")      # 保留2位小数 -> 3.14
print(f"π ≈ {pi:.4f}")      # 保留4位小数 -> 3.1416

# 对齐输出
print(f"|{'左对齐':<10}|")    # < 左对齐，宽度10
print(f"|{'右对齐':>10}|")    # > 右对齐，宽度10
print(f"|{'居中':^10}|")      # ^ 居中，宽度10


# ==================== 六、综合小练习 ====================

print("\n=== 综合练习：个人信息卡片 ===")

# 定义个人信息
my_name = "张三"
my_age = 28
my_height = 1.78
is_employed = True

# 用 f-string 生成格式化输出
info_card = f"""
╔══════════════════════╗
║      个人信息卡片       ║
╠══════════════════════╣
║ 姓名  : {my_name:<8} ║
║ 年龄  : {my_age:<8} ║
║ 身高  : {my_height:<8.2f} ║
║ 在职  : {str(is_employed):<8} ║
╚══════════════════════╝
"""
print(info_card)


# ==================== 练习区（取消注释即可运行） ====================

# 练习1：定义三个变量，分别存储你的姓名、年龄和身高，然后用 f-string 输出一句话
# 例如："我叫XX，今年XX岁，身高XX米"
name = '夏俊杰'
age = 22
hight = 1.65
print(f"我叫{name}，今年{age}岁，身高{hight}米")

# 练习2：计算半径为 5 的圆的面积（π 取 3.14），公式：面积 = π * r²
# 提示：r = 5; area = 3.14 * r ** 2
r = 5
pai = 3.14
print(f"圆的面积是：{pai * r ** 2}")


# 练习3：将字符串 "123" 转换为整数，加 100 后再转回字符串输出
numstr = "123"
num = int(numstr) + 100
print(f"结果是：{num}")
