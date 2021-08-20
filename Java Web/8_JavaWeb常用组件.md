1、在线编辑器

> 作用：用于在线编辑HTML文档，不需要手写HTML代码，通过界面是的操作来实现内容的HTML展示。
>
> 工具：
> 1、UEditor：由百度“FEX”前端研发团队开发的所见即所得的富文本web编辑器。基于MIT协议，开源。
> 2、CKEditor：创建于2003年，起初为FCKeditor，2009年更名为CKEditor。免费、开源
> 3、YUI Editor：是Yahoo！YUI的一部分，能输出纯净的Xhtml代码。
>
> UEditor编辑器示例：
>
> ```html
> <!-- 1、下载UEditor的jsp版本，url：http://ueditor.baidu.com -->
> <!-- 2、将下载好的文件夹中的jsp\lib下的jar包放置在WEB-INF/lib/目录下，其他文件放置在WEB-INF下的任意位置 -->
> <!-- 3、在网页中调用UEditor -->
> 
> <form id="form1" name="form1" method="POST" action="test1">
>     <input name="title" type="text" />文章标题</br>
> 	文章正文
>     <textarea cols="50" id="ArtContent" name="ArtContent" row="3">欢迎使用UEditor！</textarea>
> </form>
> <!-- 导入配置文件 -->
> <script type="text/javascript" scr="ueditor.config.js"></script>
> <!-- 导入UEditor源文件 -->
> <script type="text/javascript" scr="ueditor.all.js"></script>
> <!-- 创建实例 -->
> <script type="text/javascript">
>     // 将ArtContent文本域替换成UEditor编辑器
> 	var editor=UE.getEditor("ArtContent");
>     // 在编辑器中设置内容，一般用来设置默认值
>     editor.setContent("<p>Hello</p>")
>     // 可以读取文本域中原有的内容
>     editor.ready(function(){语句块})
> </script>
> 
> 
> ======================================
> <!-- 简化版UEditor -->
> <form id="form1" name="form1" method="POST" action="test1">
>     <input name="title" type="text" />文章标题</br>
> 	文章正文
>     <textarea cols="50" id="ArtContent" name="ArtContent" row="3">欢迎使用UEditor！</textarea>
> </form>
> <!-- 导入配置文件 -->
> <script type="text/javascript" scr="ueditor.config.js"></script>
> <!-- 导入UEditor源文件 -->
> <script type="text/javascript" scr="ueditor.all.js"></script>
> <!-- 创建实例 -->
> <script type="text/javascript">
>     // 将ArtContent文本域替换成UEditor编辑器，自定义需要的工具，简化编辑器的展示
>     // 这里导入了全屏，源码、撤销、重做、字体加粗。其他根据见配置文件：ueditor.config.js
> 	var editor=UE.getEditor("ArtContent",{
>         toolbars:[
>             ['fullcreen', 'source', 'undo', 'redo', 'bold'], 
>           ]
>             autoHeightEnabled:true,
>             autoFloatEnable:true
>     });
> </script>
> ```
>
> 

2、发送邮件

> 作用：实现邮件发送功能
>
> 步骤：
> 1、下载JavaMail API：发送邮件需要下载对应的API加载到服务器后才可以正常运行。JavaMail API下载地址为：http://java.sun.com/products/javamail/download/index.html。下载后解压mail,jar包到WEB-INF/lib目录下。也可以直接解压到Tomcat安装目录的lib路径下。
>
> 2、编写身份验证类
>
> ```java
> import java.util.ProPerties;
> import javax.mail.Authenticator;
> import javax.mail.PasswordAuthentication;
> 
> public class Auth extends Authenticator{
>     private String username="";
>     private String password="";
>     
>     public Auth(String username,String password){
>         this.username=username;
>         this.password=password;
>     }
>     // 重写了Authenticator类中的getPasswordAuthentication()，返回PasswordAuthentication对象，供认证时session调用
>     protected PasswordAuthentication getPasswordAuthentication(){
>         return new PasswordAuthentication(username,password);
>     }
> }
> ```
>
> 3、编写邮件发送类
>
> ```java
> import java.util.Properties;
> import javax.mail.Message;
> import javax.mail.Session;
> import javax.mail.Transport;
> import javax.mail.internet.InternetAddress;
> import javax.mail.internet.MimeMessage;
> 
> public class SendMail{
>     private Properties props;// 系统属性
>     private Session mailSession;
>     private MimeMessage mineMsg;
>     
>     public SendMail(String SMTPHost, String Port, String MailPassword, String MailUsername){
>         Auth au = new Auth(MailUsername, MailPassword);//上面创建的身份验证类
>         //props类似表单，将需要的参数全部收集在一起，收集主机信息
>         props.put("mail.smtp.host", SMTPHost);
>         props.put("mail.smtp.port", Port);
>         props.put("mail.smtp.auth", "true");
>         // 创建邮件会话对象，需要Properties类的对象和Authenticator类的对象
>         // 会话收集用户信息和主机信息
>         mailSession = Session.getInstance(props,au);
>     }
>     public boolean sendingMimeMail(String MailFrom, String MailTO, String MailCopyTo, String 			MailBCopyTo, String MailSubject, String MailBody){
>         // 上面变量含义分别为：发送人、收件人，抄送人，密送人，主题，主体
>         try{
>             // MimeMessage类用来设置邮件主要内容，接收会话对象初始化
>             mimeMsg = new MimeMessage(mailSession);
>             // 设置发件人邮箱
>             mimeMsg.setFrom(new InternetAddress(MailFrom));
>             // 设置收件人邮箱
>             if(MailTo!=null){
>                 // setRecipients()该方法的第一个参数说明接收人的类型，是指定的、抄送的还是密送的。
>                 // 第二个参数接受一个邮箱地址，并需要通过地址解析将邮箱地址解析为IP地址
>                 mimeMsg.setRecipients(Message.RecipientType.TO, 															InternetAddress.parse(MailTO));
>             }
>             // 设置抄送人邮箱
>             if(MailCopyTo!=null){
>                 mimeMsg.setRecipients(Message.RecipientType.CC, 															InternetAddress.parse(MailCopyTo));                
>             }
>             // 设置密送人邮箱
>             if(MailBCopyTo!=null){
>                 mimeMsg.setRecipients(Message.RecipientType.BCC, 															InternetAddress.parse(MailBCopyTo));               
>             }
>             // 设置邮件主题
>             mimeMsg.setSubject(MailSubject,"gb2312");
>             // 设置邮件主体
>             mimeMsg.setContent(MailBody,"text/html;chatset=gb2312");
>             // 发送邮件
>             Transport.send(mineMsg);
>             return true
>         }
>         catch(Exception e){
>             e.printStackTrace();
>             return false;
>         }
>     }
> }
> ```
>
> 4、编写发送邮件功能Servlet类
>
> ```java
> import java.io.*;
> import javax.servlet.*;
> import javax.servlet.http.*;
> import SendMail;// 上面编写的邮件发送类
> 
> 
> // 该servlet处理前端注册表单提交的注册信息，并对注册成功的用户发送注册成功的邮件。
> public class Reg extends HttpServlet{
>     private ServletConfig Servletconfig;
>     private String username;
>     private String email;
>     private String msg;
>     
>     public void init(ServletConfig config)throw ServletException{
>         super.init(config);
>         // 配置信息也就是写在web.xml中对应servlet节点的<init-param>节点中的信息
>         // servlet引擎会读取该配置信息，并在由对应任务时将配置信息打包成ServletConfig对象的实例交给该			servlet的init()方法作为参数。
>         this.Servletconfig = config;
>     }
>     
>     protected void doPost(HttpServletRequest request,HttpServletResponse response)throw 				ServletException, IOException{
>         request.setCharacterEncoding("UTF-8");
>         username=request.getParameter("username");
>         email=request.getParameter("email");
>         /*
>         	将新用户写入数据库
>         */
>         // 开始发送欢迎邮件
>         if(sendmail(email, username)){
>             msg="邮件发送成功";
>         }
>         else{
>             msg="邮件发送失败";
>         }
>         toResponse(response, msg);
>     }
>     
>     // 准备发送邮件相关信息和内容，调用邮件发送类的相关方法
>     private boolean sendmail(String username, String mailto){
>         String MailTo=mailto;
>         String MailSubject="注册成功！";
>         String MailCopyTo="";
>         String MailBCopyTo="";
>         String MailBody="<p>欢迎来到。。。。<p>";
>         // 邮件发送服务器IP地址
>         String SMTPHost=Servletconfig.getInitParameter("smtphost");
>         // 邮件发送服务器端口地址
>         String Port=Servletconfig.getInitParameter("port");
>         // 以下是发送人信息,可以说是网站管理者的信息，所以在配置文件中可以获得
>         String MailUsername=Servletconfig.getInitParameter("mailusername");
>         String MailPassword=Servletconfig.getInitParameter("mailpassword");
>         String MailFrom=Servletconfig.getInitParameter("mailfrom");
>         // 判断信息是否完整
>         if(SMTPHost==null || SMTPHost=="" || MailUsername==null ||
>           MailUsername=="" || MailPassword==null || MailPassword=="" ||
>           MailFrom==null || MailFrom=="" || Port==null || port==""){
>             System.out.println("config parameter Wrongs！");
>         }
>         else{
>             SendMail send=new SendMail(SMTPHost,Port,MailUsername,MailPassword);
>         }
>         if(send.sendingMimeMail(MailFrom,MailTo,MailCopy,MailBCopy,MailSubject,MailBody)){
>             return true;
>         }
>         else{
>             return false;
>         }
>     }
>     
>     private void toResponse(HttpServletResponse response, String toString)throws IOException{
>         response.setCharacterEncoding("UTF-8");
>         PrintWriter out=response.getWriter();
>         out.println(toString);
>     }
> }
> ```
>
> 5、配置web.xml
>
> ```xml
> <servlet>
>     <description>reg</description>
>     <display-name>Reg</display-name>
>     <servlet-name>Reg</servlet-name>
>     <servlet-class>Reg</servlet-class>
>     <init-param>
>         <description>SMTP Host</description>
>         <param-name>smtphost</param-name>
>         <param-value>smtp.myeyou.net</param-value>
>     </init-param>
>     <init-param>
>     	<description>Mail Port</description>
>         <param-name>port</param-name>
>         <param-value>25</param-value>
>     </init-param>
>     <init-param>
>     	<description>Mail Host Username</description>
>         <param-name>mailusername</param-name>
>         <param-value>webmaster@myeyou.net</param-value>
>     </init-param>
>     <init-param>
>     	<description>Mail Host Password</description>
>         <param-name>mailpassword</param-name>
>         <param-value>wdesix3s#</param-value>
>     </init-param>
>     <init-param>
>     	<description>Mail From</description>
>         <param-name>mailfrom</param-name>
>         <param-value>us@myeyou.net</param-value>
>     </init-param>
> </servlet>
> <servlet-mapping>
> 	<servlet-name>Register</servlet-name>
>     <url-pattern>/Reg.do</url-pattern>
> </servlet-mapping>
> ```
>
> 

3、文件的上传与下载

> 上传模块：
>
> 0、准备工作
>
> > 到Apache官网下载文件上传组件。http://commons.apache.org/fileupload/。下载commons FileUpload组件和commons io组件。
> >
> > 将jar包添加到WEB-INF/lib/目录下
>
> 1、web前端页面提交文件
>
> ```html
> <!-- 关键点：form标签的enctype属性必须设置为multipart/form-data值 -->
> <!-- 关键点：file类型的input标签，用来选择本地文件 -->
> 
> <form id="fileUploadFrom" action="/doPaperUpload" method="post" enctype="multipart/form-data">
>     学号：<input type="text" name="stuNum" /></br>
> 	姓名：<input type="text" name="stuName" /></br>
> 	论文标题：<input type="text" name="title" /></br>
> 	论文文件：<input type="file" name="paper" /></br>
> 	<input type="submit" name="submit" value="提交"/>
> </form>
> ```
>
> 2、servlet处理上传文件
>
> ```java
> import java.io.IOException;
> // java中的File类对象，可以看作是操作系统上的一个虚拟文件
> // 写入操作时通过File对象的信息在指定位置写入
> // 读取操作时根据File对象的信息从指定位置读出
> // File起到一个指引作用，器本身并不包含数据
> import java.io.File;
> import java.io.PrintWrite;
> import java.util.Iterator;
> import java.util.List;
> import javax.servlet.http.*;
> // FileItem用来保存表单信息
> import org.apache.commons.fileupload.FlieItem;
> import org.apache.commons.fileupload.disk.DiskFileItemFactory;
> // ServletFileUpload用于处理表单信息
> import org.apache.commons.fileupload.servlet.ServletFileUpload;
> 
> public class PaperUpload_do extends HttpServlet{
>     @Overide
>     protected void doPost(HttpServletResponse response,HttpServletRequest request){
>         try{
>             request.setCharacterEncoding("UTF-8");
>             response.setContentType("text/html;charset=UTF-8");
>             String uploadPath = "D:/uploadPaper/";
>            	// 获取表单数据的编码类型是否为“multipart”
>             boolean isMultipart = ServletFileUpload.isMultipartContent(request);
>             // 创建存储目录
>             if(isMultipart){
>                 File savedPath = new File(uploadPath);
>             }
>             if(! savedPath.exists()){
>                 savedPath.mkdirs();
>             }
>             // 创建临时文件存放目录
>             File tempPath = new File(uploadPath + "buffer/");
>             if(! tempPath.exists()){
>                 tempPath.mkdirs();
>             }
>             // 创建FileItem的工厂类DiskFileItemFactory实例
>             DiskFileItemFactory factory = new DiskFileItemFactory();
>             // 设置工厂制作FileItem的参数
>             factory.setSizeThreshold(4*1024);
>             // 设置FileItem临时存放路径
>             factory.setRepository(tempPath);
>             /*
>             ServletFileUpload类可以解析request请求
>             它会将请求中的所有输入项封装到一个由FileItem对象组成的List对象中。
>             ServletFileUpload类解析式依赖DiskFileItemFactory对象的createItem()方法去生成具体的			FileItem对象，所以需要传入DiskFileItemFactory对象进行初始化。
>             */
>             ServletFileUpload upload = new ServletFileUpload(factory);
>             // 调用解析方法解析请求，生成一个FileItem列表
>             List<FileItem> list = upload.parseRequest(request);
>             // 将列表内容生成一个可迭代对象
>             Iterator<FileItem> iter = list.iterator();
>             String stuNum = "";
>             String stuname = "";
>             String title = "";
>             FileItem fileItem = null;
>             while(iter.hasNext()){
>                 FileItem item=(FileItem)iter.next();
>                 // 判断对象封装的数据是否普通表单域，是则返回true，如果是文件表单域则返回false
>                 if(item.isFormField()){
>                     // getFieldName()方法获取input对象的name属性值
>                     if(item.getFieldName().equals("stuNum")){
>                         // getString()方法获取input标签中输入的内容，可以指定编码格式
>                         stuNum = item.getString("UTF-8");
>                     }
>                     else if(item.getFieldName().equals("stuName")){
>                         stuName = item.getString("UTF-8");
>                     }
>                     else if(item.getFieldName().equals("title")){
>                         title = item.getString("UTF-8");
>                     }
>                 }
>                 else{
>                     fileItem=item;
>                 }
>             }
>             if(fileItem!=null){
>                 // fileItem.getName()方法获取文件域的文件名
>                 String fileName=fileItem.getName();
>                 String suffix=fileName.substring(fileName.lastIndexOf(".")+1);
>                 File savedFile = new File(savedPath, newFileName);
>                 // FileItem类对象的write(File file)方法根据File对象的信息将文件内容写入到磁盘中
>                 fileItem.write(savedFile);
>                 // 响应前端
>                 PrintWriter out=response.getWriter();
>                 out.println("已经上传文件："+ fileName + "</br>");
>                 // FileItem类对象的getSize()方法可以获得文件的大小，以字节为单位
>                 out.println("文件大小为：" + fileItem.getSize() + "字节" + "</br>");
>                 out.println("重命名为：" + newFileName);
>             }
>         }
>         catch(Exception e){
>             try{
>                 response.getWriter().println("异常错误" + e.toString());
>             }
>             catch(IOException el){
>                 el.printStackTrace();
>             }
>         }
>     }
> }
> ```
>
> 3、配置web.xml
>
> ```xml
> <servlet>
> 	<servlet-name>doPaperUpload</servlet-name>
>     <servlet-class>PaperUpload_do</servlet-class>
> </servlet>
> <servlet-mapping>
> 	<servlet-name>doPaperUpload</servlet-name>
>     <url-pattern>/doPaperUpload</url-pattern>
> </servlet-mapping>
> ```
>
> (另)：servlet3.0中的文件上传处理
>
> ```java
> import java.io.IOEeception;
> import java.io.PringWriter;
> import javax.servlet.annotation.MultipartConfig;
> import javax.servlet.http.HttpServlet;
> import javax.servlet.http.HttpServletReuqest;
> import javax.servlet.http.HttpServletResponse;
> import javax.servlet.http.Part;
> 
> 
> // Part类对象会根据MultipartConfig的注释完成文件存储操作
> /*
> 	MultipartConfig中提供的参数
> 	int fileSizeTreshold：阙值，当文件大小超过该值时会先将文件写入临时文件，类似缓存区以免意外丢失。
> 	String location：文件将要被保存的目录
> 	long maxFileSize：允许上传的文件的最大值，下面设置的是10MB
> 	long maxRequestSize：所能够允许的“multipart/form-data”请求的最大值
> */ 
> @MultipartConfig(fileSizeThreshold=4*1024,location="D:/uploadDir/",maxFileSize=10000*1024)
> public class PaperUploadwithS3_do extents HttpServlet{
>     @Override
>     protected void doPost(HttpServletRequest request,HttpServlet response){
>         try{
>             request.setCharacterEncoding("UTF-8");
>             response.setContentType("text/html;charset=UTF-8");
>             /*
>             	servlet3.0组件上传文件夹最大的特点是可以直接使用getParameter()方法来获取
>             	multipart类型的表单中的元素信息。
>             */
>             String stuNum=request.getParameter("stuNum");
>             String stuName=request.getParameter("stuName");
>             String title=request.getParameter("title");
>             // Part类对象用来保存表单中的文件格式数据
>             // request的getPart()方法可以将对应名称的表单域封装到一个Part类对象中并返回
>             Part paperPart=request.getPart("paper");
>             // part类对象的getHeader(String name)，以字符串的形式返回指定MIME头中对应key的值
>             // 这里用来获取文件的名称信息
>             String contentDes=paperPart.getHeader("content-disposition");
>             // 提取contentDes变量中的文件名信息
>             String fileName=contentDes.substring(contentDess.lastIndexOf("filename=\"")+10, 							contentDes.length()-1);
>             // 获取文件名后缀
>             String fileNameSuffix=fileName.substring(fileName.lastIndexOf("."));
>             String newFileName=stuNum + "-" + stuName + "-" + title + fileNameSuffix;
>             /*
>             	Part类对象的writer(String fileName)方法，接收一个字符串作为文件名，
>             	将表单域汇总的内容写到磁盘指定路径下的fileName文件中。如果表单为普通域则
>             	将其包含的值写入文件，如果是文件域，则将文件原本内容写入文件。
>             	这里的指定磁盘路径是由MultipartConfig注释指定
>             */ 
>             paperPart.writer(newFileName);
>             // 响应前端
>             PrintWriter out=response.getWriter();
>                 out.println("已经上传文件："+ fileName + "</br>");
>             // Part类对象的getSize()方法用来获取文件大小，以字节为单位
>                 out.println("文件大小为：" + paperPart.getSize() + "字节" + "</br>");
>                 out.println("重命名为：" + newFileName);
>         }
>         catch(Exception e){
>             try{
>                 response.getWriter().println("发生异常：" + e.toString());
>             }
>             catch(Exception e1){
>                 e1.printStackTrace();
>             }
>         }
>     }
> }
> ```
>
> 下载模块：
>
> 1、前端页面
>
> ```html
> <!-- 该页面实现2011-010201-张三-浅谈Sprint机制的Ioc机制.docx文件的下载功能 -->
> 
> <form name="downloadForm" action="/downloadFile" method="post">
>     <input type="hidden" name="filename" value="2011-010201-张三-浅谈Sprint机制的Ioc机制.docx"/>
> 	<input type="submit" value="下载" />
> </form>
> ```
>
> 2、servlet处理
>
> ```java
> import java.io.File;
> import java.io.IOException;
> import javax.servlet.ServletException;
> import javax.servlet.HttpServlet;
> import javax.servlet.HttpServletRequest;
> import javax.servlet.HttpServletRepsonse;
> 
> public class DownLoad_do extends HttpServlet{
>     public void doPost(HttpServletRequest request, HttpServletRespsonse response)throws 			ServletException, IOException{
>         // 这里照常设置响应体，在发生异常时输出HTML内容
>         request.setCharacterEncoding("UTF-8");
>         response.setContentType("text/html");
>         // 获取ServletOutputStream类输出流对象，用来传输文件数据
>         javax.servlet.ServletOutputStream out=response.getOutputStream();
>         // 准备读取文件的路径+文件名
>         String filepath="D:/uploadPaper/";
>         String filename=request.getPatameter("filename");
>         // 创建对应文件的File对象
>         File file=new File(filepath, filename);
>         if(! file.exists()){
>             out.println(new String((filename + "文件不存在！").getBytes(),"iso8859-1"));
>             return;
>         }
>         // 创建一个输入流，从操作系统中读取对应的文件，传入File对象作为参数
>         java.io.FileInputStream fileInputStream=new java.io.FileInputStream(file);
>         if(filename!=null && filename.length()>0){
>             // 设置传输文件时的响应体格式
>             response.setContentType("binary/octet-stream");
>             response.setHeader("Content-Disposition", "attachment;filename=" + 
>                                new String(filename.getByte(),"iso8859-1") + "");
>             // 准备传输文件
>             if(fileInputStream!=null){
>                 // 以1024字节为单位读取文件
>                 // 创建byte类数组，每个元素可存放以字节数据
>                 byte[] buffer=new byte[1024];
>                 int i=-1;
>           // java.io.FileInputStream类的read()方法读取文件内容放入byte数组中，返回实际读取个数
>                 // 若剩余内容大小小于1024，则读取剩余部分，并返回实际读取大小
>                 while((i=fileInputStream.read(buffer))!=-1){
>          // 将byte数组内容写入输出流中，后两个传输表示将byte数组的，0位置起到i位置结束的内容写入输出流
>                     out.write(buffer,0,i);
>                 }
>                 // 关闭输入流
>                 fileInputStream.close();
>                 // 输出缓存中的数据并清空缓存
>                 out.flush();
>                 // 关闭输出流
>                 out.close();
>             }
>         }
>     }
> }
> ```
>
> 3、web.xml配置
>
> ```xml
> <servlet>
> 	<servlet-name>downloadFile</servlet-name>
>     <servlet-class>DownLoad_do</servlet-class>
> </servlet>
> <servlet-mapping>
> 	<servlet-name>downloadFile</servlet-name>
>     <url-pattern>/downloadFile</url-pattern>
> </servlet-mapping>
> ```
>
> 

4、图片的缩小、水印添加

> 图片缩放
>
> 1、创建工具类
>
> ```java
> // 图片变换参数设置器，为后续的图片变换类提供参数，该类中为AffinetransformOp对象提供服务
> import java.awt.geom.AffineTransform;
> // 图片缩小器，根据AffineTransform对象的参数对图片进行变换
> import java.awt.image.AffinetransformOp;
> // 图片数据缓存对象，将磁盘中读取出的数据放置在该对象中可以利用该对象的一些方法便捷的获取图片的信息，如宽、高等信息。
> import java.awt.image.BufferedImage;
> import java.io.IOException;
> import java.io.File;
> // ImageIO类可以根据一个File类对象去磁盘中读取对应图片文件的数据
> import javax.imageio.ImageIO;
> 
> /*
> 	图片缩放的3种方法
> 	1、已知缩小图片的长度，根据原图的长宽比例计算小图的宽度
> 	2、已知缩小图片的宽度，根据原图的长宽比例计算小图的长度
> 	3、已知原图与小图的缩小比例，根据比例计算小图的长宽
> */
> public class JpegTool{
>  private boolean isInitFlag=false;
>  private String pic_big_pathfilename=null;
>  private String pic_small_pathfilename=null;
>  private int smallpicwidth=0;
>  private int smallpicheight=0;
>  private int pic_big_width=0;
>  private int pic_big_height=0;
>  private double picscale=0;
>  
>  public JpegTool(){
>      this.isInitFlag=false;
>  }
>  
>  private void resetJepgToolParams(){
>      this.picscale=0;
>      this.smallpicheight=0;
>      this.smallpicwidth=0;
>      this.isInitFlag=0;
>  }
>  
>  // JpegToolException自定义异常。
>  /*
>  	java中异常分为两种：checked exception、runtime exception异常两大类（父类是Exception），
>  	当发生checked exception时，java要求必须要有语句去处理该异常，就是必须要有catch去捕获
>  	不然程序就会意外停止。
>  	而发生runtime exception异常时则没有强制要求一定要有carch语句去处理，即使在调用函数中
>  	使用throws抛出了异常，调用函数也可以无视该异常，然后程序中断。
>  	所有直接继承Exception类的异常都属于checked exception异常
>  	
>  	java中函数异常处理checked exception异常有两种不同的方式
>  	一种是通过try...catch...finally语句捕获并处理
>  	一种是自身不处理异常，将异常交给调用者处理。这时就需要在函数声明时加上throws。
>  	抛出该函数执行时可能发生的异常。不需要任何多余的代码，主要发生异常就会将异常抛出给调用者。
>  	throw抛出异常，该关键字用在函数体中，也是自身不处理异常，它将抛出一异常对象给调用者处理。
>  */
>  
>  // 设置缩小倍数
>  public void SetScale(double scale)throws JpegToolException{
>      if(scale<0){
>          // 执行异常抛出后，之后的语句不在执行，相当于结束函数体。
>          throw new JpegToolException("缩放比例不能为负数");
>      }
>      this.resetJpegToolParams();
>      this.picscale=scale;
>      this.isInitFlag=true;
>  }
>  // 设置小图宽度
>  public void SetSmallWidth(int smallpicwidth)throws JpegToolException{
>  	if(smallpicwidth<0){
>          throw new JpegToolException("缩略图宽度不能为负数！");
>      }
>      this.resetJpegToolParams();
>      this.smallpicwidth=smallpicwidth;
>      this.isInitFlag=true;
>  }
>  // 设置小图高度
>  public void SetSmallHeight(int smallpicheight)throws JpegToolException{
>      if(smallpicheight<0){
>          throw new JpegToolException("缩略图高度不能为负数");
>      }
>      this.resetJpegToolParams();
>      this.smallpicheight=smallpicheight;
>      this.isInitFlag=true;
>  }
>  // 获取原图保存路径
>  public String getpic_big_pathfilename(){
>      return this.pic_big_pathfilename;
>  }
>  // 获取小图保存路径
>  public String getpic_small_pathfilename(){
>      return this.pic_small_pathfilename;
>  }
>  // 获取原图宽度
>  public int getsrcw(){
>      return this.pic_big_width;
>  }
>  // 获取原图高度
>  public int getsrch(){
>      return this.pic_big_height;
>  }
>  // 制作小图方法
>  public void doFinal(String pic_big_pathfilename, String pic_small_pathfilename)throws
>      JpegToolException{
>      System.out.println(pic_big_pathfilename);
>      // 判断缩小条件是否合理
>      if(!this.isInitFlag){
>          throw new JpegToolException("未设置缩放参数");
>      }
>      if(pic_big_pathfilename==null || pic_small_pathfilename==null){
>          throw new JpegToolException("图片保存路径为空");
>      }
>      if((! pic_big_pathfilename.toLowerCase().endWith("jpg"))&&
>         		(! pic_big_pathfilename.toLowerCase().endWith("jpeg"))){
>          throw new JpegToolException("只能处理Jpg/Jpeg图片");
>      }
>      if((! pic_small_pathfilename.toLowerCase().endWith("jpg"))&&
>         		(! pic_small_pathfilename.toLowerCase().endWith("jpeg"))){
>          throw new JpegToolException("只能处理Jpg/Jpeg图片");
>      }
>      // 原图和小图绝对路径
>      this.pic_big_pathfilename=pic_big_pathfilename;
>      this.pic_small_pathfilename=pic_small_pathfilename;
>      int smallw=0;
>      int smallh=0;
>      // 创建原图File对象
>      File fi=new File(pic_big_pathfilename);
>      // 创建小图File对象
>      File fo=new File(pic_small_pathfilename);
>      // 图片变换参数设置器
>      AffineTransform transform=new AffineTransform();
>      // 创建图片数据保存对象
>      BufferedImage bsrc=null;
>      try{
>          // 读取图片数据保存到BufferedImage类对象中，后续会用到该对象的方法获取原图的宽、高
>          bsrc=ImageIO.read(fi);
>      }
>      catch(IOException ex){
>          throw new JpegToolException("读取原始文件出错！");
>      }
>      // BufferedImage类对象的getWidth()方法可以获取被读取图片的宽度
>      this.pic_big_width=bsrc.getWidth();
>      // BufferedImage类对象的getHeight()方法可以获取被读取图片的高度
>      this.pic_big_height=bsrc.getHeight();
>      // 计算原图长宽比
>      double scale=(double)pic_big_width/pic_big_height;
>      // 根据小图宽度，计算长度
>      if(this.smallpicwidth!=0){
>          smallw=this.smallpicwidth;
>          smallh=smallw/scale;
>      }
>      // 根据小图长度计算宽度
>      else if(this.smallpicheight!=0){
>          smallh=this.smallpicheight;
>          smallw=smallh*scale;
>      }
>      // 根据小图缩小倍率计算长宽
>      else if(this.picscale!=0){
>          smallh=(int)this.pic_big_width*this.picscale;
>          smallw=(int)this.pic_big_height*this.picscale;
>      }
>      else{
>          throw new JpegToolException("缩小参数未设置");
>      }
>      // 计算长宽缩小比率
>      double sx=(double)smallw/pic_big_width;
>      double sy=(double)smallh/pic_big_height;
>      // 保存到参数设置器中
>      transform.setToScale(sx,sy);
>      // 传入参数设置器，创建图片变换对象。
>      AffineTransformOp ato=new AffineTransformOp(transform,null);
>      // 创建小图的数据保存对象，需要传入长，宽，BufferedImage类属性
>      BufferedImage bsmall=new BufferedImage(smallw,smallh,BufferedImage.TYPE_3BYTE,BGP);
>      // 图片变换器的filer()方法接受两个BufferedImage对象，将第一个参数根据参数设置器中的值变换图片，输出新的图片数据保存在第二个参数中
>      ato.filer(bsrc,bsmall);
>      try{
>          // ImageIO类将BufferedImage对象数据写入到磁盘中第
>          // 第一个参数为BufferedImage对象
>          // 第二个参数为图片格式
>          // 第三个参数为File对象，写入到磁盘指定位置
>          ImageIO.write(bsmall,"jpeg",fo);
>      }
>      catch(IOException ex1){
>          throw new JepgToolException("保存缩略图文件出错！");
>      }
>  }
> }
> // 自定义异常类
> public class JepgToolException extends Exception{
>  private String errMsg="";
>  
>  public JepgToolException(String errMsg){
>      this.errMsg=errMsg;
>  }
>  
>  public String toString(){
>      return "JpegToolException:" + this.errMsg;
>  }
> }
> ```
>
> 2、创建前端页面
>
> 
>
> ```html
> <form action="/uploadImage" method="post" enctype="multipart/form-data">
>  请选择上传的图片<input type="file" name="img" />
>  <input type="submit" name="submit" value="上传" />
> </form>
> ```
>
> 3、创建servlet，调用工具类处理图片
>
> ```java
> import java.io.IOEception;
> import java.io.PrintWriter;
> import java.util.Calendar;
> import javax.servlet.annotation.MultipartConfig;
> import javax.servlet.http.HttpServlet;
> import javax.servlet.http.HttpServletRequest;
> import javax.servlet.http.HttpServletResponse;
> // 该servlet使用Servlet3.0方法保存用户上传的原图
> import javax.servlet.http.Part;
> import JpegTool.*;
> 
> @MultipartConfig(fileSizeThreshould=4*1024,location="D:/uploadImg",maxFileSize=10000*1024){
>  public class ImageUpload_do extends HttpServlet{
>      // @override注释表示重写父类方法
>      @override
>      protected void doPost(HttpServletRequest request,HttpServletResponse response){
>          try{
>              request.setCharacterEncoding("UTF-8");
>              response.setContentType("text/html;charset=utf-8");
>              // 获取文件表单域数据
>              Part imgPart=request.getPart("img");
>              // 获取文件后缀
>              String contentDes=imgPart.getHeader("content-disposition");
>              String fileName=contentDes.substring(contentDes.lastIndexOF("filename=\"")+
>                                                  10,contentDex.length()-1);
>              String fileNameSuffix=fileName.substring(fileName.lastIndex(".")+1);
>              if(! fileNameSuffix.toLowerCase().equals("jpg") || 
>                 		! fileNameSuffix.toLowerCase().equals("jpeg")){
>                  throw new JpegToolException("只能处理JPG/JPEG文件!");
>              }
>              // 重命名文件：当前时间毫秒数+下划线+一百以内的随机数+文件后缀命名
>              long currTime=System.currentTimeMillis();
>              int randomNumber=(int)(Math.random()*100)+1;
>              String newFileName=currTime+"_"+randomNumber+"."+fileNameSuffix;
>              // 将图片写入磁盘
>              imgPart.write(newFileName);
>              // 创建自定义图片缩小类对象
>              JpegTool jpgTool=new JpegToll();
>              // 已知宽进行缩小
>              jpgTool.SetSmallWidth(200);
>              // doFinal()方法中传入源文件路径和目标文件路径
>              String pic_big_pathfilename="D:/uploadImg/" + newFileName;
>              String pic_small_pathfilename="D:/uploadImg/small/small" + newFileName;
>              jpgTool.doFinal(pic_big_pathfilename,pic_small_pathfilename);
>              // 响应前端
>              PrintWriter out=response.getWriter();
>              out.println("已成功上传图片：" + fileName);
>              out.println("<img src=\"" + pic_small_pathfilename+"\">");
>              out.println("图片大小为："+ imgPart.getSize() + "字节");
>              out.println("原始图片：" + "</br>");
>              out.println("<img src=\"" + pic_big_pathfilename + "\">");
>          }
>          catch(Exception e){
>              try{
>                  // 处理被抛出的JpegToolException异常，将异常信息返回给客户端
>                  response.getWriter().println("发生异常：" + e.toString());
>              }
>              catch(IOException e1){
>                  el.printStackTrace();
>              }
>          }
>      }
>  }
> }
> ```
>
> 4、配置web.xml
>
> ```xml
> <servlet>
> 	<servlet-name>uploadImage</servlet-name>
>  <servlet-class>ImageUpload_do</servlet-class>
> </servlet>
> <servlet-mapping>
> 	<servlet-name>uploadImage</servlet-name>
>  <url-pattern>/uploadImage</url-pattern>
> </servlet-mapping>
> ```
>
> 图片水印添加
>
> 1、添加水印工具类
>
> ```java
> import java.awt.AlphaComposite;
> import java.awt.Color;
> import java.awt.Font;
> import java.awt.Graphics2D;
> import java.awt.image.BufferedImage;
> import java.io.File;
> import java.io.FileNotFoundException;
> import javax.imageio.ImageIO;
> 
> public class ImageMarkTool{
>   // 这里创建两个同名函数，但形参个数不同的函数，实现函数的重载
>   // 因为java中不允许形参设置默认值，所以要实现一个变量随意用户是否输入就要通过重载功能实现
>   public static void markedByText(String text, String srcImgPath, String targetImgPath){
>       markedByText(text,srcImgPath,targetImgPath,null);
>   }
>   
>   public static void markedByText(String text, String srcImgPath, String targetImgPath
>                                  	Integer degree){
>       try{
>           // 创建原始图片File对象
>           File srcFile=new File(srcImgPath);
>           if(! srcFile.exists()){
>               throw new FileNotFoundException("找不到原始图片" + srcImgPath);
>           }
>           // 读取原始图片
>           BufferedImage srcBuffImg=ImageIO.read(srcFile);
>           // 创建绘制对象
>           Graphics2D g=srcBuffImg.createGraphics();
>           // 设置对线段的锯齿边缘处理
>           g.setRenderingHint(RenderingHints.KEY_INTERPOLATION,
>                              		RenderingHints.VALUE_INTERPOLATION);
>           // 加载图片到绘制对象中，第一个参数为图片对象，第二、第三个参数为图片左上角坐标。
>           g.drawImage(srcBuffImg,0,0,null);
>           if(null!=degree){
>               // 设置绘制样式之于水平线的旋转角度
>               g.totate(Math.toRadians(degree),(double)srcBuffImg.getWidth()/2,
>                        		(double)srcBuffImg.getHeight()/2);
>           }
>           // 设置画笔颜色
>           g.setColor(Color,blue);
>           // 设置字体
>           g.setFont(new Font("宋体", Font.BOLD, 30));
>           // 设置透明度
>           float alpha=0.5f;
>           g.setComposite(AlphaComposite.getInstance(AlphaComposite.SRC_ATOP,alpha));
>           // 在图片上绘制文字，第一个参数为文字内容，第二第三个参数为内容的起始坐标
>           g.drawString(text, srcBuffImg.getWidth()-500, srcBuffImg.getHeight()-100);
>           // 结束，释放画笔资源
>           g.dispose();
>           // 创建新图片的File对象
>           File targetFile=new File(targetImgPath);
>           // 保存图片到新文件中
>           ImageIO.write(srcBuffImg,"JPG",targetFile);
>       }
>       catch(Exception e){
>           e.printStackTrace();
>       }
>   }
> }
> ```
>
> 2、前端页面
>
> ```html
> <form action="uploadImgAndMarked" method="post" enctype="multipart/formdata">
>     用户名<input type="text" name="username" /></br>
> 	<input type="file" name="img" /></br>
> 	“注意只能上传Jpg或JPEG格式文件”
> 	<input type="submie" name="submit" value="上传" />
> </form>
> ```
>
> 3、servlet编写
>
> ```java
> import java.io.IOException;
> import java.io.PrintWriter;
> import javax.servlet.annotation.MultipartConfig;
> import javax.servlet.http.HttpServlet;
> import javax.servlet.http.HttpServletRequest;
> import javax.servlet.http.HttpServletResponse;
> import javax.servlet.http.Part;
> import JpegTool.JpegToolException;
> import ImageMarkTool;
> 
> @MultipartConfig(fileSizeThreshold=4*1024,location="D:/uploadImg", maxFileSize=10000*1024)
> public class ImageUploadAndMark_do extends HttpServlet{
>     @Override
>     public void doPost(HttpServletRequest request,HttpServletResponse response){
>         try{
>             request.setCharacterEncoding("UTF-8");
>             String username=request.getParameter("username");
>             response.setContentType("text/html;charset=UTF-8");
>             // 获取文件表单域数据，提取文件名
>             Part imgPart=request.getPart("img");
>             String contentDes=imgPart.getHeader("content-disposition");
>             String fileName=contentDes.substring(contentDes.lastIndexOf("filename=/")+10,
>                                                 		contentDes.lenth()-1);
>             String fileNameSuffix=fileName.substring(fileName.lastIndexOf(".")+1);
>             if((! fileNameSuffix.toLowerCase().equals("jpg")) &&
>                			(! fileNameSuffix.toLowerCase().equals("jpeg"))){
>                 throw new JpegToolException("只能处理JPG/JPEG文件");
>             }
>             // 当前时间毫秒数+100以内随机数重命名，并保存图片
>             long currTime=System.currentTimeMillis();
>             int randomNumber=(int)(Math.random()*100)+1;
>             String newFileName=currTime+"_"+randomNumber+"."fileNameSuffix;
>             imgPart.write(newFileName);
>             // 创建两个目标路径，分别测试带旋转角度和不带旋转角度的markedByText()方法
>             String srcImgPath="D:/uploadImg/" + newFileName;
>             String targetImgPath="D:/uploadImg/marked/marked_"+newFileName;
>             String targetImgPath2="D:/uploadImg/marked/marked2_"+newFileName;
>             ImageMarkTool.markedByText("@" + username, srcImgPath, targetImgPath);
>             ImageMarkTool.markedByText("@" + username, srcImgPath, targetImgPath2, -45);
>             // 响应前端
>             PrintWriter out=respsone.getWriter();
>             out.println("上传图片成功："+fileName+"</br>");
>             out.println("<img src=\"" + targetImgPath2 + "\"/>");
>         }
>         catch(Exception e){
>             try{
>                 resposne.getWriter().println("发生异常：" + e.toString());
>             }
>             catch(IOException e1){
>                 e1.printStackTrace();
>             }
>         }
>     }
> }
> ```
>
> 4、web.xml编写
>
> ```xml
> <servlet>
> 	<servlet-name>uploadImageAndMarked</servlet-name>
>     <servlet-class>ImageUploadAndMark_do</servlet-class>
> </servlet>
> <servlet-mapping>
> 	<servlet-name>uploadImageAndMarked</servlet-name>
>     <url-pattern>/uploadImageAndMarked</url-pattern>
> </servlet-mapping>
> ```
>
> 

5、验证码制作

> JSP验证码生成
>
> 1、前端页面
>
> ```html
> <!--第一次会访问网页会浏览器会自动请求checknum.jsp加载验证码，后续要更换验证码则通过点击验证码图片调用js中的changeCheckNum()方法再次请求checknum.jsp页面请求验证码-->
> <img src="checknum.jsp" alt="change" border="1" onclick="changeCheckNum()" />
> ```
>
> 2、JSP页面
>
> ```jsp
> <%@ page language="java" import="java.sql.*" errorPage="" %>
> <%@ page contentType="image/jpeg" import="java.awt.*,java.awt.image.*,java.util.*,javax.imageio.*"
> %>
> <%!
>  // 自定义函数，根据rgb值生成Color对象
> Color getRandColor(int fc, int bc)    {
>  Random random=new Random();
>  if(fc>255) fc=255;
>  if(bc>255) bc=255;
>  int r=fc+random.nextInt(bc-fc);
>  int g=fc+random.nextInt(bc-fc);
>  int b=fc+random.nextInt(bc-fc);
>  return new Color(r,g,b);
> }
> %>
> <%
> // 设置响应页面不缓存
> respsonse.setHeader("Pragma","No-cache");
> respsonse.setHeader("Cache-Control","no-cache");
> respsonse.setDateHeader("Expires", 0);
> // 设置验证码图片的宽和高
> int width=80,height=30;
> // 创建一个新的图片缓存框架
> BufferedImage image=new BufferedImage(width,height,BufferedImage.TYPE_INT_RGB);
> // 准备画笔，进行验证码绘制
> Graphics g=image.createGraphics();
> // 创建随机数生成对象
> Random random=new Random();
> // 调用自定义getRandColor()方法获取Color对象，设置画笔颜色，用于矩形背景
> g.setColor(getRandColor(200,250));
> // 填充矩形，类似于drawImage(srcBuffImg,0,0,null);方法
> g.fillRect(0,0,width,height);
> // 设置字体
> g.setFont(new Font("Times New Roman", Font.PLAIN,18));
> // 设置画笔颜色，用于绘制155条干扰线
> g.setColor(getRandColor(160,200));
> for(int i=0;i<155;i++){
>  // 绘制干扰线，每条干扰线都有起始(X,Y)坐标和终止(xl,yl)坐标
>  int x=random.nextInt(width);
>  int y=random.nextInt(height);
>  int xl=random.nextInt(12);
>  int yl=random.nextInt(12);
>  // 画线
>  g.drawLine(x,y,x+x1,y+y1);
> }
> // 生成4个10以内的随机数，作为验证码
> String sRand="";
> for(int i=0;i<4;i++){
>  String rand=String.valueOf(random.nextInt(10));
>  sRand+=rand;
>  // 设置画笔颜色，用于绘制验证码
>  g.setColor(new Color(20+random.nextInt(110),20+random.nextInt(110),
>                       	20+random.nextInt(110)));
>  // 每个验证码的y坐标不变，x坐标间隔一定距离
>  g.drawString(rand,13*i+6,16);
> }
> // 在会话中保存验证码，和后续用户提交的验证码做比对
> session.setAttribute("rand", sRand);
> // 释放画笔资源
> g.dispose();
> // 输出验证码图片到输出流
> ImageIO.write(image,"JPEG",respsonse.getOutputStream());
> // 清空输出缓存区
> out.clear();
> // 发送验证码到客户端
> out=pageContext.pushBody();
> %>
> ```
>
> servlet验证码生成
>
> 1、前端页面
>
> ```html
> <img src="CheckNum" alt="Change" border="1" onclick="changeCheckNum()" />
> ```
>
> 2、servlet编写
>
> ```java
> import java.awt.Color;
> import java.awt.Font;
> import java.awt.Graphics;
> import java.awt.image.BufferedImage;
> import java.io.IOException;
> import javax.servlet.ServletException;
> import javax.servlet.http.HttpServlet;
> import javax.servlet.http.HttpServletRequest;
> import javax.servlet.http.HttpServletResponse;
> import javax.servlet.ServletOutputStream;
> import javax.servlet.http.Session;
> // 解码输出图片
> import com.sun.image.codec.jpeg.JPEGCodec;
> import com.sum.image.codec.jepg.JPEGImageEncoder;
> 
> public class CheckNum extends HttpServlet{
>  private static final long serialVersionUID=1L;
>     //设置字体对象
>  private Font mFont=new Font("Time New Roman", Font.PLAIN,18);
>  protected void doGet(HttpServletRequest request, HttpServletResponse response)throws
>  	ServletException, IOException{
>      // 设置响应体内容不缓存，响应格式为图片jpg
>      HttpSession session=request.getSession(false);
>      response.setContentTpye("image/jpg");
>      response.setHeader("Pragma", "No-cache");
>      response.setHeader("Cache-Control", "no-cache");
>      response.setDateHeader("Expires",0);
>      // 获取响应体输出流，当输出文件类信息时使用
>      ServletOutputStream out=response.getOutputStream();
>      // 设置图片长宽，用于生成图片框架
>      int width=60,height=20;
>      BufferedImage image=new BufferedImage(width,height,BufferedImage.TYPE_INT_RGB);
>      // 获取画笔
>      Graphics g=image.getGraphics();
>      Random random = new Random();
>      // 设置画笔颜色，用于绘制矩形背景
>      g.setColor(getRandColor(200,250));
>      g.fillRect(0,0,width,height);
>      // 设置画笔字体
>      g.setFont(mFont);
>      // 设置画笔颜色，用户绘制155条干扰线
>      g.setColor(getRandColor(160,200));
>      for(int i=0;i<155;i++){
>          int x=random.nextInt(width);
>          int t=random.nextInt(height);
>          int xl=random.nextInt(12);
>          int yl=random.nextInt(12);
>          g.drawLine(x,y,x+xl,y+yl);
>      }
>      // 生成4个验证码
>      String sRand="";
>      for(int i=0;i<4;i++){
>          String rand=String.valueOf(random.nextInt(10));
>          sRand+=rand;
>          // 设置画笔颜色，用于绘制验证码
>          g.setColor(new Color(20+random.nextInt(110),20+random.nextInt(110),
>                              	20+random.nextInt(110)));
>          // 每个验证码y坐标不变，x坐标相隔一定距离
>          g.drawString(rand,13*i+6,16);
>      }
>      // 保存验证码到会话中，用于之后与用户提交的验证码比对
>      session.setAttribute("getImg",sRand);
>      // 创建图片编码器，传入响应输出流进行实例化。
>      JPEGImageEncoder encoder=JPEGCodec.createJPEGEncoder(out);
>      // 解码制作好的验证码图片，并写入到输出流中，写完后会自动调用输出流的filsh()方法输出到客户端。
>      encoder.encode(image);
>      // 关闭输出流
>      out.close();
>  }
>     
>     // 自定义方法，生成Color对象
>     static Color getRandColor(int fc,int bc){
>         Random random=new Random();
>         if(fc>255)fc=255;
>         if(bc>255)bc=255;
>          int r=fc+random.nextInt(bc-fc);
>          int g=fc+random.nextInt(bc-fc);
>          int b=fc+random.nextInt(bc-fc);
>          return new Color(r,g,b)；
>     }
> }
> ```
>
> 3、web.xml配置
>
> ```xml
> <servlet>
> 	<servlet-name>CheckNum</servlet-name>
>     <servlet-class>CheckNum</servlet-class>
> </servlet>
> <servlet-mapping>
> 	<servlet-name>CheckNum</servlet-name>
>     <url-pattern>/CheckNum</url-pattern>
> </servlet-mapping>
> ```
>
> 

6、MD5加密