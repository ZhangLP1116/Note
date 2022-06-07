### 一、队列持久化

持久化队列（Durable queues）会被存储在磁盘上，当消息代理（broker）重启的时候，它依旧存在。没有被持久化的队列称作暂存队列（Transient queues）。

持久化的队列并`不会使得路由到它的消息也具有持久性`。倘若消息代理挂掉了，重新启动，那么在重启的过程中持久化队列会被重新声明，无论怎样，只有经过持久化的消息才能被重新恢复。

```java
// 第二个参数控制创建的是否为持久化队列
channel.queueDeclare(QUEUE_NAME,true,false,false,null);
```



### 二、消息持久化

将消息标记为持久化并不能完全保证不会丢失消息。尽管它告诉 RabbitMQ 将消息保存到磁盘，但是 这里依然存在当消息刚准备存储在磁盘的时候 但是还没有存储完，消息还在缓存的一个间隔点。此时并没 有真正写入磁盘。



```java
// 消息持久化由MessageProperties.PERSISTENT_TEXT_PLAIN消息属性控制
channel.basicPublish("",QUEUE_NAME, MessageProperties.PERSISTENT_TEXT_PLAIN,sc.next().getBytes());
```



