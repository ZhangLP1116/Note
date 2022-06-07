## OGNL

Object Graphic Navigation Language(对象图导航语言)，通过约定一些简单的语法规则来访问和操作java对象

官方文档：https://commons.apache.org/proper/commons-ognl/language-guide.html





### 对象访问

1、普通对象、方法访问

以`#`开头+对象名，

方法访问：#obj.method

```shell
# 访问对象
[arthas@8]$ ognl '#name=new String("zlp"),#name'

# 访问对象方法
[arthas@8]$ ognl '#name=new String("zlp"),#name.toCharArray'
```



2、静态对象、方法访问

以`@`开头+类路径，以`@`访问对象方法

方法访问：@classPath@method

```java
[arthas@8]$ ognl '@java.lang.Math@max(10,20)'
```



3、集合访问

```shell
# 创建list集合
[arthas@8]$ ognl '{1,2,3}'
# 指定创建集合的类型
[arthas@8]$ ognl 'new int[] { 1, 2, 3 }'
# 访问list
[arthas@8]$ ognl '{1,2,3}[2]'



# 创建map
[arthas@8]$ ognl '#{"name":"zlp","age":18}'
# 指定创建的map类型
[arthas@8]$ ognl '@java.util.LinkedHashMap@{"name":"zlp","age":18}'
# 访问map
[arthas@8]$ ognl '#{"name":"zlp","age":18}["name"]'

```



### 表达式

1、集合操作

```shell
# 元素是否在集合中
[arthas@8]$ ognl '4 in {1,2,3}'
@Boolean[false]

# 集合投影，对集合中的每个元素进行指定的处理
[arthas@8]$ ognl '{1,2,3}.{#this instanceof String ? #this : #this.toString()}'
@ArrayList[
    @String[1],
    @String[2],
    @String[3],
]

# 从集合中选择符合条件的元素，保存到新集合中
[arthas@8]$ ognl '{1,2,3}.{? #this>1}'
@ArrayList[
    @Integer[2],
    @Integer[3],
]

# 获取第一个符合条件的元素
[arthas@8]$ ognl '{1,2,3}.{^ #this>1}'
@ArrayList[
    @Integer[2],
]

# 获取最后一个符合条件的元素
[arthas@8]$ ognl '{1,2,3}.{$ #this>1}'
@ArrayList[
    @Integer[3],
]


```



