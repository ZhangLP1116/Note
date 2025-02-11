### 基础

RPC&Netty

dubbo框架时对RPC过程的实现，其中网络通信使用netty框架

![img](https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg-blog.csdnimg.cn%2F20210524231634504.png%3Fx-oss-process%3Dimage%2Fwatermark%2Ctype_ZmFuZ3poZW5naGVpdGk%2Cshadow_10%2Ctext_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3MTA5NDU2%2Csize_16%2Ccolor_FFFFFF%2Ct_70&refer=http%3A%2F%2Fimg-blog.csdnimg.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1658295282&t=6947b3f41e25242ed73c1a71387185c3)



### 框架

官方文档：https://dubbo.apache.org/zh/docsv2.7/dev/design/

![dubbo-framework](image/dubbo-framework.jpg)



### 1、标签解析

类：DubboBeanDefinitionParser的parse()方法

dubbo名字空间解析器，中配置了所有dubbo相关标签的对象

![image-20220623152114202](image/image-20220623152114202.png)



### 2、服务暴露过程

![dubbo-服务暴露](image/dubbo-%E6%9C%8D%E5%8A%A1%E6%9A%B4%E9%9C%B2.jpg)



### 3、服务引用

![dubbo-服务引用](image/dubbo-%E6%9C%8D%E5%8A%A1%E5%BC%95%E7%94%A8.jpg)



### 4、服务调用

![image-20220623154720680](image/image-20220623154720680.png)