> os库
>
> system方法：
>
> ```python
> import os
> 
> # 该方法会有一个返回状态值：0表示成功
> # 缺点：该方法无法查看命令执行后的信息，如dir命令等就不适合使用该方法
> os.system("chcp 65001")
> ```
>
> popen方法
>
> ```python
> import os
> 
> # 这种调用方式是通过管道的方式来实现,函数返回一个file-like的对象,里面的内容是脚本输出的内容(可简单理解为echo输出的内容)。
> # file-like的对象有read()、readline()方法逐行读取或则全部读取。执行后的信息
> info = os.popen("dir")
> print(info.read())
> ```

