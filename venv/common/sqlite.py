# -*- coding = utf-8 -*-
# @Time : 2021/3/10 13:30
# @Author : Fang Shang Yang
# @File : rest_base.py
# @Software : PyCharm

import sqlite3



class Sqlite(object):
    def __init__(self):
        self.conn = sqlite3.connect(r'D:\Final_work\venv\test.db')
        self.c = self.conn.cursor()
        self.conn.execute("PRAGMA foreign_keys = ON;")  # 设立外键选项

    def __del__(self):
        self.c.close()
        self.conn.close ()
    def create_table_management(self):
        self.c.execute('''CREATE TABLE certificate_management_system
               (ID INTEGER PRIMARY KEY  autoincrement,
                USERNAME CHAR(25) UNIQUE,
                PASSWORD CHAR(25) NOT NULL,
                Image TEXT,
                Content TEXT,
                FOREIGN KEY(USERNAME) REFERENCES permission(USERNAME)
               );''')

    def create_table_permission(self):
        self.c.execute('''CREATE TABLE permission
                       (
                        USERNAME CHAR(25) UNIQUE,
                        PERMISSION INTEGER
                       );''')

    def c_management(self,values):  # insert
        try:
            self.c.execute("insert into certificate_management_system values (?,?,?,?,?);", (None, values[0],values[1],values[2],values[3]))
            self.conn.commit()
            return 1
        except:
            return -1

    def c_permission(self,values): # insert
        try:
            self.c.execute("insert into permission values (?,?);",
                           (values[0],values[1]))
            self.conn.commit()
            return 1
        except:
            return -1

    def r_management(self,username):  #select
            self.c.execute('select * from certificate_management_system where USERNAME=?;', (username,))
            values = self.c.fetchall()
            self.conn.commit()
            if values == []:
                return -1
            else:
                return values,1

    def r1_management(self,password): #select
            self.c.execute('select * from certificate_management_system where PASSWORD=?;', (password,))
            values = self.c.fetchall()
            self.conn.commit()
            if values == []:
                return -1
            else:
                return values,1
    def r_permission(self,username):
            self.c.execute('select * from permission where USERNAME=?;',(username,));
            values = self.c.fetchall()
            self.conn.commit()
            if values == []:
                return -1
            else:
                return values, 1

    def u_management(self,values):  #update,new_password,username
        try:
            self.c.execute('update certificate_management_system set PASSWORD=?  where USERNAME=?;', (values[0],values[1]))
            self.conn.commit()
            return 1
        except:
            return -1

    def d_management(self,username):  #delete
         try:
            self.c.execute('delete from certificate_management_system where USERNAME=?;', (username,))
            self.conn.commit()
            return 1
         except:
             return -1
    def d_permission(self,username):
        try:
            self.c.execute('delete from permission where USERNAME = ?;',(username,))
            self.conn.commit()
            return 1
        except:
            return -1
    def delete_table(self,table):
        try:
            self.c.execute('drop table if exists '+table+';')
            self.conn.commit()
            return 1
        except:
            return -1
#
# if __name__ == '__main__':
#     a = Sqlite()
#     a.delete_table("certificate_management_system")
#     a.delete_table("permission")
    # print(a.create_table_management())
    # print(a.create_table_permission())
    # print(a.c_management(["admin", "123456", "0", "0"]))
    # print(a.c_management(["afyy", "123456", "0", "0"]))
    # print(a.c_management(["lwj", "123456", "0", "0"]))
    # print(a.r_management("admin")[1])
    # print(a.u_management(["123456", "afyy"]))
    # print(a.create_table_permission())
    #
    # print(a.c_permission(["aa",8]))
    # print(sqlite3.version)
    # print(a.r_permission("afyy")[1])
    # del a

