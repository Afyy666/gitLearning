import configparser
import os
from common import sqlite


class ConfigPick():
    def __init__(self):
        root_dir = os.path.dirname(os.path.abspath('config_load.py'))  # 获取当前文件所在目录的上一级目录
        self.cf = configparser.ConfigParser()
        self.cf.read(root_dir+"/data/config.ini")  # 拼接得到config.ini文件的路径，直接使用
        print(root_dir+"/data/config.ini")
        self.stream = None

    def __del__(self):
        pass

    def config_loads_database(self):
        try:
            options = self.cf.get("database_table_url", "table_permission")
            options1 = self.cf.get("database_table_url", "table_management")
            system= sqlite.Sqlite()
            system.create_table_permission()
            system.create_table_management()
            list1 = []
            self.stream = open(file=options,encoding='utf-8')
            text = self.stream.readlines()
            for content in text:
                content = content.split('、')
                data = system.c_permission(content)
                if data == 1:
                    msg = "permission数据表角色"+content[0]+"初始化成功！"

                else:
                    msg = "permission数据表角色"+content[0]+"初始化失败！"
                list1.append(msg)

            self.stream = open(file=options1, encoding='utf-8')
            text = self.stream.readlines()
            for content in text:
                content = content.split('、')
                data = system.c_management(content)
                if data == 1:
                    msg = "management数据表角色"+content[0] + "初始化成功！"
                else:
                    msg = "management数据表角色"+content[0]+"初始化失败!"
                list1.append(msg)
            self.stream.close()
            return list1
        finally:
            if self.stream:
                self.stream.close()

# if __name__ == '__main__':
#     k = ConfigPick()
#     k.config_loads_database()