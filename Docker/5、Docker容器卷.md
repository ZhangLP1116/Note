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



### 匿名挂载、具名挂载

```shell
# 匿名挂载
docker run -d -P --name nginx01 -v /etc/nginx nginx

# 使用docker volume指令查看容器卷信息
[root@localhost ~]# docker volume ls
DRIVER    VOLUME NAME
local     f55c64422dc00887405612cb0332d203c71b3fb3108fd67d9ea832d252105bc3


# 具名挂载
docker run -d -P --name nginx02 -v test-nginx:/etc/nginx nginx

[root@localhost ~]# docker volume ls
DRIVER    VOLUME NAME
local     f55c64422dc00887405612cb0332d203c71b3fb3108fd67d9ea832d252105bc3
local     test-nginx

# 路径挂载
docker run -d -P --name nginx03 -v /mnt/docker/nginx:/etc/nginx nginx

[root@localhost mnt]# docker volume ls
DRIVER    VOLUME NAME
local     f55c64422dc00887405612cb0332d203c71b3fb3108fd67d9ea832d252105bc3
local     test-nginx
```

查看具名挂载和匿名挂载信息

```shell
# docker volume inspect 容器卷名，指令查看指定容器卷信息

# 匿名挂载信息
docker volume inspect f55c64422dc00887405612cb0332d203c71b3fb3108fd67d9ea832d252105bc3 
[
    {
        "CreatedAt": "2022-01-06T00:36:01-05:00",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/f55c64422dc00887405612cb0332d203c71b3fb3108fd67d9ea832d252105bc3/_data",
        "Name": "f55c64422dc00887405612cb0332d203c71b3fb3108fd67d9ea832d252105bc3",
        "Options": null,
        "Scope": "local"
    }
]

#具名挂载选项
docker volume inspect test-nginx 
[
    {
        "CreatedAt": "2022-01-06T00:39:54-05:00",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/test-nginx/_data",
        "Name": "test-nginx",
        "Options": null,
        "Scope": "local"
    }
]

```

具名挂载和匿名挂载都默认挂载在`/var/lib/docker/volumes`路径下

具名挂载和匿名挂载由docker容器卷管理、路径挂载用户自行管理

> 扩展容器读写容器卷权限的挂载
>
> docker run -d -P --name nginx03 -v /mnt/docker/nginx:/etc/nginx:ro nginx
>
> ro：表示readonly，容器只读容器卷
>
> docker run -d -P --name nginx03 -v /mnt/docker/nginx:/etc/nginx:rw nginx
>
> rw：表示readwrite，容器跨域读写容器卷



### 多容器共享容器卷

指令：volumes-from，共享指定容器的容器卷

```shell
docker run -d -P --name nginx01 -v test:/etc/nginx nginx

docker run -d -P --name nginx02 --volumes-from nginx01 nginx

docker run -d -P --name nginx03 --volumes-from nginx01 nginx
```

```shell
# 在nginx01中创建test.txt文件
touch test.txt
ls

conf.d	fastcgi_params	mime.types  modules  nginx.conf  scgi_params  test.txt	uwsgi_params


# 在nginx02中访问
docker exec -it nginx02 /bin/bash
cd /etc/nginx/
ls
conf.d	fastcgi_params	mime.types  modules  nginx.conf  scgi_params  test.txt	uwsgi_params

# 在nginx03中访问
docker exec -it nginx03 /bin/bash
cd /etc/nginx/
ls
conf.d	fastcgi_params	mime.types  modules  nginx.conf  scgi_params  test.txt	uwsgi_params
```

