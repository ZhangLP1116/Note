> scanf函数：将屏幕上的字符串按照格式化样式保存在变量中
>
> sscanf函数：将指定的字符串常量按照格式化样式保存在变量中

> printf函数：将格式化字符串输出到屏幕
>
> sprintf函数：将格式化字符串输出到一个目标字符串中，可以用来构建一个字符串
>
> sprintf函数的原形：int sprintf( char *buffer, const char *format [, argument,...] );
>
> 用法与printf类似，第一个参数为目标字符串，第二个参数为格式化字符串，后续为可变个数的参数
>
> sprintf函数返回这次添加的字符串长度