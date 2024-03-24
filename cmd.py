import os
import random

def main():
    print("欢迎使用命令行开发版界面！")

    else:
        os.system("taskkill /im py.exe /F")

    while True:
        command = input("请输入命令（输入 'help' 获取帮助）：")

        if command == 'help':
            print("可用命令:")
            print("  help - 显示帮助信息")
            print("  greet - 打招呼")
            print("  quit - 退出程序")
            print("  system - 运行系统命令")
            print("  cmd - 运行cmd")
            print("  java - 运行ATLauncher")
            print("  shutdown - 关机")
            print("  web - Oryun官网")
            print("  Mypy - 小游戏列表")
            print("  smc - 打开MC")
        elif command == 'greet':
            name = input("请输入你的名字：")
            print("你好，" + name + "!")
        elif command == 'quit':
            print("谢谢使用，再见！")
            break
        elif command == 'system':
            system = input("请输入系统命令:")
            os.system(system)
        elif command == 'cmd':
            os.system("start cmd")
        elif command == 'download':
            soc=(input("download URL:"))
            os.system(powershell)
            os.system("$client = new-object System.Net.WebClinet")
            os.system("$client.DownloadFile(soc)")
        elif command == 'java':
            print("请将jar放在D:\Mc\server.jar")
            os.system("java -jar C:\Mc\ATLauncher.jar")
        elif command == 'shutdown':
            os.system("shutdown /p")
        elif command == 'web':
            os.system("start https://oryun1001.github.io")
        elif command == 'smc':
            print("请将MC放置D:")
            print("正在启动中")
            os.system("start D:\MC\LatestLaunch.bat")

        else:
            print("无效的命令，请输入 'help' 查看可用命令。")


if __name__ == "__main__":
    main()

