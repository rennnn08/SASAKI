import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="dpt-newcomer")
 
cursor=db.cursor()

cursor.execute('USE test_db')
cursor.execute('SELECT * FROM answer')
rows = cursor.fetchall()

cursor.close()
db.close()

count = 1

for i in rows:
    print("------------{}.row----------".format(count))
    print("ID：{}".format(i[0]))
    print("日付：{}".format(i[1]))
    print("内容：{}".format(i[2]))
    print("質問ID：{}".format(i[3]))
    count += 1