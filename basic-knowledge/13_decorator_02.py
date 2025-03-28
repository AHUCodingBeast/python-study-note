def my_decorator(cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)

        def display(self):
            print("在类方法之前执行")
            self.wrapped.display()
            print("在类方法之后执行")

    return Wrapper


@my_decorator
class MyClass:
    def display(self):
        print("这是 MyClass 的 display 方法")


obj = MyClass()
obj.display()


# -----------------------------------------------

# 内置装饰器 python语言中存在一些内置装饰器
class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method.")

    @classmethod
    def class_method(cls):
        print(f"This is a class method of {cls.__name__}.")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


# 使用
MyClass.static_method()
MyClass.class_method()

obj = MyClass()
obj.name = "Alice"
print(obj.name)
