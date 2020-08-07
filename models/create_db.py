import mysql.connector
import sys

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="dpt-newcomer")
 
cursor=db.cursor()

if("-r" in sys.argv):
    cursor.execute("DROP DATABASE IF EXISTS test_db")

cursor.execute("CREATE DATABASE test_db")

cursor.execute("USE test_db")

cursor.execute("""
                CREATE TABLE IF NOT EXISTS question(
                id          INT UNSIGNED  AUTO_INCREMENT PRIMARY KEY,
                title       VARCHAR(60)   NOT NULL,
                category    VARCHAR(60)   NOT NULL,
                regist_date DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
                text        VARCHAR(6000) NOT NULL
                );
                """)

cursor.execute("""
                CREATE TABLE IF NOT EXISTS answer(
                id          INT UNSIGNED  AUTO_INCREMENT PRIMARY KEY,
                regist_date DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
                text        VARCHAR(6000) NOT NULL,
                q_id        INT UNSIGNED  NOT NULL,
                FOREIGN KEY (q_id) REFERENCES question(id)
                );
                """)

cursor.execute("""
                CREATE TABLE IF NOT EXISTS user(
                user_id       VARCHAR(60)   PRIMARY KEY,
                user_password VARCHAR(60)   NOT NULL,
                user_name     VARCHAR(60)   NOT NULL,
                profile       VARCHAR(6000),
                sex           CHAR(1) NOT NULL
                );
                """)

cursor.execute("""
                CREATE TABLE IF NOT EXISTS user_question(
                user_id VARCHAR(60) REFERENCES user(user_id),
                q_id    INT         REFERENCES question(id)
                );
                """)

cursor.execute("""
                CREATE TABLE IF NOT EXISTS user_answer(
                user_id VARCHAR(60) REFERENCES user(user_id),
                a_id    INT         REFERENCES answer(id)
                );
                """)

db.commit()

cursor.close()
db.close()
