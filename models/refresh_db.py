import mysql.connector
 
db=mysql.connector.connect(host="localhost", user="root", password="dpt-newcomer")
 
cursor=db.cursor()

cursor.execute("DROP DATABASE IF EXISTS test_db")

cursor.execute("CREATE DATABASE test_db")

cursor.execute("USE test_db")

cursor.execute("""CREATE TABLE IF NOT EXISTS
                question(
                id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(30),
                category VARCHAR(30),
                regist_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                text VARCHAR(3000)
                );
                """)

cursor.execute("""
                CREATE TABLE IF NOT EXISTS 
                answer(
                id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                regist_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                text VARCHAR(3000),
                q_id INT UNSIGNED,
                FOREIGN KEY (id) REFERENCES question(id)
                );
                """)

db.commit()

cursor.close()
db.close()

