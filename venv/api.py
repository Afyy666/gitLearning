# -*- coding = utf-8 -*-
# @Time : 2021/1/3 11:01
# @Author : Fang Shang Yang
# @File : api.py
# @Software : PyCharm

from flask import Flask,jsonify,request,redirect
# from SQL_CRUD import Certificate_management_system
from common import sqlite,utils_networks,user_permission,config_load
import json
import datetime


from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity
)

user = user_permission.user_loads("NULL","NULL")  #空用户


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'afyyno1'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(minutes=20)
app.config['JWT_REFRESH_TOKEN_EXPIRES']= datetime.timedelta(days=10)
jwt = JWTManager(app)



@app.route('/')
def CREATE_DB_TB():
    a = config_load.ConfigPick()
    list_load = a.config_loads_database()
    list_load1 = []
    for load in list_load:
        list_load1.append(utils_networks.code_word("200","NULL",load))
    return jsonify(list_load1)



@app.route('/user/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return "<h1>此处为注册界面！<h1>"
    if request.method == 'POST':
        param = json.loads(request.data.decode('utf-8'))
        username = param.get("username","")
        password = param.get("password","")
        if not username :
            return utils_networks.code_word("999","NULL","账号不能为空！")
        elif not password:
            return utils_networks.code_word("999", "NULL", "密码不能为空！")
        system = sqlite.Sqlite()
        data = system.r_management(username)
        print(data)
        if data == -1:
            data2 = system.c_permission([username, 7])
            data1 = system.c_management([username,password,"0","0"])
            return utils_networks.code_word("200","","用户名"+username+"注册成功！")
        else :
            return utils_networks.code_word("999","","已有用户名"+username+"请重新输入！")


@app.route('/user/login', methods=['POST','GET'])
def login():
    if request.method == 'GET':
        return "<h1>此处为注册界面！<h1>"
    if request.method == 'POST':
        param = json.loads(request.data.decode('utf-8'))
        username = param.get('username', "")
        password = param.get('password', "")
        if not username:
            return utils_networks.code_word("999", "NULL", "账号不能为空！")
        elif not password:
            return utils_networks.code_word("999", "NULL", "密码不能为空！")
        system = sqlite.Sqlite()
        data1 = system.r_management(username)
        data2 = system.r1_management(password)
        # print(data1)
        if data1 == -1 or data2 == -1:
            return utils_networks.code_word("999","NULL","账号密码错误，请检查！")
        else:
            ret = {
                'access_token': create_access_token(identity=username),
                'refresh_token': create_refresh_token(identity=username)
            }
            user.username = get_jwt_identity()
            user.permission = system.r_permission(username)[0][0][1]
            return utils_networks.code_word("200",ret,"登录成功！")

@app.route("/admin",methods=['GET'])
@jwt_required
def admin():
    username = get_jwt_identity()
    if username == 'admin':
        msg = '管理员' + username + '正在访问'
        return utils_networks.code_word("200", "NULL", msg)
    else:
        return utils_networks.code_word("403", "NULL", "非管理员，无权限登录！")


@app.route('/user/<name>',methods = ['GET'])
@jwt_required
def test(name):
    username = get_jwt_identity()
    msg = '用户'+username+'正在访问'+name+'主页.'
    return utils_networks.code_word("200","NULL",msg)



@app.route('/user/<name>/<certificate_name>',methods = ['GET'])
@jwt_required
def test1(name,certificate_name):
    username = get_jwt_identity()
    if name == username:
        msg = '正在查看'+certificate_name+'证书内容.'
        return utils_networks.code_word("200","NULL",msg)
    else:
        msg = username + '正在访问' +name+'的'+certificate_name+'内容.'
        if user.has_permission(user_permission.Permission.WODERATE):
            return utils_networks.code_word("200","NULL",msg)
        else:
            return utils_networks.code_word("403", "NULL", '当前无权限访问他人证书内容.')



@app.route('/refresh', methods=['GET'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    ret = {
        'access_token': create_access_token(identity=current_user)
    }
    return utils_networks.code_word("200",ret,"重新获取access_token成功！")


@app.route('/user/<name>',methods = ['GET'])
@jwt_required
def Get_user(name):
    system = sqlite.Sqlite()
    data = system.r_management(name)[0]
    return utils_networks.code_word("200",data,name)


@jwt.invalid_token_loader
def invalid_token_callback(identity):
    return jsonify({'code': '999', 'message': identity, 'data': 'access_token过期！'})

@jwt.expired_token_loader
def expired_token_callback(identity):
    return jsonify({'code': '999', 'message': identity, 'data': 'refresh_token过期！'})

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