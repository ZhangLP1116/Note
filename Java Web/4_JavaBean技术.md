**相关知识**

> **Java Bean**：是一种规范，表达实体和信息的规范，便于代码的封装重用。
> 	它是一个容器，程序员需要在容器内封装好功能代码，使得这个容器变成一个自动热水器，每当需要喝热水时	主要调用这个水壶去倒出热水，不需要再次编写代码去烧热水。
> 	增加代码的复用，使得项目中的每一个部分都成为一个独立的个体，程序员不需要明白内部功能的编写，只需	要关注外部逻辑及调用它们的功能。
>
> **J2EE**（Java 2 Platform Enterprise Edition也叫java EE）
> 	是一种企业级分布式应用平台规范，其中包含
> 	**JDBC**:  Java 数据库连接， 没有数据库的支持怎么能叫企业级应用？
> 	**JNDI** :  Java 命名和目录接口， 通过一个名称就可以定位到一个数据源， 连jdbc连接都不用了，JNDI可以看	作是一个容器，容器里已经把我需要的对象给创建好了，我们只需要取出来用就行
> 	**RMI**：  远程过程调用，  让一个机器上的java 对象可以调用另外一个机器上的java 对象 ， 你们不是要分布式	吗？
> 	**JMS** :  Java 消息服务，  可以使用消息队列了， 这不是企业级应用非常需要的吗？
> 	**JTA**：  Java 事务管理， 支持分布式事务， 能在访问、更新多个数据库的时候，仍然保证事务， 还是分布		式。
> 	**Java mail** : 收发邮件也是必不可少的啊。
> 	**EJB**：(Enterprise Java bean)，是对Java Bean 的一种扩展，增加了事务管理、安全管理、线程管理等

**JavaBean与JSP**

**0、JavaBean规范**

> 规范
> 1、JavaBean必须是一个公共类
> 2、JavaBean的构造方法，如果存在则必须是public并且是无参的
> 3、JavaBean不应该有公共成员变量，成员变量应该都是private（私有的）
> 4、私有属性必须实现属性的存取方法用于属性的交互，getXxx和setXxx
> 5、属性名以小写字母开头，以驼峰命名格式，如userNman对应的方法就是getUserName / setUserName
>
> 特点
> 1、一次编写：一个成功的JavaBean组件重用时不需要重新编写，开发者只需要根据需求进行修改和升级
> 2、任何地方执行：因为时Java语言编写的类，所以具有和Java一样的特性
> 3、任何地方重用：JavaBean能够被多个方案中使用。

**1、使用JavaBean封装用户信息**

> **JavaBean类的编写**
>
> ```java
> // UserInfo.java
> Public class UserInfo{
>     // 根据规范，设置变量属性为private，驼峰命名
>     private String userName;
>     private String userPassword;
>     private String sex;
>     private int age;
>     private String address;
>     // 属性操作的方法名也要依据规范
>     public void setUserName(String userName){
>         this.name = name;
>     }
>     public String getUserName(){
>         return this.userName
>     }
>     // ......其余方法同上，根据JavaBean规范编写好的类就是一个JavaBean类
> }
> ```
>
> **JavaBean的调用**
>
> ```jsp
> <!-- 导入编写好的JavaBean类 -->
> <%@ page import='UserInfo'%>
> 
> <!-- 使用JSP动作创建JavaBean实例，参数id表示实例名，class表示类名，scope表示该实例的作用范围，有page，request，session，application四个范围可以选择详细见P119页 -->
> <jsp:usebean id='user' scope='page' class='UserInfo'/>
> 
> <!-- 直接调用JavaBean类创建实例 -->
> <%
> UserInfo user = new UserInfo()
> %>
> ```
>
> **JavaBean的属性交互**
>
> ```jsp
> 			<!-- 使用JSP动作进行JavaBean实例的属性交互 一般用于和前端的交互-->
> 设置实例user的userName属性，这里看起来是直接对访问实例的属性，实际上是通过setUserName()方法去设置属性
> 这体现了JavaBean的好处，外部的交互有统一的接口，内部的修改不会改变外部的交互方式
> 这种设置属性的方式是在已知属性值的情况下，如tom
> <jsp:setProperty name='user' property='userName' value='tom'/>
> 查看实例user的userName属性，这里同理使用了getUserName()方法查看userName属性的值
> <jsp:getProperty name='user' property='userName'/>
> 
> 			<!-- 通过表单自动设置JavaBean实例的属性 -->
> 该语句会根据表单提交的参数自动设置user实例的属性，要求表单中的name属性值要和user实例的属性名一致，P120
> <jsp:setProperty name="user" property='*'/>
> 
> 			<!-- 通过request对象设置JavaBean实例的属性 -->
> 这种方法一般用于属性值未知，需要用户提交后自动设置的场景，param表示被设置属性的值，psw是一个变量，该变量的值从客户端发起的请求中获取，要求请求中的变量名和该变量名一致/
> 注意param和value参数不能同时出现
> <jsp:setProperty name="user" property="nameUser" param,="psw" />
> 
> 			<!-- 直接调用方法进行属性交互 一般用于和数据库的交互-->
> <%
> // 直接创建实例并调用方法，一般用于数据库JavaBean实例调用场景
> UserInfo user = new UserInfo();
> user.setUserNmae("tom");
> out.user.getUserName();
> %>
> ```
>
> 
>

**2、使用JavaBean封装数据库连接**

> **JavaBean数据库连接类的编写**
>
> ```java
> // DBManager.java
> import java.sql.*;
> class pubic DBManager{
>     private Connection conn = null;
>     private Statement st = null;
>     private ResultSet re = null;
>     private PreparedStatement pstm = null;
>     
>     // 加载驱动创建连接
>     public Connection ConnDB(){
> 		conn = null;        
>         try{
>             String url = 'jdbc:mtsql://localhost:3306/test?userUnicode=true&character=UTF-8';
>             Class.forNmae("com.mysql.jdbc.Driver").newInstance();
>             conn = DriverManager.getConnection(url, "hncst", "123");
>             return conn;
>         }
>         catch (Exception fe){
>             System.err.println("ConnDB()" + fe.getMessage());
>             return null;
>         }
>     }
>     
>     // 创建Statement声明对象
>     public Statement createStat(){
>         st = null;
>         try{
>         if (conn == null){
>             conn = this.ConnDB();
>         }
>             st = conn.CreateStatement();
>             return st;
>         }
>         catch (Exception fe){
>             System.out.println("CreateStat()" + fe.getMessage());
>             return null;
>         }
>     }
>     
>     // 创建Prepared Statement声明对象
>     public PreparedStatement prepareStat(String sql){
>         pstm = null;
>         try{
>             if(conn == null){
>                 conn = this.ConnDB();
>             }
>             pstm = conn.preparedStatement(sql);
>             return pstm;
>         }
>         catch(SQLException e){
>             e.prtintStackTrace();
>             return null;
>         }
>     }
>     
>     //执行数据库查询SQL语句
>     public ResuluSet getResult(String sql){
>         try{
>             if(st == null){
>                 this.createStat();
>             }
>             re = st.executeQuery(sql);
>             return re;
>         }
>         catch(SQLExpection ex){
>             System.err.prtint("getResult()" + ex.getMessage());
>             return null;
>         }
>     }
>     
>     // 执行数据库修改SQL语句
>     public int executeSql(String sql){
>         int count;
>         try{
>             if(st == null){
>                 this.createStat();
>             }
>              count = st.executeUpdate(sql);
>             return count;
>         }
>         catch(Exception e){
>             System.err.println("executeSQL()" + e.toString());
>             return 0;
>         }
>     }
>     
>     //释放资源
>     public Release()throws SQLException{
>         if(re != null){
>             re.close();
>         }
>         if(st != null){
>             st.close();
>         }
>         if(pstm != null){
>             pstm.close()
>         }
>         if(conn != null){
>             conn.close();
>         }
>     }
> }
> ```
>
> **JavaBean数据库实例的使用**
>
> ```jsp
> 				<!-- 使用JSP动作调用实例 -->
> <%@page import='DBManager'%>
> <jsp:usebean id='db' scope='page' class='DBManager' />
> <%
> String sql1 = "select * from user";
> String sql2 = 'insert into user(name, password) values("tom","123")';
> db.executeQuery(sql1);
> db.excuteSql(sql2);
> %>
> 
> 			<!-- 直接使用类创造实例 -->
> <%
> DBManager db = new DBManger();
> String sql1 = "select * from user";
> String sql2 = 'insert into user(name, password) values("tom","123")';
> db.executeQuery(sql1);
> db.excuteSql(sql2);
> %>
> ```
>
> 

**3、使用JavaBean+JNDI封装数据库连接池**

> **JNDI配置，==属性详情见P130==**
>
> ```xml
> <ContextdocBase="JavaWebExample" path="/JavaWebExample" reloadable="true" source="org.eclipse.jst.jee.server:JavaWebExample">
>     <Resourceauth="Container" type='javax.sql.DataSource' usrl="jdbc:mysql://localhost:3306/user?useUnicode=true&amp;characterEncoding=utf-8&amp;autoReconnection=true" usename="root" password="root" logAbandoned="true" maxActive="100" maxIdle="50" minIdle="10" maxWait="10000" removeAbandoned="true" removeAbandonedTime="30" testOnResult="true" testWhileIdle="true" validationQuery="select now()" />
> </Context>
> ```
>
> **JavaBean数据库连接池类创建**
>
> ```java
> // DBManager.java
> import java.sql.*;
> // javax.naming.InitianContext用于读取配置文件，javax.naming.Context用来读取连接池对象
> // JNDI作用见上面的相关知识
> import javax.naming.Context;
> import javax.naming.InitianContext;
> 
> class pubic DBManager{
>     private Connection conn = null;
>     private Statement st = null;
>     private ResultSet re = null;
>     private PreparedStatement pstm = null;
>     
>     // 加载驱动创建连接
>     public Connection ConnDB(){
> 		conn = null;        
>         try{
>             Context InitCtx = new InitialContext();
>             // initCtx实例用来读取配置文件
>             Context ctx = (context)initCtx.loopup("java:comp/env");
>             // ctx根据配置文件中的信息取出数据库连接池实例，实例的类型为配置文件中type属性的值
>             javax.sql.DataSource ds = (javax.sql.DataSource)ctx.loopup("jdbc/WebDataPool");
>             Connection conn = ds.getConnection();
>             return conn;
>         }
>         catch (Exception fe){
>             System.err.println("ConnDB()" + fe.getMessage());
>             return null;
>         }
>     }
>     
>     // 创建Statement声明对象
>     public Statement createStat(){
>         st = null;
>         try{
>         if (conn == null){
>             conn = this.ConnDB();
>         }
>             st = conn.CreateStatement();
>             return st;
>         }
>         catch (Exception fe){
>             System.out.println("CreateStat()" + fe.getMessage());
>             return null;
>         }
>     }
>     
>     // 创建Prepared Statement声明对象
>     public PreparedStatement prepareStat(String sql){
>         pstm = null;
>         try{
>             if(conn == null){
>                 conn = this.ConnDB();
>             }
>             pstm = conn.preparedStatement(sql);
>             return pstm;
>         }
>         catch(SQLException e){
>             e.prtintStackTrace();
>             return null;
>         }
>     }
>     
>     //执行数据库查询SQL语句
>     public ResuluSet getResult(String sql){
>         try{
>             if(st == null){
>                 this.createStat();
>             }
>             re = st.executeQuery(sql);
>             return re;
>         }
>         catch(SQLExpection ex){
>             System.err.prtint("getResult()" + ex.getMessage());
>             return null;
>         }
>     }
>     
>     // 执行数据库修改SQL语句
>     public int executeSql(String sql){
>         int count;
>         try{
>             if(st == null){
>                 this.createStat();
>             }
>              count = st.executeUpdate(sql);
>             return count;
>         }
>         catch(Exception e){
>             System.err.println("executeSQL()" + e.toString());
>             return 0;
>         }
>     }
>     
>     //释放资源
>     public Release()throws SQLException{
>         if(re != null){
>             re.close();
>         }
>         if(st != null){
>             st.close();
>         }
>         if(pstm != null){
>             pstm.close()
>         }
>         if(conn != null){
>             conn.close();
>         }
>     }
> }
> ```
>
> **JavaBean数据库实例使用**
>
> ```jsp
> 				<!-- 使用JSP动作调用实例 -->
> <%@page import='DBManager'%>
> <jsp:usebean id='db' scope='page' class='DBManager' />
> <%
> String sql1 = "select * from user";
> String sql2 = 'insert into user(name, password) values("tom","123")';
> db.executeQuery(sql1);
> db.excuteSql(sql2);
> %>
> 
> 			<!-- 直接使用类创造实例 -->
> <%
> DBManager db = new DBManger();
> String sql1 = "select * from user";
> String sql2 = 'insert into user(name, password) values("tom","123")';
> db.executeQuery(sql1);
> db.excuteSql(sql2);
> %>
> ```

**Java小知识**

> ArrayList类：是一个集合，里面可以存放同一类型的对象实例，使用可以指明存放的对象类型。
>
> ```java
> public static ArratList<Book> getbooks(){
>     ArrayList books = new ArrayList();
>     for(i=1;i<=10;i++){
>         Book book = new Book();
>         books.add(book);
>     }
>     return books
> }
> ```

**QA**

Q：JavaBean是什么，怎么创建JavaBean类，怎么创建JavaBean实例并使用
A：1、JavaBean是一种规范，目的是为了更好的复用代码。
	  2、JavaBean类和普通的Java类并没有什么不同，只是我们把按照JavaBean规范书写的Java类叫做JavaBean类。所		以JavaBean类的创建就是依据JavaBean规范创建的Java类
  	3、JavaBean实例可以通过JSP动作去生成，也可以直接使用Java语句去生成，实例的使用方法也和Java普通实例使		用方法一致