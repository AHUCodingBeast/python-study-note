# 为变量指定类型
name: str = "John"
age: int = 25
is_student: bool = True


def add_numbers(a: int, b: int) -> int:
    return a + b

def add_numbers2(a, b):
    return a + b

result = add_numbers2("3", "5")
print(result)

result = add_numbers("3", "5")
print(result)


from typing import Optional

def get_name() -> Optional[str]:
    # 模拟可能返回 None 的情况
    import random
    if random.random() > 0.5:
        return "Alice"
    return None

name = get_name()