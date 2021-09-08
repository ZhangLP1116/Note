> 输出异常信息
>
> ```python
> try:
>     pass
> except Exception as e:
>     print(str(e))
>     print(repr(e))
> 
> # str(e)，输出异常信息，——>division by zero
> # repr(e)，输出异常类型和异常信息，——>ZeroDivisionError('division by zero')
> ```

> Traceback模块
>
> ```python
> import traceback
> 
> try:
>     1/0
> except:
>     print('error:', traceback.format_exc())
>     
> """输出信息，包含了异常发送的地点，异常类型，异常信息
> error: Traceback (most recent call last):
>   File "C:/Users/zhang/Desktop/page/1.py", line 4, in <module>
>     1/0
> ZeroDivisionError: division by zero
> """
> ```
>
> 