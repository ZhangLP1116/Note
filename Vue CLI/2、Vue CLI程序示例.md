### Vue CLI构建Vue程序

#### 1、创建一个webpack打包的项目

1. 进入项目放置目录

   ```
   cd C:\Users\zhang\Desktop\Project\Vue\vue-cli
   ```

2. 执行项目构建命令，构建基于webpack打包工具的项目

   ```
   vue init webpack firstvue-cli
   ```

   ![image-20210924171255410](image/image-20210924171255410.png)

   拒绝自动安装依赖

3. 项目结构
   ![image-20210924171433649](image/image-20210924171433649.png)
   ![image-20210924171457607](image/image-20210924171457607.png)

#### 2、使用npm安装项目依赖

项目的依赖信息都放在package.json文件中

![image-20210924171616592](image/image-20210924171616592.png)

进入项目目录，执行npm insatll命令，安装依赖模块

```
cd firstvue-cli
npm install // 该命令会自动读取package.json文件的信息，安装对应依赖
```

安装依赖后的目录结构

![image-20210924172039442](image/image-20210924172039442.png)

安装的依赖都存放在node_modules目录下

![image-20210924172140679](image/image-20210924172140679.png)

#### 3、启动项目

1. 当前目录下执行npm run dev，启动开发环境
2. 浏览器访问http://localhost:8080/，进入首页
   ![image-20210924172410208](image/image-20210924172410208.png)

#### 4、项目目录解析

build文件夹：存放项目构建文件

![image-20210924172707986](image/image-20210924172707986.png)

webpack.base.conf.js：基础环境搭建

webpack.dev.conf.js：开发环境搭建

webpack.prod.conf.js：生产环境搭建



config文件夹：存放项目配置文件

![image-20210924172935467](image/image-20210924172935467.png)



node_modules文件夹：存放依赖



src文件夹：存放源码

![image-20210924174814264](image/image-20210924174814264.png)



static文件夹：存放静态资源



#### 5、项目入口页面

入口页面：index.html

![image-20210924174937174](image/image-20210924174937174.png)

入口页面的js文件：main.js，将Vue实例挂载到DOM

![image-20210924175028372](image/image-20210924175028372.png)

App.vue：index.html的主要内容，这里引用了组件HelloWorld.vue

![image-20210924175215516](image/image-20210924175215516.png)

HelloWorld.vue：修改该组件内容为

![image-20210924175325612](image/image-20210924175325612.png)

效果

![image-20210924175341253](image/image-20210924175341253.png)