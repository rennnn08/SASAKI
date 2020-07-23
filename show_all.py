import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="dpt-newcomer")
 
cursor=db.cursor()

cursor.execute('USE test_db')
cursor.execute('SELECT question.id, question.title, question.category, question.regist_date, question.text, answer.id, answer.regist_date, answer.text FROM question LEFT JOIN answer ON question.id = answer.q_id WHERE q_id IS NOT NULL')
rows = cursor.fetchall()

cursor.close()
db.close()

count = 1

for i in rows:
    print("------------{}.row----------".format(count))
    print("質問ID：{}".format(i[0]))
    print("タイトル：{}".format(i[1]))
    print("カテゴリ：{}".format(i[2]))
    print("質問日：{}".format(i[3]))
    print("内容：{}".format(i[4]))
    print("回答ID：{}".format(i[5]))
    print("回答日：{}".format(i[6]))
    print("回答内容：{}".format(i[7]))
    count += 1