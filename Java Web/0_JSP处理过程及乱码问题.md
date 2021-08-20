JSP处理过程：
		1、JSP Web服务器将浏览器端所请求的JSP文件安装pageEncoding指定的编码转换成Servlet类
		2、将该Servlet类生成.java源代码文件
		3、将Servlet源代码.java文件生成.class文件
		4、服务器执行这个.class文件后将执行结果以网页显示发送给浏览器进行展示，响应页面按照contentType指定的编		码进行显示



JSP乱码问题：==pageEncoding==和==contentType==属性设置错误
	由于服务器传出的乱码
		1、根据上述处理过程可知，当JSP文件中含有中文字符时如编码格式不支持中文则会造成.java源代码文件乱码，进		而到客户端显示时也会乱码，也就是pageEncoding属性设置错误
		2、当服务器收到用户发起的请求时，当使用requests对象去读取提交的参数时，如参数中含有中文字符，如姓名		等，那么若提交的字符集不支持中文则，读取的姓名就会乱码，那么返回页面中的姓名也就会出现乱码的情况。
		==（书本P46页）==
	在客户端生成的乱码
		1、当文件展示页面包含中文字符时，若编码格式不支持中文则浏览器显示时会发生乱码，即contentType属性设置错		误
		

JSP pageEncoding和contentType属性缺省情况
	1、如果用户设置了pageEncoding属性值，则JSP页面编码由pageEncoding属性决定
	2、如果没有设置pageEncoding属性值，则该属性值默认采用contentType属性中的charset值
	3、如果pageEncoding和charset都没有设置，则按照默认的ISO-8859进行编码。