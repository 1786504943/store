import random
list=["小红","小兰","小绿","小黑","小妹","小张","小三"]
for i in list:
    z=int(input("请选择你要处罚的对象"))
    s=list[z-1]
    x=random.randint(1,50)
    print(s,"被处罚了",x,"遍")
