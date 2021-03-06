> 域名系统
>
> ​	理论上使用IP地址既可以找到Internet中的一台机器进行通信，但是IP地址不便于通信，并IP对应的是机器，而人想要通信的往往一个能够提供服务的程序。这样的程序可以在一台机器上，也可以在另一台机器上，但是访问时却需要用不同的IP地址，增加用户使用的困惑。
>
> ​	所以需要一个更高层次的名字来代表对应的服务——域名
>
> ​	**域名：**使用语义化的名称作为通信地址，一个域名可以对应多个IP地址，在寻址时可以通过选播路由提供地理位置最近的机器提供服务。
>
> ​	**地址映射：**由于机器只能识别数字形式的地址，所以需要一个映射关系将DNS映射成对应的IP地址，早期时是在本地设备上维护一个hosts.txt文件，其中保存着域名——IP的映射。但随着互联网规模的扩大，个人计算机渐渐无法维护庞大的文件，并且每台计算机都维护整个Internet中的域名映射是愚蠢的，大多数域名不会被使用，并且新域名映射的添加也是一个问题。所以需要一个集中式的管理方法——域名系统DNS。
>
> ​	**域名系统（DNS）：**域名系统通过**DNS名字空间**将域名分类、分层。在不同存储设置不同的**域名服务器**，该服务器保存这个层次的**域名资源记录**，为需要DNS映射的主机提供IP地址。

> DNS名字空间
>
> ​	域名由一个专门的组织管理——ICANN（Internet名字与数字地址分配机构）。ICANN划分250个顶级域名。顶级域名可以非为通用域名和国家域名。顶级域名下又可以划分二级域名。完整的域名由各级域名组成，如：eng.cisco.com。若自己要注册一个.com的域名那么申请的域名就是二级域名如：zlp.com
>
> ​	为了创建一个新域，创建者必须得到包含该域的上级域许可。一旦创建了一个新域就可以创建属于自己的子域无需上级上层域许可。这样的创建方式主要是防止域名冲突。
>
> （P472图7-1）

> 域名资源记录
>
> ​	无论是只有一台主机的域还是顶级域，每个域都有一组与它相关联的资源记录。这些记录组成了DNS数据库。最常见的记录就是主机的域名和IP地址信息。
>
> ​	资源记录：由五元组组成。
>
> ​	Domain_name：域名
>
> ​	Time_to_live：记录的有效时间，用于缓存机制中判断是否过期
>
> ​	Class：类别，对应Internet信息它总是IN
>
> ​	Type：类型，对应后续的Value，体现Value值的含义（P473图7-3），如type为A，则value值就表示IPv4
>
> ​	Value：值
>
> （实例P477图7-4）

> 域名服务器
>
> ​	域名服务器用来维护一个区域内的资源记录，区域的划分（P477图7-5）。
>
> ​	一台设备在服务一个域名时就会网DNS服务器发送一个DNS请求包，请求对应的IP地址。（DNS服务器可以时DHCP动态配置，也可以手动指定）DNS服务器收到请求后若请求的域在管理范围内则返回一个**资源记录**。若不在范围内则向根域名服务器询问，根域名服务器收到请求后返回一个知道怎么处理的二级域名服务器IP，本地DNS服务器继续继续向二级服务器询问，直到收到对应的IP地址返回给设备。这种一级一级的查找方式称为**迭代查询**。
>
> ​	得到结果的设备会将资源记录缓存起来以便下次直接取用，缓存的资源记录有效时间就是Time_to_live字段设置的时间。
>
> ​	对应域名服务器返回的记录称作权威记录，为域名服务器就是管理这个记录的权威机构是不会出错的。与之对应的是缓存记录。缓存中得到的信息不一定是可靠的，因为旧的记录可能被更新了。
>
> ​	DNS数据包的传输：DNS使用UDP传输数据包，因为UDP没有可靠性服务，所以在一定时间内没有收到响应就要重新发送请求。每个请求数据包中都包含16为标识符，这个标识符是用在DNS服务器中以便能够区分要对哪一个请求进行响应。