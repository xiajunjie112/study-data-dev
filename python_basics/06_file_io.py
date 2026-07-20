"""
============================================
第6课：文件读写
============================================
读写文件是数据处理的基础操作。
数据分析中经常需要从 CSV、txt 等文件中读取数据，然后进行处理。
"""

# ==================== 一、打开和读取文件 ====================

print("=== 读取文件 ===")

# 方式1：使用 with 语句（推荐）—— 会自动关闭文件
# 先创建一个示例文件
with open("sample_data.txt", "w", encoding="utf-8") as f:
    f.write("姓名,年龄,城市\n")
    f.write("张三,25,北京\n")
    f.write("李四,30,上海\n")
    f.write("王五,28,广州\n")

print("已创建 sample_data.txt")

# 读取整个文件内容
with open("sample_data.txt", "r", encoding="utf-8") as f:
    content = f.read()          # 一次性读取全部内容
    print(f"--- 文件内容 ---\n{content}")

# 逐行读取 —— 适合大文件
print("--- 逐行读取 ---")
with open("sample_data.txt", "r", encoding="utf-8") as f:
    for line in f:              # f 本身就是可迭代的
        print(repr(line))       # repr() 显示转义字符

# 读取所有行到列表
with open("sample_data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()       # 返回列表，每行一个元素
    print(f"readlines() 结果: {lines}")


# ==================== 二、写入文件 ====================

print("\n=== 写入文件 ===")

# 'w' 模式：覆盖写入（如果文件不存在则创建）
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("这是第一行\n")
    f.write("这是第二行\n")
    f.writelines(["第三行\n", "第四行\n"])  # 写入多行

print("已写入 output.txt")

# 'a' 模式：追加写入（在原文件末尾添加）
with open("output.txt", "a", encoding="utf-8") as f:
    f.write("这是追加的行\n")

# 验证追加结果
with open("output.txt", "r", encoding="utf-8") as f:
    print(f"--- output.txt 内容 ---\n{f.read()}")


# ==================== 三、读取模式详解 ====================

print("\n=== 文件打开模式 ===")

# 常用模式：
# 'r'   读取（默认）
# 'w'   写入（覆盖）
# 'a'   追加
# 'x'   创建新文件（如果已存在则报错）
# 'b'   二进制模式（如图片、视频）
# '+'   读写模式

# 二进制模式示例（读取图片）
# with open("image.jpg", "rb") as f:
#     data = f.read()
#     print(f"图片大小: {len(data)} 字节")


# ==================== 四、使用 with 语句 + 上下文管理器 ====================

print("\n=== with 语句说明 ===")

# with 语句的好处是：即使代码中发生异常，文件也会被正确关闭
# 等同于 try-finally 的简写

# 错误示范（忘记关闭文件）：
# f = open("test.txt", "w")
# f.write("忘记关闭了...")
# # f.close()  ← 忘记这行的话，文件可能没有真正写入

# 正确写法（自动关闭）：
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("with 会自动关闭文件")
# 退出 with 块后，文件自动关闭


# ==================== 五、CSV 文件读写（手动方式） ====================

print("\n=== CSV 文件处理 ===")

# CSV（逗号分隔值）是数据分析中最常见的文件格式之一

# 读取 CSV 文件
students_data = []
with open("sample_data.txt", "r", encoding="utf-8") as f:
    header = f.readline().strip().split(",")    # 读取表头
    print(f"表头: {header}")
    for line in f:
        values = line.strip().split(",")        # 每行数据
        # 将表头和数据组合成字典
        record = dict(zip(header, values))
        students_data.append(record)

print("解析结果:")
for s in students_data:
    print(f"  {s}")

# 写入 CSV 文件
new_data = [
    {"name": "小明", "score": 92, "grade": "A"},
    {"name": "小红", "score": 85, "grade": "B"},
    {"name": "小刚", "score": 78, "grade": "C"},
]

with open("students.csv", "w", encoding="utf-8") as f:
    # 写表头
    headers = list(new_data[0].keys())
    f.write(",".join(headers) + "\n")
    # 写数据行
    for row in new_data:
        f.write(",".join(str(row[h]) for h in headers) + "\n")

print("已创建 students.csv")


# ==================== 六、路径操作（os.path） ====================

print("\n=== 路径操作 ===")

import os

# 检查文件是否存在
print(f"sample_data.txt 存在吗? {os.path.exists('sample_data.txt')}")

# 获取文件信息
if os.path.exists("sample_data.txt"):
    print(f"文件大小: {os.path.getsize('sample_data.txt')} 字节")
    print(f"最后修改时间: {os.path.getmtime('sample_data.txt')}")

# 路径拼接（自动处理不同系统的分隔符）
data_dir = "data"
file_path = os.path.join(data_dir, "sample.txt")
print(f"拼接路径: {file_path}")

# 确保目录存在
if not os.path.exists(data_dir):
    os.makedirs(data_dir)          # 创建目录（含父目录）
    print(f"创建目录: {data_dir}")


# ==================== 综合练习区 ====================

# 练习1：读取 sample_data.txt 中的数据，计算所有人的平均年龄
# 提示：年龄在第二列（索引1），记得转成整数 int()

# 练习2：创建一个名为 diary.txt 的文件，写入你今天的学习心得

# 练习3：读取前面创建的 students.csv 文件，打印出分数大于等于 80 的学生姓名
