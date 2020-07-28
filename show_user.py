import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="dpt-newcomer")
 
cursor=db.cursor()

cursor.execute('USE test_db')
cursor.execute('SELECT * FROM user')
rows = cursor.fetchall()

cursor.close()
db.close()

count = 1

for i in rows:
    print("------------{}.row----------".format(count))
    print("ID：{}".format(i[0]))
    print("パスワード：{}".format(i[1]))
    print("名前：{}".format(i[2]))
    print("プロフィール：{}".format(i[3]))
    print("性別：{}".format(i[4]))
    count += 1