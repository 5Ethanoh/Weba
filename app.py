from flask import Flask,render_template
from flask.globals import request
import pymysql


app = Flask(__name__)


@app.route('/')
def index():
  return render_template('register.html')
  #메인화면 route


#회원 가입 진행시 Route
@app.route('/Sign-Up', methods=['GET','POST'])
def post():
    if request.method == 'POST':
        value = request.form['id_name']
        value = str(value)
        value2 = request.form['pwd_name']
        value2 = str(value2)
        value3 = request.form['name_name']
        value3 = str(value3)
        insert_table(value,value2,value3)
        
        callid=call_all_id()
        arrayid=[]
        for i in range(len(callid)):
            arrayid.append(callid[i][0])

        callpwd=call_all_pwd()
        arraypwd=[]
        for i in range(len(callpwd)):
            arraypwd.append(callpwd[i][0])

        callname=call_all_name()
        arrayname=[]
        for i in range(len(callname)):
            arrayname.append(callname[i][0])

    return render_template('table.html',id_list=arrayid,pwd_list=arraypwd,name_list=arrayname)

# #로그인 진행 루트
# @app.route('/Sign-In', methods=['GET','POST'])
# def post():
#     if request.method=='POST':
#         id_check=request.form['id_name']
#         pw_check=request.form['pw_name']
#         id_list=[]
#         pw_list=[]
#         id_list.append(show_Id_table())
#         pw_list.append(show_Pwd_table())

#     return id_list

def dbconn():
    db = pymysql.connect(host='dbserver-new-study-tdg.mariadb.database.azure.com', port=3306, user='ethan@dbserver-new-study-tdg', passwd='rkskek123#@!', db='web-dbms-study', charset='utf8')
    return db


#테이블 전체 조회 함수
def show_table():
    db=dbconn()
    cursor = db.cursor()
    sql = '''SELECT * FROM users;'''
    cursor.execute(sql)
    result = cursor.fetchall()
    db.close()
    return str(result)

#테이블 ID 조회 함수
def show_Id_table():
    db=dbconn()
    cursor = db.cursor()
    sql = '''SELECT id FROM users;'''
    cursor.execute(sql)
    result = cursor.fetchall()
    db.close()
    return str(result)

def call_all_id():
    cnx=dbconn()
    cursor = cnx.cursor()
    queryArr = []
    queryArr.append("SELECT")
    queryArr.append("id")
    queryArr.append("FROM users")
    queryStr = " ".join(queryArr)
    cursor.execute(queryStr)
    dbCheckArr = []
    for row in cursor:
        dbCheckArr.append(row) 
    cnx.close()
    return dbCheckArr

def call_all_pwd():
    cnx=dbconn()
    cursor = cnx.cursor()
    queryArr = []
    queryArr.append("SELECT")
    queryArr.append("password")
    queryArr.append("FROM users")
    queryStr = " ".join(queryArr)
    cursor.execute(queryStr)
    dbCheckArr = []
    for row in cursor:
        dbCheckArr.append(row) 
    cnx.close()
    return dbCheckArr

def call_all_name():
    cnx=dbconn()
    cursor = cnx.cursor()
    queryArr = []
    queryArr.append("SELECT")
    queryArr.append("name")
    queryArr.append("FROM users")
    queryStr = " ".join(queryArr)
    cursor.execute(queryStr)
    dbCheckArr = []
    for row in cursor:
        dbCheckArr.append(row) 
    cnx.close()
    return dbCheckArr       


# #TABLE INSERT 함수
def insert_table(ID,PW,NAME):
    db=dbconn()
    cursor = db.cursor()
    sql="INSERT INTO users VALUES('%s','%s','%s')" %(ID,PW,NAME)
    cursor.execute(sql)
    result=cursor.fetchall()
    db.commit()
    db.close()
    a=show_table() #Insert 후 조회하기
    print(a)
    return a;


if __name__ == '__main__':
    app.run()
