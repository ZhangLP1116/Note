> JDK
>
> ​		JDK（Java Development Kit）Java开发包，**是**编写Java小程序和应用程序的**开发环境**，它包含java运行环境（Java Runtime Environment），java根据，Java核心库类。
>
> （相对的SDK，software Development Kit软件开发工具包，就是一类用于软件编写的开发环境）

> JRE
>
> ​		JRE（Java Runtime Environment，java运行环境），顾名思义JRE是java程序运行时需要的环境，与JDK相比JRE体量更小，没有JDK中编写Java程序所需要的组件。所以运行一个Java程序只需要安装JRE组件即可，若要编写Java程序就需要JDK

> ![image-20210622112701695](image\image-20210622112701695.png)

> JAR
>
> ​		JAR（java Archive，java归档），是一种软件包文件格式，通常将实现一种功能的大量java类文件，相关源数据，资源（图片、文本）通过ZIP格式归档到一个文件包中。
>
> ​		JAR文件经常用于部署、封装库、组件和插件程序 。**可以被编译器和JVM等程序直接使用而不需要先提取JAR中的文件。**
>
> ​		JAR可以使用JAVA自带的jar命令创建和提取。也可以使用zip压缩工具创建和提取，不过压缩时zip文件头里的条目顺序很重要，因为Manifest文件常需放在首位。
>
> #### **JAR分类：**
>
> ​		**可执行的JAR：**一个可执行的jar 文件是一个自包含的 Java 应用程序，它存储在特别配置的JAR 文件中，可以由 JVM 直接执行它而无需事先提取文件或者设置类路径
>
> ​		**不可执行的JAR：**要运行存储在非可执行的 JAR 中的应用程序，必须将它加入到您的类路径中，并用名字调用应用程序的主类
>
> #### **JAR提供的优势：**
>
> ​			**安全性：**可以对 JAR 文件内容加上数字化签名。这样，能够识别签名的工具就可以有选择地为您授予[软件安全](https://baike.baidu.com/item/软件安全)特权，这是其他文件做不到的，它还可以检测代码是否被篡改过。
>
> ​			**减少下载时间：**如果一个 applet 捆绑到一个 JAR 文件中，那么浏览器就可以在一个 HTTP [事务](https://baike.baidu.com/item/事务)中下载这个 applet 的类文件和相关的资源，而不是对每一个文件打开一个新连接。
>
> ​			**压缩：**JAR 格式允许您[压缩文件](https://baike.baidu.com/item/压缩文件)以提高存储效率。
>
> ​			传输平台扩展：Java 扩展框架（Java Extensions Framework）提供了向 Java 核心平台添加功能的方法，这些扩展是用 JAR [文件打包](https://baike.baidu.com/item/文件打包)的（Java 3D 和 JavaMail 就是由 Sun 开发的扩展例子）。

