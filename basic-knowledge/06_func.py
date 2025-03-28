print("---------传值还是传引用----------")


def change(a):
    print(id(a))  # 指向的是同一个对象
    a = 10  # 看起来像是修改了a的值 但是对外部变量无影响 这里相当于定义了一个新的a
    print(id(a))  # 一个新对象


a = 1
print(id(a))
change(a)


def changeme(mylist):
    "修改传入的列表"
    # mylist.append([1, 2, 3, 4])
    mylist += [1, 2, 3, 4]
    print("函数内取值: ", mylist)
    return


# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值: ", mylist)


# 带有默认值的函数
def printinfo(name, age=35):
    print("名字: ", name)
    print("年龄: ", age)
    return


printinfo(age=50, name="runoob")
printinfo(name="runoob")


# 带有可变长参数的函数
def printinfo(arg1, *vartuple):
    print("输出: ")
    print(arg1)
    # vartuple就是个元组
    print(vartuple)
    print(type(vartuple))


printinfo(70, 60, 50)


# 带有可变长参数的字典传参
def printinfo(arg1, **vardict):
    print("输出: ")
    print(arg1)
    print(vardict)


printinfo(1, a=2, b=3)

# lambda函数
sum = lambda arg1, arg2: arg1 + arg2
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))


# 任意参数的函数 调用这个函数可以随意传参
def anyParamFunc(*args, **kwargs):
    print(args)
    print(kwargs)


anyParamFunc(1, 2, 3, a=1, b=2)
print("----")
anyParamFunc(a=1, b=2)
print("----")
anyParamFunc()
print("----")


def sum(*args) -> int:
    res = 0
    for arg in args:
        res += arg
    return res


print(sum(1, 2, 3))
# print(sum([1,2,3])) 这样传递参数会报错，需要参数解包
print(sum(*[1, 2, 3]))
