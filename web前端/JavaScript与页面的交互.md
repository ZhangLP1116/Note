**1、发生特定事件时触发javascript**

> **主要内容**：事件——>事件句柄——>处理程序
>
> 在浏览器中通过为特定事件句柄绑定javascript代码，来实现用户执行特定操作时触发一个事件，浏览器就会去查找该事件的句柄是否绑定了处理程序，若有则执行该程序。浏览器中的事件有点击，双击，选中等。具体分类如下。
>
> **1、鼠标事件**
>
> ![image-20201017114900563](C:\Users\zhang\AppData\Roaming\Typora\typora-user-images\image-20201017114900563.png)
>
> **2、键盘事件**
>
> ![image-20201017114917057](C:\Users\zhang\AppData\Roaming\Typora\typora-user-images\image-20201017114917057.png)
>
> **3、HTML事件：html中的元素触发的一些事件**
>
> ![image-20201017115121343](C:\Users\zhang\AppData\Roaming\Typora\typora-user-images\image-20201017115121343.png)
>
> ![image-20201017114959312](C:\Users\zhang\AppData\Roaming\Typora\typora-user-images\image-20201017114959312.png)
>
> ![image-20201017115205490](C:\Users\zhang\AppData\Roaming\Typora\typora-user-images\image-20201017115205490.png)
>
> ![image-20201017115230550](C:\Users\zhang\AppData\Roaming\Typora\typora-user-images\image-20201017115230550.png)
>
> ![image-20201017115547221](C:\Users\zhang\AppData\Roaming\Typora\typora-user-images\image-20201017115547221.png)
>
> ![image-20201017115632354](C:\Users\zhang\AppData\Roaming\Typora\typora-user-images\image-20201017115632354.png)
>
> ![image-20201017115655243](C:\Users\zhang\AppData\Roaming\Typora\typora-user-images\image-20201017115655243.png)
>
> 
>
> **4、突变事件：**是指文档对象底层元素发生改变时触发的事件。如文档的子树因为添加或者删除节点时会触发DomSubtreeModified（DOM子树修改事件）
>
> **5、其他事件**
>
> ![image-20201017115245974](C:\Users\zhang\AppData\Roaming\Typora\typora-user-images\image-20201017115245974.png)
>
> ![image-20201017115736529](C:\Users\zhang\AppData\Roaming\Typora\typora-user-images\image-20201017115736529.png)
>
> **6、事件处理：**当事件触发时，如果需要执行特定程序就需要为该事件的事件句柄指定特定的程序。一般有以下方法。事件句柄原则上以on+事件名的形式
>
> ```html
> // 静态指定，事件句柄=“事件处理程序”
> <input type='button' onclick='show()'>
> 
> // 动态指定，这种方法允许程序向操作javascript属性一样来处理事件
> <事件发生对象>.<事件句柄>=函数名/founction(){} //此处必须使用无名函数，若想复用可以在函数体内返回一个函数
> document.getElementById('inp').onclick=function(){return show();}
> document.getElementById("inp").attachEvent("onclick", display)
>     
> // 特定指定
> <script type='text/javascript' for='事件发生对象' event='事件句柄名称'>程序</script>
> <script type='text/javascript' for='window' event='onload'>
> 	alert('Tip');
> </script>
> 
> // 主动触发事件
> object.事件句柄
> myform.mybutton.onclick()，主动触发单击事件
> ```
>
> **7、带有返回值的事件处理程序：**一般来说事件触发时执行一段程序时没有返回值的，因为事件句柄之上不属于页面的程序范围，是浏览器程序的范围，是没有特定程序去处理页面程序的各种各样的函数返回值。所以事件程序有返回值的时候也只能有两种，True或False。当浏览器接收到句柄返回值时判断若值为True则正常执行程序，若值为False时则停止执行后续程序。一般使用在表单提交时判断数据是否正确，若正确则封装数据发送到后台，若事件返回值为False不正确，则不封装数据发送给后台。
>
> ```html
> <form name='form1' action='simple.jsp' onsubmit='return showName();'>
> 	<input type='text' name='inp'/>
>     <input type='submit' name='submit' />
> </form>
> ```
>
> 

**2、javascript与html节点的交互**

> javascript与html节点的操作主要时通过操作DOM和BOM两个模型去实现，事件也是属于DOM模型中的一个对象，每一个对象都有着自身的属性和方法。
>
> ![image-20201018103955710](C:\Users\zhang\AppData\Roaming\Typora\typora-user-images\image-20201018103955710.png)
>
> **1、DOM：（Document Object Model，文档对象模型）**
>
> > **document对象是window对象的下一层，该对象包含了所有HTML内容，所以javascript通过和该对象的交互来实现和节点的交互。**
> >
> > **1、DOM节点树：**HTML中的所有内容都树形结构保存在DOM中，DOM中的每一个成分都是节点，节点树种有三种类型的节点：元素节点、属性节点、文本节点。其中该元素的元素节点和属性节点互为兄弟节点，文本节点则为元素节点的子节点。
> >
> > ![image-20201017124656658](C:\Users\zhang\AppData\Roaming\Typora\typora-user-images\image-20201017124656658.png)
> >
> > ![image-20201017124817563](C:\Users\zhang\AppData\Roaming\Typora\typora-user-images\image-20201017124817563.png)
> >
> > **2、节点对象访问**
> >
> > ```javascript
> > // 通过属性访问节点，document对象的documentElement属性可以获得整个DOM节点数上的任何一个节点。
> > 
> > var root = document.documentElement; // 获取根节点
> > var childs = root.chileNodes; // 获取根节点下的所有子节点，也就是head和body节点，以数组形式,其中每个元素都是对象类型，可以在访问其中的属性
> > document.write(childs[0].nextSibing.nodedName);
> > // 按这种方法逐层向下就可以访问到所有节点
> > 
> > 
> > // 通过document的方法访问节点，就是根据标签的一些特征去定位标签进行访问
> > // 1、document.getElementById()通过标签ID访问标签，该方法返回一个页面元素，若有相同的ID存在则返回第一个ID的标签
> > // 2、document.getElementByName()通过标签name属性访问标签，该方法返回一个对象数组，若没有找到对应的元素则返回0
> > // 3、document.getElementByTagName()通过标签名访问节点，该方法返回一个对象数组，即使元素只有一个。
> > // 通过forms属性访问表单，该属性返回一个数组对象，包含页面中所有的form对象
> > var myform = document.forms;
> > var imgform = myform[0]; // 通过索引获取想要的表单对象
> > // 直接通过表单name属性获取表单对象
> > var imgform = document.imgform; // 同样也获得了imgform表单对象
> > // 获取表单对象中的元素
> > var username = imgform.element[0]; //通过element属性可以访问表单中的所有标签
> > var username1 = imgform.username1; //通过表单中标签的name属性也可以访问对应的标签
> > var password = imgform.element[2];
> > var password1 = imgform.password1;
> > ```
> >
> > **3、节点操作**
> >
> > ```javascript
> > // 增加一个节点
> > document.createElement(tagname)
> > document.createTextNode(string)
> > .appendChild(node) //添加一个子节点，参数为节点对象
> > .insertBefore(nodeB, nodeA)// 在节点A前插入一个节点B，参数为节点对象
> > // 例：增加一个带文本的标签
> > var newp = document.createElement('p'); //创建p节点
> > var ptext = document.createTextNode('hello world');//创建p节点内容
> > newp.appendChild(ptext);// 将内容绑定在p节点下，内容放置位置
> > document.forms[0].appendChild(newp);// 将p节点放置在表单元素第一个元素下，标签放置位置
> > 
> > // 删除一个标签
> > var p = $('p');
> > document.form1.removeChild(p);// 将form1标签中的p节点删除
> > // 替换一个节点
> > var p1 = document.createElement('p');
> > document.form1.replaceChild(p1, p);//将form1中的p节点替换为p1节点
> > // 插入一个节点
> > document.form1.insertBefore(p1, p)//在form1标签中的p标签前插入一个p1节点
> > ```
> >
> > **4、节点内容的交互**
> >
> > ```javascript
> > // 节点文本内容的获取和修改，innerHTML、innerText
> > // 通过innerText属性获取和修改节点纯文本内容,innerText属性包含节点中的所有纯文本内容，不包含HTML文本内容。
> > var p = $('p');
> > p.innerText = 'HELLO';
> > document.write(p.innerText);
> > // 通过innerHtml属性获取和修改节点的HTML文本内容，该属性包含所有文本+HTML代码
> > // 因为该属性能够修改HTML代码，所以也可以通过该属性在节点内添加节点
> > p.innerHtml = '<strong> hello </strong>';
> > document.write(p.innertHtml);
> > ```
> >
> > **5、节点属性的交互**
> >
> > ```javascript
> > // 通过方法获取和修改节点
> > .getAttribute(name)，通过节点的属性名获取属性值
> > .setAttribute(name, value)，通过属性名设置属性值
> > // 例
> > var div = $('main');
> > var color = div.getAttribute('bgColor'); //获取标签的背景色
> > div.setAttribute('bgColor', '#333333');//设置标签的背景色
> > 
> > // 通过属性获取和修改节点，
> > // 例
> > var img_path = $('img').src;//获取img节点的scr属性值
> > $('img').scr='....';//设置src节点的属性值，实现图片切换效果
> > ```
> >
> > 
>
> **2、BOM：（Broswer Object Model， 浏览器对象模型）**
>
> >BOM定义了浏览器对象的组织形式和相互关系，描述了浏览器对象的层次结构是WEB页面中内置对象的组织形式：**BOM的对象包括windows、document、history、location、navigator、screen、frame**，其结构关系如下
> >
> >![image-20201018110034844](C:\Users\zhang\AppData\Roaming\Typora\typora-user-images\image-20201018110034844.png)
> >
> >**1、window对象**
> >
> >![image-20201018110314844](C:\Users\zhang\AppData\Roaming\Typora\typora-user-images\image-20201018110314844.png)
> >
> >![image-20201018110338500](C:\Users\zhang\AppData\Roaming\Typora\typora-user-images\image-20201018110338500.png)
> >
> >![image-20201018110408115](C:\Users\zhang\AppData\Roaming\Typora\typora-user-images\image-20201018110408115.png)
> >
> >![image-20201018110425512](C:\Users\zhang\AppData\Roaming\Typora\typora-user-images\image-20201018110425512.png)
> >
> >```javascript
> >// window对象的常用方法
> >// 1、警告框
> >alter('ss')//弹出警告框
> >// 2、提示框
> >prompt('提示信息', 默认值)// 用于提示用户在进入每个页面前输入某个值。
> >// 3、确认框
> >// 弹出一个具有确认和取消按钮的窗口，当用户点击确认时该窗口返回True，当用户点击取消时返回false
> >var f = confirm(message)
> >if(f){}else{}
> >// 弹出上面3种提示框时都会暂停javascript代码的执行，等待用户做出响应后才继续执行
> >
> >// 4、focus()，为一个页面元素获取焦点，相当于选中该元素
> >$('input').focus(); //将焦点基于input标签，这样该标签就可以获取键盘的输入，相当于鼠标点击选中
> >
> >// 5、定时方法
> >setinterval(code,interval)// 按照指定周期调用函数或者表达式，返回一个intervalID，(ms)
> >setTimeout(code, delay)// 在指定时间后调用函数或表达式，只执行一次，返回一个timeoutID，(ms)
> >clearInterval(intervalID)// 取消setInterval设置的timeout
> >clearTimeout(timeoutID)// 取消setTimeout设置的timeout
> >
> >var TimerID = setinterval(show(), 100);//设置定时器每100ms执行一次show()函数，将该计时器的ID保存在变量TimerID中
> >clearInterval(TimerID);// 清楚对应ID的计时器
> >
> >//因为window对象时最顶层的所以在使用该对象的方法时不需要object.f()的方式去调用
> >```
> >
> >**2、navigator对象**
> >		该对象保存客户端浏览器本身的一些信息，如版本、浏览器名称、客户机的操作系统等
> >
> >![image-20201018113339885](C:\Users\zhang\AppData\Roaming\Typora\typora-user-images\image-20201018113339885.png)
> >
> >```javascript
> >document.write(navigator.appName)
> >```
> >
> >**3、screen对象**
> >		该对象保存着客户机屏幕信息。
> >
> >![image-20201018113843089](C:\Users\zhang\AppData\Roaming\Typora\typora-user-images\image-20201018113843089.png)
> >
> >```javascript
> >document.write('屏幕可用高度：' + screen.avaiHeight);
> >```
> >
> >**4、history对象**
> >		该对象表示窗口的浏览历史，有window的history属性引用该窗口的history对象。history对象是一个		数组，其中的元素存储了浏览历史中的全部url，所以可以通过引用该对象获取浏览历史中的某个		URL
> >
> >![image-20201018114533111](C:\Users\zhang\AppData\Roaming\Typora\typora-user-images\image-20201018114533111.png)
> >
> >```javascript
> >window.history.back()// 加载上一个页面
> >// 加载下一个页面，只有使用过浏览器中的后退按钮，或者back()、go()方法则forward()方法无效
> >window.history.forward()
> >window.history.go(-2)// 加载倒数第二个页面
> >```
> >
> >**5、location对象**
> >		该对象用来表示浏览器当前加载的文档URL。该对象的属性说明了URL中的各个部分
> >
> >![image-20201018115116810](C:\Users\zhang\AppData\Roaming\Typora\typora-user-images\image-20201018115116810.png)
> >
> >```javascript
> >document.write(location.href);
> >location.href = 'http://baidu.com';// 当URL改变时页面也会跟着改变
> >
> >location.assign('obj.html');// 转到指定的URL
> >// reload()方法用于刷新当前文档。
> >// reload() 方法类似于你浏览器上的刷新页面按钮。
> >//如果把该方法的参数设置为 true，那么无论文档的最后修改日期是什么，它都会绕过缓存，从服务器上重新下载该文档。这与用户在单击浏览器的刷新按钮时按住 Shift 健的效果是完全一样。
> >location.reload(Boolean);
> >location.replace('obj.html')// 用指定的URL替换当前资源
> >```
> >
> >