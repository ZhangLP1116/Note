**JSP内置对象**

1、**request：**
		所属类：==**javax.servlet.http.HttpServletRequest**==
		说明：封装了客户端请求信息
		作用：可以通过这个对象获取用户发起请求时的参数，如用户名，密码等。
		常用方法：.getParameter("KEY-NAME")，.setCharacterEncoding("UTF-8")， ==（详细见P44页）==

```jsp
<!--例 -->
<%
// .setCharacterEncoding(String encoding)，这个方法用来设置接受到的请求头的解码字符集
requests.setCharacterEncoding("UTF-8");
// .getParameter(String name)，在post、get请求中通过属性名获取属性值
String username = requests.getParameter("username");
String password = requests.getParameter("password");
String sex = requests.getParameter("sex");
// getHerder可以获取请求头中的参数，如获取请求的URL地址
String url = requests.getHerder("Request URL")
//获取浏览器中随着这次请求所发送的所有cookie
Cookie []cookies = requests.Cookies();
%>
```

2、**response**
		所属类：==**javax.servlet.http.HttpServletResponse**==
		说明：包含了响应客户端请求的相关消息
		作用：可以通过这个对象设置返回头中的个个参数，添加cookie，重定向等
		常用方法：.setHeader(String name, String value)，.sendRedirect(String location)，addCookie(Cookie cookie)
		==（详细见P52页）==

```jsp
<%
// 设置请求头中的Refresh属性的参数为5，该属性的作用是网页每5秒刷新一次
response.setHeader("Refresh", "5");
// 添加了一个url地址，5s后将转跳到该页面
response.setHeader("Refresh", "5;url=a.jsp");
// 将页面重定向到url
response.sendReDirect("www.baodu.com");
// 设置返回文件类型，如html、txt、word文件等
response.setContentType("text/html; charset=UTF-8");
response.setContentType("text/plain; charset=UTF-8");
response.setContentType("application/msword; charset=UTF-8");
%>
```

3、**out**
		所属类：==**javax.servlet.jsp.JspWriter**==
		说明：向客户端输出数据的对象
		作用：向客户端输出数据，可以用于显示文字
		常用方法：print()，println()，close()。==（详细见P53页）==

```jsp
<div class="test">
    <% 
    // out可以直接将内容输出到页面上
	name = zhang;
    out.print(name);
    out.println("hello world");
    %>
</div>
```

4、**session**
		所属类：==**javax.servlet.http.HttpSession**==
		说明：与当前请求相关的会话
		作用：在一段时间内保存用户的相关信息，当用户访问同一网站内的不同页面时，服务器可以直接读取该对象中的信		息，不需要用户在进行重复性的操作，如单保存用户登录信息等，该对象默认情况下会保存到这个浏览器关闭。
		常用方法：setAttribute(String name, String value)，getAttribute(String name)，removeAttribute(String name)
		setMaxInterval(int interval)==（详细见P60页）==

```jsp
<%
// 在会话中添加属性和值
session.setAttribute("name", "tom");
session.setAttrebute("passwd", "123456");
// 获取会话中属性对应的值
session.getAttribute("passwd");
// 删除会话中某一属性
session.removeAttribute("name");
// 设置会话心跳，当客户端在指定时间内没有在发送请求则自动关闭会话，以秒为单位。若参数小于0则session不会自动失效。
session.serMaxInterval(100);
%>
```

5、**application**
		所属类：==**javax.servlet.ServletContext**==
		说明：一台Java虚拟机上的一个Web应用只有一个application对象，该对象在服务器启动时创建，直到服务器关闭，		所有访问该Web应用的用户都共享该对象
		所用：存放全局数据，实现用户间数据共享
		常用方法：getAttribute(Srting name,)，serAttribuet(String name, Object object)，removeAttribute(Steing name)
		getServerInfo()==（详细见P61页）==

```jsp
<%
//使用Map创建绑定关系，将商品编号和商品实例绑定，书本P64页项目
class Book{ pass };
MAP<String, Book> bookMap = new HashMap<String, Book>();
// 为application对象设置属性，因为setAttribute对象的第二个参数为object时所有对象的父类所以在可以传递任意类型的对象给这个形参
application.setAttribute("bookMap", bookMap);
%>
<%
// 获取application对象bookMap属性的值，正因为getAttribute方法时void类型所以方便类型转换
Map<String, Book> bookMap = Map<String, Book> application.getAttribute("bookMap");
// 删除application对象bookMap属性
removeAttribute("bookMap");
// 获取服务器信息
application.getServerInfo("")
%>
```

6、**page**
		所属类：==**javax.lang.Object**==
		说明：指当前JSP页面本身，作用类似于this

7、**pageContext**
		所属类：==**javax.servlet.jsp.PageContext**==
		说明：提供了对JSP页面内所有对象及名字空间的访问

8、**config**
		所属类：==**javax.servlet.servletConfig**==
		说明：Servlet初始化时，向其传递配置参数的对象

9、**exception**
		所属类：==**javax.lang.Throwable**==
		说明：页面运行中发生异常而产生的对象

附：**cookie**
		1、cookie对象的创建：Cookie c = new Cookie("cookieName", "cookieValue")
		2、将cookie发送给客户端：response.addCookie(Cookie c)
		3、从客户端读取cookie：Cookie [] cookies = requests.getCookies()
		4、从cookie中获取属性和属性值：cookies[0].getName()、cookies[0].getValue()



QA

Q：response.sendReDirect()方法的重定向和\<jsp:forward>的重定向有什么区别
A：1、前者重定向时会改变客户端页面的URL，后者不会
	  2、前者重定向时不会共享requests的资源，后者可以共享
	  3、前者可以重定向到其他站点的页面，后者只能重定向到同一Web应用下的页面

Q：application、session、requests、page作用域大小排序
A：application \>  session \> requests \> page

> page里的变量没法从index.jsp传递到test.jsp。只要页面跳转了，它们就不见了。
>
> request里的变量可以跨越forward前后的两页。但是只要刷新页面，它们就重新计算了。
>
> session和application里的变量一直在累加，开始还看不出区别，只要关闭浏览器，再次重启浏览器访问这页，session里的变量就重新计算了。
>
> application里的变量一直在累加，除非你重启tomcat，否则它会一直变大。