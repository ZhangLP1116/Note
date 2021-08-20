1、XML介绍

> XML：可扩展标记语言（EXtensible Markup Language）
>
> ![image-20201122125405534](C:\Users\zhang\AppData\Roaming\Typora\typora-user-images\image-20201122125405534.png)
>
> ![image-20201122125510517](C:\Users\zhang\AppData\Roaming\Typora\typora-user-images\image-20201122125510517.png)

2、XML作用

> XML作用：XML是一种结构化标记语言，广泛的用于传输轻量级的结构化数据，相较于JSON无解释类型的数据文件，XML能更好的表现出数据的含义，更容易解读。
>
> XML是一种用来存储和传输数据的纯文本文件格式，使用XML规定的格式编写，无依赖，可以在各种各样的平台上交换数据。

3、XML的编写

> XML文本的编写规范：
> 1、一个XML中有且只有一个根节点
> 2、标签必须闭合
> 3、大小写敏感
>
> XML内容格式与HTML类似，使用标签来标记内容，与HTML不同的是XML标签的作用是用来更好的解读内容的含义，HTML标签更多的是用来解决如何去这是内容。
>
> XML没有固定的标签，所有标签、标签的属性、内容都由用户自定义。
>
> 如：描述一系列图书的XML文件
>
> ```xml
> <!-- 该XML描述了4本书籍信息，包含书籍的标题，作者，出版日期，售价 -->
> <bookstore>
> <book category="COOKING">	<!-- category属性描述了分类 -->
>   <title lang="en">Everyday Italian</title> <!-- lang属性表述了标题使用的语言 -->
>   <author>Giada De Laurentiis</author> 
>   <year>2005</year> 
>   <price>30.00</price> 
> </book>
> <book category="CHILDREN">
>   <title lang="en">Harry Potter</title> 
>   <author>J K. Rowling</author> 
>   <year>2005</year> 
>   <price>29.99</price> 
> </book>
> <book category="WEB">
>   <title lang="en">Learning XML</title> 
>   <author>Erik T. Ray</author> 
>   <year>2003</year> 
>   <price>39.95</price> 
> </book>
> </bookstore>
> ```

4、XML的解析

> **1、在浏览器中：**
> （1）DOM解析：浏览器由内置的XML解析器，当调用解析器时就可以将xml文件解析成XML DOM模型保存在内存中。DOM定义了访问和处理XML文档的标准方法，所有DOM解析后的对象都应该实现其标准方法
>
> ```js
> // XML文件解析
> if (window.XMLHttpRequest)
>   {// code for IE7+, Firefox, Chrome, Opera, Safari
>   xmlhttp=new XMLHttpRequest();
>   }
> else
>   {// code for IE6, IE5
>   xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
>   }
> 
> xmlhttp.open("GET","books.xml",false);
> xmlhttp.send();
> xmlDoc=xmlhttp.responseXML; 
> 
> // 或通过微软的 XML 解析器来加载 XML文件
> var xmlDoc=new ActiveXObject("Microsoft.XMLDOM");
> xmlDoc.async="false";
> xmlDoc.load("note.xml");
> 
> // XML字符串解析，Internet Explorer 使用 loadXML() 方法来解析 XML 字符串，而其他浏览器使用 DOMParser 对象。
> // loadXML() 方法用于加载字符串（文本），load() 用于加载文件。
> txt="<bookstore><book>";
> txt=txt+"<title>Everyday Italian</title>";
> txt=txt+"<author>Giada De Laurentiis</author>";
> txt=txt+"<year>2005</year>";
> txt=txt+"</book></bookstore>";
> 
> if (window.DOMParser)
>   {
>   parser=new DOMParser();
>   xmlDoc=parser.parseFromString(txt,"text/xml");
>   }
> else // Internet Explorer
>   {
>   xmlDoc=new ActiveXObject("Microsoft.XMLDOM");
>   xmlDoc.async="false";
>   xmlDoc.loadXML(txt);
>   }
> ```
>
> **2、在高级语言中：**
> （1）DOM解析：将XML文档解析成标准DOM模型，并实现标准方法，DOM强制使用树模型来访问XML文档中的信息。由于XML本质上就是一种分层结构，所以这种描述方法是相当有效的。
> （2）SAX解析：SAX的全称是Simple APIs for XML，也即XML简单应用程序接口。与DOM不同，SAX提供的访问模式是一种顺序模式，这是一种快速读写XML数据的方式。当使用SAX分析器对XML文档进行分析时，会触发一系列事件，并激活相应的事件处理函数，应用程序通过这些事件处理函数实现对XML文档的访问，因而SAX接口也被称作事件驱动接口。
> **（以上两种为高级语言中通用的解析方式，以下两种为java中优化后的解析方式）**
> （3）JDOM解析：
> （4）DOM4J解析：
>
> DOM解析与SAX解析的区别
> DOM
>
> ![image-20201122135007929](C:\Users\zhang\AppData\Roaming\Typora\typora-user-images\image-20201122135007929.png)
>
> SAX
>
> ![image-20201122135026769](C:\Users\zhang\AppData\Roaming\Typora\typora-user-images\image-20201122135026769.png)

5、XML内容提取

> XML文档被解析后，就需要被使用。使用时就需要从解析好的内容提取出需要的部分。
>
> DOM解析下提取内容：
> 1、使用标准方法提取内容
> 2、使用Xpath提取内容：Xpath是一种专门为XML设计的内容提取语言，语言，经常被用在XSLT中。
>
> SAX解析下的内容提取：
> 1、使用标准方法提取内容

6、规范的XML

> XML的拥有高自由度的同时也会带来许多意料之外的混乱。
>
> ```XML
> <!-- 如下列的书本信息中，第二本书缺少了出版日期信息，第三本书中缺少了价格信息 -->
> <!-- 这中不规范的格式会给信息读取程序带来意料之外的错误，导致程序中断 -->
> <bookstore>
> <book category="COOKING">	<!-- category属性描述了分类 -->
>   <title lang="en">Everyday Italian</title> <!-- lang属性表述了标题使用的语言 -->
>   <author>Giada De Laurentiis</author> 
>   <year>2005</year> 
>   <price>30.00</price> 
> </book>
> <book category="CHILDREN">
>   <title lang="en">Harry Potter</title> 
>   <author>J K. Rowling</author> 
>   <price>29.99</price> 
> </book>
> <book category="WEB">
>   <title lang="en">Learning XML</title> 
>   <author>Erik T. Ray</author> 
>   <year>2003</year>  
> </book>
> </bookstore>
> ```
>
> XML-DTD：文档类型定义，用来定义XML的语法格式，使其符合规范。

