### 容器数据卷

作用：容器数据持久化，将容器中的数据保存在本地机器中。通过数据卷可以实现容器间数据共享。数据卷和容器之间的数据流是双向的，数据卷不仅仅被写入也可以被读取



实现方式：将容器中的目录挂载到本地机器上



示例

方式一

```shell
docker run -it -v 主机目录:容器内目录
```

主机home目录

```shell
[root@VM-16-16-centos ~]# ls /home/
lighthouse
```

执行命令

```shell
[root@VM-16-16-centos ~]# docker run -it -v /home/test:/home centos /bin/bash
```

容器中的home目录

```shell
[root@e191134fbb71 /]# ls /home
[root@e191134fbb71 /]# 
```

查看容器挂载信息

![image-20211230154719160](image/image-20211230154719160.png)

在容器中创建test.txt文件

```shell
[root@e191134fbb71 /]# touch /home/test.txt
[root@e191134fbb71 /]# ls /home
test.txt
```

在主机上查看

```shell
[root@VM-16-16-centos ~]# ls /home
lighthouse  test
[root@VM-16-16-centos ~]# ls /home/test/
test.txt
[root@VM-16-16-centos ~]# 
```

在主机上创建test2.txt文件

```shell
[root@VM-16-16-centos ~]# touch /home/test/test2.txt
[root@VM-16-16-centos ~]# ls /home/test/
test2.txt  test.txt
[root@VM-16-16-centos ~]# 
```

在容器中查看

```shell
[root@e191134fbb71 /]# ls /home
test.txt  test2.txt
```

