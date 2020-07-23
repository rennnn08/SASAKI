from flask import Flask,render_template,request
from models.models import QuestionContent
from models.database import db_session
from datetime import datetime
import os
from flask_paginate import Pagination, get_page_parameter
from models.MySQL import MySQL

app = Flask(__name__)
db = MySQL()

@app.route("/")
@app.route("/index")
def index():
    search = False
    q = request.args.get('q')
    if q:
        search = True

    page = request.args.get(get_page_parameter(), type=int, default=1)
    #all_question = QuestionContent.query.all()
    all_questions = db.extract_all_questions()
    all_question = all_questions[(page - 1)*20: page*20]
    pagiantion = Pagination(page=page, total=len(all_questions), search=search, per_page=20, record_name='all_question', css_framework='bootstrap4')
    return render_template("index.html", all_question=all_question,pagination=pagiantion)

@app.route("/", methods=["post"])
def get():
    create_title_id = request.form["create_title_id"]
    create_category_id = request.form["create_category_id"]
    create_detail_id = request.form["create_detail_id"]

    db.regist_question(create_title_id,create_category_id,create_detail_id)

    search = False
    q = request.args.get('q')
    if q:
        search = True

    page = request.args.get(get_page_parameter(), type=int, default=1)
    #all_question = QuestionContent.query.all()
    all_questions = db.extract_all_questions()
    all_question = all_questions[(page - 1)*20: page*20]
    pagiantion = Pagination(page=page, total=len(all_questions), search=search, per_page=20, record_name='all_question', css_framework='bootstrap4')
    return render_template("index.html", all_question=all_question,pagination=pagiantion)

@app.route("/search", methods=["post","get"])
def search():

    search_word = request.form["search_word"]
    
    search = False
    q = request.args.get('q')
    if q:
        search = True

    page = request.args.get(get_page_parameter(), type=int, default=1)
    all_questions = db.search_title_category(search_word)
    all_question = all_questions[(page - 1)*20: page*20]
    pagiantion = Pagination(page=page, total=len(all_questions), search=search, per_page=20, record_name='all_question', css_framework='bootstrap4')
    return render_template("index.html", all_question=all_question,pagination=pagiantion)

@app.route("/question_detail/<int:question_id>",methods=["POST","GET"])
def answer_regist(question_id):
    
    answer2 = db.extract_answers(question_id)
    answers = answer2[2]
    answer_list = db.extract_question(question_id)
    create_title_id = answer_list[1]
    create_category_id = answer_list[2]
    create_detail_id = answer_list[4]
    #tryは実行したい
    try:
        answer_text = request.form["answer_text.xt"]
        db.regist_answer(question_id,answer_text)
        ##expectは例外が起きたとき(実行できなかったとき)
    except:
        print("Nosignal")
    return render_template("question_detail.html",answers=answers,create_title_id=create_title_id,
    create_category_id=create_category_id,create_detail_id=create_detail_id)    

@app.route("/my_page")
def my_page():

    search = False
    q = request.args.get('q')
    if q:
        search = True

    page = request.args.get(get_page_parameter(), type=int, default=1)
    #all_question = QuestionContent.query.all()
    all_questions = db.extract_all_questions()
    all_question = all_questions[(page - 1)*20: page*20]
    pagiantion = Pagination(page=page, total=len(all_questions), search=search, per_page=20, record_name='all_question', css_framework='bootstrap4')

    return render_template("my_page.html",pagination=pagiantion,all_questions=all_questions) 

@app.route("/create_question")
def create_question():
    
    return render_template("create_question.html")

if __name__ == "__main__":
    app.run(debug=True)

@app.context_processor
def add_staticfile():
    def staticfile_cp(fname):
        path = os.path.join(app.root_path, 'static', fname)
        mtime =  str(int(os.stat(path).st_mtime))
        return '/static/' + fname + '?v=' + str(mtime)
    return dict(staticfile=staticfile_cp)

