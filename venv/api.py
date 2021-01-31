# -*- coding = utf-8 -*-
# @Time : 2021/1/3 11:01
# @Author : Fang Shang Yang
# @File : api.py
# @Software : PyCharm

from flask import Flask,jsonify,request,redirect
from SQL_CRUD import Certificate_management_system
import json


from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity
)


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'odmbryqoshrmffogowegxh'
jwt = JWTManager(app)










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


@app.route('/user/login', methods=['POST','GET'])
def login():
    if request.method == 'GET':
        return "<h1>此处为注册界面！<h1>"
    if request.method == 'POST':
        msg = {
            'code': '',
            'data': '',
            'message': ''
        }
        param = json.loads(request.data.decode('utf-8'))
        username = param.get('username', "")
        password = param.get('password', "")
        if not username:
            msg['code'] = '999'
            msg['data'] = 'Null'
            msg['message'] = '账号不能为空！'
            return jsonify(msg)
        elif not password:
            msg['code'] = '999'
            msg['data'] = 'Null'
            msg['message'] = '密码不能为空！'
            return jsonify(msg)
        system = Certificate_management_system()
        data = system.Use(db_name='certificate_management_system')
        data1 = system.Query_DATA(user_name=username)
        data2 = system.Query_DATA_pw(password=password)
        # print(data1)
        if data1['code'] == '999' or data2['code'] == '999':
            msg['code'] = '999'
            msg['data'] = 'Null'
            msg['message'] = '请仔细检查账号密码！'
        else:
            ret = {
                'access_token': create_access_token(identity=username),
                'refresh_token': create_refresh_token(identity=username)
            }
            msg['code'] = '200'
            msg['data'] = ret
            msg['message'] = '用户'+username+'登录成功！'
        return jsonify(msg)


@app.route("/user/test",methods = ['GET'])
@jwt_required
def test():
    username = get_jwt_identity()
    if username:
        return jsonify({'code': '200', 'message': '现在用户'+username+'正在登录', 'data':[]})
    else:
        return jsonify({'code': '200', 'message': '暂无用户处于登录状态.', 'data': []})

@app.route('/user/refresh', methods=['GET'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    ret = {
        'access_token': create_access_token(identity=current_user)
    }
    return jsonify({'code': '200', 'message': '重新获取token!', 'data': ret})

@app.route('/user/<name>',methods = ['GET'])
def Get_user(name):
    system = Certificate_management_system()
    data = system.Use(db_name='certificate_management_system')
    data1 = system.Query_DATA(user_name=name)
    return jsonify(data1)

@jwt.invalid_token_loader
def invalid_token_callback(identity):
    return jsonify({'code': '999', 'message': identity, 'data': []})

@jwt.expired_token_loader
def expired_token_callback(identity):
    return jsonify({'code': '999', 'message': identity, 'data': []})

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