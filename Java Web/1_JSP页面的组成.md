**JSP页面的组成**：动态部分+静态部分
		静态部分：使用HTML标记来完成内容的展示
		动态部分：包括脚本元素、指令元素、动作元素来完成数据的处理

**JSP脚本元素**：用来嵌入JAVA代码，这些代码将成为转换得到的Servlet的一部分
	格式：
			\<%！ %>：声明部分，用来声明变量，方法
			\<%     %>：代码部分，用来插入JAVA代码
			\<%=表达式%>：表达式，可以直接把JSP页面的数据输出到页面，要注意表达式语句中不能使用分号且一次只能			嵌入一个表达式。

**JSP指令元素**：为JSP引擎所设计，产生不可使输出，只告诉引擎如何处理JSP页面，从整体上控制Servlet的结构。
	格式：\<%@ %>
	指令：
			page：页面设置指令，通过设置该指令的属性去定义JSP页面的全局特性。
			例：\<%@ page language="java" contentType="text/html"; chatset="UTF-8" %>
			==（详细属性描述见书本P27）==
			include：页面包含指令，在一个JSP中包含另外一个文本内容，文本类型可以是HTML、Word、JSP、TXT等，被			包含文件的内容会展示在该指令的位置，该指令只能包含静态内容无法传递参数。
			例：\<%@ include file ="文件路径"%>
			taglib：标签导入指令，在JSP文本中导入标签，以便在JSP中使用标签更方便的完成一些动作
			例：\<%@ taglib uri="tagLibraryURI" prefix="tagPrefix"%>，uri是一个URI标识标记库描述器，用来唯一的命名一			组定制的标记，并告诉包容器如何处理特殊标记。prefix定义一个字符串前缀，用于定义定制的标签。

**JSP动作元素**：是JSP中的一类标记符合XML语法格式，利用这些标记可以起到控制Servlet引擎行为的作用。
	常用指令：
			\< jsp:include >：用来包含一个静态或者动态的文件
			\< jsp:forward >：用来重定向带一个静态HTML文本或者程序段
			\< jsp:params >：用于传递参数，必须和其他支持参数的标签一起使用
			==（更多指令见书本P35）==
	例子：

```jsp
<%-- 不带参数的文件包含，flush参数表示是否在目标被包含前将其刷新到缓存区 --%>
< jsp:include page="被包含文件路径|\<%=表达式%>" flush="true|false" />
<%/* 带参数的文件包含，包含文件时会携带参数到指定的文件中 */%>
< jsp:include page="被包含文件路径|\<%=表达式%>" flush="true|false" >
< jsp:params name="params1" value="value1">
< /jsp:include>
```

```jsp
<!--不带参数的重定向-->
< jsp:forward page="转向的文件路径|\<%=表达式%>" />
<!-- 带参数的重定向 -->
< jsp:forward page="转向的文件路径|\<%=表达式%>"  >
< jsp:params name="params1" value="value1">
< /jsp:forward>
```

**JSP注释**：
	显示注释：HTML注释 \<!-- 内容 -->，浏览器端可见
	隐式注释：客户端不可见
		1、// ：java单行注释
		2、/* */：java多行注释
		3、\<%-- 内容 --%>：JSP单行注释
		4、\<% /\* 内容 */%>：JSP多行注释



QA

Q：静态包含指令include和动态包含\<jsp:include>有什么不同
A：静态包含不能传递参数，被包含的内容总是不变的；动态包含可以携带参数，被包含的内容随参数而变化。

Q：JSP的默认脚本语言是什么，怎么修改。
A：默认脚本语言是JAVA，可以通过指令\<%@ page language="java"%>来修改