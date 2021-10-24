### 简介

⦁	Redis是一个开源的key-value存储系统。
⦁	和Memcached类似，它支持存储的value类型相对更多，包括string(字符串)、list(链表)、set(集合)、zset(sorted set --有序集合)和hash（哈希类型）。
⦁	这些数据类型都支持push/pop、add/remove及取交集并集和差集及更丰富的操作，而且这些操作都是原子性的。
⦁	在此基础上，Redis支持各种不同方式的排序。
⦁	与memcached一样，为了保证效率，数据都是缓存在内存中。
⦁	区别的是Redis会周期性的把更新的数据写入磁盘或者把修改操作写入追加的记录文件。
⦁	并且在此基础上实现了master-slave(主从)同步。



Linux下后台启动redis：修改配置文件，将daemonize no修改为yes



默认端口号：6379



默认数据库有16个，默认使用0号数据库，通过select 命令可以修改使用的数据库

```shell
// 选中1号数据库
select 1
```



底层使用单线程+多路IO复用