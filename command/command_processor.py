# _*_ coding: UTF-8 _*_
# @Time     :2024/1/6 20:42
# @Author   :xiaolong wang
# @File     :command_processor.py
def process_list(studentdata):
    records = list(studentdata.values())
    records.sort(key=lambda a:a.get("name"))
    for record in records:
        print(record.get("name"))
        print(f"chinese:",record.get("chinese"))
        print(f"math:",record.get("math"))
        print(f"english:",record.get("english"))
        print(' ')

def process_add(studentdata):
    studen_name = input(f"请输入学生姓名:")
    math_score = int(input(f"请输入mathscore:"))
    chinese_score = int(input(f"请输入chinesescore:"))
    english_score = int(input(f"请输入englishscore:"))
    record = {
                    "name":studen_name,
                    "chinese":chinese_score,
                    "math":math_score,
                    "english":english_score
                }
    studentdata["name"] = record
    print(studentdata)
    print(f"添加学生{studen_name}成绩完成")


def process_delete(studentdata:dict):
    delete_student = input(f"请输入要删除的学生的姓名:")
    if delete_student in studentdata:
        studentdata.pop(delete_student)
        print(f"删除{delete_student}的成绩完成")
def process_edit(studentdata:dict):
    edit_list = {"name",'math','chinese','english'}
    while True:
        edit_student = input(f"请选择你要进行修改的学生的姓名：")
        if edit_student in studentdata.keys():
            edit_type = input(f"请输入你要更改的类型:")
            if edit_type in edit_list:
                temp = studentdata[edit_student]
                edit_info = input(f"请输入你要修改后的信息:")
                studentdata.pop(edit_student)
                temp[edit_type] = edit_info
                studentdata[temp["name"]] = temp
                print(f"{edit_student}信息修改完毕!")
                break
            else:
                print(f"请选择指定类型")
        else:
            print(f"查无此人")
def process_command(cmd,studentdata):
    if cmd == "list":
        process_list(studentdata)
    elif cmd == "add":
        process_add(studentdata)
    elif cmd == "delete":
        process_delete(studentdata)
    elif cmd == "edit":
        process_edit(studentdata)