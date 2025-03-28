#!/usr/bin/python3


import sys
# 我们自己定义的模块起名字不要用中划线，需要使用下划线，否则无法导入
# import data_structure

from data_structure import Queue as MyQueue

print('命令行参数如下:')
for i in sys.argv:
    print(i)
# sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表。
print('模块查找路径为:')
for e in sys.path:
    print(e)

queue = MyQueue()
queue.enqueue('a')
queue.enqueue('b')
queue.enqueue('c')
print("队首元素:", queue.peek())


# 如果我们想在模块 被引入 时，模块中的某一程序块不执行，我们可以用 __name__ 属性来使该程序块仅在该模块自身运行时执行
# @see data_structure.py。

# 获取目标模块定义的属性和方法
for i,e in enumerate(dir(sys)):
    print(i,e)

# 获取当前模块定义的属性
for i,e in enumerate(dir()):
    print(i,e)