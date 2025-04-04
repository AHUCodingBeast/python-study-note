在 Python 中，解包操作符 * 主要有两种用途：在函数调用中的参数解包和在序列类型（如列表、元组）中的元素解包。下面分别详细介绍这两种情况。
## 1、参数解包
### 在函数定义中
当你在函数定义中使用 *，它可以用来接收任意数量的位置参数，并将这些参数打包成一个元组。
```python
def func(*args):
    print(args)

func(1, 2, 3)  # 输出: (1, 2, 3)

def sum(*args) -> int:
    res = 0
    for arg in args:
        res += arg
    return res

print(sum(1, 2, 3))
# print(sum([1,2,3])) 这样传递参数会报错，需要参数解包
print(sum(*[1, 2, 3]))
```
这里，*args 接收所有传递给函数的位置参数，并将它们打包成一个元组。

### 在函数调用中
当你在函数调用中使用 *，它可以用来将一个可迭代对象（如列表或元组）拆解开，并将每个元素作为单独的参数传递给函数。

```python
def func(a, b, c):
    print(a, b, c)

values = [1, 2, 3]
func(*values)  # 输出: 1 2 3
```
这里，*values 将列表 values 中的每个元素拆解开，并将它们作为单独的参数传递给 func


## 2、元素解包
### 列表和元组
在赋值语句中，* 可以用来解包列表或元组中的元素。
```python
a, *b, c = [1, 2, 3, 4, 5]
print(a)  # 输出: 1
print(b)  # 输出: [2, 3, 4]
print(c)  # 输出: 5
```
这里，*b 将中间的所有元素收集到一个列表中。

### 字典
在字典中，** 用于解包关键字参数。

```python
def func(a, b, c):
    print(a, b, c)

kwargs = {'a': 1, 'b': 2, 'c': 3}
func(**kwargs)  # 输出: 1 2 3
```
这里，**kwargs 将字典中的键值对解包，并作为关键字参数传递给 func。

## 总结
* 在函数定义中：*args 用于接收任意数量的位置参数，并将它们打包成一个元组。
* 在函数调用中：*iterable 用于将一个可迭代对象拆解开，并将每个元素作为单独的参数传递给函数。
* 在赋值语句中：*variable 用于解包列表或元组中的元素。
* 在字典中：**dict 用于解包字典中的键值对，并作为关键字参数传递。
* 这些用法可以帮助你更灵活地处理参数和数据结构。