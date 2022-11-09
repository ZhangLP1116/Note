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
- $ git branch -v：查看每个分支最后的提交
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
- *git stash list* 查看所有被隐藏的文件列表
- **git stash apply** :应用某个存储,但不会把存储从存储列表中删除，默认使用第一个存储,即stash@{0}，如果要使用其他个，git stash apply stash@{$num} ， 比如第二个：git stash apply stash@{1} 
- `git stash pop` ：命令恢复之前缓存的工作目录，将缓存堆栈中的对应stash删除，并将对应修改应用到当前的工作目录下,默认为第一个stash,即stash@{0}，如果要应用并删除其他stash，命令：git stash pop stash@{$num} ，比如应用并删除第二个：git stash pop stash@{1}
- **git stash drop** stash@{$num} ：丢弃stash@{$num}存储，从列表中删除这个存储
- `git stash clear ：`删除所有缓存的stash

### 查看历史操作

- git log：查看历史
- git log --pretty=oneline：查看简化的历史信息

- **git log --oneline --decorate --graph --all：查看分支历史**
- git log --oneline --decorate：查看各个分支指向的对象

