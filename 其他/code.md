助手客户化
	安装包描述：10558
	例外进程：N:mono.exe;N:AuditPlus.exe;N:UniFrm*.exe;N:vrv*.exe;N:Edp*.exe;N:Pcc*.exe;N:bipc.exe
	自定义配置文件：{MozartBreathCore.arc} 
		          Append.Main.PNKFL=bipc.exe:CreateProcessW|


代理软件：CCProxy.exe
远程软件：TeamViewer.exe、SunloginClient.exe

屏幕水印拓展配置
NoHideTaskbarWin=1

敏感文件
C:\Windows
C:\Program Files
C:\Program Files (x86)

打印配置
except1=154.233.5.1:8080*
except2=*154.233.25.*

系统安装
ExtendedKB

文件读写
rdpclip.exe
explorer.exe

数据表刷新
update tbl_fileclassifyconfig set uiddomainid=(select uiddomainid from tbl_infoswitchcfg);

更改一列
update 表名 set 列=‘值’

删除一条记录
DELETE from Tbl_Secpolicy WHERE uidsecpolicyid='06d6-481d2b74961024f5d61'
删除表中所有记录
DELETE from Tbl_Secpolicy


省联社一级服务器
OA：155.211.2.41
yw：154.211.27.41
端口：20099

正文字体文件放入
C:\Windows\LVUAAgentInstBaseRoot\lan