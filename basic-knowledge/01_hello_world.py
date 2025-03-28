#!/usr/bin/python3
# 在脚本顶部添加上面命令可以让Python脚本可以像SHELL脚本一样可直接执行：
import sys

print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
print('站点列表 {0}, {1}, 和 {other}'.format('Google', 'Runoob', other='Taobao'))

sites = ['Google', 'Runoob', 'Taobao']
print(f'站点列表 {sites[0]}, {sites[1]}, 和 {sites[2]}')

print('------------------------------')
x = 'Hello World!'
sys.stdout.write(x + '\n')
# input("\n\n按下 enter 键后退出。")
sys.stdout.write(" hi ")
print(x)  # 换行输出
print(x, end=" ")  # 不换行输出

str = '''
曾经有个菇凉叫小芳
  小芳是个小公主
   小公主是个小公主
'''
# str中的格式会得以保留 原样输出
print(str)
