
# 它接受一个参数 func，这个参数代表被装饰的函数, 装饰器一定会返回一个函数
def my_decorator(func):
    def wrapper():
        print("在原函数之前执行")
        func()
        print("在原函数之后执行")
    return wrapper

# 使用 @my_decorator 语法糖将装饰器应用到 say_hello 函数上，这相当于 say_hello = my_decorator(say_hello)。
@my_decorator
def say_hello():
    print("Hello!")

say_hello()


'''
repeat 函数是一个装饰器工厂，它接受一个参数 num_times，返回一个装饰器 decorator。
decorator 接受一个函数 func，并返回一个 wrapper 函数。wrapper 函数会调用 func 函数 num_times 次。
使用 @repeat(3) 装饰 say_hello 函数后，调用 say_hello 会打印 "Hello!" 三次。
'''
def repeat(num_times):
    def decorator(funct):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                funct(*args, **kwargs)
        return wrapper
    return decorator

#  等价于这样执行了这样的函数  repeat(3)(say_hello)
@repeat(3)
def say_hello():
    print("Hello!")

say_hello()


# 多个装饰器

def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper

@decorator1
@decorator2
def say_hello():
    print("Hello!")

say_hello()