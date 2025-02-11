## Objects目录

> Git数据对象、树对象、提交对象
>
> 工作区（Working Directory）、暂存区（Index）、提交区（HEAD）

Git 是一个内容寻址文件系统，将文件的内容作为参数生成一个SHA-1的值，核心部分是一个简单的键值对数据库（key-value data store），可以高效根据key的从数据库中获取对应的内容。

### 将内容存入数据库

执行`$ git init test`命令后会在`.git`目录下创建一个objects文件夹（即 **对象数据库**）

```shell
# 从标准输入获取数据保存到数据库中
$ echo 'test content' | git hash-object -w --stdin
d670460b4b4aece5915caf5c68d12f560a9fe3e4

# 从文件中获取数据保存到数据库中
$ git hash-object -w test.txt
```

该命令会在`.git`目录生成如下文件

```
# SHA-1 值的前两位将作为目录名，剩下的作为文件名
.git/objects/d6/70460b4b4aece5915caf5c68d12f560a9fe3e4
```

在这种最简单的形式中，`git hash-object` 会接受你传给它的东西，而它只会返回可以存储在 Git 仓库中的唯一键。 `-w` 选项会指示该命令不要只返回键，还要将该对象写入数据库中。 最后，`--stdin` 选项则指示该命令从标准输入读取内容；若不指定此选项，则须在命令尾部给出待存储文件的路径。

此命令输出一个长度为 40 个字符的校验和。 这是一个 SHA-1 哈希值——一个将==待存储的数据==外加一个==头部信息（header）==一起做 SHA-1 校验运算而得的校验和。



### 从数据库中提取内容

```shell
#  -p 选项可指示该命令自动判断内容的类型，并输出显示，结果输出到标准输出中
$ git cat-file -p d670460b4b4aece5915caf5c68d12f560a9fe3e4
test content

# 将内容结果输出到指定文件，相当于取回历史文件的操作
$ git cat-file -p 83baae61804e65cc73a7201a7252750c76066a30 > test.txt

# -t输出文件类型
$ git cat-file -t d8329fc1cc938780ffdd9f94e0d364e0ea74f579
tree
```



## Refs目录

> 引用对象，用一个友好名称来替代SHA-1来作为上层操作对象，对外体现为分支的效果

### 引用的创建和修改

```shell
# 创建master引用指向cac0ca对象
$ git update-ref refs/heads/master cac0ca

# 修改master引用指向1a410e对象
$ git update-ref refs/heads/master 1a410efbd13591db07496601ebc7a059dd55cfe9
```

当运行类似于 `git branch <branch>` 这样的命令时，Git 实际上会运行 `update-ref` 命令， 取得当前所在分支最新提交对应的 SHA-1 值，并将其加入你想要创建的任何新引用中。

### Head引用

现在的问题是，当你执行 `git branch <branch>` 时，Git 如何知道最新提交的 SHA-1 值呢？ 答案是 HEAD 文件。HEAD 文件通常是一个符号引用（symbolic reference），指向目前所在的分支。 所谓符号引用，表示它是一个指向其他引用的指针。

```shell
$ cat .git/HEAD
ref: refs/heads/master

$ git symbolic-ref HEAD
refs/heads/master

# 修改head指向的引用
$ git symbolic-ref HEAD refs/heads/test
$ cat .git/HEAD
ref: refs/heads/test
```

### Tags目录

前面我们刚讨论过 Git 的三种主要的对象类型（**数据对象**、**树对象** 和 **提交对象** ），然而实际上还有第四种。 **标签对象（tag object）** 非常类似于一个提交对象——它包含一个标签创建者信息、一个日期、一段注释信息，以及一个指针。 主要的区别在于，标签对象通常指向一个提交对象，而不是一个树对象。 ==它像是一个永不移动的分支引用==——永远指向同一个提交对象，只不过给这个提交对象加上一个更友好的名字罢了。

```shell
# 创建一个标签，这就是轻量标签的全部内容——一个固定的引用。
$ git update-ref refs/tags/v1.0 cac0cab538b970a37ea1e769cbbde608743bc96d

```

若要创建一个附注标签，Git 会创建一个标签对象，并记录一个引用来指向该标签对象，而不是直接指向提交对象。 可以通过创建一个附注标签来验证这个过程（使用 `-a` 选项）：

```shell
$ git tag -a v1.1 1a410efbd13591db07496601ebc7a059dd55cfe9 -m 'test tag'

$ cat .git/refs/tags/v1.1
9585191f37f7b0fb9444f35a9bf50de191beadc2
```

