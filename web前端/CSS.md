CSS：层叠样式表

单位

> 绝对单位：现实中的实际单位，在网页中使用很少，只有在某些特殊场景下使用
> in：英寸，1in=2.54cm
> cm：厘米
> mm：毫米
> pt：磅，12pt=1/6in，1pt=1/72in
>
> 相对单位：与绝对得相比，相对得的显示大小不固定，大多取决于屏幕的分辨率视觉区域，浏览器设置等。？
> em：表示元素字体的高度，根据font-size属性值的大小来确定
>
> ```html
> p{font-size:24px; line-height:2em}
> 这里的2em=48px，em=24px。若font-size=em，那么这里的em大小由父元素的font-size来确定
> ```
>
> ex：表示所使用字体中小写字母x的高度作为值，实际使用中为em值的一半
> px：根据屏幕的像素点来确定，分辨率越大的屏幕每个单位内的像素点越多
> %：百分比单位，一般通过父元素的值来确定
>
> ```html
> p{font-sizr:150%; line-height:100%}
> ```
>
> 

字体样式

> **字体大小**：font-size属性，用来设置字体大小
>
> ```html
> 基本语法：font-size:绝对大小| 相对大小| 关键字
> 绝对大小：in,cm,mm,pt,pc等
> 相对大小：em,ex,px,%
> 关键字：xx-small,x-small,small,medium,large,x-large,xx-large
> ```
>
> **字体风格**：font-style属性，设置字体的风格，如斜体、粗体等
>
> ```html
> font-style:normal| italic| oblique
> normal：不使用斜体，该属性为默认属性
> italic：使用斜体显示文字
> oblique：使用倾斜字体展示文字
> ```
>
> **字体类型**：font-family属性，设置字体类型，宋体、楷体、微软雅黑等
>
> ```html
> font-style:字体1，字体2，字体3
> 浏览器会根据该属性的设置使用排列靠前的字体，若不支持该字体则使用下一个字体类型
> ```
>
> **字体变形**：font-variant属性：一般用于英文文字，将大写字母展示为小写型
>
> ```html
> font-variant:normal| small-caps
> normal:表示使用默认
> small-caps:表示将大写字母展示为小写字母大小
> ```
>
> **字体粗细**：font-weight属性：用来设置字体粗细
>
> ```
> font-weight:normal| bold| bolder| lighter| 100| 200|...|900
> normal：表示使用默认
> bold：表示标准粗体
> bolder：表示特粗体
> lighter：表示细体
> 整数：数字约大越粗，400相当于normal，700相当于bold
> ```
>
> 

文本样式

> **字符间距**：letter-spacing属性/word-spacing，设置字符间距
>
> ```html
> letter-spacing：normal| 长度单位
> word-spacing：normal|长度单位
> 
> word-spacing属性针对英文单词
> letter-spacing对中文、英文字符串斗气作用
> ```
>
> **行间距**：line-height：设置行与行之间的距离
>
> ```html
> line-height:normal| 长度单位
> 一般使用em，根据字体大小相对设置
> ```
>
> **首行缩进**：text-indent属性：设置首行缩进长度
>
> ```
> text-indent:长度单位| 百分比单位
> 一般使用em，根据字体大小相对设置
> ```
>
> **字符装饰**：text-decoration属性：设置文字上划线、下划线、删除线等效果
>
> ```html
> text-decoration:none| underline| overline| line-through
> ```
>
> **英文大小写转换**：text-transform属性：转换文本中英文字母的大小写
>
> ```html
> text-transform: capitalize| uppercase| lowercase| none
> capitalize：只将单词的开头字母转换为大写
> uppercase：将所有字母转换为大写
> lowercase：将所有字母转换为小写
> none：不转换
> ```
>
> **水平对齐**：text-align：设置文本水平对齐方式
>
> ```html
> text-align:left | right | center | justify
> left：左对齐，默认
> right：右对齐
> center：中间对齐
> justify：两端对齐
> ```
>
> **垂直对齐**：vertical-align：设置垂直对齐方式
>
> ```html
> vertical-align:top | middle | bottom | text-top | text-bottom
> top：把元素顶端与行中最高元素顶端对齐
> middle：把元素放在父元素的中间
> bottom：把元素底部与行中最低元素底部对齐
> text-top：把元素顶端与父元素字体顶端对齐，一般用于图片与文字的对齐
> text-bottom：把元素底部与父元素字体底部对齐，一般用于图片与文字的对齐
> ```
>
> 

颜色与背景

> **字体颜色属性**：color属性，用来设置页面中的字体颜色
>
> ```html
> color:rgb(r,g,b) | rgb(r%,g%,b%) | #ffffff | #3ff | colorname
> rbg()：使用函数设置元素，参数可以是百分比(0%~100%)，也可以是整数(0~255)
> 十六进制：设置颜色因为每个颜色占8bit所以一个颜色可以用两个十六进制数来表示。有重复时可以简写，如#f
> colorname：使用内置的颜色名来设置颜色，如：blue、red、black、white、yellow、lime、aqua等
> ```
>
> **背景颜色属性**：background-color属性设置背景颜色
>
> ```html
> background-color:语法同上
> ```
>
> **背景图像属性**：background-image，设置图片作为背景
>
> ```
> background-image:url('图片路径') | none
> url():图片所在地
> none：不使用图片作为背景
> ```
>
> **背景重复属性**：background-repeat属性，用于设置背景图片的重叠覆盖方式，当背景图片不能全覆盖背景时使用
>
> ```html
> background-repeat: repeat | no-repeat | repeat-x | repeat-y
> repeat：在x轴、y轴上重复使用背景图片覆盖未覆盖到的位置
> repeat-x：只在x轴上重复使用背景图片覆盖未覆盖到的位置
> repeat-y：只在y轴上重复使用背景图片覆盖未覆盖到的地方
> no-repeat：表示不重复使用背景图片去覆盖未覆盖到的地方
> ```
>
> **背景附件属性**：background-attachment属性，设置背景图像是否随滚动条一起滚动
>
> ```html
> background-attachment:scroll | fixed
> scroll：表示滚动条滚动时背景图片一起滚动，滚动条移动时背景图片的绝对为位置保存不变，滚动条下移时被的图片的开头会随着被遮挡
> fixed：背景图片固定不动，背景图片的相对位置保持不变，不论滚动条怎么移动背景图片一直处于浏览器窗口的那个位置，可以防止背景图片因滚动条下拉而被遮挡
> ```
>
> **背景图像位置属性**：background-position属性：用于设置背景图片的起始位置
>
> ```html
> background-position:参数1参数2
> 第一个参数表示水平位置
> 第二个参数表示垂直位置
> 默认值为0%0%，如果指定了其中一个那么另外一个取值为center
> 参数取值如下图
> ```
>
> ![image-20201008151404813](image\image-20201008151404813.png)

列表样式

> **list-style-type**：属性设置列表符号类型
>
> ```html
> list-style-type:属性值
> none:不使用列表符号
> disc：实心圆
> circle：空心圆
> square：实心方块
> decimal：阿拉伯数字
> lower-roman：小写罗马数字
> upper-roman：大写罗马数字
> lower-alpha：小写英文数字
> upper-roman：大写英文数字
> ```
>
> **list-style-image**：属性设置列表符号为图片
>
> ```html
> list-style-image:url('图片路径')
> ```
>
> **list-style-postion**：属性设置列表符号的位置
>
> ```html
> list-style-postion: outside | inside
> ourside：默认值，符号放在文本之外，换行文本在符号下均不对齐，根据文字对齐
> inside：符号放在文本内，换行符在符号下均对齐
> ```
>
> 

盒子模型

> **边界**：margin属性，用于设置块的外边距
>
> ```html
> margin-(top | right | borrom | left): 长度单位 | 百分比 | auto
> 分别用于设置上边距、右边距、下边距、左边距
> 也可以同时设置
> margin:10px 10px 30px 20px
> 顺序也是上右下左，顺时针
> ```
>
> **边框**：border属性，用来设置块的边框线
>
> ```html
> <!-- 边框样式 -->
> border-style:属性值
> none：无边框
> hidden：隐藏边框，用于解决边框冲突
> solid：实线
> botted：点状边框
> dashed：虚线
> double：双线，其宽度取决于border-width属性
> groove：3D凹槽边框，其效果取决于border-color属性
> ridge：山脊状边框，其效果取决于border-color属性
> inset：沉入感边框，其效果取决于border-color属性
> outset：浮出感边框，其效果取决于border-color属性
> 也可以分别设置边框，border-(top | right | bottom | left)-style:属性
> 
> <!-- 边框颜色 -->
> border-color:格式和color相同
> 也可以分别设置：border-(top | right | bottom | left)-color:属性值
> 
> <!-- 边框宽度 -->
> border-width:长度单位 | 关键字
> 关键字：medium（默认），thin（小于默认） ,thick（大于默认）
> 也可以分别设置：border-(top | right | bottom | left)-width:属性值
> 
> <!-- 统一设置 -->
> border:border-width border-style border-color
> ```
>
> **填充**：padding属性。用于设置块的内边距
>
> ```html
> padding-(top | right | borrom | left): 长度单位 | 百分比
> 分别用于设置上边距、右边距、下边距、左边距
> 也可以同时设置
> padding:10px 10px 30px 20px
> 顺序也是上右下左，顺时针
> ```
>
> 

