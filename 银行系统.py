import random
bank={12345678: {'mingzi': 'xh', 'mima': 123456, 'guojia': 'china', 'shengfen': 'hebei', 'jiedao': 'yanshan', 'door': '111', 'qian': 100, 'bank_name': '工商银行'},
      12345677: {'mingzi': 'hc', 'mima': 123456, 'guojia': 'china', 'shengfen': 'hebei', 'jiedao': 'yanshan', 'door': '111', 'qian': 100, 'bank_name': '工商银行'}}
bank_name="工商银行"
print("-------工商银行账户管理系统---------")
print("--------1、开户------------------")
print("--------2、取钱------------------")
print("--------3、存钱------------------")
print("--------4、转账------------------")
print("--------5、查询------------------")
print("--------6、退出------------------")
def bank_add(mingzi,mima,guojia,shengfen,jiedao,door,zhanghao,qian):
  if mingzi in bank:
    return 2
  if len(bank)>5:
    return 3
  bank[mingzi]={
    "zhanghao":zhanghao,
    "mima":mima,
    "guojia":guojia,
    "shengfen":shengfen,
    "jiedao":jiedao,
    "door":door,
    "qian":qian,
    "bank_name":bank_name
}
  return 1
def kaihu():
    mingzi=input("请输入你的用户名")
    mima=int(input("请输入你的密码"))
    print("请输入你的地址")
    guojia= input("\t国际")
    shengfen= input("\t省份")
    jiedao= input("\t街道")
    door= input("\t门牌号")
    zhanghao=random.randint(00000000,99999999)
    qian=0
    kaihu=bank_add(mingzi,mima,guojia,shengfen,jiedao,door,zhanghao,qian)
    if kaihu==1:
        print("添加用户成功，以下是您的信息")
        info='''
           ---------个人信息----------
           -------------------------
           用户名：%s
           账号：%s
           密码：%s
           国籍：%s
           省份：%s
           街道：%s
           开户行名称：%s
           钱： %s   
        '''
        print(info % (mingzi,zhanghao,mima,guojia,shengfen,jiedao,bank_name,qian))
    elif kaihu==2:
        print("用户已经存在")
    elif kaihu==3:
        print("用户库已满")
#
def cunqian_add(zhanghao):
    if zhanghao in bank:
        return 2
    else :
        return 1
def cunqian():
    zhanghao=int(input("请输入你的账号"))
    cunqian=cunqian_add(zhanghao)
    if cunqian==2:
        a=int(input("请输入你要存的钱"))
        bank[zhanghao]["qian"]=bank[zhanghao]["qian"]+a
        print("存钱成功")
        print(bank[zhanghao]["qian"])
    elif cunqian==1:
        print("账号不存在，请重新输入")
#
def quqian_add(a,b,c):
    if a not in bank:
      return 1
    else:
      if  b!=bank[a]["mima"]:
        return 2
      else:
          if c > bank[a]["qian"]:
            return 3
          else:
            return 4
def quqian():
     a = int(input("请输入你的账号"))
     b = int(input("请输入你的密码"))
     c = int(input("请输入要取的钱"))
     quqian = quqian_add(a,b,c)
     if quqian == 1:
      print("账号不存在")
     if quqian == 2:
        print("密码不正确")
     if quqian == 3:
        print("余额不足")
     if quqian == 4:
         bank[a]["qian"] = bank[a]["qian"] - c
         print("余额:",bank[a]["qian"])
#
def zhuanzhang_add(a,b,c,d):
    if  a and b not in bank:
          return 1
    else :
        if c!=bank[a]["mima"]:
            return 2
        else:
           if d >=bank[a]["qian"]:
            return 3
           else :
            return 4
def zhuanzhang():
    a=int(input("请输入您的账号"))
    b=int(input("请输入对方账号"))
    c=int(input("请输入你要转出账户的密码"))
    d=int(input("请输入转出的钱"))
    zhuanzhang = zhuanzhang_add(a,b,c,d)
    if zhuanzhang==1:
        print("账号不存在")
    if zhuanzhang == 2:
        print("密码错误")
    if zhuanzhang ==3:
        print("余额不足")
    if zhuanzhang==4:
        bank[a]["qian"] = bank[a]["qian"] - d
        bank[b]["qian"] = bank[b]["qian"] + d
        print("余额", bank[a]["qian"])
        print("余额",bank[b]["qian"])
#
def chaxun_add(a,b):
    if a not in bank:
        print("用户不存在")
    else:
        if b!=bank[a]["mima"]:
            print("密码错误")
        else:
            print("------以下是您的信息--------")
            info='''
            当前账号：%s
            密码：********
            余额：%s
            国籍：%s
            省份：%s
            街道：%s
            开户行名称：%s
            '''
            print(info %(a,bank[a]["qian"],bank[a]["guojia"],bank[a]["shengfen"],bank[a]["door"],bank_name))
def chaxun():
    a = int(input("请输入你的账号"))
    b = int(input("请输入你的密码"))
    chaxun = chaxun_add(a,b)
#
while True:
    begin=int(input("请选择你的业务"))
    if begin==1:
        kaihu()
    elif begin==2:
        cunqian()
    elif begin==3:
        quqian()
    elif begin==4:
        zhuanzhang()
    elif begin==5:
        chaxun()
    elif begin==6:
        print("退出")
        break
    else:
        print("请重新输入")




