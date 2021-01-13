# -*- coding = utf-8 -*-
# @Time : 2021/1/3 11:01
# @Author : Fang Shang Yang
# @File : api.py
# @Software : PyCharm

from flask import Flask,jsonify,request
from SQL_CRUD import Certificate_management_system
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

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
        return "None"
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



@app.route('/user/<name>',methods = ['GET'])
def Get_user(name):
    system = Certificate_management_system()
    data = system.Use(db_name='certificate_management_system')
    data1 = system.Query_DATA(user_name=name)
    return jsonify(data1)


@app.route('/user/<name>',methods = ['POST'])
def Create_user(name,password,data):
    pass

@app.route('/user/<name>',methods = ['PUT'])
def Update_user(name,password,data):
    pass

@app.route('/user/<name>',methods = ['DELETE'])
def Delete_user(name):
    pass

@app.route('/user/login',methods = ['GET','POST'])
def login():
    pass






if __name__ =='__main__':
    app.run(port = 8080,debug = True)