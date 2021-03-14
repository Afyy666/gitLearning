

#使用2的幂表示权限，可以让每种不同权限的组合对应的值是唯一的
class Permission:
    FOLLOW = 1     #关注用户
    COMMENT = 2    #查看证书内容
    WRITE = 4      #生成、修改证书
    WODERATE = 8   #查看他人的证书
    ADMIN = 16     #管理员权限


class user_loads(Permission):
    def __init__(self,username,permission):
        self.username = username
        self.permission = permission

    def __del__(self):
        pass

    def add_permission(self,perm):
        if not self.has_permission(perm):
            self.permission += perm

    def remove_permission(self,perm):
        if self.has_permission(perm):
            self.permission -= perm

    def reset_permission(self):
        self.permission = 0

    def has_permission(self,perm):
        return self.permission & perm == perm

# if __name__ == '__main__':
#     user = user_loads("afyy",Permission.ADMIN)
#     print(user.has_permission(16))