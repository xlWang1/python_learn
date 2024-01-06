# _*_ coding: UTF-8 _*_
# @Time     :2024/1/6 20:28
# @Author   :xiaolong wang
# @File     :user_command.py
command_list = {'list','add','delete','edit','exit','avg'}
def get_user_command()->str:
    while True:
        command = input(f"请输入指令(输入'exit'退出):")
        cmd = command.lower()
        if cmd in command_list:
            return cmd
        else:
            print(f"不是合法命令")
if __name__ == '__main__':
    get_user_command()