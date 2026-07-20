"""
============================================
第5课：函数
============================================
函数是组织代码的基本单元，可以把重复的逻辑封装起来。
掌握函数 = 学会"一次编写，多次使用"。
"""

# ==================== 一、定义和调用函数 ====================

print("=== 函数的定义与调用 ===")

# 用 def 关键字定义函数
def greet(name):
    """向指定的人打招呼"""  # 这就是文档字符串（docstring）
    return f"你好，{name}！"

# 调用函数
message = greet("小明")
print(message)


# ==================== 二、参数类型详解 ====================

print("\n=== 参数类型 ===")

# 1. 位置参数 —— 按顺序传递
def introduce(name, age, city):
    return f"我叫{name}，今年{age}岁，来自{city}"

print(introduce("小红", 20, "北京"))

# 2. 默认参数 —— 给参数提供默认值
def power(base, exp=2):
    """计算 base 的 exp 次方，默认平方"""
    return base ** exp

print(f"power(3)   = {power(3)}")       # 3² = 9
print(f"power(3, 4) = {power(3, 4)}")   # 3⁴ = 81

# 3. 关键字参数 —— 明确指定参数名，顺序可以随意
print(introduce(city="上海", age=25, name="小刚"))

# 4. *args —— 接收任意数量的位置参数
def sum_all(*numbers):
    """计算任意多个数的总和"""
    total = 0
    for n in numbers:
        total += n
    return total

print(f"sum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
print(f"sum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")

# 5. **kwargs —— 接收任意数量的关键字参数
def print_info(**info):
    """打印任意键值对信息"""
    for key, value in info.items():
        print(f"  {key}: {value}")

print("print_info 示例:")
print_info(name="张三", age=30, job="工程师")


# ==================== 三、返回值 ====================

print("\n=== 返回值 ===")

# 函数可以返回多个值（实际上返回的是元组）
def get_min_max(numbers):
    """返回列表的最小值和最大值"""
    return min(numbers), max(numbers)

nums = [3, 7, 1, 9, 4, 2]
min_val, max_val = get_min_max(nums)    # 元组拆包接收
print(f"列表: {nums}")
print(f"最小值: {min_val}, 最大值: {max_val}")

# 没有 return 语句的函数返回 None
def say_hello(name):
    print(f"你好，{name}")

result = say_hello("测试")
print(f"没有 return 的函数返回: {result}")


# ==================== 四、作用域（变量可见范围） ====================

print("\n=== 变量作用域 ===")

global_var = "我是全局变量"   # 全局作用域

def scope_demo():
    local_var = "我是局部变量"  # 局部作用域：只能在函数内部访问
    global global_var          # 声明要修改全局变量
    global_var = "函数内修改了全局变量"
    print(f"  函数内部: {local_var}")
    return local_var

scope_demo()
print(f"  函数外部: {global_var}")


# ==================== 五、lambda 匿名函数 ====================

print("\n=== lambda 匿名函数 ===")

# lambda 是简短的匿名函数，一般用作参数传递
# 语法：lambda 参数: 表达式

# 普通函数
def double(x):
    return x * 2

# 等价的 lambda
double_lambda = lambda x: x * 2

print(f"普通函数: double(5) = {double(5)}")
print(f"lambda:   double(5) = {double_lambda(5)}")

# lambda 常用于 sorted()、filter()、map() 等
students = [
    {"name": "小明", "score": 85},
    {"name": "小红", "score": 92},
    {"name": "小刚", "score": 78},
]

# 按分数排序
sorted_students = sorted(students, key=lambda s: s["score"], reverse=True)
print("按分数从高到低排序:")
for s in sorted_students:
    print(f"  {s['name']}: {s['score']}分")


# ==================== 六、函数作为参数 ====================

print("\n=== 函数作为参数 ===")

# 函数可以作为参数传递给另一个函数 —— 这是 Python 的重要特性

def apply_operation(x, y, operation):
    """对 x, y 应用指定的操作函数"""
    return operation(x, y)

# 定义不同的操作
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

print(f"apply(add, 10, 5)      = {apply_operation(10, 5, add)}")
print(f"apply(multiply, 10, 5) = {apply_operation(10, 5, multiply)}")
print(f"apply(lambda 求最大值, 10, 5) = {apply_operation(10, 5, lambda a, b: a if a > b else b)}")


# ==================== 七、实战：数据分析函数 ====================

print("\n=== 实战：数据分析函数 ===")

def describe_data(data):
    """
    计算一组数据的描述性统计信息
    参数: data 是数字列表
    返回: 包含统计信息的字典
    """
    if not data:
        return {"error": "数据为空"}

    n = len(data)
    total = sum(data)
    mean = total / n
    sorted_data = sorted(data)

    # 中位数
    if n % 2 == 1:
        median = sorted_data[n // 2]
    else:
        median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2

    # 方差
    variance = sum((x - mean) ** 2 for x in data) / n

    return {
        "个数": n,
        "总和": total,
        "平均值": round(mean, 2),
        "中位数": round(median, 2),
        "最小值": min(data),
        "最大值": max(data),
        "方差": round(variance, 2),
        "标准差": round(variance ** 0.5, 2),
    }

# 测试
data = [12, 15, 18, 20, 22, 25, 28, 30, 35, 40]
stats = describe_data(data)
print(f"数据: {data}")
print("描述性统计结果:")
for key, value in stats.items():
    print(f"  {key}: {value}")


# ==================== 练习区 ====================

# 练习1：写一个函数 is_palindrome(s) 判断字符串是否是回文
# 提示：反转字符串看是否等于原串

# 练习2：写一个函数 calculate(a, b, operator) 实现简单计算器
# operator 可以是 '+', '-', '*', '/'

# 练习3：写一个函数 filter_by_threshold(values, threshold)，
#        返回列表中大于 threshold 的所有元素
