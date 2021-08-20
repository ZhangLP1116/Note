requests请求库

get请求

> 基本格式：requests.get(url)
>
> 添加请求参数：requests.get(url, params=data)
>
> 添加请求头：requests.get(url, params=data, headers=headers)
>
> 添加超时：requests.get(url, params=data, headers=headers, timeout=30)
>
> 添加代理：requests.get(url, params=data, headers=headers, timeout=30, proxies=proxies)
>
> proxies = {
> 'http': 'http://10.10.1.10:3128'
> 'https':'https://10.10.1.10:1080'}
>
> 获取文本请求结果：.text属性
>
> 获取二进制请求结果：.content属性
>
> 获取json请求结果：.json()方法
>
> 获取请求的请求头：.headers属性
>
> 获取请求的cookie：.cookies属性
>
> 获取请求的url：.url属性
>
> 获取请求历史：.history属性

post请求

> 基本格式：requests.post(url)
>
> 上传文件：requests.post(url, file=file)
>
> 添加参数：requests.post(url, data=data)
>
> 其他格式与get请求一致

会话维持

> requests库中使用Session对象来维持一次请求的会话(在重复发送请求时Session会携带服务器的会话标识，以代表这是同一个会话的请求)
>
> 基本形式：
> s = requests.Session()
> s.get(url)

附：urllib.parse库的url操作

>将字典形式的url参数转换成get请求形式的参数
>
>```python
>from urllib.parse import urlencode, parse_qs
>params = {
>    'name': 'tom',
>    'age': 22,
>}
>
>base_url = 'http://baidu.com'
># urlencode()方法的作用就是将字典转换为get请求中的参数格式
>url = base_url + urlencode(params)
>print(url)
>>http://baidu.com?name=tom&age=22
>
># parse_qs()是一个逆向urlencode()方法的作用
>str = 'name=tom&age=22'
>print(parse_qs(str))
>> {'name': 'tom', 'age':22}
>```
>
>请求url编码
>
>```python
>from urllib.parse import quote, unquote
>
>key = '壁纸'
># quote()方法将字符串转换为url编码格式
>url = 'http://baidu.com/s?wd=' + quote(key)
>print(url)
>>'http://baodu.com/s?wd=%E5%A3%81%E7%BA%B8'
># unquote()方法将url编码的url转换为正常字符串格式
>print(unquote(url))
>>'http://baidu.com/s?wd=壁纸'
>```
>
>