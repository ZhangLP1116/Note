基本操作

- git add .：跟踪或添加修改
- git commit -m ""：提交

远程仓库操作

- git remote add myfork <url>：添加远程仓库
- git fetch orgin：拉取远程仓库
- git clone url：克隆远程仓库
- git remote：查看所有远程仓库
- **git remote show name：查看远程仓库详细信息**
- git remote rename：重命名远程仓库

分支操作

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

变基操作

- git rebase master：将当前分支变基到master分支中
- git rebase --onto master server client：跨分支变基，将server分支中的client分支变基到master中
-  git push -f orgin featureA：推送变基后的分支到远程仓库

查看历史操作

- git log：查看历史
- git log --pretty=oneline：查看简化的历史信息

- **git log --oneline --decorate --graph --all：查看分支历史**
- git log --oneline --decorate：查看各个分支指向的对象

