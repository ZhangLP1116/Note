文件完整性校验 
	certutil -hashfile D:\1.exe MD5
	certutil -hashfile D:\1.exe SHA1
	certutil -hashfile D:\1.exe SHA256



删除文件夹：rd

删除文件：del 路径

移动文件：move	源文件	目标路径，一次只能移动一个文件无法使用通配符批量移动

文件复制：copy	源文件	目标路径，可以使用通配符批量复制多个文件



网络命令

ipconfig /renew 接口（可以使用通配符）：更新IPv4地址

ipconfig /release 接口（可以使用通配符）：释放IPv4地址

ipconfig /registerdns：刷新所有DHCP租用并重新注册DNS名称（需要管理员权限）

（可以用/release+/registerdns更换路由器DHCP分配的IP地址）

ipconfig /flushdns 清除 DNS 解析程序缓存

route print -4：打印IPv4路由表