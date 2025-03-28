import os
import glob
import sys
import re
import math
import random
import datetime

from urllib.request import urlopen

# 获取当前工作目录
current_dir = os.getcwd()
print("当前工作目录:", current_dir)

# 列出目录下的文件
files = os.listdir(current_dir)
print("目录下的文件:", files)

# glob 模块提供了一个函数用于从目录通配符搜索中生成文件列表:
print(glob.glob('*.py'))

#  给出命令行参数列表
print(sys.argv)

# 输出到标准错误
sys.stderr.write('Warning, log file not found starting a new one\n')

# 正则匹配 输出所有以f 开头的单词
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')

# 数学运算
math.cos(math.pi / 4)

# 随机数
random.choice(['apple', 'pear', 'banana'])
random.sample(range(100), 10)
random.random()
random.randrange(6)

# 日期
# 获取当前日期和时间
current_datetime = datetime.datetime.now()
print(current_datetime)

# 获取当前日期
current_date = datetime.date.today()
print(current_date)

# 格式化日期
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_datetime)  # 输出：2023-07-17 15:30:45


# 网络
url = 'https://www.baidu.com'
response = urlopen(url)
print(response.read().decode('utf-8'))