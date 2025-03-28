### `httpx` 模块使用笔记
#### 1. 简介
`httpx` 是一个功能强大的 Python HTTP 客户端，它既支持同步请求，也支持异步请求。其 API 设计与 `requests` 类似，易于上手，同时还支持 HTTP/2 协议，能显著提升性能，非常适合用于处理大量并发请求的场景，如网络爬虫、异步 API 调用等。

#### 2. 安装
使用 `pip` 来安装 `httpx`：

```bash
pip install httpx
```

#### 3. 常用 API 及实例
##### 3.1 同步请求：`httpx.get()` 和 `httpx.post()`
`**httpx.get()**`** 示例**：  
用于发送同步的 HTTP GET 请求，从服务器获取数据。

```python
import httpx

try:
    # 发送 GET 请求
    response = httpx.get('https://www.example.com')
    # 检查响应状态码
    if response.status_code == 200:
        # 打印响应文本内容
        print(response.text)
    else:
        print(f"请求失败，状态码: {response.status_code}")
except httpx.RequestError as e:
    print(f"请求发生错误: {e}")
```



`**httpx.post()**`** 示例**：  
用于发送同步的 HTTP POST 请求，向服务器提交数据。

```python
import httpx

# 定义要提交的数据
data = {
    'username': 'Alice',
    'password': '123456'
}

try:
    # 发送 POST 请求
    response = httpx.post('https://www.example.com/login', data=data)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"请求失败，状态码: {response.status_code}")
except httpx.RequestError as e:
    print(f"请求发生错误: {e}")
```

##### 3.2 异步请求
借助 `async` 和 `await` 关键字，`httpx` 能高效处理大量并发请求。

```python
import asyncio
import httpx

async def fetch_url(url):
    async with httpx.AsyncClient() as client:
        try:
            # 发送异步 GET 请求
            response = await client.get(url)
            if response.status_code == 200:
                print(response.text)
            else:
                print(f"请求失败，状态码: {response.status_code}")
        except httpx.RequestError as e:
            print(f"请求发生错误: {e}")

async def main():
    urls = [
        'https://www.example1.com',
        'https://www.example2.com',
        'https://www.example3.com'
    ]
    tasks = [fetch_url(url) for url in urls]
    await asyncio.gather(*tasks)

asyncio.run(main())
```

##### 3.3 `response.status_code`
获取响应的状态码，用于判断请求是否成功。

```python
import httpx

response = httpx.get('https://www.example.com')
print(f"响应状态码: {response.status_code}")
```

##### 3.4 `response.text` 和 `response.json()`
+ `response.text`：获取响应的文本内容。
+ `response.json()`：将响应内容解析为 JSON 格式（前提是响应内容是有效的 JSON 数据）。

```python
import httpx

response = httpx.get('https://api.example.com/data')
if response.status_code == 200:
    print("响应文本内容:")
    print(response.text)
    try:
        print("响应 JSON 数据:")
        print(response.json())
    except ValueError:
        print("响应内容不是有效的 JSON 数据")
else:
    print(f"请求失败，状态码: {response.status_code}")
```

##### 3.5 `httpx.Client()` 和 `httpx.AsyncClient()`
+ `httpx.Client()`：用于创建同步的客户端会话，可在多次请求中共享配置信息，如 headers、cookies 等。
+ `httpx.AsyncClient()`：用于创建异步的客户端会话。



**同步客户端示例：**

```python
import httpx

# 创建同步客户端
client = httpx.Client()
headers = {'User-Agent': 'MyCustomUserAgent'}
client.headers = headers

try:
    response = client.get('https://www.example.com')
    print(response.text)
finally:
    # 关闭客户端
    client.close()
```

  
**异步客户端示例**：

```python
import asyncio
import httpx

async def main():
    # 创建异步客户端
    async with httpx.AsyncClient() as client:
        headers = {'User-Agent': 'MyCustomAsyncUserAgent'}
        client.headers = headers
        response = await client.get('https://www.example.com')
        print(response.text)

asyncio.run(main())
```

#### 4. 错误处理
在使用 `httpx` 发送请求时，可能会遇到各种错误，如网络连接错误、请求超时等。可以使用 `try-except` 语句捕获并处理这些错误。

```python
import httpx

try:
    response = httpx.get('https://www.example.com', timeout=3)
    response.raise_for_status()
    print(response.text)
except httpx.RequestError as e:
    print(f"请求发生错误: {e}")
except httpx.HTTPStatusError as e:
    print(f"请求返回错误状态码: {e.response.status_code}")
```

#### 5. 总结
`httpx` 模块为 Python 开发者提供了灵活且高效的 HTTP 请求解决方案。无论是同步请求还是异步请求，都能通过简洁的 API 轻松实现。同时，它对 HTTP/2 协议的支持进一步提升了性能，在处理并发请求的场景中表现出色。在实际使用时，要注重错误处理和资源管理，以保证程序的稳定性和可靠性。

