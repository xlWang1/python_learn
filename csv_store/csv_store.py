# _*_ coding: UTF-8 _*_
# @Time     :2024/1/6 20:59
# @Author   :xiaolong wang
# @File     :csv_store.py
import csv
import os.path
file = "student.csv"

def load_data():

    dict_data = {}
    if os.path.exists(file):

        file_instance = open(file,encoding="UTF8")
        csv_reader = csv.DictReader(file_instance)
        for line in csv_reader:
            name = line.get("name")
            dict_data[name] = line

    return dict_data

def save_data(dictdata:dict):
    file_insance = open(file,'w',encoding="UTF8")
    if len(dictdata) > 0:
        rows = list(dictdata.values())
        # print(f"rows>>{rows}")
        csv_writer = csv.DictWriter(file_insance,rows[0].keys())
        # print(f"rows[0].keys>>{rows[0].keys()}")
        csv_writer.writeheader()
        csv_writer.writerows(rows)
    file_insance.close()