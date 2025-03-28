#!/usr/bin/python3

class People:
    # 定义基本属性
    name = ''
    age = 18
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    # 两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类的外部调用
    def __foo(self):
        print('这是私有方法')

    # 实例方法是类中最常见的方法类型，在定义实例方法时，第一个参数通常是self，它代表类的实例对象。
    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))

    # 类方法通过@classmethod装饰器来定义，它的第一个参数通常是cls，代表类本身，而非实例对象。类方法可以访问和修改类的属性，不需要实例化类就可以调用
    @classmethod
    def print_class_variable(cls):
        print(cls.age)

    # 静态方法使用@staticmethod装饰器定义，它不需要self或cls参数。静态方法与类的实例和类本身没有直接关联，只是在逻辑上属于类的一部分。
    @staticmethod
    def add(*args):
        sum = 0;
        for arg in args:
            sum += arg
        return sum
        # return age + __weight # 报错，静态方法不能访问私有变量


p = People('runoob', 10, 30)
p.speak()
# print(p.__weight)  # 报错，实例不能访问私有变量
# p.__foo() # 报错，实例不能访问私有方法
p.print_class_variable()  # 调用类方法 输出的结果依然为 0
People.print_class_variable()  # 调用类方法 输出的结果依然为 0
print(p.add(1, 2, 3))