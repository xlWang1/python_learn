"""
编写一个基于命令行交互的软件，能够增加，修改，查看学生的成绩，以及能打印出学科平均分，并能保存在csv文件中
"""
from student_manager.command.user_command import get_user_command
from student_manager.command.command_processor import process_command
from csv_store.csv_store import load_data
from csv_store.csv_store import save_data
def main():

    try:
        studentdata = load_data()
    except Exception as e:
        print(e)
        return

    while True:
        command = get_user_command()
        if command == "exit":
            break
        process_command(command,studentdata)
    try:
        save_data(studentdata)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()