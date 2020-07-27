import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="dpt-newcomer")
 
cursor=db.cursor()

cursor.execute('USE test_db')
cursor.execute('SELECT * FROM question')
rows = cursor.fetchall()

cursor.close()
db.close()

count = 1

for i in rows:
    print("------------{}.row----------".format(count))
    print("ID：{}".format(i[0]))
    print("タイトル：{}".format(i[1]))
    print("カテゴリ：{}".format(i[2]))
    print("日付：{}".format(i[3]))
    print("内容：{}".format(i[4]))
    count += 1