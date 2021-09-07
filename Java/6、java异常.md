> 异常
>
> 静态语言的异常发现有两中场景
>
> 1、编译时发现的错误：这时发现的一般时语法错误
>
> 2、运行时会出现的错误：比如NullPointerException、ClassNotFoundException
>
> Throwable类：是所有错误和异常的父类，只有继承Throwable的类才能被抛出，或者使用@throw注解
>
> ![image-20210624110844939](image\image-20210624110844939.png)
>
> Throwable常用方法
>
> ![image-20210624111017472](image\image-20210624111017472.png)

> Exception：有两个子类RunTimeException和CheckedException异常
>
> RunTimeException子类
>
> ![image-20210624111237827](image\image-20210624111237827.png)
>
> CheckedException子类
>
> ![image-20210624111255896](image\image-20210624111255896.png)

> throws和throw关键字：java内异常也是一种类的对象
>
> throw：用在方法体内，抛出异常实例，有方法体内的语句处理
>
> throws：用在方法声明时，表示再抛出异常，有调用该发放的程序处理，throws后面跟可能会抛出的异常种类
>
> ![image-20210624111407086](image\image-20210624111407086.png)

> try、catch、finally
>
> try：关键字后的代码块表示可能发生异常的代码
>
> catch：关键字后的代码块表示捕捉到异常后的处理
>
> finally：关键字后的代码块表示一定会被执行的代码

> ERROR
>
> error是程序无法处理的错误，表示运行程序中出现了严重的问题。大多数错误和代码编写者执行的操作无关，而表示代码运行时JVM出现的问题。这些错误往往是不可检查的，不被运行发生的。
>
> 如OutOfMemoryError、StackOverflowError

> java内存模型：由所**有线程共享的数据区**和**线程隔离的数据区**组成
>
> ![image-20210624112611832](image\image-20210624112611832.png)
>
> ![image-20210624112731166](image\image-20210624112731166.png)
>
> 程序计数器不会发生OutOfMemoryError，它只保存下一条指令的地址