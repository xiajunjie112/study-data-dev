"""
============================================
第2课：字符串操作
============================================
字符串是 Python 中最常用的数据类型之一。
对于数据分析来说，字符串处理是非常重要的一项技能。
"""

# ==================== 一、字符串的创建与索引 ====================

print("=== 字符串创建与索引 ===")

# 创建字符串
s = "Hello Python"
print(f"原始字符串: {s}")

# 索引（下标从 0 开始）
print(f"第1个字符 s[0]  = '{s[0]}'")          # H
print(f"第2个字符 s[1]  = '{s[1]}'")          # e
print(f"最后1个字符 s[-1] = '{s[-1]}'")       # n（-1 表示最后一个）
print(f"倒数第2个 s[-2] = '{s[-2]}'")         # o

# 切片 [起始:结束:步长] —— 注意：结束位置不包含在内
print(f"s[0:5]   = '{s[0:5]}'")     # 索引 0~4 -> Hello
print(f"s[6:]    = '{s[6:]}'")      # 索引 6 到结尾 -> Python
print(f"s[:5]    = '{s[:5]}'")      # 开头到索引 4 -> Hello
print(f"s[::-1]  = '{s[::-1]}'")    # 反转字符串 -> nohtyP olleH


# ==================== 二、字符串常用方法 ====================

print("\n=== 字符串常用方法 ===")

text = "  Python数据分析学习  "
print(f"原始字符串: '{text}'")

# 去除空白字符
print(f"strip() 去两端空格: '{text.strip()}'")
print(f"lstrip() 去左端空格: '{text.lstrip()}'")
print(f"rstrip() 去右端空格: '{text.rstrip()}'")

# 大小写转换
msg = "hello, Python!"
print(f"upper() 全大写: '{msg.upper()}'")
print(f"lower() 全小写: '{msg.lower()}'")
print(f"capitalize() 首字母大写: '{msg.capitalize()}'")
print(f"title() 每个单词首字母大写: '{msg.title()}'")

# 查找与替换
sentence = "我爱学习，学习使我快乐"
print(f"原始句子: '{sentence}'")
print(f"find('学习') = {sentence.find('学习')}")       # 返回第一次出现的位置索引
print(f"find('编程') = {sentence.find('编程')}")       # 没找到返回 -1
print(f"replace('学习', '编程'): '{sentence.replace('学习', '编程')}'")

# 判断字符串内容
print(f"'123'.isdigit() = {'123'.isdigit()}")      # 是否全是数字
print(f"'abc'.isalpha() = {'abc'.isalpha()}")      # 是否全是字母
print(f"'abc123'.isalnum() = {'abc123'.isalnum()}")  # 是否全是字母或数字

# 分割与连接
csv_data = "张三,25,北京,工程师"
parts = csv_data.split(",")     # 按逗号分割 → 列表
print(f"split(',') 结果: {parts}")       # ['张三', '25', '北京', '工程师']

joined = " | ".join(parts)      # 用 " | " 连接列表元素
print(f"join() 结果: '{joined}'")        # 张三 | 25 | 北京 | 工程师


# ==================== 三、字符串格式化（三种方式） ====================

print("\n=== 字符串格式化 ===")

name, score = "小明", 92.5

# 方式1：f-string（推荐，Python 3.6+）
print(f"f-string: {name} 的分数是 {score}")

# 方式2：format() 方法
print("format(): {} 的分数是 {}".format(name, score))

# 方式3：% 格式化（旧式）
print("%%格式化: %s 的分数是 %.1f" % (name, score))

# f-string 高级用法
price = 9.9
print(f"价格：{price:.2f} 元")        # 保留两位小数
print(f"百分比：{0.8567:.1%}")        # 转百分比 -> 85.7%
print(f"补零：{42:05d}")              # 补零 -> 00042


# ==================== 四、转义字符与原始字符串 ====================

print("\n=== 转义字符与原始字符串 ===")

# 常用转义字符
print("第一行\n第二行")              # \n 换行
print("制表符\t缩进")                # \t 制表符
print("他说：\"你好\"")              # \" 输出双引号
print("反斜杠：\\")                  # \\ 输出反斜杠

# 原始字符串 r"" —— 忽略转义，常用于文件路径
path = r"C:\Users\name\Documents"
print(f"原始字符串路径: {path}")


# ==================== 五、实战案例：文本数据清洗 ====================

print("\n=== 实战案例：文本数据清洗 ===")

# 模拟从文件或网页抓取的脏数据
raw_data = "  【Python】《数据分析实战》-价格: ￥49.90/本  "
print(f"原始脏数据: '{raw_data}'")

# 数据清洗步骤
cleaned = raw_data.strip()          # 1. 去除首尾空格
cleaned = cleaned.replace("【", "")  # 2. 去除特殊符号
cleaned = cleaned.replace("】", "")
cleaned = cleaned.replace("《", "")
cleaned = cleaned.replace("》", "")
cleaned = cleaned.replace("￥", "¥")  # 3. 统一货币符号

print(f"清洗后: '{cleaned}'")

# 提取有用信息
name_part = cleaned.split("-")[0]            # 书名部分
price_part = cleaned.split("-")[1]           # 价格部分
price_value = price_part.replace("价格: ", "").replace("/本", "")

print(f"书名: {name_part}")
print(f"价格: {price_value}")


# ==================== 练习区 ====================

# 练习1：将字符串 "python data analysis" 转换为每个单词首字母大写
# 提示：使用 .title() 方法

# 练习2：从 "2024-01-15" 中提取年、月、日
# 提示：用 split('-')

# 练习3：反转字符串 "上海自来水来自海上"，判断它是否是对称的（回文）
# 提示：反转用 [::-1]
