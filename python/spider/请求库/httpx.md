> ## **简介**
>
> HTTPX是Python 3的功能齐全的HTTP客户端，它提供同步和异步API，并支持HTTP / 1.1和HTTP / 2。
>
> HTTPX所使用的API名与requests基本一致，requests的使用者可以很容易的上手HTTPX

> ## **基础用法**
>
> ### **请求**
>
> ```python
> r = httpx.get('https://httpbin.org/get')
> r = httpx.post('https://httpbin.org/post', data={'key': 'value'})
> r = httpx.put('https://httpbin.org/put', data={'key': 'value'})
> r = httpx.delete('https://httpbin.org/delete')
> r = httpx.head('https://httpbin.org/get')
> r = httpx.options('https://httpbin.org/get')
> 
> # 带参数的get请求
> params = {'key1': 'value1', 'key2': ['value2', 'value3']}
> r = httpx.get('https://httpbin.org/get', params=params)
> r.url
> >>> URL('https://httpbin.org/get?key1=value1&key2=value2&key2=value3')
> 
> # 携带请求头
> r = httpx.get(url, headers=headers)
> 
> # 携带cookie
> cookies = {"peanut": "butter"}
> r = httpx.get('http://httpbin.org/cookies', cookies=cookies)
> 
> # 设置重定向
> r = httpx.get('http://github.com/', allow_redirects=False)
> 
> # 设置超时，httpx所有请求都带有默认5s超时时间，若访问一些响应较慢的网站需要手动设置超时，若进行大型下载可以禁用超时
> httpx.get('https://github.com/', timeout=0.001)
> 
> # 设置认证
> httpx.get("https://example.com", auth=("my_user", "password123"))
> ```
>
> ### **响应**
>
> ```python
> # 文本响应
> r.text
> # 设置编码格式，默认为UTF-8编码
> r.encoding = 'ISO-8859-1'
> # 二进制响应
> r.content
> # json响应
> r.json()
> # 响应状态码
> r.status_code
> r.status_code == httpx.codes.OK
> ```
>
> ### **上传数据**
>
> 上传文本
>
> ```python
> # 使用HTTP分段编码上传文件
> files = {'upload-file': open('report.xls', 'rb')}
> r = httpx.post("https://httpbin.org/post", files=files)
> 
> # 使用项目元组作为文件值来显式设置文件名和内容类型：
> files = {'upload-file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel')}
> r = httpx.post("https://httpbin.org/post", files=files)
> 
> # 如果需要以多部分形式包括非文件数据字段，请使用data=...参数：
> data = {'message': 'Hello, world!'}
> files = {'file': open('report.xls', 'rb')}
> r = httpx.post("https://httpbin.org/post", data=data, files=files)
> ```
>
> 上传JSON
>
> ```python
> data = {'integer': 123, 'boolean': True, 'list': ['a', 'b', 'c']}
> r = httpx.post("https://httpbin.org/post", json=data)
> ```
>
> 上传二进制内容
>
> ```python
> content = b'Hello, world'
> r = httpx.post("https://httpbin.org/post", content=content)
> ```
>
> ### **流式请求和响应**
>
> 对应大型http下载使用流式传输可以避免一次性保存，和长时间等待后保存
>
> ```python
> # 请求二进制内容
> >>> with httpx.stream("GET", "https://www.example.com") as r:
> ...     for data in r.iter_bytes():
> ...         print(data)
> 
> # 请求文本内容
> >>> with httpx.stream("GET", "https://www.example.com") as r:
> ...     for text in r.iter_text():
> ...         print(text)
> 
> # 逐行流文本
> >>> with httpx.stream("GET", "https://www.example.com") as r:
> ...     for line in r.iter_lines():
> ...         print(line)
> 
> # 原始数据保存
> >>> with httpx.stream("GET", "https://www.example.com") as r:
> ...     for chunk in r.iter_raw():
> ...         print(chunk)
> ```

> ## **使用会话客户端**
>
> ### **什么是会话客户端**
>
> 如果您来自Requests，`httpx.Client()`那么可以使用代替`requests.Session()`。
>
> 最初的HTTP协议每次请求都会创建一个TCP连接，得到响应后释放连接，这种低效的方法在HTTP1.1和HTTP2中被抛弃。后续的HTTP协议充分使用已经建立的TCP连接，每个TCP连接可以用来多次发送HTTP数据包。减少多次TCP连接创建浪费的时间，提高了传输效率。
>
> `httpx.Client()`还支持跨请求的Cookie持久性， 每次发送请求时会携带上一次请求得到的Cookie
>
> ### **创建客户端实例**
>
> ```python
> client = httpx.Client()
> 
> # 使用上下文管理器自动管理客户端资源
> with httpx.Client() as client
> ```
>
> ### **客户端发送请求**
>
> ```python
> # 客户端实例发送请求的方式和基本请求方法一致，参数设置也一致
> >>> with httpx.Client() as client:
> ...     headers = {'X-Custom': 'value'}
> ...     r = client.get('https://example.com', headers=headers)
> ```
>
> ### **客户端参数**
>
> ```python
> # 在客户端实例化时设置参数，可以减少每次请求时携带参数的麻烦
> # 在客户端对象和请求级别同时设置参数，一般以请求级别优先。
> 
> # 客户端设置请求头
> httpx.Client(headers=headers)
> # 设置请求参数
> with httpx.Client(headers=headers, params=params) as client
> # 设置基本url
> >>> with httpx.Client(base_url='http://httpbin.org') as client:
> ...     r = client.get('/headers')
> ...
> r.request.url
> >>>URL('http://httpbin.org/headers')
> # 设置代理
> with httpx.Client(proxies="http://localhost:8030") as client
> proxies = {
>     "http://": "http://localhost:8030",
>     "https://": "http://localhost:8031",
> }
> 
> with httpx.Client(proxies=proxies) as client
> # 设置超时
> client = httpx.Client(timeout=10.0)
> # 使用超时对象，HTTPX还允许您更精细地指定超时行为。
> timeout = httpx.Timeout(10.0, connect=60.0)	# 表示连接超时为60s，其他超时为10s
> client = httpx.Client(timeout=timeout)
> response = client.get('http://example.com/')
> 
> # 设置客户端最大TCP连接数
> # max_keepalive，允许的保持活动连接数或None始终允许。（默认为20）
> # max_connections，允许的最大连接数或None无限制。（默认为100）
> limits = httpx.Limits(max_keepalive_connections=5, max_connections=10)
> client = httpx.Client(limits=limits)
> ```

> ## **异步支持**
>
> ### **异步客户端**
>
> ```python
> # 异步客户端提供了对并python协程的支持
> 
> # 创建异步客户端
> async with httpx.AsyncClient() as client
> 
> # 手动关闭
> client = httpx.AsyncClient()
> await client.aclose()
> 
> # 异步客户端下的请求方法和同步客户端下的请求方法种类一致，并这些方法都是异步的，发生阻塞时会自动切换到下一个请求执行
> async with httpx.AsyncClient() as client:	# async关键字用来标记异步上下文块，发生协程切换时不要执行退出操作
> 	r = await client.get('https://www.example.com/') # await关键字使用在会发生阻塞的位置，等待取回结果
> 
> 
> # 异步流式请求
> >>> client = httpx.AsyncClient()
> >>> async with client.stream('GET', 'https://www.example.com/') as response:
> ...     async for chunk in response.aiter_bytes()
> ```
>
> ### **异步客户端使用环境**
>
> ![image-20210509111604406](C:\Users\zhang\AppData\Roaming\Typora\typora-user-images\image-20210509111604406.png)
>
> ![image-20210509111619561](C:\Users\zhang\AppData\Roaming\Typora\typora-user-images\image-20210509111619561.png)
>
> ![image-20210509111634210](C:\Users\zhang\AppData\Roaming\Typora\typora-user-images\image-20210509111634210.png)
>
> 

