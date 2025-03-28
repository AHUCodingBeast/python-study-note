import urllib.request

#-----------------urllib:python 标准库（无需安装） 适合简单的网络请求----------------------------

try:
    response = urllib.request.urlopen('https://www.baidu.com')
    html = response.read().decode('utf-8')
    print(html)
except urllib.error.URLError as e:
    print(f"Error: {e}")



# -----------------requests:第三方库（需要安装） 适合复杂的网络请求----------------------------
import requests

try:
    response = requests.get('https://www.baidu.com')
    response.raise_for_status()
    # `response.raise_for_status()` 方法用于检查 HTTP 请求的状态码。如果状态码表示请求失败（即状态码不在 200-299 范围内），则抛出 `HTTPError` 异常。这有助于确保只有成功的响应才会继续处理。
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")



# -----------------httpx:第三方库（需要安装）适用于需要处理大量并发请求的场景----------------------------
# httpx 既支持同步请求，也支持异步请求，借助 async 和 await 关键字，能高效处理大量并发请求。
# 它的 API 设计和 requests 类似，容易上手。此外，它还支持 HTTP/2 协议，性能更优。
import httpx

try:
    response = httpx.get('https://www.example.com')
    print(response.text)
except httpx.RequestError as e:
    print(f"Error: {e}")

import asyncio


async def fetch_url():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get('https://www.example.com')
            print(response.text)
        except httpx.RequestError as e:
            print(f"Error: {e}")


asyncio.run(fetch_url())
