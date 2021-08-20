XML组成成分

> 1、元素
> 2、属性
> 3、实体
> 4、PCDATA
> 5、CDATA

元素

> 含义：是XML的主要组成部分，每一个标签都是一个元素
>
> 元素的语法声明
>
> ```xml-dtd
> 1、<!ELEMENT 元素名称 类别>
> <!-- 说明元素br为空类型 -->
> <!ELEMENT br EMPTY>
> 
> 2、<!ELEMENT 元素名称 (元素内容)>
> <!-- 表示to元素只有文本内容，不允许包含其他元素 -->
> <!ELEMENT to (#PCDATA)>
> 
> 3、带有子元素（序列）的元素
> <!ELEMENT 元素名称 (子元素名称 1,子元素名称 2,.....)>
> <!-- 表示元素note元素内容必须包含to，from，heading，body元素，并且必须按照这个顺序出现，并且只能出现一次 -->
> <!ELEMENT note (to,from,heading,body)>
> 
> 4、带有任何内容的元素
> <!ELEMENT 元素名称 ANY>
> 
> 5、声明最少出现一次的元素
> <!ELEMENT 元素名称 (子元素名称+)>
> <!ELEMENT note (message+)>
> 
> 6、声明出现零次或多次的元素
> <!ELEMENT 元素名称 (子元素名称*)>
> <!ELEMENT note (message*)>
> 
> 7、声明出现零次或一次的元素
> <!ELEMENT 元素名称 (子元素名称?)>
> <!ELEMENT note (message?)>
> 
> 8、声明“非.../既...”类型的内容
> <!ELEMENT note (to,from,header,(message|body))>
> <!-- 上面的例子声明了："note" 元素必须包含 "to" 元素、"from" 元素、"header" 元素，以及非 "message" 元素既 "body" 元素。 -->
> 
> 9、声明混合型的内容
> <!ELEMENT note (#PCDATA|to|from|header|message)*>
> <!-- 上面的例子声明了："note" 元素可包含出现零次或多次的 PCDATA、"to"、"from"、"header" 或者 "message"。 -->
> 
> ```
>
> 

属性

> 元素的属性
>
> 属性语法说明
>
> ```xml-dtd
> <!ATTLIST 元素名称 属性名称 属性类型 默认值>
> 
> 1、默认值
> <!ELEMENT square EMPTY>
> <!ATTLIST square width CDATA "0">
> 合法的XML
> <square width="100" />
> 
> 2、#IMPLIED语法
> <!ATTLIST 元素名称 属性名称 属性类型 #IMPLIED>
> <!ATTLIST contact fax CDATA #IMPLIED>
> 合法的XML
> <contact fax="555-667788" />
> 合法的XML
> <contact />
> 
> 3、#REQUIRED
> <!ATTLIST 元素名称 属性名称 属性类型 #REQUIRED>
> <!ATTLIST person number CDATA #REQUIRED>
> 合法的XML
> <person number="5677" />
> 非法的XML
> <person />
> 
> 4、#FIXED
> <!ATTLIST 元素名称 属性名称 属性类型 #FIXED "value">
> <!ATTLIST sender company CDATA #FIXED "Microsoft">
> 合法的XML
> <sender company="Microsoft" />
> 非法的XML
> <sender company="W3School" />
> 
> 5、列举属性类型
> <!ATTLIST 元素名称 属性名称 (en1|en2|..) 默认值>
> <!ATTLIST payment type (check|cash) "cash">
> <payment type="check" />
> <payment type="cash" />
> ```
>
> ![image-20201122144212939](C:\Users\zhang\AppData\Roaming\Typora\typora-user-images\image-20201122144212939.png)
>
> ![image-20201122144251887](C:\Users\zhang\AppData\Roaming\Typora\typora-user-images\image-20201122144251887.png)

实体

> 实体是用来定义普通文本的变量。实体引用是对实体的引用。大多数同学都了解这个 HTML 实体引用："\&nbsp;"。这个“无折行空格”实体在 HTML 中被用于在某个文档中插入一个额外的空格。
>
> 语法声明：
>
> ```xml-dtd
> <!ENTITY 实体名称 "实体的值">
> <!ENTITY writer "Bill Gates">
> <!ENTITY copyright "Copyright W3School.com.cn">
> 
> <author>&writer;&copyright;</author>
> <!--一个实体由三部分构成: 一个和号 (&), 一个实体名称, 以及一个分号 (;)-->
> ```
>
> 

PCDATA

> PCDATA 的意思是被解析的字符数据（parsed character data）。
>
> 可把字符数据想象为 XML 元素的开始标签与结束标签之间的文本。

CDATA

> CDATA 的意思是字符数据（character data）。
>
> CDATA 是不会被解析器解析的文本。在这些文本中的标签不会被当作标记来对待，其中的实体也不会被展开。

DTD应用

> XML内部编写DTD
>
> ```xml
> <!--假如 DTD 被包含在您的 XML 源文件中，它应当通过下面的语法包装在一个 DOCTYPE 声明中：-->
> <!DOCTYPE 根元素 [元素声明]>
> 
> <?xml version="1.0"?>
> <!DOCTYPE note [
>   <!ELEMENT note (to,from,heading,body)>
>   <!ELEMENT to      (#PCDATA)>
>   <!ELEMENT from    (#PCDATA)>
>   <!ELEMENT heading (#PCDATA)>
>   <!ELEMENT body    (#PCDATA)>
> ]>
> <note>
>   <to>George</to>
>   <from>John</from>
>   <heading>Reminder</heading>
>   <body>Don't forget the meeting!</body>
> </note>
> ```
>
> XML导入外部DTD文件
>
> ```xml
> <!DOCTYPE 根元素 SYSTEM "文件名">
> 
> <?xml version="1.0"?>
> <!DOCTYPE note SYSTEM "note.dtd">
> <note>
> <to>George</to>
> <from>John</from>
> <heading>Reminder</heading>
> <body>Don't forget the meeting!</body>
> </note> 
> ```
>
> ```xml-dtd
> <!-- note.dtd文件 -->
> <!ELEMENT note (to,from,heading,body)>
> <!ELEMENT to (#PCDATA)>
> <!ELEMENT from (#PCDATA)>
> <!ELEMENT heading (#PCDATA)>
> <!ELEMENT body (#PCDATA)>
> ```

XML-DTD验证

> 在解析设置了DTD的XML文件时，若语法不正确，则解析过程就会产生错误。
>
> 在浏览器中可以通过parseError对象去查看解析发生的错误。
>
> 同时也可以选择不进行DTD检查
>
> ```js
> var xmlDoc = new ActiveXObject("Microsoft.XMLDOM")
> xmlDoc.async="false"
> xmlDoc.validateOnParse="false"	// 关闭DTD检查
> xmlDoc.load("note_dtd_error.xml")
> ```



