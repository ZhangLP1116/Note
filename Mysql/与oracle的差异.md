参考文档

数据类型、函数、存储过程、存储函数、游标触发器差异：

https://blog.csdn.net/qq_42239765/arti2842790



SQL语法方面区别：https://blog.csdn.net/HaixWang/article/details/54973125?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1-54973125-blog-115454155.pc_relevant_aa&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1-54973125-blog-115454155.pc_relevant_aa&utm_relevant_index=1



​    

### 时间类型差异

提供数据类型

- mysql：提供DATE和TIME两类
- oracle：只提供DATE类型



获取当前时间差异：

- mysql：
    - NOW()函数以`YYYY-MM-DD HH:MM:SS'返回当前的日期时间，可以直接存到DATETIME字段中。
    - CURDATE()以’YYYY-MM-DD’的格式返回今天的日期，可以直接存到DATE字段中。
    - CURTIME()以’HH:MM:SS’的格式返回当前的时间，可以直接存到TIME字段中。
- oracle：sysdate



日期格式转换

- mysql：
    - str_to_date('2019-02-12 11:34:32', '%Y-%m-%d %H:%i:%s')，`字符串到日期格式`
    - date_format(now(),'%Y-%m-%d')，`日期到字符串格式`
    - time_format(now(),'%H-%i-%S')，`日期到字符串格式`
- oracle：
    - to_date('2019-02-12 14:20:22', 'yyyy-mm-dd hh24:mi:ss')，`字符串到日期格式`
    - to_char(sysdate,'yyyy-mm-dd')，`日期到字符串格式`



日期运算

- mysql：
    - 日期相加: date_add(now(), INTERVAL 180 DAY)
    - 日期相减: date_sub('1998-01-01 00:00:00', interval '1 1:1:1' day_second)
- oracle：
    - 当前时间加N天: sysdate+N 
    - 当前时间减N天: sysdate-N



### 其他

字符串连接

- mysql：Mysql使用concat方法连接字符串. MySQL的concat函数可以连接一个或者多个字符串,如
           mysql> select concat('10');   结果为: 10.
           mysql> select concat('11','22','33','aa'); 结果为: 112233aa

- oracle：

    - 使用||连接字符串,也可以使用concat函数

        ```sql
        '11' || '22' || '33' || 'aa'
        >'112233aa'
        ```

    - Oracle的concat函数只能连接两个字符串



类型转换函数

- mysql
    - date_format/ time_format，转换为字符串格式
    - STR_TO_DATE(str,format)，转换为时间格式
    - cast(xxx AS 类型)，将参数转换为指定类型
- oracle
    - TO_CHAR(param)，将类型转换为字符串
    - to_date(str,format)，转换为日期格式
    - trunc(-1.002, 1)，可以保留小数点后几位
    - TO_NUMBER(str)，转换为数值格式



Null处理

- mysql：IFNULL(参数,0)，若形参为null，这返回默认值
- oracle：
    - nvl函数
         nvl函数基本语法为nvl(E1,E2)，意思是E1为null就返回E2，不为null就返回E1。
    - nvl2函数
         nvl2函数的是nvl函数的拓展，基本语法为nvl2(E1,E2,E3)，意思是E1为null，就返回E3，不为null就返回E2。

