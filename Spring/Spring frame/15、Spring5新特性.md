# Spring5新特性

> Spring整个框架基于java8实现，兼容JDK9，删除了旧版本中不建议使用的方法

## 核心特性

> ![image-20210825140836492](image/image-20210825140836492.png)
>
> ![image-20210825144120672](image/image-20210825144120672.png)

### Spring5整合log4j2

> Spring5弃用了Log4ConfigListener，建议使用log4j2
>
> 1. 引入log4j2所需依赖
>     ![image-20210825141436664](image/image-20210825141436664.png)
> 2. 创建log4j2.xml配置文件（文件名固定Spring5自动检测）
>     ![image-20210825141711385](image/image-20210825141711385.png)

### Spring5核心容器支持@Nullable注解

> @Nullable注解表示可以为空值
>
> 1. 作用在方法上，表示返回值可以为空
>     ![image-20210825142835257](image/image-20210825142835257.png)
> 2. 使用在方法的参数上，表示该参数可以为空
>     ![image-20210825143521424](image/image-20210825143521424.png)
> 3. 使用在属性上，表示该属性可以为空
>     ![image-20210825143619346](image/image-20210825143619346.png)

### Spring5核心容器支持函数式风格

> 通过CenericApplicationContext类实现
>
> 示例：手动创建对象并向Spring注册
>
> 1. 创建CenericApplicationContext对象
>     ![image-20210825144409173](image/image-20210825144409173.png)
> 2. 调用registerBean方法注册对象，对象使用函数式风格创建
>     ![image-20210825144635790](image/image-20210825144635790.png)
> 3. 获取对象，由于调用registerBean方法时没有传入对象名，所有只能用类所在的全路径获得对象，类属于类型注入
>     ![image-20210825144841605](image/image-20210825144841605.png)
>
> registerBean方法
>
> ![image-20210825145035534](image/image-20210825145035534.png)

## 测试方面的改进

> ![image-20210825145318138](image/image-20210825145318138.png)

### 整合JUnit4

> 1. 引入JUnit4依赖
>
>     ![image-20210825145607833](image/image-20210825145607833.png)![image-20210825150355655](image/image-20210825150355655.png)
>
> 2. 创建测试类，使用注解完成测试
>
>     1. 使用@RunWith注解说明整合的测试框架
>         ![image-20210825145914947](image/image-20210825145914947.png)
>
>     2. 使用注解取代手动加载配置文件
>         ![image-20210825150031703](image/image-20210825150031703.png)
>
>         ![image-20210825150005050](image/image-20210825150005050.png)
>
>     3. 使用注入得到bean对象
>         ![image-20210825150159930](image/image-20210825150159930.png)
>
>     4. 编写测试方法
>
>         ![image-20210825150230315](image/image-20210825150230315.png)

### 支持整合JUnit5

> 1. 引入JUnit5依赖
>     ![image-20210825150622797](image/image-20210825150622797.png)
>
> 2. 创建测试类，使用注解完成测试
>     （除了引入框架的注解其他都不变）
>
>     1. 使用@ExtendWith注解引入JUnit5框架（@ExtendWith注解包含Spring5新扩展支持的框架）
>
>     ![image-20210825151006216](image/image-20210825151006216.png)

#### @SpringJUnitConfig使用复合注解一步完成配置

> ![image-20210825151358499](image/image-20210825151358499.png)

