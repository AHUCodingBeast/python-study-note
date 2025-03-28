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
