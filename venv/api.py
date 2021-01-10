# -*- coding = utf-8 -*-
# @Time : 2021/1/3 11:01
# @Author : Fang Shang Yang
# @File : api.py
# @Software : PyCharm

from flask import Flask,jsonify
from SQL_CRUD import Certificate_management_system

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

@app.route('/user/<name>/login',methods = ['GET','POST'])
def login(name):
    pass

if __name__ =='__main__':
    app.run(port = 8080,debug = True)