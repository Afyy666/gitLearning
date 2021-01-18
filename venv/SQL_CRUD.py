# -*- coding = utf-8 -*-
# @Time : 2021/1/3 10:47
# @Author : Fang Shang Yang
# @File : Sql_connect.py
# @Software : PyCharm

from pymysql import connect
from pymysql.cursors import DictCursor

class Certificate_management_system(object):
    def __init__(self):
        self.conn = connect(
            port = 3306,
            user = 'root',
            password = 'root',

        )
        self.cursor = self.conn.cursor(DictCursor)
    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def Create_DB(self,db_name):
        create_db_sql = 'CREATE DATABASE IF NOT EXISTS '+db_name+' CHARACTER SET UTF8'
        try:
            self.cursor.execute(create_db_sql)
            results = self.cursor.fetchone()
            result = {'code': '200', 'message': '登入/创建数据库'+db_name+'成功!', 'data': results}
            self.conn.commit()
            return result
        except :
            return {'code': '999', 'message': '登入/创建数据库'+db_name+'失败!', 'data': []}

    def Use(self,db_name):
        use_sql = 'use '+db_name
        try:
            self.cursor.execute(use_sql)
            results = self.cursor.fetchone()
            result = {'code': '200', 'message': '切换到数据库'+db_name+'成功!', 'data': results}
            self.conn.commit()
            return result
        except:
            pass

    def Create_TABLE(self,table_name):
        create_table_sql = 'CREATE TABLE IF NOT EXISTS '+table_name+'(ID INT PRIMARY KEY auto_increment,USERNAME VARCHAR (25) NOT NULL UNIQUE,PASSWORD VARCHAR(25) NOT NULL,DATA VARCHAR (255))'
        try:
            self.cursor.execute(create_table_sql)
            results = self.cursor.fetchone()
            result = {'code': '200', 'message': '登入/创建数据表'+table_name+'成功!', 'data': results}
            self.conn.commit()
            return result
        except :
            return {'code': '999', 'message': '登入/创建数据表'+table_name+'失败!', 'data': []}

    def Delete_DB(self,db_name):

        delete_db_sql ='DROP DATABASE IF EXISTS '+db_name
        try:
            self.cursor.execute(delete_db_sql)
            results = self.cursor.fetchone()
            result = {'code': '200', 'message': '删除数据库'+db_name+'成功!', 'data': results}
            self.conn.commit()
            return result
        except:
            return {'code': '999', 'message': '删除数据库'+db_name+'成功！', 'data': []}

    def Delete_TABLE(self,table_name):

        delete_table_sql = 'DROP TABLE IF EXISTS ' + table_name
        try:
            self.cursor.execute(delete_table_sql)
            results = self.cursor.fetchone()
            result = {'code': '200', 'message': '删除数据表' + table_name + '成功!', 'data': results}
            self.conn.commit()
            return result
        except:
            return {'code': '999', 'message': '删除数据表' + table_name + '失败！', 'data': []}

    def INSERT_DATA(self,table_name,user_name,user_pw,data):
        insert_data_sql = 'INSERT INTO '+table_name+"(USERNAME,PASSWORD,DATA) VALUES ('"+user_name+"','"+user_pw+"','"+data+"')"
        try:
            self.cursor.execute(insert_data_sql)
            result = {'code': '200', 'message': '插入数据 username='+user_name+'成功!', 'data': 'username: '
                      + user_name+', user_pw: '+user_pw+', user_data: '+data}
            self.conn.commit()
            return result
        except :
            return {'code': '999', 'message': '插入数据 username='+user_name+'失败!', 'data': []}
    def Query_DATA(self,user_name):
        query_sql = "SELECT * FROM ccertificate_management_system WHERE USERNAME= '"+user_name+"'"
        self.cursor.execute(query_sql)
        results = self.cursor.fetchone()
        self.conn.commit()
        if not results:
            result = {'code': '999', 'message': '查询' + user_name + '失败!', 'data': []}
        else:
            result = {'code': '200', 'message': '查询' + user_name + '成功！', 'data': results}
        return result
    def Query_DATA_id(self,id):
        query_sql = "SELECT * FROM ccertificate_management_system WHERE ID= '" + id+"'"
        self.cursor.execute(query_sql)
        results = self.cursor.fetchone()
        self.conn.commit()
        if not results:
            result = {'code': '999', 'message': '查询' + id + '失败!', 'data': []}
        else:
            result = {'code': '200', 'message': '查询' + id + '成功！', 'data': results}
        return result
    def Update_DATA(self):
        pass

