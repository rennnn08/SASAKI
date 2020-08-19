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
print(db.regist_question('「り」から始まり「ん」で終わる言葉を教えてください。','宿題','「り」から始まり「ん」で終わる言葉を教えてください。','uSqzaC2'))
print(db.regist_question('暑くて24時間ずっとエアコン点けっぱなしなんですが、エアコン壊れるでしょうか、、、','エアコン、空調家電','暑くて24時間ずっとエアコン点けっぱなしなんですが、エアコン壊れるでしょうか、、、','Joseph0425'))
print(db.regist_question('HDMIケーブルで接続すればパソコンの画面をテレビで見られるようになりますか？','パソコン','HDMIケーブルで接続すればパソコンの画面をテレビで見られるようになりますか？','Sergio Carlo Di Benedetto'))
print(db.regist_question('Core i シリーズとXeonはどちらの方が動画編集に向いていますか？','パソコン','Core i シリーズとXeonはどちらの方が動画編集に向いていますか？','uSqzaC2'))
print(db.regist_question('コバエを退治するのにいい方法はありますか？','掃除','コバエを退治するのにいい方法はありますか？','スコット・J・ギルバード'))
print(db.regist_question('高いfpsを出すにはcpuにも関係ありますか？','パソコン','高いfpsを出すにはcpuにも関係ありますか？','uSqzaC2'))


#コピペ用
#print(db.regist_question('タイトル','カテゴリ','内容','回答者'))


#回答の作成
print(db.regist_answer(1,'8848メートルです','スコット・J・ギルバード'))
print(db.regist_answer(1,'3776メートルです','Sergio Carlo Di Benedetto'))
print(db.regist_answer(2,'なんとなくです','Joseph0425'))
print(db.regist_answer(3,'区役所にでも行ってください','uS5qzaC2'))
print(db.regist_answer(3,'梨園、離縁、罹患、離婚、リジン \n利点、理念、リボン、裏面、リヨン \n力点、陸軍、リスボン、リターン、立案 \nリムジン、リモコン、旅館、リリヤン、リン酸 \n隣人、鱗粉、リズム感、立春、リフレイン \n溜飲、硫酸、留年、料金、良品 \nリンパ腺、リアクション、領事館、龍馬伝 \n旅行券、理路整然、竜王戦、リロケーション、臨場感\nリアス式海岸、リハビリテーシヨン','スコット・J・ギルバード'))
print(db.regist_answer(1,'不良品や低価格品、怪しいメーカーじゃない限り壊れません\n\n余程、温度調整とかでエアコンをガチャガチャいじらなければの話ですが。','Sergio Carlo Di Benedetto'))

#コピペ用
#print(db.regist_answer(1,'回答内容','名前'))

