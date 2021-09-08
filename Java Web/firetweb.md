碰到的问题

> Q：js中xmlHttp.open('POST', url, true)中url参数该怎么与后台文件web.xml文件中的url-pattern，相匹配。
>
> 
>
> A：url-pattern中的参数总是以web该文件夹为根目录开始计算，如\<url-pattern>/AdminLogin\</url-pattern>，就表示该url匹配问web目录下的AdminLogin资源时调用对应的Servlet。
>
> 所以对应xmlHttp.open('POST', url, true)中url是以当前js所在后台地址算起，如果js在后台中的位置为/web/xx.js，那么url就要设置为“./AdminLogin”，表示寻找当前文件夹下的AdminLogin资源，也就是web目录下的AdminLogin资源。
>
> 这样就使得js中xmlHttp.open('POST', url, true)中url参数该怎么与后台文件web.xml文件中的url-pattern，对应起来了。

> Q：JDBC无法调用
>
> 
>
> A：没有将mysql-connector-java-8.0.21.jar文件放在WEB-INF/lib/目录下，导致无法调用

> Q：xml中某个标签的文本值如何访问
>
> 
>
> A：在xml中标签元素没有文本只有子节点，所以要访问某个标签的文本时就要获取该标签的子节点，获取该节点的nodevalue属性值

> ```javascript
> function parseAdmin(){
>     if(xmlHttp.readyState==4){
>         if(xmlHttp.status==200){
>             let xmlDoc = xmlHttp.responseXML;
>             let error=xmlDoc.getElementsByTagName('error')[0].firstChild.nodeValue;
>             let errorText = xmlDoc.getElementsByTagName('errorText')[0].firstChild.nodeValue;
>             if(error==0){
>                 location.replace('welcome.html');
>             }
>             else if(error==1){
>                 alert(errorText);
>                 $('button')[0].removeAttribute('disabled');
>             }
>             else{
>                 alert('服务器异常！请稍后再试！');
>                 $('button')[0].removeAttribute('disabled');
>             }
>         }
>         // else应该放在此处
>     }
>     else{
>         alert('服务器异常！请稍后再试！');
>         $('button')[0].removeAttribute('disabled');
>     }
> }
> 
> ```
>
> Q：为什么该段响应方法会在正确弹出提示之前，多弹出2个或以上 alert('服务器异常！请稍后再试！');警告框。
>
> A：因为浏览器在进行ajax请求后会不断的检查xmlHttp.readyState的状态码，因为服务器响应需要时间，在服务器没有响应的这段时间内浏览器检查xmlHttp.readyState属性时发现不等于4，所以就执行else{}中的代码，就导致了在正确弹出提示之前不断的弹出alert('服务器异常！请稍后再试！');警告框。
>
> 其实该处的else位置不对，应该对应if(xmlHttp.status==200)才是正确的
>
> 
>
> **XMLHTTP.readyState的五种就绪状态：**
>
> - **0**：请求未初始化（还没有调用 `open()`）。
> - **1**：请求已经建立，但是还没有发送（还没有调用 `send()`）。
> - **2**：请求已发送，正在处理中（通常现在可以从响应中获取内容头）。
> - **3**：请求在处理中；通常响应中已有部分数据可用了，但是服务器还没有完成响应的生成。
> - **4**：响应已完成；您可以获取并使用服务器的响应了。

> Q：ajax请求步骤？
>
> A：
>
> 1、设置url
>
> 2、构造参数
>
> 3、调用xmlHttp.open("POST", url, true);方法
>
> 4、设置请求头：xmlHttp.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');（可选）
>
> 5、设置解析函数：xmlHttp.onreadystatechange=函数句柄（函数名）
>
> 6、调用xmlHttp.send(Query);方法，发送请求

> Q：怎么设置服务器响应？
>
> A：
>
> 1、设置响应体类型：response.setContentType("text/xml");
>
> 2、设置响应体编码：response.setCharacterEncoding("UTF-8");
>
> 3、设置响应体内容：
>
> ```java
> xml.append("<status><error>");
> xml.append(this.error);
> xml.append("</error></status>");
> response.getWriter().write(xml.toString());
> ```

> Q：以下两者的区别
>
> ```javascript
> let error=xmlDoc.getElementsByTagName("error")[0].firstChild.nodeValue;
> let error=xmlDoc.getElementsByTagName("error")[0].firstElementChild.nodeValue;
> ```
>
> A：firstChild属性获取该节点下的第一个孩子节点，firstElementChild获取该节点下的第一个标签孩子节点
>
> 若要获取文本信息则需要使用firstChild属性获取，因为文本不属于标签节点。用firstElementChild属性获取结果为null

> Q：java怎么获取当前系统时间
>
> A：
>
> ```java
> import java.util.Date;
> import java.text.SimpleDateFormat;
> 
> SimpleDateFormat time=new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");// 设置时间格式
> System.out.println(time.format(new Date()));//获取时间
> ```

> Q：子div的上边距成为了父div的上边距？
>
> A：一个盒子如果没有上补白(padding-top)和上边框(border-top)，那么这个盒子的上边距会和其内部文档流中的第一个子元素的上边距重叠。
>
> 再说白点就是：父元素的第一个子元素的上边距margin-top如果碰不到有效的border或者padding.就会不断一层一层的找自己“领导”(父元素，祖先元素)的麻烦。只要给领导设置个有效的 border或者padding就可以有效的管制这个目无领导的margin防止它越级，假传圣旨，把自己的margin当领导的margin执行。