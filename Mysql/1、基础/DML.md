DML：（Data Manipulation Language，数据操作语言）

> select查询语句
>
> 1、单表查询
>
> ```mysql
> 1、查询所有字段
> select * from sc
> 2、查询某个字段
> select sno from sc
> 3、给字段取别名
> select sno 学号 from sc
> 4、去重复字段
> select distinct sn from s
> 5、带where的查询
> select * from sc where sno="s1"
> 6、where表达式——between……and……
> select * from sc where score between 50 and 100
> 7、where表达式——模糊查询
> select * from s where sn like "_a" #（‘_’表示匹配一个字符）
> select * from s where sn like "李%" #（‘%’表示匹配0个或多个字符）
> 8、where表达式——空值判断
> select * from sc where score is null
> 9、where表达式——在集合内
> select * from sno in ("s1", "s2")
> ```
>
> 2、排序
>
> ```mysql
> 1、升序(默认)
> select * from sc order by score asc
> 2、降序
> select * from sc order by score desc
> 3、组合排序
> select * from sc order by score dese,age asc
> ```
>
> 3、分组，having
>
> ```mysql
> 1、单字段分组
> select * from sc group by sno
> 2、多字段分组
> select * from sc group by (sno,cno)
> 3、带having子句
> select from sc group by sno having score>60
> 
> # having子句必须在group by语句后，对查询的结果进行最后的筛选
> ```
>
> 4、聚合函数
>
> ```mysql
> 1、不带group by 的聚合函数
> select count(sno) from sc
> 2、带group by的聚合函数
> select count(sno) from sc group by sno
> #group by语句限制了函数的作用范围，聚合函数的应用范围从表到了每一个组
> 3、带group by + having的聚合函数
> select count(sno) from sc group by sno having count(sno)>2
> # 去掉记录个数小于2的结果
> 
> # 跟在select后from前的函数调用，都是在from之后的语句执行完成后将结果给到函数，然后函数使用该结果集作为参数运行自身函数体内部的代码，实现特定的功能
> ```
>
> ps：
> count(1)与count(*)得到的结果一致，包含null值
> count(字段)不计算null值
> count(null)结果恒为0
>
> 5、多表查询
>
> ```mysql
> # 内连接
> 1、相等连接查询
> select * from s,sc where s.sno=sc.sno # 当from后面跟着多张表时where语句中给出表的连接条件
> 2、自身连接查询
> select * from s as s1,s as s2 where s1.sno=s2.sno
> 3、不相等连接查询
> select * from emp e,salgrade s where  e.sal between s.losal in s.hisal
> 4、inner join连接，效果与相等连接一致，格式与外连接类似
> select * from t1 
> inner join t2 no t1.sno=t2.sno
> # 多表连接相当于将两张表进行笛卡尔积，再根据where中的条件将不满足的记录删除
> 
> # 外连接
> 4、左外连接查询
> select from dept left outer join emp
> on dept.depton=emp.deptno
> 5、右外连接查询
> select from dept right join emp
> on dept.deptno=emp.deptno
> # 外连接时连接的条件写在 on 语句中，外连接的特点时会保证其中一张表的完整性，在连接时主表的记录不会丢失，与主表不匹配的副表字段用null值代替。
> ```
>
> 6、子查询
>
> ```mysql
> #不相关子查询，子查询只执行一次，不依赖外部查询
> 1、单返回值子查询，因为时单返回值所有可以使用关系运算符，<、>、<=、>=、!=、=
> select sn from s where sno=(select sno from sc where score="60")
> 2、多值子查询——in
> select sn from s where sno in (select sno from where cno="c1")
> 3、多值子查询——all
> select sno from sc where score>all(select score from sc) #满足所有，相当于大于最大值
> 4、多值子查询——any
> select sno from sc where score>any(select score from sc) # 满足其中一个，相当于大于最小值
> 
> # 相关子查询，子查询依赖外部查询的参数，外层查询每检查一行内部查询旧执行一次
> 5、Exists操作符 #Exists子查询可以转换为in子查询
> select sno from s where Exists (select * from sc where s.sno=sc.sno score>60)
> # 使用Exists操作符时，外层子查询where语句格式固定为where Exists内存查询要给出外层表和内层表的连接表达式，Exists操作符返回一个布尔值来判定是否符合where条件，True为符合。所以子查询中select后的字段并不重要，重要的时内部查询是否有返回值，若有则为True，若没有则为False
> 
> 6、select sno from sc a where score>(select avg(score) from sc b where a.cno=b.cno)
> # 使用相关子查询时要给出内部查询与外部查询的连接条件
> # 子查询最多嵌套255
> ```
>

> update：语句
>
> ```mysql
> 1、更新整个字段，将整个sno字段所有的值都更新为s1
> update sc set sno="s1"
> 2、更新某个字段值，将sno字段值为s1的字段值改为s01
> update sc set sno="s01" where sno="s1"
> 
> # where语句后可以跟子查询
> ```

> insert：语句
>
> ```mysql
> 1、使用特定值插入
> insert into sc(sno,tno) value(xxx,xxx)
> insert into sc value(xxx,xxx,xxx)
> # value中的顺序要与对应字段的顺序一致，插入数据时可以只插入部分字段，其他字段默认为null
> 
> 2、使用查询语句插入
> insert into sc select 语句
> # 查询插入时要注意查询结果要和表中字段顺序对应
> 
> 3、同时插入多条记录 # 达到和查询语句同样的效果
> insert into sc value
> (xxx,xxx,xxx),
> (xxx,xxx,xxx),
> (xxx,xxx,xxx),
> (xxx,xxx,xxx)
> ```

> delete：语句
>
> ```mysql
> 1、删除表中所有记录
> delete from sc
> 2、删除表中特定记录
> delete from sc where 表达式或者子查询
> 3、删除多张表中符合条件的记录
> delete from sc inner join s where sno="s1"
> ```
>
> 