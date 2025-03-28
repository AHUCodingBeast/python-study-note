# 定义父类
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} is Animal 发出声音")


# 定义子类，继承自 Animal 类
class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    # 重写父类的 speak 方法
    def speak(self):
        # 调用父类的 speak 方法
        super().speak()
        print(f"{self.name} 汪汪叫")

    def bark(self):
        print(f"{self.name} 汪汪叫")


# 创建 Dog 类的实例
dog = Dog("旺财")
dog.speak()
dog.bark()

# 使用 super(type, obj) 时，obj 必须是 type 类或其子类的实例，否则会引发异常。
super(Dog, dog).speak()
