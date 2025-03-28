# var1 是全局名称
var1 = 5

'''
global 关键字：用于在函数内部引用和修改全局作用域中的变量。全局作用域是指在模块顶层定义的变量所在的作用域，这些变量可以在整个模块中被访问。
nonlocal 关键字：用于在嵌套函数的内部函数中引用和修改外部函数（非全局作用域）中的变量。也就是说，它处理的是嵌套函数中的闭包变量。
'''

def some_func():
    # var2 是局部名称
    var2 = 6
    # var1 += 10  无法直接修改全局变量 需要使用global 关键字
    global var1
    var1 += 10;
    print(var1, var2)

    def some_inner_func():
        # 这里修改无效不影响全局变量值 这个var1 相当于是some_inner_func局部变量
        # var1 = 8;

        # var2 += 16  无法直接修改外部函数中的变量 需要使用nonlocal 关键字
        # var2+=16
        nonlocal var2
        var2 = 16

        var3 = 7
        print(var1, var2, var3)

    some_inner_func()
    print(var2)


some_func()
print(var1)
