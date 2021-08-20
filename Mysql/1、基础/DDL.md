**DDL：**data definition Language，数据定义语言

> create关键字
>
> 1、创建数据库
>
> ```sql
> create database name [可选参数]
> ```
>
> 2、创建表
>
> ```mysql
> create table name(
> 	empno char(5) primary key,
> 	name varchar(10) default "xxx",
> 	age Decimal(2,1) check(age>10 and age<30),#(mysql不支持check约束)
>     deptno Decimal(3), #Decimal(2,1)表示数值的个数为2，小数位数为1
>     foreign key (deptno) references tc(deptno)
> )
> # 一个中文字符在mysql中占3个字节
> # 利用查询创建表
> create table name
> select * from tablename
> ```

> drop 关键字
>
> 1、删除数据库
>
> ```sql
> drop database name
> ```
>
> 2、删除表
>
> ```sql
> drop table name
> ```

> Truncate关键字
>
> 1、截断表
>
> ```mysql
> truncate table name
> # 该命令会清空表中所有记录
> ```

> Alter关键字，修改表结构
>
> 1、增加字段
>
> ```sql
> alter table name
> add number varchar(10) not null
> add str char(5) defult "abc"
> ```
>
> 2、修改字段
>
> ```sql
> alter table name
> modify str char(5) defult "abcd"
> ```
>
> 3、删除字段
>
> ```sql
> alter table name
> drop str
> ```

**约束**：起到维护数据库完整性的作用

> 1、创建约束
>
> ```mysql
> create table name(
> 	empno char(5),
> 	name varchar(10) default "xxx",
> 	age Decimal(2,1) check(age>10 and age<30),#(mysql不支持check约束)
>     deptno Decimal(3), # Decimal(2,1)表示数值的个数为2，小数位数为1
>     primary key(empno)/constraint empno primaty key(empno)
>     foreign key (deptno) references tc(deptno)
> )# 该表的主键同上
> # 在定义主键和外键时若没有声明约束名，系统将自动为约束命名，一般为字段名
> 
> alter table name
> add constraint (约束名) primary key(stn)/primart(stn, age)# 实体完整性规则
> add constraint (约束名) foreign key(dept) reference tc(dept)# 参照完整性规则
> add constraint (约束名) unique(name)# 实体完整性规则
> add constraint (约束名) check(表达式)# 用户自定义完整性规则，mysql中可定义但不生效
> ```

> 1、删除约束
>
> ```mysql
> alter table name
> drop primary key/ drop primary key (约束名)# 删除主键约束
> drop foreign key/ drop foreign key (约束名)# 删除外键约束
> drop index (约束名) # 删除唯一约束，也是索引约束
> drop check (约束名)# 删除自定义约束
> ```

> 1、查看约束
>
> ```sql
> show create table name
> ```

**索引**：加快数据的查询能力，但索引不是越多越好

> 1、唯一索引
>
> ```sql
> 当用户在创建“主键约束”或者“唯一约束”时，系统会自动创建唯一索引(unique index)
> ```
>
> 2、用户自定义索引（Nonunique Index,非唯一索引）
>
> ```mysql
> create index (索引名) on 表名(列明)# 在某张表上的一个列或多个列创建索引
> ```

> 1、删除索引
>
> ```sql
> drop index (索引名) on 表名
> ```

> 1、查看索引
>
> ```mysql
> show index from (表名)
> ```

**视图**：保护数据库的一种手段，使得查询数据库的人只能看到，管理员想让他看到的数据。视图数据来源于表。

> 1、创建视图
>
> ```sql
> create view name
> as
> select 语句
> ```
>
> 2、带约束的视图
>
> ```mysql
> create or replace view name #创建或者替换视图
> as
> select 语句
> with check option# 保留数据来源的约束，在数据插入时起约束作用
> ```

> 1、视图的修改
>
> ```mysql
> create or replace view name
> as 
> select 语句
> ```
>
> 2、alter关键字修改视图
>
> ```mysql
> alter view name
> as 
> select 语句
> ```

> 1、删除视图
>
> ```mysql
> drop view name
> ```

> 视图的注意事项：用户可以对一些视图进行DML操作，从而影响到基本表中的数据
>
> 视图的分类
>
> 1、简单视图
> 数据仅从一个表中提取
> 不包含函数和分组数据
>
> 2、复杂视图
> 数据从多个表中提取
> 包含函数和分组数据
> 不一定能对该视图进行DML操作
>
> 视图DML操作规则：
>
> 1、可以在简单视图上进行DML操作
> 2、在一个包含了分组和函数，或distinct关键字的视图中，则不能进行delete、update、insert操作
> 3、如果视图中包含了表达式组成的列，则不能进行update、insert操作
> 4、如果在视图中没有包含那些不能为空的列，则不能通过该视图进行insert操作

