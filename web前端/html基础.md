**html基础**

> ==html==：超文本标记语言，如其名html语言仅仅起到一个标记作用，它将内容的各个部分用特定标签去标记。
>
> 比如用\<h3>去标记一个标题，用\<p>去标记一个段落。这些标记的作用是告诉浏览器怎么去解读这些内容。当浏览器解读到\<h3>时发现这个内容是一个标题，那么就给这段内容加粗，字体放大来形式标题。解读到\<p>标签发现这是一个段落标签，后面的内容是一个段落，那么浏览器在形式这个内容时会先换行，在形式以表明这是新的一段开始。
> html本身不生成内容，它只告诉浏览器怎么解读内容。
>
> ==css==：层叠样式表，用来告诉浏览器怎么去展示内容
>
> 原本浏览器根据html标签就会用内置的样式去展示这些内容，但是实在是不美观。如果直接去修改html标签的内置样式又会出现新的问题，灵活性差这些修改后的样式可能满足了一部分人的审美需求，但另一部分人不喜欢，那是不是又要修改浏览器源代码？
>
> 所以就有了css的出现，让用户去自定义页面样式（这里的用户是指制作页面的人员），浏览器只负责解读内容和根据css样式定义展示内容。若没有定义css那么浏览器就会按照内置的样式去展示这些内容。
> 这时候浏览器开发商只需要源代码中支持css功能就行，不需要在为了一个需求就去修改一次源代码。
>
> ==ps==：所以在讨论属性样式的时候就可以从两个方面进行
> 1、css
> 2、标签+标签属性：最早就是使用标签的属性去实现小部分的样式修改。
> （现在都不推荐使用标签属性去修改样式）
>
> 所以学习web前端主要是在学习怎么使用css和javascript，html的内容不多

**html文档结构**

> 头部\<head>：头部一般包含网页标题标记，元信息标记，样式标记，脚本标记，连接标记等。头部标记的内容一般不会展示在页面上。
>
> ```html
> <!-- 标题标记，其内容会展示在浏览器选项卡上 -->
> <title>选项卡标题</title>
> 
> <!-- 元信息标记 -->
> 有三个主要属性：name，http-equiv，content
> name: 属性用于描述网页，它就像一个文章的简介告诉别人这个页面的主要内容信息，关键词。要注意这个表述不是给人看的，是给搜索引擎爬虫看的，网页的SEO就需要对这个属性进行优化。
>  
> http-equiv：属性是用来帮助浏览器正确展示网页内容用的，它会告诉浏览器使用哪种编码解读页面，是否缓存，缓存的过期时间等
>  
> content：是用来辅助声明以上两个属性，相当于属性值的作用
> <!-- 元信息标记 -->
> 
> <!-- name属性的样例 name一般有固定取值，content用来描述name取值的内容。-->
> <meta name='keywords' content='网页内容关键字' />
> <meta nem='author' content='网页作者信息' />
> <meta name='description' content='网页内容描述' />
> <meta name='copyright' content='版权信息' />
> <meta name='robots' content='告诉机器人应该抓取的页面' />
> <meta name='generator' content='编辑器信息' />
> 
> <!-- http-equiv属性样例 -->
> <meta http-equiv='cache-control' content='no-cache' /> 禁止缓存页面内容
> <meta http-equiv='refresh' content='time url=http://baidu.com' /> 定时刷新
> <meta http-equiv='content-type' content='text/html charset=utf-8' /> 页面类型和编码格式
> <meta http-equiv='expires' content='100' /> 缓存过期时间
> 
> <!-- 更加详细的用法请参考P21或W3C -->
> 
> <!-- 连接标签 -->
> <link type='' ref='' href='url'>type表示被连接的文档类型，ref表示当前文档与被连接文档的关系
> <link type='text/css' ref='stylesheet' href='url'>
> ```
>
> 身体\<body>：用来标记网页需要展示的全部内容

**格式化文本和段落**

> 标题标签：\<h1~6>\</h>
>
> 段落标签：\<p>\</p>
>
> 基本属性：align内容对其方式，取值left、center、right、justify
>
> 换行标签：\<br />
>
> 水平分割线标签\<hr />
>
> 代码块标签：\<code>\</ code>
>
> 特殊字符：&nbsp(空格)、&lt(小于号)、&reg(注册商标)、&times(乘号)、&copy(注册商标)

**列表**

> 有序列表：\<ol>\</ol>表示有序列表的开始与结束，\<li>\</li>表示列表表项
> 属性：type（取值：1、A、a、Ⅰ、i），start
> type：表示列表表项前的序号，可以是大小写英文字母、阿拉布数字、大小写罗马字母
> start：表示序号的开始位置，start=1就表示有序列表表项从1开始
>
> 无序列表：\<ul>\</ul>表示无序列表的开始与结束，\<li>\</li>表示列表表项
> 属性：tpye（取值：disc、circle、square）
> type：表示列表表项前的标记，可以是圆形，空心圆、正方形，也可以不要。
>
> ```html
> <!-- 有序列表和无序列表中的li可以单独设置type类型，不影响后续li的type -->
> <li type=''></li>
> 
> <!-- 有序列表的li可以单独设置value，会影响后续li -->
> <li value=2>
> ```
>
> 定义列表：\<dl>\</dl>表示自定义列表的开头与结束，dt表示表项相当于li，dd是dt的详细内容
>
> ```html
> <dl>
>     <dt>联系人</dt>
>     	<dd张三</dd>
>     	<dd>电话：123124</dd>
>     	<dd>邮箱：123123@xx.com</dd>
>     <dt>地址</dt>
>     	<dd>xxxxxx</dd>
> </dl>
> ```
>
> 

**超链接与浮动框架**

> 超链接：\<a>\</a>
>
> ```html
> <!-- 基本格式 -->
> <a href='URL' target='打开窗口' title='提示信息'></a>
> <!-- target取值：_self(在当前页面打开) _blank(在新页面打开) _top() _parent() framename() -->
> 
> <!-- 文件下载连接，以文件名为后缀的超链接 -->
> <a href='xxxx.word'></a>
> 
> <!-- 锚连接,带有#的超链接 -->
> <a href='#'></a>
> 
> <!-- 发送邮件连接，P63页 -->
> ```
>
> 浮动框架：\<iframe>\</iframe>，必须在body中插入，不能插入到frameset中
>
> ```html
> <!-- 直接插入内容 -->
> <iframe><html></html></iframe>
> 
> <!-- 使用连接引用内容 -->
> <iframe src='http://xxxxx'></iframe>
> ```
>
> 

**图像与多媒体**

> 图片标签：\<img src='url' alt='鼠标移动到图片上出现的文本说明' width='' height='' align='P77页'/>
> usemap属性：图像热区连接，用于将图片中一部分区域设置为超链接。大多用于页游
>
> ```html
> <img src='url' alt='' usemap='#映射图像名称'>
> <map name='映射图像名称' id=''>
>     <area shape='热区现状，有固定取值' coords='热区坐标' url=''>
> </map>
> ```
>
> 音频、视频及flash文件：\<embed src='url' width='' height='' autostart='是否自动播放' loop='是否循环播放'>\</embed>

**DIV 与 SPAN**

> 块标记：\<div>\</div>，该标记的内容会在开始时自动换行
> 属性：P109
>
> 行内标记：\<span>\</span>，内容前不会自动换行
> 属性：P113

**表格**

> 表格标签：\<table>\</table>
>
> ```html
> <!-- tr行标记，th字段标记，td列标记 -->
> <table>
>     <tr>
>         <th></th>
>         <th></th>
>     </tr>
>     <tr>
>         <td></td>
>         <td></td>
>     </tr>
> </table>
> ```
>
> 

**表单与按钮**

> 表单标签：\<form>\</form>，是用户与后台程序交互的主要手段
>
> > 表单的enctype属性：enctype 属性规定在发送到服务器之前应该如何对表单数据进行编码。
> > 默认地，表单数据会编码为 "application/x-www-form-urlencoded"。就是说，在发送到服务器之前，所有字符都会进行编码（空格转换为 "+" 加号，特殊符号转换为 ASCII HEX 值）。
> >
> > 在表单发送特殊格式的数据时已修改该变量，如文件格式数据时要设置成"enctype='multipart/form-data' "。
> >
> > ![image-20201201164352955](image\image-20201201164352955.png)
>
> 按钮标签：\<input>\</input>
>
> ```html
> <form method='post' action='后台应用程序'>
> 	<input type=''/>
> </form>
> 
> <!-- 单行文本输入框 -->
> <input type='text' name='名字' maxlength='最大输入长度' size='文本框大小,小于等于最大长度' value='默认值' readonly/> readonly表示只读，不能修改内容。
> <!-- 密码输入框 -->
> <input type='password' maxlength='' size=''/>
> <!-- 复选框 -->
> <input type='checkbox' name='' value='' checked='checked'/>chedked表示是否预选中
> <!-- 单选按钮 -->
> <input type='radio' name='' value='' checked='checked'/>
> <!-- 图像按钮 -->
> <input type='image' src='url' name='' width='' height=''/>
> <!-- 提交按钮 -->
> <input type='submit' name='' value='提交'/>
> <!-- 重置按钮 -->
> <input type='reset' name='' value='重置'/>
> <!-- 普通按钮 -->
> <input type='button' name='' value=''/>
> <!-- 文件选择框 -->
> <input type='file' name=''/>
> <!-- 隐藏按钮 -->
> <input type='hidden' name=''/>
> ```
>
> 多行文本输入标签\<textarea>\</textarea>
>
> ```html
> <textarea name='' row='可见行数' cols='可见宽度' wrap='提交表单的换行方式，P203'></textarea>
> ```
>
> 下拉列表：\<select>\</select>
>
> ```html
> <select name='' size='可见选项数量' multiple> multiple表示可以多选
> 	<option value='选项值' selected>selected表示预先被选中
> </select>
> ```
>
> 





