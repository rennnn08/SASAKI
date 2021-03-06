import  mysql.connector

class MySQL:
    def __init__(self):
        self.dns = {
            'user': 'root',
            'host': 'localhost',
            'password': 'dpt-newcomer',
            'database': 'test_db'
        }
        self.dbh = None
    

    def _open(self):
        self.dbh = mysql.connector.MySQLConnection(**self.dns)
        

    def _close(self):
        self.dbh.close()

    def _SCharaReplace(self, moji):
        moji = moji.replace("\\","\\\\")
        moji = moji.replace("\'","\\\'")
        return moji


    """
    引　数：なし
    戻り値：データ配列（ID・タイトル・カテゴリ・日付,ユーザID,ユーザ名）
    機　能：データベース内にある質問のテーブルデータを返す
    """
    def extract_all_questions(self):
        try:
            self._open()
            stmt = 'SELECT question.id, question.title, question.category, question.regist_date, user.user_id, user.user_name FROM question \
                JOIN user_question ON question.id = user_question.q_id \
                JOIN user ON user_question.user_id = user.user_id'
            cursor = self.dbh.cursor()
            cursor.execute(stmt)
            questions = cursor.fetchall()
            
        except mysql.connector.Error as err:
            print(err)#テスト用
            questions = []

        else:
            cursor.close()
            self._close()
            
        return questions
    
    """
    引　数：質問ID(question_id)
    戻り値：データ配列（質問ID,タイトル,カテゴリ,日付,ユーザID,ユーザ名）
    機　能：データベースから20行ずつ質問を取得する。
    """
    def extract_20_questions(self, question_id):
        try:
            self._open()
            stmt = 'SELECT question.id, question.title, question.category, question.regist_date, user.user_id, user.user_name FROM question \
                JOIN user_question ON question.id = user_question.q_id \
                JOIN user ON user_question.user_id = user.user_id \
                WHERE question.id >= {}'.format(question_id)
            cursor = self.dbh.cursor(buffered = True)
            cursor.execute(stmt)
            questions = cursor.fetchmany(size=20)
            
        except mysql.connector.Error as err:
            print(err)#テスト用
            questions = []
        
        else:
            cursor.close()
            self._close()

        return questions

    """
    引　数：質問ID(question_id),行数(any_num)
    戻り値：データ配列（質問ID,タイトル,カテゴリ,日付,ユーザID,ユーザ名）
    機　能：データベースから指定した行数分だけ質問を渡す。
    """
    def extract_any_questions(self, question_id, any_num):
        try:
            self._open()
            stmt = 'SELECT question.id, question.title, question.category, question.regist_date, user.user_id, user.user_name FROM question \
                JOIN user_question ON question.id = user_question.q_id \
                JOIN user ON user_question.user_id = user.user_id \
                WHERE question.id >= {}'.format(question_id)
            cursor = self.dbh.cursor(buffered = True)
            cursor.execute(stmt)
            questions = cursor.fetchmany(size=any_num)
            
        except mysql.connector.Error as err:
            print(err)#テスト用
            questions = []
        
        else:
            cursor.close()
            self._close()

            print(questions)#テスト用
        return questions

    """
    引　数：質問ID(question_id)
    戻り値：データ配列(ID,タイトル,カテゴリー,日付,本文,ユーザID,ユーザ名)
    機　能：IDでデータの行を検索し、渡す（質問本文）
    """
    def extract_question(self, question_id):
        try:
            self._open()
            stmt = 'SELECT question.id, question.title, question.category, question.regist_date, question.text, user.user_id, user.user_name FROM question \
                JOIN user_question ON question.id = user_question.q_id \
                JOIN user ON user_question.user_id = user.user_id \
                WHERE question.id = {}'.format(question_id)
            cursor = self.dbh.cursor()
            cursor.execute(stmt)
            question = cursor.fetchall()
        
        except mysql.connector.Error as err:
            print(err)#テスト用
            question = []
        
        else:
            cursor.close()
            self._close()

        return question

    """
    引　数：質問ID（question_id)
    戻り値：データ配列（回答ID,日付,回答内容,ユーザID,ユーザ名）
    機　能：質問の回答を渡す
    """
    def extract_answers(self, question_id):
        try:
            self._open()
            stmt = 'SELECT answer.id, answer.regist_date, answer.text, user.user_id, user.user_name FROM answer \
                JOIN user_answer ON answer.id = user_answer.a_id \
                JOIN user ON user_answer.user_id = user.user_id \
                WHERE answer.q_id = {}'.format(question_id)
            cursor = self.dbh.cursor()
            cursor.execute(stmt)
            answer = cursor.fetchall()
        
        except mysql.connector.Error as err:
            print(err)#テスト用
            answer = []
        else:
            cursor.close()
            self._close()

        return answer

    """
    引　数：検索文字(search_str)
    戻り値：データ配列(質問ID,タイトル,カテゴリ,日付,ユーザID,ユーザ名)
    機　能：受け取った文字列が含まれる質問を返す
    """
    def search_title_category(self, search_str):
        try:
            self._open()
            stmt = "SELECT question.id, question.title, question.category, question.regist_date, user.user_id, user.user_name FROM question \
                JOIN user_question ON question.id = user_question.q_id \
                JOIN user ON user_question.user_id = user.user_id \
                WHERE title LIKE '%{}%' OR category LIKE '%{}%'".format(search_str, search_str)
            cursor = self.dbh.cursor()
            cursor.execute(stmt)
            questions = cursor.fetchall()
        
        except mysql.connector.Error as err:
            print(err)#テスト用
            questions = []
        
        else:
            cursor.close()
            self._close()

        return questions

    """
    引　数：質問のタイトル（question_title),質問のカテゴリ(question_category),質問の内容(question_text),ユーザID(user_id)
    戻り値：書き込みが成功かどうか（boolean型）
    機　能：質問をデータベースに書き込む
    """
    def regist_question(self, question_title, question_category, question_text, user_id):
        try:
            question_title = self._SCharaReplace(question_title)
            question_category = self._SCharaReplace(question_category)
            question_text = self._SCharaReplace(question_text)

            self._open()
            cursor = self.dbh.cursor()
            stmt = "INSERT INTO question(title, category, text) VALUES('{}', '{}', '{}')".format(question_title, question_category, question_text)
            cursor.execute(stmt)

            #questionテーブルのidの最大値を取得
            stmt = "SELECT MAX(id) FROM question"
            cursor.execute(stmt)
            row = cursor.fetchall()

            stmt ="INSERT INTO user_question VALUES('{}', {})".format(user_id, row[0][0])
            cursor.execute(stmt)

        
        except mysql.connector.Error as err:
            print(err)#テスト用
            return False
        
        else:
            self.dbh.commit()
            cursor.close()
            self._close()

            return True

    """
    引　数：質問ID(question_id),回答の内容(answer_text),ユーザID(user_id)
    戻り値：書き込みが成功かどうか（boolean型）
    機　能：質問への回答をデータベースに書き込む
    """
    def regist_answer(self, question_id, answer_text, user_id):
        try:
            answer_text = self._SCharaReplace(answer_text)

            self._open()
            cursor = self.dbh.cursor()
            stmt = "INSERT INTO answer(text, q_id) VALUES('{}', {})".format(answer_text, question_id)
            cursor.execute(stmt)

            #questionテーブルのidの最大値を取得
            stmt = "SELECT MAX(id) FROM answer"
            cursor.execute(stmt)
            row = cursor.fetchall()

            stmt = "INSERT INTO user_answer VALUES('{}', {})".format(user_id, row[0][0])
            cursor.execute(stmt)

        except mysql.connector.Error as err:
            print(err)#テスト用
            return False
        
        else:
            self.dbh.commit()
            cursor.close()
            self._close()

            return True

    """
    引　数：質問ID(question_id)
    戻り値：削除が成功かどうか（boolean型）
    機　能：指定したIDの質問を削除する(自動的に回答も削除される)
    """
    def delete_question(self, question_id):
        a_flag = False

        try:
            self._open()
            cursor = self.dbh.cursor()
            
            #IDの検索
            stmt = "SELECT id FROM answer WHERE q_id = {}".format(question_id)
            cursor.execute(stmt)
            a_id = cursor.fetchall()

            for ans_ids in a_id:
                #回答があった場合のフラグ
                a_flag = True

                #user_answerで一致する回答IDの削除
                stmt = "DELETE FROM user_answer WHERE a_id = {}".format(ans_ids[0])
                cursor.execute(stmt)
                
            if a_flag:
                #回答の削除
                stmt = "DELETE FROM answer WHERE q_id = {}".format(question_id)
                cursor.execute(stmt)
            
            #user_questionで一致する質問IDの削除
            stmt = "DELETE FROM user_question WHERE q_id = {}".format(question_id)
            cursor.execute(stmt)

            #質問の削除
            stmt = "DELETE FROM question WHERE id = {}".format(question_id)
            cursor.execute(stmt)
        
        except mysql.connector.Error as err:
            print(err)#テスト用
            return False
        
        else:
            self.dbh.commit()
            cursor.close()
            self._close()

            return True

    """
    引　数：ユーザID(user_id)、ユーザパス(user_pass)
    戻り値：ログインできたかどうか（boolean型）
    機　能：ログイン認証をする
    """
    def check_account(self, user_id, user_password):
        try:
            self._open()
            #ログイン
            stmt = "SELECT user_id, user_password FROM user \
                WHERE user_id = '{}' AND user_password = '{}'".format(user_id, user_password)
            cursor = self.dbh.cursor()
            cursor.execute(stmt)
            login = cursor.fetchall()
        
        except mysql.connector.Error as err:
            print(err)#テスト用
            return False
        
        else:
            self.dbh.commit()
            cursor.close()
            self._close()

            if login:
                return True
            else:
                return False

    """
    引　数：検索するカテゴリ(search_category)
    戻り値：データ配列(質問ID,タイトル,カテゴリ,日付,ユーザID,ユーザ名)
    機　能：受け取ったカテゴリが含まれる質問を返す
    """
    def search_category(self, search_category):
        try:
            self._open()
            stmt = "SELECT question.id, question.title, question.category, question.regist_date, user.user_id, user.user_name FROM question \
                JOIN user_question ON question.id = user_question.q_id \
                JOIN user ON user_question.user_id = user.user_id \
                WHERE category LIKE '%{}%'".format(search_category)
            cursor = self.dbh.cursor()
            cursor.execute(stmt)
            questions = cursor.fetchall()
        
        except mysql.connector.Error as err:
            print(err)#テスト用
            questions = []
        
        else:
            cursor.close()
            self._close()

        return questions

    """
    引　数：ID(user_id),パスワード(user_password),名前(user_name),性別(user_sex)
    戻り値：Boolean型
    機　能：ユーザの登録
    """
    def regist_user(self, user_id, user_password, user_name, user_sex):
        try:
            user_id = self._SCharaReplace(user_id)
            user_password = self._SCharaReplace(user_password)
            user_name = self._SCharaReplace(user_name)

            self._open()
            stmt = "INSERT INTO user(user_id, user_password, user_name, sex) \
                VALUES('{}', '{}', '{}', {})".format(user_id, user_password, user_name, user_sex)
            cursor = self.dbh.cursor()
            cursor.execute(stmt)
        
        except mysql.connector.Error as err:
            print(err)#テスト用
            return False
        
        else:
            self.dbh.commit()
            cursor.close()
            self._close()

            return True
    
    """
    引　数：ID(user_id)
    戻り値：配列(名前,性別,プロフィール)
    機　能：ユーザの詳細データを渡す
    """
    def get_user_info(self, user_id):
        try:
            self._open()
            stmt = "SELECT user_name, sex, profile \
                FROM user WHERE user_id = '{}'".format(user_id)
            cursor = self.dbh.cursor()
            cursor.execute(stmt)
            user = cursor.fetchall()
        
        except mysql.connector.Error as err:
            print(err)#テスト用
            user = []
        
        else:
            cursor.close()
            self._close()

        return user    
    
    """
    引　数：ID(user_id),名前(user_name)
    戻り値：Boolean型
    機　能：ユーザの名前の編集
    """
    def set_user_name(self, user_id, user_name):
        try:
            user_name = self._SCharaReplace(user_name)

            self._open()
            stmt = "UPDATE user SET user_name = '{}' \
                WHERE user_id = '{}'".format(user_name, user_id)
            cursor = self.dbh.cursor()
            cursor.execute(stmt)
        
        except mysql.connector.Error as err:
            print(err)#テスト用
            return False
        
        else:
            self.dbh.commit()
            cursor.close()
            self._close()

            return True

    
    """
    引　数：ID(user_id),プロフィール(user_profile)
    戻り値：Boolean型
    機　能：ユーザのプロフィールの編集
    """
    def set_user_profile(self, user_id, user_profile):
        try:
            user_profile = self._SCharaReplace(user_profile)

            self._open()
            stmt = "UPDATE user SET profile = '{}' \
                WHERE user_id = '{}'".format(user_profile, user_id)
            cursor = self.dbh.cursor()
            cursor.execute(stmt)
        
        except mysql.connector.Error as err:
            print(err)#テスト用
            return False
        
        else:
            self.dbh.commit()
            cursor.close()
            self._close()

            return True
    
    """
    引　数：ID(user_id)
    戻り値：Boolean型
    機　能：ユーザのIDがかぶっているかどうか
    """
    def check_id_already_exists(self, user_id):
        try:
            self._open()
            stmt = "SELECT user_id FROM user \
                WHERE user_id = '{}'".format(user_id)
            cursor = self.dbh.cursor()
            cursor.execute(stmt)
            user = cursor.fetchall()
        
        except mysql.connector.Error as err:
            print(err)#テスト用
            return True
        
        else:
            cursor.close()
            self._close()
            
            if user:
                return True
            else:
                return False

    """
    引　数：ユーザID(user_id)
    戻り値：データ配列（質問ID,タイトル,カテゴリ,日付）
    機　能：ユーザがした質問の一覧を渡す
    """
    def extract_user_question(self, user_id):
        try:
            self._open()
            stmt = "SELECT question.id, question.title, question.category, question.regist_date FROM user_question \
                LEFT JOIN question ON user_question.q_id = question.id \
                WHERE user_question.user_id = '{}'".format(user_id)
            cursor = self.dbh.cursor()
            cursor.execute(stmt)
            user_questions = cursor.fetchall()
        
        except mysql.connector.Error as err:
            print(err)#テスト用
            user_questions = []
        
        else:
            cursor.close()
            self._close()
            
        return user_questions
    
    """
    引　数：ユーザID(user_id)
    戻り値：データ配列（回答ID,日付,回答内容）
    機　能：ユーザがした質問の一覧を渡す
    """
    def extract_user_answer(self, user_id):
        try:
            self._open()
            stmt = "SELECT answer.id, answer.regist_date, answer.text FROM user_answer \
                LEFT JOIN answer ON user_answer.a_id = answer.id \
                WHERE user_answer.user_id = '{}'".format(user_id)
            cursor = self.dbh.cursor()
            cursor.execute(stmt)
            user_answers = cursor.fetchall()
        
        except mysql.connector.Error as err:
            print(err)#テスト用
            user_answers = []
        
        else:
            cursor.close()
            self._close()
            
        return user_answers
        
    """
    引　数：質問ID(id),質問内容(text)
    戻り値：Boolean型
    機　能：質問の編集
    """
    def update_question_text(self, question_id, question_text):
        try:
            question_text = self._SCharaReplace(question_text)

            self._open()
            stmt = "UPDATE question SET text = '{}' \
                WHERE id = {}".format(question_text, question_id)
            cursor = self.dbh.cursor()
            cursor.execute(stmt)
        
        except mysql.connector.Error as err:
            print(err)#テスト用
            return False
        
        else:
            self.dbh.commit()
            cursor.close()
            self._close()
            
            return True
    
    """
    引　数：回答ID(id),回答内容(text)
    戻り値：Boolean型
    機　能：回答の編集
    """
    def update_answer_text(self, answer_id, answer_text):
        try:
            answer_text = self._SCharaReplace(answer_text)

            self._open()
            stmt = "UPDATE answer SET text = '{}' \
                WHERE id = {}".format(answer_text, answer_id)
            cursor = self.dbh.cursor()
            cursor.execute(stmt)
        
        except mysql.connector.Error as err:
            print(err)#テスト用
            return False
        
        else:
            self.dbh.commit()
            cursor.close()
            self._close()
            
            return True
    
    """
    引　数：回答ID(answer_id)
    戻り値：削除が成功かどうか（boolean型）
    機　能：指定したIDの回答を削除する

    def delete_answer(self, answer_id):
        self._open()
        
        try:
            cursor = self.dbh.cursor()

            
            stmt = "DELETE FROM answer WHERE id = {}".format(answer_id)
            cursor.execute(stmt)
        
        except mysql.connector.Error as err:
            print(err)#テスト用
            return False
        
        else:
            self.dbh.commit()
            cursor.close()
            self._close()

            return True
    """