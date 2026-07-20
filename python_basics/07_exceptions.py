"""
============================================
第7课：异常处理
============================================
程序运行时难免会出错。异常处理就是提前预判可能的错误，
并优雅地处理它们，避免程序崩溃。
"""

# ==================== 一、常见的异常类型 ====================

print("=== 常见异常类型 ===")

# Python 中常见的异常（错误）类型：

# ZeroDivisionError —— 除以零
# print(10 / 0)  ← 取消注释会报错

# ValueError —— 值错误
# int("abc")     ← 无法将 "abc" 转为整数

# TypeError —— 类型错误
# "hello" + 123  ← 字符串不能和数字直接相加

# IndexError —— 索引越界
# lst = [1, 2, 3]; lst[10]

# KeyError —— 字典键不存在
# d = {"name": "小红"}; d["age"]

# FileNotFoundError —— 文件不存在
# open("不存在的文件.txt", "r")


# ==================== 二、try-except 捕获异常 ====================

print("\n=== try-except 捕获异常 ===")

# 基本结构
def safe_divide(a, b):
    """安全除法：捕获除零错误"""
    try:
        result = a / b
        print(f"{a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        print(f"错误：除数不能为零！({a} / {b})")
        return None

safe_divide(10, 2)     # 正常执行
safe_divide(10, 0)     # 捕获到 ZeroDivisionError

# 捕获多种异常
def parse_number(text):
    """将字符串转为数字，处理多种错误"""
    try:
        num = int(text)
        print(f"'{text}' → 数字 {num}")
        return num
    except ValueError:
        print(f"错误：'{text}' 不是一个有效的数字")
    except TypeError:
        print(f"错误：输入类型不匹配")

parse_number("42")       # 正常
parse_number("abc")      # ValueError
parse_number(None)       # TypeError


# ==================== 三、捕获所有异常 ====================

print("\n=== 捕获所有异常 ===")

# 使用 except: 或 except Exception as e: 捕获所有异常
# 但最好只捕获你知道的特定异常，避免隐藏 bug

try:
    x = int("abc")    # 会触发 ValueError
    y = 10 / 0        # 会触发 ZeroDivisionError
except ValueError as e:
    print(f"值错误: {e}")
except ZeroDivisionError as e:
    print(f"除零错误: {e}")
except Exception as e:           # 捕获所有其他异常
    print(f"未知错误: {e}, 类型: {type(e).__name__}")


# ==================== 四、else 和 finally ====================

print("\n=== else 和 finally ===")

# try-except-else-finally 完整结构
def process_file(filename):
    """尝试读取文件"""
    try:
        f = open(filename, "r", encoding="utf-8")
        content = f.read()
    except FileNotFoundError:
        print(f"❌ 文件 '{filename}' 不存在")
    except PermissionError:
        print(f"❌ 没有权限读取 '{filename}'")
    else:
        # 没有发生异常时执行
        print(f"✅ 成功读取文件，共 {len(content)} 个字符")
        return content
    finally:
        # 无论是否发生异常，都会执行
        print(f"  [finally] 清理操作完成")
        if 'f' in locals() and not f.closed:
            f.close()

# 测试
process_file("sample_data.txt")      # 存在文件
process_file("不存在.txt")            # 不存在文件

print("\n--- finally 的典型用途 ---")
print("finally 常用于：关闭文件、关闭数据库连接、释放资源等")


# ==================== 五、主动抛出异常（raise） ====================

print("\n=== 主动抛出异常 ===")

def set_age(age):
    """设置年龄，验证输入有效性"""
    if not isinstance(age, (int, float)):
        raise TypeError(f"年龄必须是数字，而不是 {type(age).__name__}")
    if age < 0 or age > 150:
        raise ValueError(f"年龄必须在 0~150 之间，你输入了 {age}")
    print(f"✅ 年龄设置成功: {age}")
    return age

# 正确的调用
set_age(25)

# 错误的调用（会被捕获）
try:
    set_age(-5)
except ValueError as e:
    print(f"捕获到错误: {e}")


# ==================== 六、自定义异常类 ====================

print("\n=== 自定义异常 ===")

# 可以创建自己的异常类型，让代码更有语义

class InsufficientBalanceError(Exception):
    """余额不足异常"""
    pass

def withdraw(balance, amount):
    """从账户取款"""
    if amount > balance:
        raise InsufficientBalanceError(
            f"余额不足！当前余额: {balance}，想取: {amount}"
        )
    new_balance = balance - amount
    print(f"取款 {amount} 成功，剩余余额: {new_balance}")
    return new_balance

# 测试
try:
    withdraw(500, 200)    # 成功
    withdraw(300, 500)    # 触发自定义异常
except InsufficientBalanceError as e:
    print(f"❌ {e}")


# ==================== 七、实战：健壮的 CSV 读取 ====================

print("\n=== 实战：健壮的 CSV 读取 ===")

def read_csv_safe(filename):
    """
    安全地读取 CSV 文件
    返回: (成功标志, 数据列表或错误信息)
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        return False, f"文件 '{filename}' 未找到"
    except PermissionError:
        return False, f"无权限读取 '{filename}'"
    except Exception as e:
        return False, f"读取文件时出错: {e}"

    if not lines:
        return False, "文件为空"

    try:
        header = lines[0].strip().split(",")
        data = []
        for i, line in enumerate(lines[1:], start=2):
            values = line.strip().split(",")
            if len(values) != len(header):
                print(f"  ⚠️ 第 {i} 行列数不匹配，已跳过")
                continue
            record = dict(zip(header, values))
            data.append(record)
        return True, data
    except Exception as e:
        return False, f"解析 CSV 时出错: {e}"

# 测试
success, result = read_csv_safe("sample_data.txt")
if success:
    print(f"✅ 成功读取 {len(result)} 条记录:")
    for r in result:
        print(f"  {r}")
else:
    print(f"❌ {result}")


# ==================== 练习区 ====================

# 练习1：写一个函数 get_list_element(lst, index)，安全地获取列表元素，
#        如果索引越界，返回 None 并打印友好提示

# 练习2：写一个函数 calc_bmi(weight, height) 计算 BMI，
#        参数必须为正数，否则抛出 ValueError

# 练习3：写一个函数 divide_all(numbers, divisor)，
#        对列表中每个数执行除法，捕获 ZeroDivisionError 和 TypeError，
#        将异常的元素用 None 代替，返回新列表
