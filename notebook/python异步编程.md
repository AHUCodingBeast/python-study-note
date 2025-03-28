Python 异步编程是一种高效处理 I/O 密集型任务的编程方式，下面为你详细介绍相关内容。

协程主要适用于 I/O 密集型任务，因为在 I/O 操作等待期间，协程可以将控制权让出，去执行其他任务。
但对于 CPU 密集型任务，如大量的数学计算、图像和视频处理等，协程并不能提升性能，因为协程的切换是在单线程内进行的，无法利用多核 CPU 的优势。
而多线程可以让不同的线程在不同的 CPU 核心上并行执行，从而显著提高 CPU 密集型任务的处理速度。

### 异步编程的概念

在传统的同步编程中，程序按顺序依次执行每个任务，若一个任务被阻塞（如等待网络请求响应、文件读写等），程序会暂停执行后续任务，直到该任务完成。
而异步编程允许程序在等待某个任务完成时，去执行其他任务，不会被阻塞，从而提高程序的整体执行效率。

### 异步编程适用场景

异步编程主要适用于 I/O 密集型任务，如网络请求、文件读写等。在这些场景中，程序大部分时间都在等待外部资源的响应，使用异步编程可以充分利用等待时间执行其他任务。
但对于 CPU 密集型任务，异步编程并不能提高效率，因为 CPU 始终处于忙碌状态，不存在等待时间。

### 核心概念

#### 1. 协程（Coroutine）

协程是一种轻量级的线程，它允许在程序执行过程中暂停和恢复。在 Python 中，协程使用 `async def` 定义，使用 `await`
关键字暂停协程的执行，等待另一个协程或异步操作完成。

```python
import asyncio


async def hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")


# 创建事件循环并运行协程
asyncio.run(hello())
# async def 定义的函数实际是一个协程对象 不能直接调用
# hello()
```

在上述代码中，`hello` 是一个协程函数，`await asyncio.sleep(1)` 会暂停协程的执行 1 秒，期间可以执行其他任务。

#### 2. 事件循环（Event Loop）

事件循环是异步编程的核心，它负责调度和执行协程。事件循环会不断地检查是否有可执行的协程或异步操作，并按顺序执行它们。在
Python 中，可以使用 `asyncio` 模块的 `run` 函数来创建和运行事件循环。

```python
import asyncio


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
    # 并发执行任务
    await asyncio.gather(*tasks)


# 运行事件循环
asyncio.run(main())
```

在上述代码中，`asyncio.gather` 函数用于并发执行多个协程，事件循环会调度这些协程的执行。

#### 3. Future 和 Task

+ **Future**：表示一个尚未完成的异步操作的结果。可以通过 `asyncio.Future` 类创建一个 Future 对象，并在操作完成后设置其结果。
+ **Task**：是 Future 的子类，用于包装协程。可以通过 `asyncio.create_task` 函数将协程包装成任务，并将其添加到事件循环中执行。

```python
import asyncio


async def my_coroutine():
    await asyncio.sleep(1)
    return "Result"


async def main():
    # 创建任务
    task = asyncio.create_task(my_coroutine())
    # 等待任务完成
    result = await task
    print(result)


# 运行事件循环
asyncio.run(main())
```

### 异步编程库

+ `**asyncio**`：Python 标准库中用于异步编程的库，提供了事件循环、协程、Future、Task 等核心组件。
+ `**aiohttp**`：基于 `asyncio` 的异步 HTTP 客户端 / 服务器库，用于处理异步网络请求。

```python
import asyncio
import aiohttp


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'https://www.baidu.com')
        print(html)


# 运行事件循环
asyncio.run(main())
```

### 注意事项

+ 异步函数（协程）必须使用 `async def` 定义，并使用 `await` 关键字调用其他异步函数。
+ 异步代码需要在事件循环中运行，可以使用 `asyncio.run` 函数创建和运行事件循环。
+ 避免在异步代码中使用阻塞式的 I/O 操作，否则会阻塞事件循环，影响异步性能。

通过掌握上述内容，你可以开始使用 Python 进行异步编程，提高程序在 I/O 密集型任务中的执行效率。

