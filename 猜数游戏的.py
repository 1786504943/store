import random
a=int(input("请充值你的钱"))
if a<1000:
    print("钱不够，请你去充钱 ")
    a = int(input("请充值你的钱"))

ran =random.randint(0,10)
start =int(input("输入1开始游戏，q退出游戏"))
i=0
while i<5:
    i=i+1
    num=int(input("请输入你想输入的数字"))
    if num >ran :
            print("大了")
    if num <ran :
            print("小了")
    elif num==ran:
            print("你对了")
            break
