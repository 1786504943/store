# class person:
#     username=""
#     age=0
#     high=0
#
#     def eat(self,eatname):
#         print(self.username,"正在吃",eatname)
#     def play(self,playname):
#         print(self.username,"正在玩",playname)
#     def watch(self,watchname):
#         print(self.username,"正在看",watchname)
# a=person()
# a.username="韩聪"
# a.high=150
# a.age=100
#
# a.eat("饭")
# a.play("王者")
# a.watch("洗衣液")
# '''
# 封装：1.将属性隐藏，不对外开放
#    __属性
#      2.提供方法用于间接赋值
#       setxxx 用于赋值,git用于取值
# '''
# class person:
#     __username=""
#     __age=0
#     __high=0
#     __computer=""
#     def setusername(self,username):
#         self.__username=username
#     def getusername(self):
#         return self.__username
#
#
#     def setage(self,age):
#         if age<0 or age >120:
#             print("别瞎输")
#         else:
#             self.__age=age
#     def getage(self):
#         return  self.__age
#     def sethigh(self,high):
#         if high <0.3 or high >2.6:
#             print("别瞎输")
#         else:
#             return self.__high
#     def eat(self, eatname):
#         print(self.__username,"正在吃",eatname)
#     def play(self,playname):
#         print(self.__username,"正在玩",playname)
#     def watch(self,watchname):
#         print(self.__username,"正在看",watchname)
# a = person()
# a.setusername("韩聪")
# a.setage(10)
# a.sethigh(2)
#
# a.eat("饭")
# a.play("王者")
# a.watch("洗衣液")

# 分析一个水杯的属性和功能，使用类描述并创建对象

class shuibei:
    __high=0
    __color=""
    __rongji=0
    __caizhi=""
    def sethigh(self,high):
        if high<0.3 or high>2.6:
            print("别瞎输")
        else:
            self.__high=high
    def gethigh(self):
        return self.__high


    def setcolor(self,color):
        self.__color=color
    def getcolor(self):
        return self.__color


    def setrongji(self,rongji):
        if rongji<0:
            print("别瞎输")
        else:
            self.__rongji=rongji
    def getrongji(self):
        return self.__rongji



    def setcaizhi(self, caizhi):
        self.__caizhi = caizhi
    def getcaizhi(self):
        return self.__caizhi


    def yeti(self,yetiname):
        print("这是一个高度为",self.__high,"的",yetiname,"的杯子")
    def xu(self,xu123):
        print("这是一个",self.__color,xu123,"的杯子 ")
    def rongji(self,rongji123):
        print("这是一个容积为",self.__rongji,rongji123,"的杯子")
a=shuibei()
a.setrongji(10)
a.setcolor("黄色")
a.sethigh(1.3)
a.yeti("可以存放液体")
a.xu("可以存放液体")
a.rongji("可以存放液体")




# 有笔记本电脑（屏幕大小，价格，cpu型号，内存大小，待机时长），行为（打字，打游戏，看视频）
class computer:
    __daxiao=""
    __jiage=""
    __cpu=""
    __neicun=""
    __daiji=""
    def setdaxiao(self,daxiao):
        if daxiao>100 or daxiao<10:
            print("别瞎输")
        else :
            self.__daxiao=daxiao
    def getdaxaio(self):
        return self.__daxiao
    def setjiage(self,jiage):
        if jiage>1000000 or jiage <1000:
            print("别瞎输")
        else:
            self.__jiage=jiage
    def getjiage(self):
        return self.__jiage
    def setcpu(self,cpu):
        self.__cpu=cpu
    def getcpu(self):
        return self.__cpu
    def setneicun(self,neicun):
        self.__neicun=neicun
    def getneicun(self):
        return self.__neicun
    def setdaiji(self,daiji):
        if daiji<0 or daiji >100:
            print("别瞎输")
        else:
            self.daiji=daiji
    def getdaiji(self):
        return self.daiji
    def dazi(self, dazina):
        print("屏幕大小为",self.__daxiao,"可以",dazina)
    def wa(self,playname):
        print("价格为",self.__jiage,"可以",playname)
    def watch(self,watchname):
        print("剩余",self.__neicun,"可以",watchname)
a=computer()
a.setdaxiao(90)
a.setneicun(100)
a.setjiage(1000)
a.dazi("打字")
a.wa("玩游戏")
a.watch("看电视")




