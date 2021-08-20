<h1>pyhton
</h1>
<a href='#str'>变量类型——字符串</a>

<a href='#number'>变量类型——数值</a>

<a href='#list'>变量类型——列表</a>

<a href='#y'>变量类型——元组</a>

<a href='#dict'>变量类型——字典</a>

<a href='#func'>函数</a>

<a href='#class'>类</a>

<a href='#import'>模块的导入</a>

<a href='#error'>异常</a>

<h4>常见变量类型，与方法
</h4>

 <span name='str'>**字符串**</span>

> > 由成对的单引号或者双引号构成
> > 	如：a = 'hello world'，b = "hello world"
> > 	常用方法：
> > 	.title()：将字符串中的每个单词首字母大写
> > 	.upper()：将字符串中的每个字母大写
> > 	.lower()：将字符串中的每一个字母小写
> > 	.rstrip()：将字符变量串末尾的空格删除
> > 	.lstrip()：将字符串开通的空格删除
> > 	.strip()：将字符串首尾的空格删除
> > 	.split()：将字符串转换成列表，默认以空格为分隔标志
> > 	str()：将变量转换成字符串类型

<span name='number'>**数值**</span>

> >可以进行算数运算的一类变量，常见的有int，float
> >
> >常见运算符+(加)、-(减)、*(乘)、\（除）、%（取余）、**（乘方）
> >
> >ps：python中的除法运算和C语言中相似，除号两边都为整形时则为整除，若任意一边为float类型时则为精确运算
> >
> >常用方法：
> >
> >int()：将变量转换成整形
> >
> >float()：将变量转换成浮点型

<span name='list'>**列表**</span>

> > 存储一组数据的变量类型，其中的元素可以是字符、数字、实例、字典、元组等，用[]方括号表示
> >
> > **列表的增删改查：**
> >
> > 用例：b = ['a', 'b']
> >
> > 1、访问列表中的元素
> >
> > 使用索引访问列表中的元素，索引从0开始。
> >
> > b[0]
> >
> > 2、修改列表中的元素
> >
> > b[0] = 'c'
> >
> > 3、增加列表中的元素
> >
> > 在列表末尾加入：b.append('c')
> >
> > 在列表中插入：b.insert(0,'c')，需要参数：索引位置，插入值。插入位置开始的每一个元素都将向右移动一位
> >
> > 4、删除列表中的元素
> >
> > del：del b[0]
> >
> > b.pop()：默认删除末尾元素，并返回删除的值，可以指定位置，如：b.pop(0)，a = b.pop(0)
> >
> > b.remote('a')：删除指定内容元素
> >
> > **切片：用于创建列表的副本**
> >
> > b[:]：从头到尾
> >
> > b[:n]：从头到n-1的位置
> >
> > b[1:]：从1到尾
> >
> > b[-2:]：从倒数第二到尾
> >
> > **列表的遍历**
> >
> > for i in range(1,10):（表示循环从1开始到n-1结束）
> >
> > for i in b:（表示遍历整个列表）
> >
> > **列表的排序**
> >
> > b.sort()：对列表b根据字母顺序进行永久性的排序，（传入形参reverse=True，可以根据字母顺序逆序排序）
> >
> > sorted(b)：对列表进行临时性的排序，如：print(sorted(b))，同样可以传入reverse=True
> >
> > b.reverse()：将列表反向排序
> >
> > **列表解析**
> >
> > b = [vaule for vaule in range(1,9)]：由列表名，表达式，for循环三部分组成
> >
> > **列表的常用方法**
> >
> > len(b)：计算列表实际长度
> >
> > s = ''.join(b)：将列表转换为字符串
> >
> > list(range(1,9))：生成一个1到8的列表
> >
> > **列表与for循环**
> >
> > 当for循环在遍历某一列表时，不可以在循环体内对该列表进行修改，这样会影响for循环的组成运行
> >
> > **列表与函数**
> >
> > 当列表以变量名形式传递给函数时，函数对列表的改变会影响的列表本身。如不想列表本身的元素被修改则可以使用**切片的形式传递**列表的副本，这样既传递了列表的元素又不会使自身的元素遭到修改

<span name='y'>**元组**</span>

> > 由一系列不可修改的元素组成，元组只能在定义时赋值，不能通过索引改变元素

<span name='dict'>**字典**</span>

> > 由花括号包裹起来的一系列键值对
> >
> > 用例：s = {‘a’:  ‘b’,'c': 'd'}
> >
> > **字典的增删改查**
> >
> > 1、增加键值对
> >
> > s.[e] = 'f'：增加新的键值对‘e’ :‘f’
> >
> > 2、访问值
> >
> > s.[a]：访问a的值
> >
> > s.get(name)：使用get()方法输入key查询value
> >
> > 3、修改值
> >
> > s.[c] = 'z'：修改c的值
> >
> > 4、删除键值对
> >
> > del s.[e]：删除键值对‘e’: ‘f’
> >
> > **字典的遍历**
> >
> > for key in s：遍历字典元素，默认对key进行遍历
> >
> > for key, value in s.items()：遍历键值对
> >
> > for i in s.keys()：返回一个包含所有键的列表，遍历所有键
> >
> > for i in s.values()：返回一个包含所有值的列表，遍历所有值
> >
> > **字典的嵌套**
> >
> > 字典的值可以是列表，也可以是字典

<span name='func'>函数</span>

>> **函数的定义**
>>
>> 以def关键字开头+函数名称+形式参数+函数体组成。每一个函数都应该是一个独立的功能模块
>>
>> **形参的类型**
>>
>> POSITIONAL_ONLY、POSITIONAL_OR_KEYWORD、VAR_POSITIONAL、KEYWORD_ONLY、VAR_KEYWORD
>>
>> 实例：def func(a, b ,*c , d, f, **e)
>>
>> POSITIONAL_ONLY：位置形参，实参传递时可以按照位置顺序进行传递，如a、b就是该类形参
>>
>> POSITIONAL_OR_KEYWORD：位置形参或关键字形参，实参可以根据位置顺序传递也可以用关键字传递，如func(a, b=2)，a，b都属于该类形参
>>
>> VAR_POSITIONAL：可变的位置形参，该类形参用来接收0个或多个实参，*c就属于该类形参
>>
>> KEYWORD_ONLY：关键字实参，实参只能通过关键字形式传递，d、f就属于该类形参，因为处于可变位置形参后所以无法用位置实参的模式去对形参d、f，赋值
>>
>> VAR_KEYWORD：可变的关键字形参，该类形参用来接收一个或多个关键字实参，**e就属于该类型
>>
>> 形参可以设置默认值，当无实参输入时则使用默认值
>>
>> **返回值**
>>
>> 函数可以有0个或多个返回值，返回值可以是字符串、数值，列表、字典、生成器等

<span name='class'>**类**</span>

> > **类的定义**
> >
> > 用来模拟现实中的一类事物，并用属性和方法来表示这类事物的特征和行为。
> >
> > **类的创建**
> >
> > 使用关键字class+类名创建
> >
> > **初始化函数**
> >
> > \__init__()：用于初始化类属性
> >
> > \__init__并不相当于C#中的构造函数，执行它的时候，实例已构造出来了。
> >
> > ```python
> > class A(object):
> >     def __init__(self,name):
> >         self.name=name
> >     def getName(self):
> >         return 'A '+self.name
> > a=A('hello')
> > #相当于下面两步，object是python中所有类的超类
> > 
> > a=object.__new__(A) #这一步才是创建实例，为实例分配内存
> > A.__init__(a,'hello') #这一步是对实例A的初始化
> > 
> > #在上面可以看出__init__中的self的作用，就是用来接收实例a，__init__()在运行时就可以看做是	a.name = name，self的作用就相当于一个占位符。
> > 
> > ```
> >
> > **类的属性**
> >
> > 用来描述特征
> >
> > 类的属性值可以直接在实例中修改，或者通过类方法去修改
> >
> > **类的方法**
> >
> > 用于描述行为
> >
> > **类的继承**
> >
> > 子类会继承父类的所有属性和方法
> >
> > 继承中的\__init__()方法
> >
> > ```python
> > # 1、当子类不重写父类中的__init__()方法时，python解释器会隐式的调用父类中的__init__()方法去初始化属性
> > class B(A):
> >     def getName(self):
> >         return 'B '+self.name
> >  
> > if __name__=='__main__':
> >     b=B('hello')
> >     print b.getName()
> > # 2、当子类重写__init__()方法时，python解释器不会调用父类中的__init__方法
> > # 因为重写的__init__方法中并没有对name进行初始化，所有运行时会报错，"AttributeError: 'C' object has no attribute 'name'”
> > class C(A):
> >     def __init__(self):
> >         pass
> >     def getName(self):
> >         return 'C'+self.name
> >  
> > if __name__=='__main__':
> >     c=C()
> >     print c.getName()
> >     
> > # 3、当想要重写父类的__init__方法时最好显示的调用父类中的__init__()方法以完整的拥有父类的属性，并且可以直接在添加新的属性
> > class C(A):
> >     def __init__(self,name):
> >         super().__init__(name)
> >     def getName(self):
> >         return 'C'+self.name
> > 
> > if __name__=='__main__':
> >     c=C('hello')   
> >     print c.getName()
> > ```
> >
> > **类的多态**
> >
> > ```python
> > class Card:
> >   def __init__(self, rank, suit):
> >     self.suit = suit
> >     self.rank = rank
> >     self.hard, self.soft = self._points()
> > 
> > class NumberCard(Card):
> >   def _points(self):
> >     return int(self.rank), int(self.rank)
> > 
> > class AceCard(Card):
> >   def _points(self):
> >     return 1, 11
> > 
> > class FaceCard(Card):
> >   def _points(self):
> >     return 10, 10
> > #父类中不定义_points()方法，当子类创建实例时会自动调用父类  __init__()方法，然后在调用对应子类的_points()去对 self.hard, self.soft属性赋值
> > ```
> >
> > **类与实例**
> >
> > 与C语言中的结构体相识，类在穿件时仅仅是创建一个抽象的概念，告诉解释器该怎么去展示这个类型，该怎么去存储这个类型。
> >
> > 类相当于一个模具，而实例就是从该模具中被创造出来的一个实体

<span name='import'>**模块导入**</span>

> > import model from funcname，从当前目录下寻找模块
> >
> > import model from classname，从当前目录下寻找模块

<span name='error'>**异常**</span>

> > try
> >
> > ​	语句块
> >
> > except
> >
> > ​	语句块
> >
> > else(可省)
> >
> > ​	语句块
> >
> > 只有当try语句块内的代码没有抛出异常时才执行else中的代码，否则则执行except中的代码

