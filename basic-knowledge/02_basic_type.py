# Python3 中常见的数据类型有：
# Number（数字）
# String（字符串）
# bool（布尔类型）
# List（列表）
# Tuple（元组）
# Set（集合）
# Dictionary（字典）

print("------------获取类型名称------------------")
a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))
print(isinstance(a, int))

del a
#  name 'a' is not defined
# print(a)

print("------------String类型------------------")
str = '123456789'
print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第六个的字符（不包含）
print(str[2:])  # 输出从第三个开始后的所有字符
print(str[1:5:2])  # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)  # 输出字符串两次
print(str + '你好')  # 连接字符串



print("------------Bool类型------------------")
a = True
b = False
print(type(a))  # <class 'bool'>
print(type(b))  # <class 'bool'>

# 布尔类型的整数表现
print(int(True))  # 1
print(int(False))  # 0

# 使用 bool() 函数进行转换
print(bool(0))  # False
print(bool(42))  # True
print(bool(''))  # False
print(bool('Python'))  # True
print(bool([]))  # False
print(bool([1, 2, 3]))  # True

# 布尔逻辑运算
print(True and False)  # False
print(True or False)  # True
print(not True)  # False

print("------------List类型------------------")
# 定义的时候使用的是 {}
list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

print(list)  # 打印整个列表
print(list[0])  # 打印列表的第一个元素
print(list[1:3])  # 打印列表第二到第四个元素（不包含第四个元素）
print(list[2:])  # 打印列表从第三个元素开始到末尾
print(tinylist * 2)  # 打印tinylist列表两次
print(list + tinylist)  # 打印两个列表拼接在一起的结果

print("------------Tuple类型------------------")
# 定义的时候使用的是 ()
tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
# 使用* 运算符进行解包
a,*b=tuple
print(b) # [786, 2.23, 'runoob', 70.2]
print(tuple[0])
print(tuple + tuple)
# tuple' object does not support item assignment  tuple不可变
# tuple[0]='123'
# print(tuple)

print("------------Set类型------------------")
# 定义的时候使用的是 {}
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
print(sites)  # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Runoob' in sites:
    print('Runoob 在集合中')
else:
    print('Runoob 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

# {'b', 'c', 'a', 'd', 'r'} 将字符串转换成集合并去重
print(a)

print(a - b)  # a 和 b 的差集
print(a | b)  # a 和 b 的并集
print(a & b)  # a 和 b 的交集
print(a ^ b)  # a 和 b 中不同时存在的元素

print("------------Dictionary类型------------------")
#!/usr/bin/python3

dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}


print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值