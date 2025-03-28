import asyncio

async def hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

# async def 定义的函数实际是一个协程对象 不能直接调用
# hello()

# 创建事件循环并运行协程
asyncio.run(hello())
# print(type(hello()))  # <class 'coroutine'>
print(type(hello))  # <class 'function'>


#----------------------------------------------------------------------------
async def task1():
    print("Task 1 started")
    await asyncio.sleep(1)
    print("Task 1 finished")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(2)
    print("Task 2 finished")

async def main():
    # 创建任务列表
    tasks = [task1(), task2()]
    # asyncio.gather 函数用于并发执行多个协程，事件循环会调度这些协程的执行
    # * 符号 代表解包操作
    await asyncio.gather(*tasks)

# 运行事件循环  run方法用来执行协程 注意main是函数实例 main()才是协程实例
asyncio.run(main())

#----------------------------------------------------------------------------



