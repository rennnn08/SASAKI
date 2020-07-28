from models.MySQL import MySQL

db = MySQL()

#ユーザを4人作成
print(db.regist_user('uS5qzaC2','Zi2WtFQ','田山　駿介','1'))
print(db.regist_user('スコット・J・ギルバード','Rf89Cnxh','S.J.G','4'))
print(db.regist_user('Joseph0425','D3qEbVs6','P.Parasite','2'))
print(db.regist_user('Sergio Carlo Di Benedetto','C7wBzfh4','@tanaka','0'))

#質問の作成
print(db.regist_question('富士山の高さは何メートルですか？','雑学','富士山よりも大きな人になりたいです。','uSqzaC2'))
print(db.regist_question('貧困層はなぜ増えるのですか？','社会','貧困層はなぜ増えるのですか？','スコット・J・ギルバード'))
print(db.regist_question('生活保護の申請方法がわかりません。','社会','生活保護の申請方法がわかりません。\n教えてください。','Joseph0425'))
print(db.regist_question('近所のピザがありえない','料理','ピザにコーンが乗っていて訳が分かりません。\n最近はこのようなピザが流行っているのですか？','Sergio Carlo Di Benedetto'))

#回答の作成
print(db.regist_answer(1,'8848メートルです','スコット・J・ギルバード'))
print(db.regist_answer(1,'3776メートルです','Sergio Carlo Di Benedetto'))
print(db.regist_answer(2,'なんとなくです','Joseph0425'))
print(db.regist_answer(3,'区役所にでも行ってください','uS5qzaC2'))

