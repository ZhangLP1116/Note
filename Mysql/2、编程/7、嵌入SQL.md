1、概述

> 嵌入式SQL：就是在高级程序语言中嵌入SQL（ESQL）语言，来完成数据库操作。
>
> 含嵌入SQL的主语言文件编译原理：
> 1、由主语言编译器中的RDBMS预处理程序对源程序进行扫描，识别出ESQL语句，并将这些语句编译成主语言编译器可识别的语句。
> 2、主语言编译程序对整个源文件进行编译成目标代码

2、主语言和SQL的通信

> 两种不同编程语言实现同一个功能时，语言之间的通信是非常重要的部分，两种之间相互通信，传递状态信息，数据信息。
>
> 大致通信过程如下：
> 1、主程序将数据库操作命令交给sql程序（可能包含查询操作，或者数据插入操作）
> 2、sql程序返回执行的状态信息
> 3、主程序根据这些状态信息判断下一步应该做什么
>
> 两者之间的通信被称作SQL通信区（SQL Communication Area，SQLCA），SQLCA是一种数据结构，由主程序定义，SQL程序使用。在SQLCA中有一个mysql系统变量SQLCODE，改变了表示SQL语句执行的状态。主语言可以根据改变了来判断SQL语句执行的结果。**SQLCA主要传递两种语言之间的运行状态信息和运作状态参数。而两个语言间的数据交互主要通过主变量进行。**
>
> **为了区分主语言和SQL语言规定在所有的SQL语句前加上前缀——EXEC SQL**
>
> 例：EXEC SQL select * from sc;（表示此处为SQL查询语句）

3、实例

> 1、主变量定义的使用：使用主应用程序语言定义的想要在SQL程序中使用的变量，叫做主变量。（主要的数据交互手段）
>
> ```mysql
> # 主变量必须定义在begin declare section 与 end declare sectionSQL语句之间，定义变量使用主语言语法和主语言变量类型，变量名不能是SQL中的关键字
> # 主变量在SQL程序中使用时必须带上冒号':'
> # 在一条SQL中主变量只能使用一次
> 
> # 实例
> exec sql begin declare section	# EXEC SQL开头表示这是一句SQL语句
> char msno[4],mcno[4],givensno[5];# 没有EXEC SQL开头这是一条主程序语句（C语言语句）
> int mgrade;
> char SQLSTATE[6]
> exec sql end declare section
> # begin declare section，end declare section使得与编译器RDBMS知道该段内的C语言变量会在SQL中使用
> 
> # 使用主变量的查询操作
> EXEC SQL select 学号,课号,分数 into :msno, :mcno, :mgrade from grade where 学号=:givensno
> 
> # 使用主变量的插入操作
> EXEC SQL insert into grade value(:msno, :mcno, :mgrade);
> 
> # 使用主变量的更新操作
> EXEC SQL update grade set 分数=:grade where 学号=:msno and 课号=:mcno;
> 
> # 使用主变量的删除操作
> EXEC SQL delete from grade where 学号=:msno and 课号=:mcno and 成绩=:mgrade;
> 
> ```
>
> 2、游标的使用
>
> ```c
> // 在嵌入式SQL用使用游标与纯SQL环境下的游标使用没有很大区别，唯一的区别就是提取数据时存放到的是主变量而不是sql变量。游标使用的基本4个步骤都不变，定义、打开、提取、关闭。
> 
> void sal(){
> 	EXEC SQL BEGIN DECLARE SECTION;
> 	char msno[4], mcno[4], givensno[5];
> 	int mgrade;
> 	char SQLSTATE[6];
> 	EXEC SQL END DECLARE SECTION;
> 	EXEC SQL DECLARE gradex cursor // 定义游标
> 		for select 学号, 课号, 分数 from grade where 学号=:givensno;
> 	EXEC SQL open gradex;// 打开游标
> 	while(1){
> 		EXEC SQL fetch gradex into :msno, :mcno, :mgrade;// 提取数据
> 		if(NO_MORE_TUPLES) break;
>         if(mgrade<60){
>             EXEC SQL delete from grade where CURRENT OF gradex;
>         }
>         else{
>             if(mgrade<70){
>                 EXEC SQL update grade set 分数=70 where CURRENT OF gradex;
>                 mgrade=70;
>             }
>         }
> 	}
>     EXEC SQL close gradex;// 关闭游标
>     printf("%s,%s,%d",msno,mcno,mgrade);
> }
> ```
>
> 3、动态SQL
>
> ```c
> // 在许多场景下SQL语句并不能在编译时就确定下来，或者在编译时不能确定SQL语句中的参数值，这些不确定部分需要在程序运行过程中动态获得。则就要求在编译源文件中要为这些不确定因素保留位置。所有了动态语句的语法定义。
> 
> // 1、动态SQL语句，在sql语句本身不确定的情况下使用
> EXEC SQL PREPARE 动态SQL语句名 from 动态变量;
> // 其中动态sql语句名只是一个代号，充当一条SQL语句，以便后续程序书写的需要。其内容保存在一个变量中，该变量的值会在程序运行过程中动态的生成。
> 
> // 2、动态sql执行语句，用在执行动态SQL语句，或者缺少参数值的SQL语句
> EXEC SQL EXECUTE 动态SQL语句名; // 在动态SQL确定后，执行动态sql语句
> EXEC SQL EXECUTE 动态SQL语句名 using 变量[,变量];//该语句表示SQL中的某些参数值来自于后续变量中
> 
> 
> // 实例，执行用户输入的SQL语句
> EXEC SQL BEGIN DECLARE SECTION;
> char *query;
> EXEC SQL END DECLARE SECTION;
> scanf("%s", query);
> EXEC SQL PREPARE que from :query;
> EXEC SQL EXECUTE que;
> // 当SQL只执行一次时（后续代码中不会用到该SQL语句时），可以用：EXEC SQL EXECUTE IMMEDIATE :query，来代替上述的定义和执行两条语句。表示执行SQL语句，内容来自query，又因为没有定义sql语句名所有后续程序想要使用该SQL时都只能通过这个方式调用，不能通过语句名调用该sql语句
> 
> // 实例，执行缺少参数值的SQL
> char *query="DELETE FROM grade where 学号=?"; // 在sql语句中使用问号(?)表示占位符
> EXEC SQL PREPARE que from :query;
> EXEC SQL BEGIN DECLARE SECTION;
> char sno[5]="1001";
> EXEC SQL END DECLARE SECTION;
> EXEC SQL EXECUTE que using :sno;// sql语句中的参数来自于主变量sno，放在SQL语句中的占位符位置
> 
> ```
>
> 