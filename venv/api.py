# -*- coding = utf-8 -*-
# @Time : 2021/1/3 11:01
# @Author : Fang Shang Yang
# @File : api.py
# @Software : PyCharm

from flask import Flask,jsonify,request,redirect,url_for,session,g
from SQL_CRUD import Certificate_management_system
import json
from dataclasses import dataclass

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['SECRET_KEY']='sndokasmdklamslk'

@dataclass
class User:
    id:int
    password:str
    username: str

@app.before_request
def before_request():
    g.User = None
    if 'user_id' in session:
        system = Certificate_management_system()
        data = system.Use(db_name='certificate_management_system')
        data1 = system.Query_DATA_id(str(session['user_id']))
        user = User(data1['data']['ID'],data1['data']['USERNAME'],data1['data']['PASSWORD'])
        g.User = user


@app.route('/')
def CREATE_DB_TB():
    data_all = []
    system = Certificate_management_system()
    data = system.Create_DB(db_name='certificate_management_system')
    data1 = system.Use(db_name='certificate_management_system')
    data2 = system.Create_TABLE(table_name='ccertificate_management_system')
    data_all.append(data)
    data_all.append(data1)
    data_all.append(data2)
    for i in range(10):
        stri = str(i+20)
        data3 = system.INSERT_DATA(table_name='ccertificate_management_system',user_name=stri,user_pw = 'i am ok',data = '逗你玩的wqqwwq')
        data_all.append(data3)
    return jsonify(data_all)

@app.route('/user/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return "<h1>此处为注册界面！<h1>"
    if request.method == 'POST':
        msg = {
            'code':'',
            'data':'',
            'message':''
        }
        param = json.loads(request.data.decode('utf-8'))
        username = param.get("username","")
        password = param.get("password","")
        if not username :
            msg['code']='999'
            msg['data']='Null'
            msg['message']='账号不能为空！'
            return jsonify(msg)
        elif not password:
            msg['code'] = '999'
            msg['data'] = 'Null'
            msg['message'] = '密码不能为空！'
            return jsonify(msg)
        system = Certificate_management_system()
        data = system.Use(db_name='certificate_management_system')
        data1 = system.Query_DATA(user_name=username)
        # print(data1)
        if data1['code'] =='999':
            data2 = system.INSERT_DATA(table_name='ccertificate_management_system',user_name=username,user_pw=password,data='0')
            return jsonify(data2)
        else :
            return jsonify({'code': '999', 'message': '已有用户名'+username+',请重新输入新的用户名!', 'data':[]})



@app.route('/user/login',methods = ['GET','POST'])
def login():
    if request.method =='GET':
        return "<h1>此处为登录界面！<h1>"
    if request.method == 'POST':
        msg = {
            'code': '',
            'data': '',
            'message': ''
        }
        session.pop("user_id",None)
        param = json.loads(request.data.decode('utf-8'))
        username = param.get("username", "")
        password = param.get("password", "")
        if not username :
            msg['code']='999'
            msg['data']='Null'
            msg['message']='账号不能为空！'
            return jsonify(msg)
        elif not password:
            msg['code'] = '999'
            msg['data'] = 'Null'
            msg['message'] = '密码不能为空！'
            return jsonify(msg)
        system = Certificate_management_system()
        data = system.Use(db_name='certificate_management_system')
        data1 = system.Query_DATA(user_name=username)
        if data1['data']['USERNAME'] == username and data1['data']['PASSWORD'] == password:
            user = User(data1['data']['ID'],password,username)
            session['user_id'] = user.id
            msg['code'] = '200'
            msg['data'] = username
            msg['message'] = username+'登录成功！'
        else:
            msg['code'] = '999'
            msg['data'] = 'NULL'
            msg['message'] = username + '登录失败！'
        return jsonify(msg)

@app.route("/user/profile",methods = ['GET'])
def profile():
    if not g.User:
        return redirect(url_for('login'))
    else :
        return "test successfully！"

@app.route('/user/login-out',methods = ['GET'])
def loginout():
    if "user_id" in session:
        msg = {'code': '200', 'message': str(session['user_id'])+'登出成功', 'data':[]}
        session.pop('user_id', None)
        return jsonify(msg)

@app.route('/user/<name>',methods = ['GET'])
def Get_user(name):
    system = Certificate_management_system()
    data = system.Use(db_name='certificate_management_system')
    data1 = system.Query_DATA(user_name=name)
    return jsonify(data1)


@app.route('/user/<name>',methods = ['POST'])
def Create_user(name,password,data):
    return None

@app.route('/user/<name>',methods = ['PUT'])
def Update_user(name,password,data):
    return None

@app.route('/user/<name>',methods = ['DELETE'])
def Delete_user(name):
    return None








if __name__ =='__main__':
    app.run(port = 8080,debug = True)