from openpyxl import load_workbook
import xlrd
import pandas as pd
import csv,pymysql
from datetime import datetime
conn = pymysql.connect(host="127.0.0.1",port = 3306,user="root",password="123456",database="health_web3",charset="utf8mb4",)

cursor = conn.cursor()

with open('Sleep_health_and_lifestyle_dataset.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        if row[0] == "ID":
            continue
        comments = "[]"
        now = datetime.now()

        formatted_time = now.strftime('%Y-%m-%d %H:%M:%S')

        sql = "INSERT INTO app_health(sex,age,career,sleep_duration,sleep_quality,physical_activity_level,pressure,bmi,blood_pressure,heart_rate,daily_steps,sleep_disorders,comments,createTime) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
            row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],comments,formatted_time)

        cursor.execute(sql)
        conn.commit()
        # except Exception as e:
        #     print(e)
        #     pass

cursor.close()
conn.close()









