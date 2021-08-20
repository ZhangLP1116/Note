> 介绍：Git是一个版本控制软件，可以对项目文件进行快照，以便故障时能够恢复到上一个版本

> windows中可以到https://msysgit.io，下载
>
> Linux中可以使用：sudo apt-get install git命令安装

> 1、配置Git，在配置中的全局变量上写入是谁在使用Git
>
> ```
> git config --global user.name "username"
> git config --global user.email "username@example.com"
> ```
>
> 2、创建忽略文件
>
> ```
> .gitignore文件中保存Git不跟踪的文件，在Git拍摄文件快照时会自动忽略这些文件
> ```
>
> 3、初始化仓库
>
> ```
> 在对应的项目根目录下初始化一个Git仓库，里面保存有项目的所有历史快照记录，是一个./git文件夹
> 初始化命令：git init
> ```
>
> 4、查看状态
>
> ```
> 命令：git status
> 将会显示当前分支，跟踪文件，未跟踪文件，发生了修改的文件
> 若输出working directory clean则表示当前工作目录是干净的不存在未提交的文件这是最希望看到的信息
> ```
>
> 5、将文件加入仓库
>
> ```
> 命令：git add .
> 将项目中未被跟踪的文件都加入到仓库中，可以使得Git知道这些文件是否被修改
> 它不提交这些文件，只是让Git开始关注他们
> ```
>
> 6、执行提交
>
> ```
> 命令：git commit -m "Started project."
> git commit是提交命令，-m为提交参数，表示这次提交的信息为"Started project."
> 每次提交都是一次快照
> 
> 命令：git commit -am “xxxx”
> 这条命令中-a表示将所有被修改的文件都提交
> ```
>
> 7、查看历史提交记录
>
> ```
> 命令：git log
> 该命令可以查看所有的提交，以及每次的提交人，提交时间，可以追加参数“--pretty=oneline”使的只输出提交ID和提交信息
> ```
>
> 8、恢复到最近一次提交
>
> ```
> 命令：git checkout .
> 该命令将放弃最后一次提交后所做的所有修改，恢复到上一次提交的状态
> ```
>
> 9、恢复到某次提交
>
> ```
> 命令：git checkout id
> 该命令将当前项目指定恢复到特点一次提交时的状态，id为那次提交的id的前6位，id可以由查看历史命令查看
> ```
>
> 

