from DBUtile import select
from DBUtile import update
# import random
# print("-------工商银行账户管理系统---------")
# print("--------1、开户------------------")
# print("--------2、取钱------------------")
# print("--------3、存钱------------------")
# print("--------4、转账------------------")
# print("--------5、查询------------------")
# print("--------6、退出------------------")
# def user_add(account, username, password, country, province, street, door, money, bankname):
#      sql="select  count(*) from user"
#      param =[]
#      data = select(sql,param)
#      sql1 = "select * from user where account=%s"
#      param1 = [account]
#      data = select(sql1, param1)
#      if len(data) >= 100:
#          return 3
#      if len(data)>0:
#          return 2
#      else:
#          sql2 = "insert into user  value(%s,%s,%s,%s,%s,%s,%s,%s,now(),%s)"
#          param2 = [account, username, password, country, province, street, door, money,bankname]
#          update(sql2,param2)
#          return 1
# def kaihu():
#      username = int(input("请输入你的用户名"))
#      password = int(input("请输入你的密码"))
#          print("请输入你的地址")
#         country = input("\t国际")
#         province = input("\t省份")
#         street = input("\t街道")
#         door = input("\t门牌号")
#         account = random.randint(00000000, 99999999)
#         money = 0
#         bankname=input("\t开户行")
#         kaihu= user_add(account, username, password, country, province, street, door, money,bankname)
#         if kaihu == 1:
#             print("添加用户成功，以下是您的信息")
#             info = '''
#                ---------个人信息----------
#                -------------------------
#                用户名：%s
#                账号：%s
#                密码：%s
#                国籍：%s
#                省份：%s
#                街道：%s
#                门牌号：%s
#                钱： %s
#                开户行：%s
#             '''
#             print(info % (username, account,password, country, province, street,door, money,bankname))
#         elif kaihu==2:
#             print("用户已经存在")
#         elif kaihu==3:
#             print("用户库已满")
def cunqian_add(account):
    sql3 = "select * from user where account=%s"
    param3 = [account]
    data = select(sql3, param3)
    if len(data)>0:
        return 2
    else :
        return 1
def cunqian():
    account=int(input("请输入你的账号"))
    cunqian=cunqian_add(account)
    if cunqian==1:
        print("账号不存在，请重新输入")
    if cunqian==2:
        a = input("请输入你要存的钱")
        sql4 = "update user set money=money+%s where account=%s"
        param4 = [a,account]
        update(sql4,param4)





def quqian_add(account,password,money):
    sql5 = "select * from user where account=%s"
    param5 = [account]
    data = select(sql5, param5)
    if len(data) < 0:
      return 1
    else:
        sql6 = "select password from user where account=%s "
        param6=[password]
        data = select(sql6,param6,mode="one")[0]
        if data != password:
            return 2
        else:
            sql7 = "select money from user where account=%s"
            param7=[account]
            data = select(sql7, param7,mode="one")[0]
            if data<money:
                return 3
            else:
                return 4
def quqian():
     account= int(input("请输入你的账号"))
     password = int(input("请输入你的密码"))
     money = int(input("请输入要取的钱"))
     quqian = quqian_add(account,password,money)
     if quqian == 1:
      print("账号不存在")
     if quqian == 2:
        print("密码不正确")
     if quqian == 3:
        print("余额不足")
     if quqian == 4:
         sql8 = "update user set money=money-%s where account=%s"
         param8 = [money, account]
         update(sql8, param8)
#


def zhuanzhang_add(account1,account2,password,money):
    sql9 = "select * from user where account=%s"
    param9 = [account1]
    data1 = select(sql9, param9)
    sql10 = "select * from user where account=%s"
    param10 = [account2]
    data2 = select(sql10, param10)
    if len(data1) < 0 or len(data2) < 0:
        return 1
    else :
        sql11 = "select password from user where account=%s "
        param11 = [password]
        data = select(sql11, param11, mode="one")[0]
        if data != password:
            return 2
        else:
            sql12 = "select money from user where account=%s"
            param12 = [account1]
            data = select(sql12, param12, mode="one")[0]
            if data < money:
                return 3
            else :
                return 4
def zhuanzhang():
    account1=int(input("请输入您的账号"))
    account2=int(input("请输入对方账号"))
    password=int(input("请输入你要转出账户的密码"))
    money=int(input("请输入转出的钱"))
    zhuanzhang = zhuanzhang_add(account1,account2,password,money)
    if zhuanzhang==1:
        print("账号不存在")
    if zhuanzhang == 2:
        print("密码错误")
    if zhuanzhang ==3:
        print("余额不足")
    if zhuanzhang==4:
        sql13 = "update user set money=money-%s where account=%s"
        param13 = [money, account1]
        update(sql13, param13)
        sql14 = "update user set money=money+%s where account=%s"
        param14 = [money, account2]
        update(sql14, param14)
def chaxun_add(account,password):
    sql5 = "select * from user where account=%s"
    param5 = [account]
    data = select(sql5, param5)
    if len(data) < 0:
        print("用户不存在")
    else:
        sql6 = "select password from user where account=%s "
        param6 = [password]
        data = select(sql6, param6, mode="one")[0]
        if data != password:
            print("密码错误")
        else:
            sql35 = "select * from user where account=%s"
            param35 = [account]
            data = select(sql35, param35)
            print("------以下是您的信息--------")
            info = '''
                            ---------个人信息----------
                            -------------------------
                            用户名：%s
                            账号：%s
                            密码：%s
                            国籍：%s
                            省份：%s
                            街道：%s
                            门牌号：%s
                            钱： %s
                            开户行：%s
                         '''
            print(info % (username, account,password, country, province, street,door, money,bankname))
def chaxun():
    account = int(input("请输入你的账号"))
    password = int(input("请输入你的密码"))
    chaxun = chaxun_add(account,password)



while True:
    begin=int(input("请选择你的业务"))
    if begin==1:# kaihu()
        print()
    elif begin==2:
        cunqian()
    elif begin==3:
        quqian()
    elif begin==4:
        zhuanzhang()
    elif begin==5:
       print()
    elif begin==6:
        print("退出")
        break
    else:
        print("请重新输入")
