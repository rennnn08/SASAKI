import mysql.connector
 
db=mysql.connector.connect(host="localhost", user="root", password="dpt-newcomer")
 
cursor=db.cursor()
 
cursor.execute("CREATE DATABASE test_db")
db.commit()
cursor.execute("USE test_db")
db.commit()
cursor.execute("""CREATE TABLE IF NOT EXISTS question(
                id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(30),category VARCHAR(30),
                regist_date DATETIME,text VARCHAR(3000));""")
db.commit()
cursor.execute("""CREATE TABLE IF NOT EXISTS answer(
                id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                regist_date DATETIME,text VARCHAR(3000),
                q_id INT UNSIGNED,
                FOREIGN KEY (id) REFERENCES question(id));""")
db.commit()

