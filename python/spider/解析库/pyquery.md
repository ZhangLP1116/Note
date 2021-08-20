pyquery解析库

初始化

>pyquery模块中使用PyQuery类来处理html文本
>
>使用PyQuery来解析时需要传入HTML文本初始化一个PyQuery类型的实例
>
>```python
>from pyquery import PyQuery as pq
># 传入HTML文本创建解析对象
>html = requests.get(url).text
># 返回一个PyQuery类型
>doc = pq(html)
>```
>
>

获取节点

>获取节点
>
>```python
># 在PyQuery实例中传入CSS选择器选中body下id为main的div，返回类型为PyQuery
>div = doc('body div#main')
># 选择body下的ul中的所有li标签，返回类型为PyQuery
>lis = doc('body ul li')
>```
>
>获取子节点
>
>```python
>ul = doc('body ul')
># find()方法用于查找父节点下的子孙节点，参数为CSS选择器，会将所有符合条件的节点全部返回,返回类型为PyQuery
>lis = ul.find('li')
># children()方法用于查找父节点下的所有子节点，参数为CSS选择器，会将所有符合条件的子节点全部返回，但不会返回符合条件的孙节点,返回类型为PyQuery
>lis = ul.children('li')
>```
>
>获取父节点
>
>```python
># parent()方法用于获取当前节点的父节点,返回类型为PyQuery
>ul = lis.parent()
># parents()方法用来获取当前节点的所有祖先节点，可以传入CSS选择器来过滤一些祖先节点,返回类型为PyQuery
>ul = lis.parents()
>ul = lis.parents('div')
>```
>
>获取兄弟节点
>
>```python
># siblings()方法用于获取当前节点的所有兄弟节点，返回类型为PyQuery，返回结果中不包含自身,可以传入CSS选择器进行过滤
>li = ul.find('li:first')
>lis = li.sibings()
>```
>
>遍历
>
>```python
># 当返回结果为多个节点时，可以通过items()方法将结果转换为生成器进行遍历，逐个获取节点，在对节点进行特定操作，如获取节点属性、文本等，遍历的每个元素类型都为PyQuery
>for li in lis.items():
>    url = li.attr('src')
>```
>
>

获取属性

> ```python
> # PyQuery对象可以通过attr()方法来获取属性，参数为属性名，返回值为属性值
> # 当PyQuery类型中有多个节点，那么attr()只返回第一个节点的对应属性，这时就可以用遍历的方式去获取每一个节点的属性
> li.attr('src')
> ```
>
> 

获取文本

> 获取text文本
>
> ```python
> # PyQuery对象可以通过text()方法去获取节点的text文本，它会忽略掉其中的所有html文本
> # 当PyQuery类型中有多个节点，text()方法会返回所有节点的文本内容，并用空格分隔
> li.text()
> ```
>
> 获取html文本
>
> ```python
> # PyQuery对象可以通过html()方法去获取节点的html文本，它会包含其中的所有text文本
> # 当PyQuery类型中有多个并列节点，则html()方法只返回第一个节点的html文本
> li.html()
> ```
>
> 

节点操作

>属性操作
>
>```python
># addClass()、removeClass()方法增加，移除class属性值，attr()方法不仅可以用来获取属性值，也可以用来增加属性
>li.addClass('active')
>li.removeClass('active')
>#attr()，增加属性时，第一个参数为属性名，第二个参数为属性值
>li.attr('src', 'http://xxx')
>```
>
>文本操作
>
>```python
># text()、html()，方法也可以用来添加text和thml文本
>li.text('hello')
>li.html('<div>xxx</div>')
>```
>
>节点操作
>
>```python
># PyQuery类型的remove()方法可以实现节点删除的功能
># 这里删除了ul中的第一个li节点，这个方法在解析文本时可以提供一些帮助，帮忙去点一些干扰节点
>ul.find('li:first-child').remove()
>```
>
>