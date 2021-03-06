> 简介
>
> ​		随着Web 广泛的使用，Web上的安全漏洞也不断的暴露出来，一些商业网站急需Web安全性的保障。Web上存在的安全威胁往往依附着其结构特点。

> Web存在的安全威胁
>
> ​		1、Web使用中无处不在的DNS成为了恶意用户的攻击点
>
> ​		2、Web的传输过程是一个攻击点
>
> ​		3、动态页面的使用，使得接收到的页面中包含可执行的代码，这些代码也成为攻击点

> 安全的DNS
>
> ## **DNS欺骗**
>
> ​		**DNS欺骗：**Trudy想要让Alice访问Bob主页时请求自己的服务器，由于用户访问一个域名时必须通过DNS解析后才能得到IP地址从而进行访问，所有伪造一个DNS回复就是Trudy想要的。
>
> ​		**欺骗Alice的DNS服务器：**由于DNS使用UDP进行通讯，所以DNS服务器没办法检查到底时谁提供了答案，Trudy通过向Alice的DNS请求Bob的主页，Alice的DNS向根服务器询问，这时Trudy抢先回复一个DNS应答，告诉Alice的DNS请求的Bob地址为Trudy服务器地址。这样就完成了欺骗。
>
> ​		**伪造DNS回复数据包：**要欺骗DNS就需要伪造UDP数据包，数据包中的根服务器IP地址总所皆知，所以容易伪造，难点在于数据包中的序列号的伪造。
>
> ​		**DNS数据包中序列号的伪造过程：**
>
> ​			原理：获得近期DNS的序列号，在这上递增序列号不断尝试
>
> ​			1、申请一个域xxx，这个域中的DNS服务器可以有申请者设置，用于管理这个域中的域名映射
>
> ​			2、向Alice的DNS服务器请求xxx域，Alice的DNS向xxx域的DNS服务器发送请求包（由于DNS解析的特点，会逐层请求到最底下的DNS服务器）
>
> ​			3、xxx域的DNS收到请求包，即得到了Alice的DNS近期的DNS请求序列号。然后进行DNS的欺骗操作
>
> ## **DNSsec**
>
> ​		**安全的DNS：**上述的DNS欺骗操作很容易挫败，只要每次使用的序列号本身有序递增即可。但是这种处理方法并不能使得DNS边的安全，只不过时填上了一个漏洞。1994年IETF成立一个工作组致力于使DNS从本质上变得安全。项目称为：DNSsec（DNS安全）
>
> ​		**DNSsec原理：**使用公开密码学，每一个DNS区域有一个公钥-私钥对。每一个DNS发送的所有消息都要经过签名，以便接收方验证消息的真实性
>
> ​		**DNSsec提供的服务：**
>
> ​			1、证明数据包从哪里来：DNS发出的每一个消息都携带自己的私钥的签名。
>
> ​			2、公钥分发：DNSsec引入了几种新的记录类型，这些记录类型可以保存公钥、用于签名算法、使用的传输协议等
>
> ​			3、事务和请求认证

> SSL——安全套接层
> 		对于传输过程的威胁，Web使用了一种安全的连接。
>
> ​		**SSL：**安全套接层，它的功能是在两个套接字之间建立安全的连接，SSL可以形象的看作是一个位于TCP之上，应用层之下的一个层。有Netscape公司在1995年创建。
>
> ​		**SSL提供的服务：**
>
> ​			1、客户与服务器之间的参数协商
>
> ​			2、客户和服务器之间的双向认证
>
> ​			3、保密的通信
>
> ​			4、数据完整性保护
>
> ​		**SSL有两个子协议组成：**一个用来建立安全的连接，一个用来使用安全的连接
>
> ​			**SSL建立安全连接：**
>
> ​				1、Alice发起SSL建立连接，指定了Alice可以支持的SSL版本、加密算法、压缩算法，临时值R~A~
>
> ​				2、Bob选择版本、算法、生成一个随机值R~B~
>
> ​				3、Bob发送自己的X.509证书，和证书链
>
> ​				4、这时Bob可以发送一些其他消息，如要求对方证书（用于双向认证），或者仅仅发送一个确认消息告诉对方可以发送消息了。
>
> ​				5、Alice选择一个预设主密钥，使用Bob公钥加密发送给Bob
>
> ​				6、Alice使用R~A~，R~b~和预设主密钥经过一个复杂运算得到一个会话密钥，发送消息更换密钥
>
> ​				7、发送消息表示她已经完成了密钥计算
>
> ​				8、收到5后Bob使用私钥进行解密的到预设主密钥，加上R~A~和R~B~进行推导得到会话密钥
>
> ​				8、9、两步作用和6、7相同。
>
> （这里的Bob相当于一个服务器，它支持各种加密算法和解压算法）
>
> ![image-20210416150519301](image\image-20210416150519301.png)
>
> ​			**使用安全连接：**
>
> ​				1、将流量器的消息分隔成最多16KB单元
>
> ​				2、如果双方支持压缩，则进行压缩
>
> ​				3、计算单元散列值，添加到消息中（MAC表示消息认证码）
>
> ​				4、使用协商好的会话密钥加密数据
>
> ​				5、加上一个分段头，不同端将在接收方的SSL层重组，交给TCP进行传输
>
> ![image-20210416151638548](image\image-20210416151638548.png)
>
> ​		SSL支持多种密码学算法，最强的一种是使用三重DES来加密数（使用3个独立的密钥），通过SHA-1保护数据完整性。一般情况使用128为的密钥进行RC4（对称密钥算法）算法进行加密，通过MD5进行验证。
>
> ​		在建立连接的第4步操作中，另一方可能没有证书，这时很常见的，Web访问用户大多都没有证书，这就要求在建立连接后一般网站会要求登录，已完成最终的双向验证。
>
> ​		在SSL之上依然使用的是HTTP协议，为了和没使用SSL的HTTP访问进行区分，在url上表示为http和https两种形式。并且https惯用端口为443。
>
> ​		1996年Netscape公司将SSL移交给IETF进行标准化，标准化的结果是TLS协议，该协议和SSL在推导会话密钥上有所区别，所有两个协议无法兼容，大多数浏览器实现了两种协议的协商。这就是所谓的SSL/TLS，第一个TLS出现在1999年，使用了ASE算法。

> 移动代码安全
>
> ​		**Java小程序安全性：**对于内嵌的Java小程序，浏览器可以将不可信任的小程序放置在沙箱中执行，每当小程序要访问系统资源时先进行本地安全策略检查。（小程序是编译成解释性语言，可以被放置在沙箱中）
>
> ​		**ActiveX安全性：**是被嵌入到web页面中的x86二进制程序，二进制程序无法被解释性执行，所以无法封装在沙箱中。ActiveX的安全性仅仅在于决定是否执行。Microsoft对此对出的决策是要求每个ActiveX控件都要携带一个数字签名，用户可以验证签名方的可信度，给用户一个判断标准，但这并不是一个解决威胁的方法。
>
> ​		**Javascript安全性：**最初的Javascript没有任何安全措施，Netscape Navigator第二版使用了类似Java小程序的处理方式，第四版使用了代码签名的模型。
>
> ​		**插件安全性：**插件要是一经安装就会被默认为信任的代码，所以插件的安全性保证，要求下载时要经过检验