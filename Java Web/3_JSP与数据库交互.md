**JSP数据库与数据库交互主要通过JDBC实现**（Java Database Connection）

**1、JDBC的核心接口与类及常用方法**==（详细见P93页）==

> **Driver接口**
> 	作用：是驱动程序与java应用程序之间的通信接口，是驱动程序必须实现的接口
>
> **DriverManager类**==（详细见P94页）==
> 	作用：负责管理JDBC驱动程序的基本服务，使用这个类与数据库建立连接
> 	常用方法：static getConnect(String url, String user, String passwd)
>
> **Connection接口**==（详细见P94页）==
> 	作用：作用与应用程序与数据库连接之间，用来创建Statement对象
> 	常用方法：Statement createStatement()，PreparedStatement preparedStatement(String sql)
>
> **Statement接口**==（详细见P95页）==
> 	作用：向数据库发送SQL语句
> 	常用方法：void addBatch(String sql)，int[] executeBatch()，ResultSett executeQuery(String sql)，
> 		int executeUpdate(String sql)

**2、使用JDBC，连接数据库的基本步骤**

```jsp
<!-- JSP与数据库交互基本流程 -->
1、加载数据库驱动程序
2、携带URL、账号、密码建立连接
3、创建Statement对象
4、Statement对象执行SQL语句
5、关闭资源
<!---->

<!-- 导入java sql包 -->
<%@ page import="java.sql.*"%>
<%
// 连接Mysql、SQL Server、Oracle
// 1、加载数据库驱动程序,Class.forname("驱动程序名").Instance();，驱动程序从对应数据库官网下载，驱动程序名有由厂商提供
// mysql
Class.forName("con.mysql.jdbc.Driver").Instance();
// SQL Server
Class.forname("com.microsoft.sqlserver.jdbc.SQLserverDriver").Instance();
// Oracle
Class.forname("oracle.jdbc.drever.OracleDriver").Instance();
// url中要指明要使用的数据库
String url = "jdbc:mysql://localhost:3366/hncst";
String name = "hncst";
String passwd = "123456";
String sql = "select * from user";
// 2、建立数据库连接
Connection con = DriverManager.getConnect(url, name, passwd);
// 3、创建Stetement对象
statement st = con.createStatement();
// 4、执行SQL语句，返回查询结果，ResultSet对象就是数据库中的表，可以一条一条的遍历
ResultSet re = st.excuteQuery(sql);
// next()方法会使结果集的下一行成为当行
re.next();
// getString(String name)方法会根据字段回复字段值
re.getString("name");
// 5、释放资源
re.close();
st.close();
con.close();
%>
```

**3、通过SQL语句查询数据库不同片段的数据实现分页效果**

```jsp
<%
// 完整代码见“ P101 ”
// mysql，利用limit关键字来限制查询结果，逗号前的参数表示起始位置，逗号后的参数表示记录数量
String sql = "select * from user limit "page(-1)*pagesize + "," + pagesize" ";
// SQL Server，使用top关键字查询到包含到当前页的数据，在这个结果中去掉当前页-1页面包含的数据，就得到当前页这一页的数据
String sql = "select top 当前页*每页记录数 * from user where id not in (select top (当前页-1)*每页记录数 id from user) ";
// oracle，利用ROWNUM伪字段，方法和SQL Server中的TOP类似
/*
select * from
(
select A.*, ROWNUM RM
from (select * from user) A
where ROWNUM <= 当前页*每页记录数
)
where RN > (当前页-1) * 每页记录数
*/
%>
```

**4、怎么高效执行批量SQL执行**

> **Statement 对象与PreparedStatement对象**：Statement是PreparedStatement接口的父接口，PreparedStatement接口在实例化对象时会传入SQL语句进行预编译，执行SQL语句时只需要传递特定的参数就可以直接执行，不需要再次编译，而Statement对象每次执行SQL语句都需要再次编译，所以PreparedStatement对象在重复执行SQL语句的效率会高于Statement对象。
>
> **Statement对象的主要功能和常用方法**
> 	主要功能：Statement对象主要用于执行select查询语句
> 	常用方法：ResultSet executeQuery(String sql)，int executeUpdate(String sql)
>
> ```jsp
> <%
> // ResultSet executeQuery(String sql)执行SQL并返回一个ResultSet对象
> // int executeUpdate(String sql) 执行SQL并返回影响行数
> %>
> ```
>
> **PreparedStatement对象的主要功能和常用方法**
> 	主要功能：PreparedStatement对象主要用于SQL使用频繁的场景，如数据的插入，修改，查询等
> 	常用方法：void addBatch(String sql)，int[] executeBatch()，ResultSett executeQuery(String sql)，
> 		int executeUpdate(String sql)，setSrting(int number, String value)
>
> ```jsp
> <%
> // setSrting(int number, String value)用于向预编译的SQL中传入参数
> String sql = "insert into user(username,passwd,sex) value(?,?,?)";
> PreparedStatement pstm = con.preparedStatement(sql);
> pstm.setString(1,"tom");
> patm.setString(2,"123456");
> patm.setString(3,"male");
> // void addBatch(String sql)增加SQL语句
> // int[] executeBatch()执行增加的SQL语句
> patm.executeBatch()
> %>
> ```
>
> 

**5、数据库连接池**

> **数据库连接的问题**：数据库接连时JDBC应用程序中最为耗时的一个部分，所以每次都重新建立连接是非常低效的。但连接如果一直保存在服务器上，当连接数量变多后会非常作用服务器资源。
>
> **数据库连接池**：就是用来解决数据库连接中的需求。连接池负责分配、管理、和释放数据库连接，它允许应用程序重复使用一个现有的数据库连接，而不是重新建立一个。并且当连接请求变多时连接池会动态创建新的连接供应用程序使用，当需求空闲时连接池就会释放一些空闲的连接减少服务器资源占用
>
> **连接池的实现**
>
> ```jsp
> <!-- 连接池实现步骤 -->
> 1、从Web应用服务器下载DBCP文件（DataBase Connection Pool），如Tomcat（见P105、110）下载三个包，commons-dbcp2，commos-pool2，commons-logging
> 2、将包放入项目特定目录下
> 3、创建DBPC配置文件
> 4、代码实现
> <!-- 配置文件 -->
> 文件名：dbcp.properties
> driverClassName = com.mysql.jdbc.Driver		#驱动名
> url = jdbc:mysql://127.0.0.1:3306/hncst
> name = hncst
> passwd = 123456
> maxActive = 50		#最大连接数
> maxIdle = 20		#最大空闲数
> minIdle = 5			#最小空闲数
> maxWait = 60000		#超时等待时间，单位毫秒
> connectionProperties=userUmicode=true;characterEncoding=gbk		#编码设置
> defaultAutoCommit=true		#自动提交状态
> 
> <!-- 代码实现 -->
> <%@ page import="导入必要包，见P106"%>
> <%
> // 1、创建配置文件对象
> Properties p = new Properties();
> // 2、读取配置文件
> InputStream instream = Thread.currentThread().getContextClassLoader().getResourceAsStream("dbcp.properties");
> // 3、将配置文件信息放入配置文件对象中
> p.load(instream);
> // 4、创建连接池，连接池创建完成后会直接创建好最小连接数的连接对象放入连接池中
> basicDataSource bds = BasicDataSourceFactory,createDataSource(p);
> // 5、从连接池中获取连接对象
> Connection con = bds.getConnection();
> %>
> ```
>
> **连接池注意点==（详细见P108页）==**
> 	1、并发问题：在多线程环境下的并发问题可以通过synchronized关键字解决
> 		如：public synchronized Connection getConnection()
>
> ​	2、多数据库服务器和多用户：如何实现不同数据库连接池的管理
> ​		可以使用==单例模式==去创建一个连接池管理类，这个类读取一个包含多个数据库连接详细的配置文件，再通过		这个类去创建特定的数据库连接池实例，如Mysql连接池实例。如果要使用不同用户去连接数据库只要把对		应的用户添加到配置文件中即可。这样就实现了多个数据库的统一管理，和多个用户登录。
>
> 3、事务处理：事务具有原子性，既要求对一组SQL语句要么全做要么全部不做。
> 		这个特性可以通过Connection类去实现，Connection类提供了对事务的支持，可以设置Connection对象的		AutoCommit = False禁止自动提交，调用commit()显示的提交SQL语句组的整个执行，调用rollback()方法实		现整个结果的回滚。
>
> 4、连接池的分配与释放：连接池中的数据库连接数量对服务器性能的影响很大，所以需要合理的使用连接
> 		在数据库连接池中会把所有空闲的连接按照创建时间先后的顺序放入一个容器中，当有应用程序需要连接资		源时就从容器中取出建立时间最长的连接如还有效则交给应用程序使用，无效则删除再从容器中取。
> 		当容器中的连接数不够时，判断连接数是否超过连接池所能创建的最大连接数，若没达到则创建新的连接。
>
> 5、最大连接数和最小连接数的配置
> 		最小连接数：是系统启动时连接池所会创建的连接数。该数量的多少会影响系统的启动
> 		设置过多则系统启动慢，但应用响应快
> 		设置过少则系统启动快，但应用响应慢
>
> ​		最大连接数：连接池中能创建的连接数量上限，基于应用场景设置数量
>
> 

