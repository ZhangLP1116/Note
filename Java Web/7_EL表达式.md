**1、EL表达式的概述**

> EL表达式全称：Expression Language，表达式语言。是JSP 2.0中的一个重要组件。在JSTL中被广泛应用。
> JSTL：Java Server Page Standard Tag Libray，JSP标准标签库。

**2、EL表达式作用**

> 代替复杂的java语句，简化对象的访问、对象属性的访问、集合元素的访问，提供运算功能，条件判断、自动类型转换等。

**3、EL表达式的语法**

> 语法结构：
> ${expression}，以$符号开头，在花括号内写表达式或者变量，作用是在JSP页面中输出对应的值。
>
> 运算符：
> 变量存取运算符
> EL表达式提供 " . " 和“ [ ] ”来存取变量，当要存取的属性名中包含特殊字符 " . " 或“ ？ ”时就需要使用“[ ]”去存取变量。要动态取值时也需要用“[ ]”去存取变量。
>
> 算输运算符
> 加，减，乘，除，取余
>
> 逻辑运算符
> 与，或，非
>
> 关系运算符
> 大于，小于，等于，大于等于，小于等于，不等于
>
> 其他运算符
> 1、empty运算符：用来判断值是否为空
> 2、条件运算符：${A ? B : C}，若A为True则值为B，否则值为C
> 3、()y运算符：用来改变运算优先级

**4、EL表达式的内建对象**

> 一共有6类11个对象
>
> 1、JSP页面类：
> pagecontext：代表此页面的oageContext对象
>
> 2、作用范围类：
> pageScope：用于读取page范围内的属性值
> requestScope：用于读取request范围内的属性值
> sessionScope：用于读取session范围内的属性值
> application：用于读取application范围内的属性值
>
> 3、请求参数类：
> param：用于读取请求参数中的参数值，相当于执行JSP中的request.getParamter(String name)方法
> paramValue：用于读取请求参数中的参数值数组，相当于执行JSP中的request.getParamterValues(String name)方法
>
> 4、请求头类型：
> header：用于取得请求头的值，相当与执行JSP中的request.getHerder(String name)
> herder Values：用于取得请求头的值数组，相当与执行JSP中的request.getHerders(String name)
>
> 5、Cookie类型：
> cookie：用于获得request中的cookie集，相当于执行JSP中的request.getCookies()
>
> 6、初始化类型：
> initParam：用于取得Web应用程序上下文初始化参数值，相当于执行application.getInitParameter(String name)

**5、EL表达式数据类型和自动类型转换**

> 数据类型：
> 1、Boolean：布尔类
> 2、Integer：整形，与Java一致
> 3、Float：浮点型，与Java一致
> 4、String：字符串，与Java一致
> 5、Null：空值，null
>
> 自动类型转换
> 1、EL表达式的输出结果，会被强制转换成字符串类型和其他静态文本拼接在一起
> 2、运算表达式中不同的类型将被自动转换成相同类型进行运算，如${param.count + 20}这个EL表达式将输出30，其中param.count的结果本来是一个字符串类型，在这个表达式中被自动转换成了整形进行运算。

**6、JSTI核心标签**

> 核心标签库：http://java.sun.com/jsp/jstl/core
>
> 标签库的引用：\<%@taglib uri = "http://java.sun.com/jsp/jstl/core" prefix = "c"%>
> uri：统一资源标识符，表示要引入的标签库
> prefix：为引入的标签库取一个别名，以便在JSP页面中使用
>
> 标签：标签一般都是成对出现
> 1、if标签：先对某个条件进行测试，如果该条件运算结果为 true，则处理它的主体内容，测试结果保存 在一个 Boolean 对象中，并创建一个限域变量来引用 Boolean 对象。可以利用 var 属性设置限域变量 名，利用 scope 属性来指定其作用范围。
> if 的语法有两种形式：没有主体内容、有主体内容
>
> ```jsp
> <%@taglib uri = "http://java.sun.com/jsp/jstl/core" prefix = "c"%>
> <%
> 		//定义一个变量
> 		int a = 66;
> 		//存入request作用域
> 		request.setAttribute("a",a);
> 	%>
> <!--if标签  -->
> 	<c:if test="${a>50}" var= "flag" scope="session" >
> 	<!--test="",一个表达式，结果为Boolean值，如果是true则执行标签中的代码,var定义一个键名，
> 	存储test的Boolean值，scope表示的是flag存储的作用域是哪个  -->
> 		<h2>a比较大</h2>
> 	</c:if>
> <!-- if主体结束 -->
> 
> 	<c:if test="${empty a} }">
> 		<!--empty判断a是否存在  -->
> 		<h2>a是存在的</h2>
> 	</c:if>
> <!-- if中结果为false不珍惜主体内容，结果：页面只显示a比较大  -->
> ```
>
> 2、choose、when、otherwise标签：作用和Java中的switch、case相似。
>
> ```jsp
> <!--choose，when和otherwise标签 ，
> 	起作用类似于java中的switch表达式 -->
> 	<!--注意
> 	1，choose标签中只能有when和otherwise标签，when和otherwise标签中可有其他标签
> 	2，choose标签中至少有一个when标签
> 	3，choose标签和otherwise标签中没有属性，when标签必须有test属性
> 	4，otherwise标签必须放在最后一个when标签之后
> 	5，当所有的when标签的条件都不成立时，才执行otherwise标签中的语句
> 	6，when标签不存在穿透 -->
> 	<%
> 		request.setAttribute("a", 4);
> 	%>
> 	<c:choose>
> 		<c:when test="${a>=3&&a<=5} ">
> 			<h2>现在是春天</h2>
> 		</c:when>
> 		<c:when test="${a>=6&&a<=8} ">
> 			<h2>现在是夏天</h2>
> 		</c:when>
> 		<c:when test="${a>=9&&a<=11} ">
> 			<h2>现在是秋天</h2>
> 		</c:when>
> 		<c:when test="${a==4 }">
> 			<h2>现在是初春</h2>
> 		</c:when>
> 		<c:otherwise>
> 			<h2>现在是冬天</h2>
> 		</c:otherwise>
> 	</c:choose>
> 	<!--结果显示为初春  -->
> 
> ```
>
> 3、forEach标签：是将一个主体内容迭代多次，或者迭代一个对象集合。可以迭代的对象包括所有的 java.util.Collection 和 java.util.Map 接口的实现，以及对象或者基本类型的数组。
>
> ```jsp
> <!--forEach标签；
> 	两种作用，1，将主体内容循环多次
> 			2，迭代集合  -->
> 	<!--将主体内容循环多次  -->
> 	<c:forEach var="i" begin="1" end="7">
> 	<!--var：用来存放现在被指到的对象，begin开始的位置，end结束的位置  -->
> 		主体内容：${i }
> 	</c:forEach>
> 	<!--结果为：主体内容：1 主体内容：2 主体内容：3 主体内容：4 主体内容：5 主体内容：6 主体内容：7 主体内容  -->
> 	
> 	<!-- 迭代集合 -->
> 	<!-- list -->
> 	<%
> 		List<String> list = new ArrayList<String>();
> 		list.add("xiaoyan");
> 		list.add("lingdong");
> 		list.add("yefan");
> 		request.setAttribute("list", list);
> 	%>
> <!-- items代表被迭代对象，var表示被迭代对象当前取值，varStatus表示被迭代对象的排序状态 -->
> 	<c:forEach items="${list}" var="str" varStatus="status" >
> 		${str }:${status.index }:${status.count }:${status.first }:${status.last }
> 		<!--index表示索引，count表示出现的位数，first表示是否是第一个，last表示是否是最后一个  -->
> 		
> 	</c:forEach>
> 	<!--map  -->
> 	<%
> 		Map<String,Object> map = new HashMap<String,Object>(); 
> 		map.put("user1",new User("zs","123"));
> 		map.put("user2", new User("ls","1234"));
> 		request.setAttribute("map",map);
> 	%>
> 	<c:forEach items="${map}" var="user">
> 	 	${user.key }:${user.value }
> 	 	${user.value.uname }
> 	 	${user.value.upwd }
> 	</c:forEach>
> 
> ```
>
> 



**7、EL表达式的使用**
从Tomcat官网下载taglibs-standard-impl-1.2.5.jar和tagilbs-standard-apec-1.2.5.jar，放到项目文件的WEB-INF\lib目录下

```jsp
	<!-- 引入标签库 -->
	<%@tarlib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
	<!--使用标签，迭代map  -->
	<%
		Map<String,Object> map = new HashMap<String,Object>(); 
		map.put("user1",new User("zs","123"));
		map.put("user2", new User("ls","1234"));
		request.setAttribute("map",map);
	%>
	<c:forEach items="${map}" var="user">
        <!-- 输出内容 -->
	 	${user.key }:${user.value }
	 	${user.value.uname }
	 	${user.value.upwd }
	</c:forEach>
```

**ps**：在使用EL表达式获取变量值时，如没有指明变量保存的范围，则EL默认按照page、request、session、application的顺序查找变量，中途找到变量这退出查找，若始终没找到变量则返回空值。如${username}

推荐在获取变量值时携带变量的所在范围，这样会加快程序的运行速率，如：${pageScope.name}、${requestScope.username}。一般用于获取会话中的会话或者application范围内的变量值

推荐在获取request请求中的变量时使用param对象，能更快的获取变量值，如：${param.name}，相当于使用JSP内置对象request.getparameter(name)。