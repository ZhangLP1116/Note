Linux常用命令
Vim命令：
	命令模式
	dd	删除
	yy	复制
	pp	粘贴
	u	撤销
	ZZ	保存并退出
	/word	从上至下查找word
	n	定位下一个匹配的被查找字符串
	末行模式
	：w	保存
	：w /root/newfile	另存
	：q	退出
	：q！	未保存强制退出
	：s /old/new 	将当前行中查找到的第一个字符“old” 串替换为“new”
	：s /old/new/g 	将当前行中查找到的所有字符串“old” 替换为“new”
	：#,# s/old/new/g 	:#,# s/old/new/g 
	：% s/old/new/g 	在整个文件范围内替换所有的字符串“old”为“new”
	：s /old/new/c 	在替换命令末尾加入c命令，将对每个替换动作提示用户进行确认

网络命令：
	配置静态ip地址的目录		/etc/network/interfaces
	ifup eth0	开启eth0接口
	ifdown eth0	关闭eth0接口
	service networking start	重启网络配置（用于刷新配置）# /etc/init.d/networking start（该命令效果相同）

文件系统：
	df  -hT	查看当前文件系统

进程命令：
	ps a/u/x	查看进程
	netstat -tlunp 	端口/进程查看命令
	top	查看动态进程排名信息
		按P键根据CPU占用情况对进程列表进行排序 
		按M键根据内存占用情况进行排序
		按N键根据启动时间进行排序
		按h键可以获得top程序的在线帮助信息
		按q键可以正常退出top程序
		按k结束进程（9：强制结束进程）
		按r修改优先级（NI）
		使用空格键可以强制更新进程状态显示
	kill PID	按进程ID杀死进程
	killall 名称	按进程名杀死进程
	pkill -9 -t TTY	踢出非法用户
	at	设置在某个特定的时间，执行一次任务（ctrl+D提交）
	crontab	设置按固定的周期（如每天、每周等）重复执行预先计划好的任务
进程启动：
	前台启动：	用户输入命令，直接执行程序
	后台启动：	在命令行尾加入“&”符号	如：cp /dev/cdrom mycd.iso &
	（前台进程就是用户使用的有控制终端的进程，后台进程一般用作系统服务）

用户命令：
	user/w/who	查询已登录到系统的用户

混合命令
	w | grep -v root	从已登录的用户中查询root
文件操作命令
	cp 源文件 目标目录	复制文件（复制目录是要选择参数‘-a’）
	mkdir	创建文件夹
	rouch 	创建文件
	rm	删除文件	-d 删除目录、-r 递归地删除指定目录及其下属的各级子目录、相应的文件
	rmdir	删除目录	-p递归式删除
文件大小查看
	ls -ll	查看文件夹中各个文件的大小
	du -h –max-depth=1 目录	可以查看当前目录下各文件、文件夹的大小
	du -sh	查看文件夹大小
	du -h –max-depth=1 目录	可以只显示直接子目录文件及文件夹大小统计值。