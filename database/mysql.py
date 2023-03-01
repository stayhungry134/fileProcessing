"""
name: mysql.py
create_time: 2023-02-08
author: Ethan White

Description: 
"""
import time
import datetime
import MySQLdb


my_db = MySQLdb.connect(
  host="stayhungry134.com",
  port=3306,
  user="root",
  password="(Ethan/997813581....",
  database='qqmirai',
)
cursor = my_db.cursor()
#INSERT INTO `qqmirai`.`chat_record` (`id`, `send_time`, `sender`, `reply`, `content`) VALUES (1, '2023-02-09 10:50:16', '3512641860', 0, '你是猪吗？');

sql = f"INSERT INTO `chat_record` (`send_time`, `sender`, `reply`, `content`) VALUES ('{datetime.datetime.now()}', '3512641860', 0, '你就是猪');"
print(sql)
cursor.execute(sql)
my_db.commit()
time.sleep(3)
cursor.execute("select * from chat_record")
data = cursor.fetchall()

print(data)

my_db.close()

