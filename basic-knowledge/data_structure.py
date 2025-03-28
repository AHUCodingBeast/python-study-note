class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("peek from empty stack")

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)




class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("dequeue from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("peek from empty queue")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


# 使用示例
if __name__ == '__main__':
    # 使用示例
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("栈顶元素:", stack.peek())  # 输出: 栈顶元素: 3
    print("栈大小:", stack.size())  # 输出: 栈大小: 3

    print("弹出元素:", stack.pop())  # 输出: 弹出元素: 3
    print("栈是否为空:", stack.is_empty())  # 输出: 栈是否为空: False
    print("栈大小:", stack.size())  # 输出: 栈大小: 2

    queue = Queue()
    queue.enqueue('a')
    queue.enqueue('b')
    queue.enqueue('c')

    print("队首元素:", queue.peek())  # 输出: 队首元素: a
    print("队列大小:", queue.size())  # 输出: 队列大小: 3

    print("移除的元素:", queue.dequeue())  # 输出: 移除的元素: a
    print("队列是否为空:", queue.is_empty())  # 输出: 队列是否为空: False
    print("队列大小:", queue.size())  # 输出: 队列大小: 2
    print('程序自身在运行')
else:
    print('我来自另一模块')
