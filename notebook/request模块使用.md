#### 1. 简介
`requests` 是 Python 中一个广泛使用的第三方 HTTP 库，它提供了简单易用的 API，使得发送 HTTP 请求变得轻松。使用 `requests` 可以方便地进行 GET、POST、PUT、DELETE 等常见的 HTTP 请求操作，还能处理会话、认证、重定向等。

#### 2. 安装
在使用 `requests` 之前，需要先进行安装。可以使用 `pip` 来安装：

```bash
pip install requests
```

#### 3. 常用 API 及实例
##### 3.1 `requests.get()`
用于发送 HTTP GET 请求，通常用于从服务器获取数据。

```python
import requests

# 发送 GET 请求
response = requests.get('https://www.example.com')

# 检查响应状态码
if response.status_code == 200:
    # 打印响应内容
    print(response.text)
else:
    print(f"请求失败，状态码: {response.status_code}")
```

##### 3.2 `requests.post()`
用于发送 HTTP POST 请求，通常用于向服务器提交数据。

```python
import requests

# 定义要提交的数据
data = {
    'name': 'John',
    'age': 30
}

# 发送 POST 请求
response = requests.post('https://www.example.com/api', data=data)

# 检查响应状态码
if response.status_code == 200:
    print(response.json())
else:
    print(f"请求失败，状态码: {response.status_code}")
```

##### 3.3 `response.status_code`
用于获取响应的状态码，常见的状态码如 200 表示请求成功，404 表示请求的资源不存在，500 表示服务器内部错误等。

```python
import requests

response = requests.get('https://www.example.com')
print(f"响应状态码: {response.status_code}")
```

##### 3.4 `response.text`
用于获取响应的文本内容，通常用于处理 HTML、JSON 等文本格式的数据。

```python
import requests

response = requests.get('https://www.example.com')
print(response.text)
```

##### 3.5 `response.json()`
用于将响应内容解析为 JSON 格式，前提是响应内容是有效的 JSON 数据。

```python
import requests

response = requests.get('https://api.example.com/data')
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"请求失败，状态码: {response.status_code}")
```

##### 3.6 `requests.Session()`
用于创建一个会话对象，会话对象可以保持连接，在多次请求中共享一些参数，如 cookies、认证信息等。

```python
import requests

# 创建会话对象
session = requests.Session()

# 发送第一次请求
response1 = session.get('https://www.example.com')
print(response1.cookies)

# 发送第二次请求，会话会自动携带之前的 cookies
response2 = session.get('https://www.example.com/another-page')
print(response2.text)

# 关闭会话
session.close()
```

#### 4. 错误处理
在使用 `requests` 发送请求时，可能会出现各种错误，如网络连接错误、请求超时等。可以使用 `try-except` 语句来捕获并处理这些错误。

```python
import requests

try:
    response = requests.get('https://www.example.com', timeout=5)
    response.raise_for_status()  # 检查响应状态码，如果不是 200 则抛出异常
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"请求发生错误: {e}")
```

#### 5. 总结
`requests` 模块是 Python 中处理 HTTP 请求的强大工具，通过上述常用 API 可以完成各种常见的 HTTP 请求操作。在实际使用中，要注意错误处理和资源管理，以确保程序的稳定性和可靠性。

