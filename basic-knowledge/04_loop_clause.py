"""
while循环 介绍
"""

n = 1
while n < 3:
    print(n)
    n = n + 1

# 无限循环
# while True:
#     num=input("输入一个数字吧")
#     print(num)


count = 0
while count < 5:
    print(count, " 小于 5")
    count = count + 1
else:
    print(count, " 大于或等于 5")

"""
for循环 介绍
"""

sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    print(site)

word = 'runoob'

sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    # 正常循环结束之后这里会执行 但是这里用了break 所以不会执行
    print("没有循环数据!")
print("完成循环!")

sites = ["Baidu", "Google", "Runoob", "Taobao"]
for index in range(len(sites)):
    print(index, sites[index])

"""
for循环 对于元组和列表以及字典的一些特殊遍历技巧
"""
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue','red']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)