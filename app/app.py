from flask import Flask,render_template,request, redirect,session,flash,url_for
from datetime import datetime
import os
from flask_paginate import Pagination, get_page_parameter
from models.MySQL import MySQL


app = Flask(__name__)
app.secret_key = "aaa"
db = MySQL()
@app.route("/")
@app.route("/",methods=["get"])
def login():
    #最初に来た時に表示
    Labeltext = ""
    return render_template("login.html",Labeltext=Labeltext)

@app.route("/",methods=["POST"])
def login_post():
    session["flag"] = False
    #ログインフラグによって返すページを返る処理
    try:
        LoginId = request.form["LoginId"]
        LoginPass = request.form["LoginPass"]
        if db.check_account(LoginId,LoginPass):
            session["flag"] = True
            session["UserId"] = LoginId
            return redirect("/home")
        else:
            Labeltext = ":IDまたはPASSが違います"
            return render_template("login.html",Labeltext=Labeltext)
            #IDとPASSを読み込んでデータべースへ問い合わせ
            #IDが存在しPASSがあっている場合マイページ?へ
            #ない場合IDまたはPASSが違いますと表示ラベル？に表示
    except:
        #上記以外の場合
        Labeltext = ":ログインできません"
        return render_template("login.html",Labeltext=Labeltext)
    
@app.route('/logout')
def logout():
    session["UserId"]=False
    session["flag"]=False
    return redirect("/")

@app.route("/home")
def index():
    try:
        flag = session["flag"]
    except:
        return redirect("/")
    if flag==True:
        search = False
        q = request.args.get('q')
        if q:
            search = True

        page = request.args.get(get_page_parameter(), type=int, default=1)
        all_questions = db.extract_all_questions()
        all_question = all_questions[(page - 1)*20: page*20]
        pagiantion = Pagination(page=page, total=len(all_questions), search=search, per_page=20, record_name='all_questions', css_framework='bootstrap4')
        return render_template("index.html", all_question=all_question,pagination=pagiantion)
        
    return redirect("/")

    

@app.route("/create_account")
def create_account():
    
    return render_template("create_account.html")

@app.route("/create_account",methods=["POST"])
def create_account_post():
    if request.method == "POST":
        if request.form["create_account_name"] and request.form["create_account_id"] and request.form["password"] and request.form["sex"]:
            create_account_name = request.form["create_account_name"]
            create_account_id = request.form["create_account_id"]
            password = request.form["password"]
            sex = request.form["sex"]
            if  db.check_id_already_exists(create_account_id) == True:
                infoMessage = "すでに登録されているidです。"
            else:
                db.regist_user(create_account_id,password,create_account_name,sex)
                infoMessage = "登録完了しました"
            flash(infoMessage,"complete")
            return render_template("login.html",infoMessage=infoMessage)

@app.route("/", methods=["post"])
def get():
    
    #db.regist_question(create_title_id,create_category_id,create_detail_id)
    search = False
    q = request.args.get('q')
    if q:
        search = True

    page = request.args.get(get_page_parameter(), type=int, default=1)
    all_questions = db.extract_all_questions()
    all_question = all_questions[(page - 1)*20: page*20]
    pagiantion = Pagination(page=page, total=len(all_questions), search=search, per_page=20, record_name='all_question', css_framework='bootstrap4')
    return render_template("index.html", all_question=all_question,pagination=pagiantion)

@app.route("/search", methods=["post","get"])
def search():

    if request.method == 'POST':
        search_word = request.form["search_word"]
        session["search_word"] = search_word

    search_word = session["search_word"]
    
    page = request.args.get(get_page_parameter(), type=int, default=1)
    all_questions = db.search_title_category(search_word)
    all_question = all_questions[(page - 1)*20: page*20]
    pagiantion = Pagination(page=page, total=len(all_questions), per_page=20, record_name='all_question', css_framework='bootstrap4')
    return render_template("index.html", all_question=all_question,pagination=pagiantion,search_word=search_word)

@app.route("/question_detail/<int:question_id>",methods=["POST","GET"])
def answer_regist(question_id):
    
    #answer2 = db.extract_answers(question_id)
    #answers = answer2[2]
    answer_list = db.extract_question(question_id)
    create_title_id = answer_list[0][1]
    create_category_id = answer_list[0][2]
    create_detail_id = answer_list[0][4]
    
    
    #tryは実行したい
    try:
        responce_answers = []
        answer_text = request.form["answer_text"]
        user_id = session["UserId"]
        db.regist_answer(question_id,answer_text,session["UserId"])
        answers = db.extract_answers(question_id)
        answerslen = len(answers)
        for ans in range(answerslen):
            responce_answers.append(answers[ans][2])
    except:
        try:
            responce_answers = []
            answers = db.extract_answers(question_id)
            answerslen = len(answers)
            for ans in range(answerslen):
                responce_answers.append(answers[ans][2])
        except:
            print("notfindall")

    return render_template("question_detail.html",answers=responce_answers,create_title_id=create_title_id,
    create_category_id=create_category_id,create_detail_id=create_detail_id,question_id=question_id)    

@app.route("/create_question")
def create_question():
    
    return render_template("create_question.html")

@app.route("/create_question",methods=["POST"])
def create_question_post():
    
    create_title_id = request.form["create_title_id"]
    create_category_id = request.form["create_category_id"]
    create_detail_id = request.form["create_detail_id"]
    
    user_id = session["UserId"]
    
    db.regist_question(create_title_id,create_category_id,create_detail_id,user_id)
    
    return redirect(url_for("index"))
    
@app.route("/my_page/<user_id>",methods=["POST","GET"])
def my_page(user_id):

    myid=session["UserId"]

    user_info = db.get_user_info(user_id)
    user_name = user_info[0][0]
    user_prof = user_info[0][2]

    search = False
    q = request.args.get('q')
    if q:
        search = True

    page = request.args.get(get_page_parameter(), type=int, default=1)
    all_questions = db.extract_user_question(user_id)
    all_question = all_questions[(page - 1)*20: page*20]
    pagiantion = Pagination(page=page, total=len(all_questions), search=search, per_page=20, record_name='all_question', css_framework='bootstrap4')

    return render_template("my_page.html",pagination=pagiantion,all_question=all_question,user_name=user_name, user_prof = user_prof,user_id=user_id,myid=myid)



@app.route("/get_user_name", methods=["POST"])
def get_user_info():
    user_id = session.get('UserId')
    user_name = request.form["user_name"]

    if not user_name:
        return redirect(url_for('my_page',user_id=user_id))

    db.set_user_name(user_id,user_name)
    
    return redirect(url_for('my_page',user_id=user_id))

@app.route("/get_user_profile", methods=["POST"])
def get_user_profile():

    user_id = session.get('UserId')
    user_prof = request.form["user_prof"]
    db.set_user_profile(user_id, user_prof)

    return  redirect(url_for('my_page',user_id=user_id))

if __name__ == "__main__":
    app.run(debug=True)

@app.context_processor
def add_staticfile():
    def staticfile_cp(fname):
        path = os.path.join(app.root_path, 'static', fname)
        mtime =  str(int(os.stat(path).st_mtime))
        return '/static/' + fname + '?v=' + str(mtime)
    return dict(staticfile=staticfile_cp)
