https://blog.csdn.net/fedorafrog/article/details/104412140



使用

1. startPage()，创建Page对象，放入Threadlocal中
2. 调用SQL
3. 连接器执行，消费Threadlocal中的Page，根据对应的参数拼接分页查询语句