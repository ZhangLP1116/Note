Tomcat是一个servlet容器

> Q：java中自定义servlet在哪里被实例化
>
> A：在Tomcart中Wrapper中被实例化，然后被运行。

> Q：==RequestFacade类==，与Request的关系。
>
> A：Request实例被包装在RequestFacade中是Servlet处理的真正实例。RequestFacade就像一个包工头，其下由很多师傅（Facade，门面设计模式）

> Q：门面设计模式？
>
> A：提供一个统一的接口去访问多个子系统的多个不同的接口，它为子系统中的一组接口提供一个统一的高层接口。内部具有多个功能，对外只提供一个接口。
>
> 例如，自己建房子需要各种各样的的工人，木匠，装修，水泥等。对于不熟悉行业的自己来说一个个单独的找这些人非常困难，并且无法保证质量。这时候可以在一个包工头，给他说明自己的要求，然后包工头再去对接自己下面的人员。这就是一个门面模式。

> Q：怎么将APP部署到Tomcat中？
>
> A：在Tomcat源码中==HostConfig类==下的deployApps方法定义了APP部署的方式，有一下三种。
>
> 1、文件夹部署：将自己的APP根目录整个放入Tomcat中的webapps目录下。
> 2、war包部署：将目录打包成war文件放入Tomcat中的webapps目录下。（Tomcat启动时会将webapps中的war包解压）
>
> 3、描述符部署：在Tomcat的conf文件夹中的server.xml文件中添加\<Context / >节点，Tomcat启动时会有对应的java程序读取XML的节点的信息，在到对应的目录下去获取APP资源。配置图如下，path属性表示虚拟跟目录，也就是浏览器中输入的目录名，docBase表示物理目录是APP源文件存在的目录。
>
> ![image-20201115111454256](image\image-20201115111454256.png)

> Q：APP中目录的作用？
>
> A：APP中最简单的实现就是只有一个WEB-INF文件夹。是APP必不可少的文件夹。一下是WEB-INF中最简单形式的目录结构。
> classes文件夹表示自己编写的java程序servlet等。（没用到则可以删除）
>
> lib文件夹，表示该项目中依赖的外部java程序。（没用到则可以删除）
>
> web.xml是用来配置servlet、filter等程序的配置文件。（没用到则可以删除）
>
> jsp、html、js等自己吧编写的前端内容。（没用到则可以删除）

> Q：Tomcat部署多个APP时是顺序部署的吗？
>
> A：不是，Tomcat是多线程部署APP。

> Q：Tomcat怎么体现出一个servlet容器的特点
>
> A：由Container类体现。

> Q：Tomcat中的Container类？
>
> A：Container类有4个主要的接口
>
> 1、Context接口：表与应用相关的接口，读取XML中的\<Context / >就是他规定的一个功能。Context中存放所有Wrapper
>
> 2、Host类：表示虚拟主机，在server.xml文件中\<Context / >节点就是写在\<host>节点下的，他定义了应用部署的方式，其中那么表示主机名，也是IP名，appBase表示该主机下对应的APP程序存放的位置。\<Value>同样是\<host>节点下的子节点。该节点表示该虚拟主机下日志存放的位置
>
> ![image-20201115113747438](image\image-20201115113747438.png)
>
> ![image-20201115115235400](image\image-20201115115235400.png)
>
> 3、Engine类：\<host>节点属于\<Engine>节点，Engine节点下可以定义多个虚拟主机，根据url的域名解析出要对应的主机，寻找该主机下对应的文件夹，这里不同的域名仅仅用于区分，实际上都是同一个物理机，只不过webapps文件夹不同。Engine还可以管理Host集群的作用
>
> ![image-20201115114426732](image\image-20201115114426732.png)
>
> ![image-20201115114306248](image\image-20201115114306248.png)
>
> 4、Wrapper类：包装，将Servlet分类，每一个List中存放一组相同的Servlet实例



> 简单理解：Engine—（包含）—>Host—（包含）—>Context—（包含）—>Wrapper—（包含）—>Servlet
>
> ![image-20201115120956447](image\image-20201115120956447.png)
>
> ![image-20201115121024908](image\image-20201115121024908.png)
>
> ![image-20201115120703775](image\image-20201115120703775.png)
>
> ![image-20201115120601129](image\image-20201115120601129.png)

> Q：Pipeline管道的作用？
>
> A：存在于每一个Engine、Host、Context、Wrapper中。其作用是可以设置一个个阀门，去过滤响应的数据，或者实现一些功能，每个管道都会有一个最后的Tomcat默认设置的阀门，用来表示将数据传递的下一个对象是谁。Engine中的管道最后一个阀门用来判断要将数据传递给后续哪一个Hose，Host的管道的最后一个阀门同理，判断传递给下一个Context是谁。其下同理。
>
> ![image-20201115122106128](image\image-20201115122106128.png)

> Q：怎么实现Pipeline
>
> A：Engine、Host、Context、Wrapper接口在Tomcat中都会有一个标准的实现类，这些类中定义了管道的实现。下面是Wrapper接口的标准实现类的构造函数，及继承信息。
>
> 其中pipeline.setBasic(swValue)语句就设置了管道的默认阀门
>
> ![image-20201115122930846](image\image-20201115122930846.png)
>
> ![image-20201115122812697](image\image-20201115122812697.png)

> Q：请求的调用过程
>
> A：主机收到网络数据包，操作系统逐层拆包将对应的应用层数据交给对应的端口应用。Tomcat收到数据并处理后生成一个Request和Response实例，经过Engine、Host、Context、Wrapper逐层传递然后交给自定义的Servlet程序，进行对应的处理。其中Wrapper并不直接调用对应Servlet的doGet()或doPost()等方法，而是调用servlet中的service()方法，该方法中会执行判断请求的类型然后调用自身对应请求的方法进行处理。
>
> ![image-20201115125205235](image\image-20201115125205235.png)
>
> 在调用FilterChain之前都是使用Request实例，在传递给FilterChain请求数据之前Wrapprer-pipeline会将Request使用request.getRequest()方法生成一个RequestFacade类型的实例，然后再交给自定义的filter和Servlet使用。
>
> ![image-20201115125842011](image\image-20201115125842011.png)
>
> ![image-20201115130003170](image\image-20201115130003170.png)

> Q：TCP协议是谁实现的，怎么实现？
>
> A：操作系统，linux中使用C应用实现
>
> 目录：
>
> ![image-20201115131628196](image\image-20201115131628196.png)
>
> 三层握手简略图：
>
> ![image-20201115131811292](image\image-20201115131811292.png)
>
> ![image-20201115131830820](image\image-20201115131830820.png)
>
> ![image-20201115131920855](image\image-20201115131920855.png)

> Q：Http协议是谁实现的？
>
> A：应用程序，TCP/IP协议栈中应用层以下的协议都是由操作系统实现，应用层以上的协议都是由运行在对应端口的应用程序实现。如Tomcat，浏览器。

> Q：客户端发送数据的过程？
>
> A：
>
> 1、浏览器收集页面参数，根据HTTP协议封装数据包。
>
> 2、将数据包交给操作系统发送数据。

> Q：应用程序怎么将数据包交给操作系统？直接调用系统实现的TCP方法？
>
> A：应用程序无法直接调用系统实现的方法，安全性限制，只能通过操作系统给定的API接口去间接的调用。这个API就是Socket。所有高级语言中都会有对应的代码去实现调用操作系统Socket接口的方法。如java中的java.net.Socket类。并且socket是用来发送TCP包的，想要发生UDP包则要使用java.net.DatagramSocket类
>
> ![image-20201115134300029](image\image-20201115134300029.png)
>
> linux中有专门的socket源码文件
>
> ![image-20201115133648092](image\image-20201115133648092.png)
>
> ![image-20201115133701078](image\image-20201115133701078.png)

> socket.connect()方法源代码可以在open JDK中查看。
>
> 在源代码后续的调用属于JNI范围，调用C语言头文件，在C语言源代码中调用操作系统层的.h文件，实现了将应用程序与操作系统连接在一起。

> Q：Tomcat怎么从操作系统中获取数据。
>
> A：BIO、NIO，Tomcat8开始只使用不使用BIO
>
> BIO：同步阻塞式IO，服务器实现模式为一个连接一个线程，即客户端有连接请求时服务器端就需要启动一个线程进行处理，如果这个连接不做任何事情会造成不必要的线程开销，当然可以通过线程池机制改善。 
> NIO：同步非阻塞式IO，服务器实现模式为一个请求一个线程，即客户端发送的连接请求都会注册到多路复用器上，多路复用器轮询到连接有I/O请求时才启动一个线程进行处理。 
> AIO(NIO.2)：异步非阻塞式IO，服务器实现模式为一个有效请求一个线程，客户端的I/O请求都是由OS先完成了再通知服务器应用去启动线程进行处理。

> Q：Tomcat处理操作系统提供的数据
>
> A：Tomcat中的Connector源代码会根据server.xml中的设置值的规范读取数据，如Connector中设置了protocol表示处理数据使用HTTP/1.1协议标准，Connector实例就会使用该协议规定的标准去生成对应的协议处理器（setProtocolHandlerClassName("org.apache.coyote.http11.Http11AprProtocol");），该处理器会使用内部设置的IO模型去读取数据，放入缓存，然后由解析函数解析数据包。
>
> ![image-20201115141351385](image\image-20201115141351385.png)
>
> ![image-20201115141826338](image\image-20201115141826338.png)
>
> ![image-20201115141801997](image\image-20201115141801997.png)
>
> 处理函数，processSocket(socket实例)，获取对应的处理器实例
>
> ![image-20201115143939314](image\image-20201115143939314.png)
>
> ![image-20201115144100151](image\image-20201115144100151.png)
>
> 内容解析，AbstractHttp11Processor.process()处理器会使用getInputBuffer()从缓存中读取数据，在通过parseRequestLine()方法解析请求行，请求头。在解析请求的步骤中是不用解析请求体的，用户所需要请求的内容都在请求头中体现。而响应时才需要将响应体按照对应的各种组合成数据包。
>
> ![image-20201115144519247](image\image-20201115144519247.png)
>
> ![image-20201115144718523](image\image-20201115144718523.png)
>
> ![image-20201115144857352](image\image-20201115144857352.png)
>
> 设置到Request实例中：
>
> ![image-20201115145734157](image\image-20201115145734157.png)
>
> ![image-20201115150358399](image\image-20201115150358399.png)

> HTTP报文格式
>
> 请求
>
> ![image-20201115143604774](image\image-20201115143604774.png)
>
> ![image-20201115143618096](image\image-20201115143618096.png)
>
> ![image-20201115143629845](image\image-20201115143629845.png)
>
> ![image-20201115143640245](image\image-20201115143640245.png)
>
> 响应
>
> ![image-20201115143748072](image\image-20201115143748072.png)
>
> ![image-20201115143755325](image\image-20201115143755325.png)

