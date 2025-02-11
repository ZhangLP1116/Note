import os
import winreg
import subprocess


if __name__ == '__main__':
    work_path = 'F:\\Games\\miHoYo Launcher\\games\\Genshin Impact Game'
    exe_path = 'F:\\Games\\miHoYo Launcher\\games\\Genshin Impact Game\\YuanShen.exe'
    config_path = 'F:\\Games\\miHoYo Launcher\\games\\Genshin Impact Game'
    plug_path = 'F:\\Games\\miHoYo Launcher\\games\\Genshin Impact Game\\YuanShen_Data\\Plugins'

    config = r'E:\yuan\b\config.ini'
    plug = r'E:\yuan\b\PCGameSDK.dll'
    g_reg_path = r'E:\yuan\g\g01.reg'
    b_reg_path = r'E:\yuan\b\b01.reg'

    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\zlp", 0, winreg.KEY_ALL_ACCESS)
    value, key_type = winreg.QueryValueEx(key, "miHoYo")
    if value == "g":
        print("当前为g服，进行替换操作")
        os.system(r'del "%s\\config.ini"' % config_path)
        os.system(r'del "%s\\PCGameSDK.dll"' % plug_path)
        os.system(r'copy %s "%s"' % (config, config_path))
        os.system(r'copy %s "%s"' % (plug, plug_path))
        # 导出官服注册表项
        os.system(r'del "%s"' % g_reg_path)
        os.system(r'REG  EXPORT HKEY_CURRENT_USER\SOFTWARE\miHoYo\原神  %s' % g_reg_path)
        # 导入B服注册表项
        os.system(r'REG IMPORT  %s' % b_reg_path)
        winreg.SetValueEx(key, "miHoYo", 0, key_type, "b")
        print("操作完成")
    else:
        print("当前注册表已经为B服，不需要替换操作")
    os.chdir(work_path)
    os.startfile(exe_path)
    # subprocess.run(exe_path)

    # input("输入任意键结束")
