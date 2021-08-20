> ![image-20210624113435049](image/image-20210624113435049.png)

> **Iterable接口：**它是所有可迭代对象的跟接口
>
> 实现该接口的对象运行使用for-each（数组也可以用for-each）
>
> ![image-20210625095609921](image/image-20210625095609921.png)

> 顶层接口**Collection：**用来定义集合的约定

> 四大类集合接口
>
> **List：**列表，是ArrayList（数组列表）和LinkedList（链表）类的上层接口
>
> **Set：**集合该接口提供了额外的规定（与集合的特性有关）对add、equals、hashCode方法提供了额外的标准
>
> **Queue：**队列，它被设计用在处理之前保持元素访问次序，处理Collection基本操作之外提供了额外的插入、读取、检查操作。
>
> **Map：**映射（可以看作字典），是一个哈希表结构，使用key-value方式存储

> List分类下的实现类
>
> **ArrayList：**是可扩容数组（动态数组），ArrayList不是线程安全的容器，多个线程操作时会发生并发错误，内部基于数组实现，定义如下
>
> ![image-20210625101141599](image/image-20210625101141599.png)
>
> **Vector：**和ArrayList作用类似，Vector是一个线程安全容器，它对内部的每个方法都粗暴的加锁，因此Vector的内存开销和使用效率与ArrayList相比较差。其内部也是基于数组实现。（Vector和ArrayList基本可以互换）
>
> **LinkedList：**它是一个双向链表的存储结构，这个性质决定了它的所有操作都可以表示双向性，它同样不是线程安全的，需要手动加锁
>
> **Stack：**堆栈它继承了Vector，是一种线程安全的容器，提供了常用的堆栈方法，如pop和push方法，是否为空empty方法等

> 快速失败机制（fast-fail机制）
>
> ![image-20210625102236646](image/image-20210625102236646.png)

> Set分类下的实现类
>
> **HashSet：**是一类哈希表结构，实际上是HashMap的一个实例，不是线程安全型
>
> **TreeSet：**基于TreeMap的NavigableSet实现，TreeSet有一个父接口**SortedSet**，这个接口规定了内部元素的有序性，使用Comparable对元素进行自然排序，或者使用Comparator在创建时对元素提供定制的排序规则，所有TreeSet也具有这类特性。不是一个线程安全型
>
> ![image-20210806200349400](image/image-20210806200349400.png)
>
> **LinkedHashSet：**是Set接口的Hash和LinkedLisk的实现，与HashSet不同的是它维护着一个贯穿所有条目的双向链表，链表定义了元素插入集合的顺序。不是线程安全型
>
> ![image-20210625103629098](image/image-20210625103629098.png)

> Queue分类下的实现类
>
> **PriorityQueue：**优先级队列，它的元素会根据自然排序或构造函数时期提供的Comparator来排序。不允许空值。
>
> ![image-20210625103955672](image/image-20210625103955672.png)

> Map分类下的实现类
>
> **HashMap：**使用哈希原理来存储元素的集合，**允许空键值对**，它不是线程安全的，支持**fast-fail机制**，影响其性能的因素有两个，初始容量和加载因子
>
> ![image-20210806200611995](image/image-20210806200611995.png)
>
> ![image-20210806200625862](image/image-20210806200625862.png)
>
> **ConcurrentHashMap**
>
> ![image-20210806201124583](image/image-20210806201124583.png)
>
> ![image-20210806201200472](image/image-20210806201200472.png)
>
> Segment部分依然存在，在原来基础上引入红黑树
>
> ![image-20210806201209642](image/image-20210806201209642.png)
>
> **TreeMap：**是一个基于NavigableMap实现的红黑树，这个Map根据key自然排序或通过Comparator进行定制的排序
>
> ![image-20210625104532272](image/image-20210625104532272.png)
>
> **LinkedHashMap：**是哈希表和链表两种结构的实现，维护着一个贯穿所有条目的双向链表，链表定义了元素插入集合的顺序
>
> ![image-20210625104748613](image/image-20210625104748613.png)
>
> **HashTable：**与HashMap功能类似，不同的是它是线程安全的，不允许空值
>
> ![image-20210625104938645](image/image-20210625104938645.png)
>
> **IdentityHashMap：**
>
> ![image-20210625105024944](image/image-20210625105024944.png)
>
> **WeakHashMap：**
>
> ![image-20210625105117232](image/image-20210625105117232.png)

> 不属于继承框架中的类
>
> Collections类：是一个包装类。它的作用是为集合框架提供某些额外的功能。
>
> **同步包装：**为不是线程安全的集合类将其包装为线程安全，主要方法
>
> ![image-20210625105931493](image/image-20210625105931493.png)
>
> **不可修改包装：**为集合提供只读功能，不允许修改
>
> ![image-20210625110045506](image/image-20210625110045506.png)
>
> ![image-20210625110058667](image/image-20210625110058667.png)

> ![image-20210625110152945](image/image-20210625110152945.png)

> 集合特征图
>
> ![image-20210625110214838](image/image-20210625110214838.png)