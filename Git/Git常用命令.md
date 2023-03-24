### 基本操作

- git add .：跟踪或添加修改
- git commit -m ""：提交

### 远程仓库操作

- git remote add myfork <url>：添加远程仓库
- git fetch orgin：拉取远程仓库
- git clone url：克隆远程仓库
- git remote：查看所有远程仓库
- **git remote show name：查看远程仓库详细信息**
- git remote rename：重命名远程仓库

### 分支操作

- git branch name：创建分支
- git checkout branchName：切换到分支
- git checkout -b <newbranchname>：创建并切换到分支
- git checkout -b serverfix origin/serverfix：在origin/serverfix分支上创建分支
- **git push orgin branchName：推送分支到远程仓库**
- **git merge origin/master：合并远程分支，更新远程分支指针**
- git merge --abort：选项会尝试恢复到你运行合并前的状态
- git branch -v：查看每个分支最后的提交
- git branch --no-merged：未合并到当前分支的分支
- git branch --merged：已经合并到当前分支的分支
- git branch --no-merged master：未合并到master分支的分支
- git ls-remote <remote>：查看远程分支指向的对象
- git branch -vv：显示出本地分支跟踪的远程分支，并提示本地分支是否是领先、落后或是都有。
- git push origin --delete serverfix：删除远程仓库上的分支

### 变基操作

- git rebase master：将当前分支变基到master分支中
- git rebase --onto master server client：跨分支变基，将server分支中的client分支变基到master中
-  git push -f orgin featureA：推送变基后的分支到远程仓库

### cherry-pick

选择一个提交到指定分支，可以用于将一个提交应用到多个分支

```
    a - b - c - d - e    Master
         \
           f - g - h - i Feature
```

现在我们需要将提交 h 合并到 `master` 分支上，用了 cherry-pick 就是如下的模型

```
    a - b - c - d - e - h Master
         \
           f - g - h - i  Feature
```

#### git cherry-pick \<commitHash>

- commitHash：表示每次提交的hash值
- 将指定提交在`当前`分支上重新提交，会生成一个新的提交Hash值

```
git cherry-pick d476dc4
```

#### git cherry-pick \<branchId>

- branchId：表示分支名
- 作用：将指定分支的最新提交在当前分支上重新提交

```
git cherry-pick feature/dev-1.0.2
```

#### git cherry-pick \<HashA> \<HashB>

- HashA：表示提交的hash值
- 作用：将 A 和 B 两个提交应用到`当前`分支，这会在当前分支生成两个对应的新提交。

```
git cherry-pick 92835bef12d6975992ef026bc3f786c54134abe8 92fa72277c90017143c05169c879839533e48a9d
```

#### git cherry-picl \<HashA> … \<HashD>

- HashA：表示提交的hash值

- 作用：将一系列提交转移到该分支，必须按照正确的顺序放置：提交 A 必须早于提交 B，否则命令将失败，但不会报错。

- 注意：该这是一个左开右闭的操作 <HashA> 不会被转移到当前分支

- 如果要包含提交 A，可以使用该语法：git cherry-pick <HashA>^…<HashD>

- 如果想让每个commit 暂缓提交，等到所有commit都拣选完成后，自己手动commit，则添加 -n 选项

```
git cherry-pick 8607f6102c8087be496ff0175d1790f83808c27c..92fa72277c90017143c05169c879839533e48a9d //左开右闭

git cherry-pick 8607f6102c8087be496ff0175d1790f83808c27c^..92fa72277c90017143c05169c879839533e48a9d //左闭右闭

git cherry-pick -n 8607f6102c8087be496ff0175d1790f83808c27c^..92fa72277c90017143c05169c879839533e48a9d
```

#### cherry-pick 时代码冲突
- --continue，用户解决代码冲突后，将修改的文件重新加入暂存区，（git add .）
    用 git cherry-pick --continue 命令，让 Cherry pick 过程继续执行。

    ```
    git cherry-pick --continue
    ```

- --abort，发生代码冲突后，放弃合并，回到操作前的样子。

    ```
    git cherry-pick --abort
    ```

- --quit，发生代码冲突后，退出 Cherry pick，但是不回到操作前的样子。

    ```
    git cherry-pick --quit
    ```


### git stash

作用：将当前工作状态暂存

> 注：1.在未`add`之前才能执行`stash` 2.新增的文件，直接执行stash是不会被存储的

-  **git stash** save "save message" : 执行存储时，添加备注，方便查找，只有git stash 也可以，但查找时不方便识别。
-  **git push**：截至 2017 年 10 月下旬，Git 邮件列表上进行了广泛讨论，该讨论中弃用了 `git stash save` 命令， 代之以现有 `git stash push` 命令。主因是 `git stash push` 引入了贮藏选定的 **路径规范** 的选项， 而有些东西 `git stash save` 不支持。
- *git stash list* 查看所有被隐藏的文件列表
- **git stash apply** :应用某个存储,但不会把存储从存储列表中删除，默认使用第一个存储,即stash@{0}，如果要使用其他个，git stash apply stash@{$num} ， 比如第二个：git stash apply stash@{1} 
- **git stash pop** ：命令恢复之前缓存的工作目录，将缓存堆栈中的对应stash删除，并将对应修改应用到当前的工作目录下,默认为第一个stash,即stash@{0}，如果要应用并删除其他stash，命令：git stash pop stash@{$num} ，比如应用并删除第二个：git stash pop stash@{1}
- **git stash drop** stash@{$num} ：丢弃stash@{$num}存储，从列表中删除这个存储
- **git stash clear **：删除所有缓存的stash

### 查看历史操作

- git log：查看历史
- git log --pretty=oneline：查看简化的历史信息

- **git log --oneline --decorate --graph --all：查看分支历史**
- git log --oneline --decorate：查看各个分支指向的对象





### 查看不同分支提交的区别

![image-20230109135734880](C:\Users\ZLP\AppData\Roaming\Typora\typora-user-images\image-20230109135734880.png)

#### 双点

```shell
$ git log master..experiment
```

查看在 experiment 分支中而不在 master 分支中的提交

```shell
$ git log origin/master..HEAD
```

查看在本地未在远端分支的提交



#### 三点

```SHELL
$ git log master...experiment
```

选择出被两个分支 **之一** 包含但又不被两者同时包含的提交



### Git搜索内容

```shell
# -n 打印内容所在行号
$ git grep -n gmtime_r
```

![image-20230109151521453](C:\Users\ZLP\AppData\Roaming\Typora\typora-user-images\image-20230109151521453.png)



### 重写历史

#### 修改最后一次提交

#### 修改多个提交

#### 重新排序提交

#### 压缩提交

#### 拆分提交

#### filter-branch

https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E9%87%8D%E5%86%99%E5%8E%86%E5%8F%B2



### 重写提交

#### 回退

```SHELL
$ git reset 9e5e6a4 --hard
```

撤销提交到指定位置

#### 引用某次提交的内容

```shell
# 是改命令的简写git reset --mixed HEAD file.txt
# 从当前Head所在的提交获取内容更新到暂存区
$ git reset file.txt

# 从指定提交获取内容更新到当前暂存区
$ git reset eb43bf file.txt
```



https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E9%87%8D%E7%BD%AE%E6%8F%AD%E5%AF%86



### Reset与checkout的区别

![image-20230109160827223](C:\Users\ZLP\AppData\Roaming\Typora\typora-user-images\image-20230109160827223.png)

### 还原提交

```shell
# 撤销指定提交，不会修改原有的提交历史，reset操作会删除旧提交历史
$ git revert -m 1 HEAD
```

`-m 1` 标记指出 “mainline” 需要被保留下来的父结点。 当你引入一个合并到 `HEAD`（`git merge topic`），新提交有两个父结点：第一个是 `HEAD`（`C6`），第二个是将要合并入分支的最新提交（`C4`）。 在本例中，我们想要撤消所有由父结点 #2（`C4`）合并引入的修改，同时保留从父结点 #1（`C6`）开始的所有内容。

![image-20230109163951829](C:\Users\ZLP\AppData\Roaming\Typora\typora-user-images\image-20230109163951829.png)

> 新的提交 `^M` 与 `C6` 有完全一样的内容，所以从这儿开始就像合并从未发生过，==除了“现在还没合并”的提交依然在 `HEAD` 的历史中==。 如果你尝试再次合并 `topic` 到 `master` Git 会感到困惑：
>
> ```shell
> $ git merge topic
> Already up-to-date.
> ```
>
> `topic` 中并没有东西不能从 `master` 中追踪到达。 更糟的是，如果你在 `topic` 中增加工作然后再次合并，Git 只会引入被还原的合并 *之后* 的修改。
>
> ![image-20230109164200052](C:\Users\ZLP\AppData\Roaming\Typora\typora-user-images\image-20230109164200052.png)

解决这个最好的方式是撤消还原原始的合并，因为现在你想要引入被还原出去的修改，**然后** 创建一个新的合并提交：

```shell
$ git revert ^M
[master 09f0126] Revert "Revert "Merge branch 'topic'""
$ git merge topic
```

![image-20230109164250726](C:\Users\ZLP\AppData\Roaming\Typora\typora-user-images\image-20230109164250726.png)

在本例中，`M` 与 `^M` 抵消了。 `^^M` 事实上合并入了 `C3` 与 `C4` 的修改，`C8` 合并了 `C7` 的修改，所以现在 `topic` 已经完全被合并了。



### 文件标注

```SHELL
$ git blame Makefile
```

展示文件中每一行的代码修改时间，提交人，提交 SHA-1 值



### 子模块

子模块允许你将一个 Git 仓库作为另一个 Git 仓库的子目录。 它能让你将另一个仓库克隆到自己的项目中，同时还保持提交的独立。

https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E5%AD%90%E6%A8%A1%E5%9D%97

- 添加子模块

  ```shell
  # 当前项目会添加两个新文件，.gitmodules、DbConnector
  $ git submodule add https://github.com/chaconinc/DbConnector
  ```

- 克隆含有子模块的项目

  ```shell
  # 拉取主项目
  $ git clone https://github.com/chaconinc/MainProject
  # 初始化子模块仓库
  $ git submodule init
  # 拉取子模块
  $ git submodule update
  
  # --recurse-submodules会自动初始化并拉取子模块
  $ git clone --recurse-submodules https://github.com/chaconinc/MainProject
  ```



### 打包

`bundle` 命令会将 `git push` 命令所传输的所有内容打包成一个二进制文件， 你可以将这个文件通过邮件或者闪存传给其他人，然后解包到其他的仓库中。

```shell
# 打包，整个仓库打包
$ git bundle create repo.bundle HEAD master

# 只打包指定提交，将 9a466c5之后的提交打包
$ git log --oneline
71b84da last commit - second repo
c99cf5b fourth commit - second repo
7011d3d third commit - second repo
9a466c5 second commit
b1ec324 first commit

$ git bundle create commits.bundle master ^9a466c5
```

然后你就会有一个名为 `repo.bundle` 的文件，该文件包含了所有重建该仓库 `master` 分支所需的数据。 在使用 `bundle` 命令时，你需要列出所有你希望打包的引用或者提交的区间。 如果你希望这个仓库可以在别处被克隆，你应该像例子中那样增加一个 HEAD 引用。

```shell
# 解包
$ git clone repo.bundle repo
```

如果你在打包时没有包含 HEAD 引用，你还需要在命令后指定一个 `-b master` 或者其他被引入的分支， 否则 Git 不知道应该检出哪一个分支。

验证部分提交包

当她拿到这个包时，她可以在导入到仓库之前查看这个包里包含了什么内容。 `bundle verify` 命令可以检查这个文件是否是一个合法的 Git 包，是否拥有共同的祖先来导入。

```shell
$ git bundle verify ../commits.bundle
```



