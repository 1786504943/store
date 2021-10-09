# class person:
#     username=""
#     age=0
#     address=None
#     def da(self,num):
#         super().da(num)
#         print(self.username,"今年",self.age,"岁","来自",self.address,"正再",num)
# a=person()
# a.username="韩聪"
# a.age=20
# b=Arrdress()
# b.country="中国"
# b.provice="北京"
# b.street="昌平"
# b.door="老牛湾"
# b.da("wan")
# a.arrdress=b
# class Arrdress(person):
#     door=""
#     street=""
#     country=""
#     provice=""
#









# '''
# 老手机：
#     打电话：彩铃，手机号
# 新手机：
#     打电话：手机号，彩铃，归属地，大头贴，录音
# '''
# import time
# class Oldphone:
#     phoneNumber=""
#     voice=""
#     def call(self,number):
#         print(self.phoneNumber,"正再打电话给",number,"正再响铃",self.voice)
#         for i in range(5):
#             print(".",end="")
#             time.sleep(1)
#         print("对方已经接通")
#
#
# class Newphone(Oldphone):
#
#     def call(self,number):
#         super().call(number)
#
#         for i in range(5):
#             print(".",end="")
#             time.sleep(1)
#         print("通话完成共用时[05:30]")
# a = Oldphone()
# a.phoneNumber=15713299012
# a.voice="喜洋洋"
# a.call(110)
# b=Newphone()
# b.phoneNumber=1111111
# b.voice="套马杆"
# b.picture="奥力给"
# b.address="日本"
# b.call(119)
#



# 按要求定义类
# 考查知识点：super关键字的使用和继承中方法的调用
# 要求：
# 1、定义老手机类，有品牌属性，且属性私有化，提供相应的getXxx与setXxx方法，提供无返回值的带一个Str类型参数的打电话的方法，内容为：“正在给xxx打电话...”
# 2、定义新手机类，继承老手机类，重写父类的打电话的方法，内容为2句话：“语音拨号中...”、“正在给xxx打电话...”要求打印“正在给xxx打电话...”这一句调用父类的方法实现，不能在子类的方法中直接打印；提供无返回值的无参数的手机介绍的方法，内容为：“品牌为：xxx的手机很好用...”
# 3、定义测试类，创建新手机对象，并使用该对象，对父类中的品牌属性赋值；
# 4、使用新手机对象调用手机介绍的方法；
# 5、使用新手机对象调用打电话的方法；
# import time
# class oldphone:
#     __pinpai=""
#     def setpinpai(self,pinpai):
#         self.__pinpai=pinpai
#     def getpinpai(self):
#         return self.__pinpai
#     def call(self,number):
#         print("正在给",number,"打电话")
#         for i in range(10):
#             print(".",end="")
#             time.sleep(1)
#     def show(self):
#         print("品牌为",self.__pinpai,"的手机很好用")
# class newphone(oldphone):
#     def call(self,number):
#         print("语音拨号中...")
#         super().call(number)
# a=oldphone()
# a.setpinpai("华为")
# a.call(str(input("你要给谁打电话")))
# b=newphone()
# b.call(str(input("你要给谁打电话")))
# a.show()


# 1、定义厨师类，有姓名和年龄的属性，且属性私有化，提供相应的getXxx与setXxx方法，提供无返回值的无参数的蒸饭方法；
# 2、定义厨师的子类，该类中要求只能写一个无返回值的无参数的炒菜的方法，其他的方法不能写；
# 3、定义厨师的子类的子类，重写所有父类的方法，每个方法的内容只需打印一句话描述方法的功能即可；(蒸饭，炒菜)
# 4、定义测试类，创建厨师的子类的子类（厨师的孙子类）对象，使用该对象，对厨师类中的姓名和年龄属性赋值，并获取赋值后的属性值打印到控制台上；
# 5、使用厨师的孙子类对象调用该对象除了getXxx与setXxx以外的其他方法；
# class cooker:
#     __name=""
#     __age=0
#     def setname(self,name):
#         self.__name=name
#     def getname(self):
#         return self.__name
#     def setage(self,age):
#         if age<0 or age>120:
#             print("别瞎输")
#         else:
#             self.__age=age
#     def getage(self):
#         return self.__age
#     def ganma(self,sss):
#         print(a.__name,"正在",sss)
# class erzi(cooker):
#     __name1 = ""
#     def setname1(self,name1):
#         self.__name1=name1
#     def getname1(self):
#         return self.__name1
#     def gan(self,ss):
#         print(b.__name1,"正在",ss)
# class sunzi(erzi):
#     def ganma(self,sss):
#         super().ganma(sss)
#     def gan(self,ss):
#         super().gan(ss)
# a=cooker()
# a.setname("韩聪")
# a.setage(20)
# a.ganma("蒸饭")
# b=erzi()
# b.setname1("王八蛋")
# b.gan("炒菜")
# c=sunzi()
# c.ganma("炒菜")
# c.gan("做饭")
#
#
#





















# i.人：年龄，性别，姓名。
# ii.现在有个工种，工人：年龄，性别，姓名 。行为：干活。请用继承的角度来实现该类。
# class person:
#     name=""
#     age=0
#     sex=""
# class worker(person):
#     def play(self,wan):
#         print(a.name,"正在",wan)
#
# # iii.现在有学生这个工种，学生：年龄，性别，姓名，学号。行为：学习，唱歌。请结合上面的几个题目用继承的角度来实现。
# class stude(person):
#     xuehao=""
#     def chang(self,sss):
#         print("学号为",c.xuehao,"名字叫",a.name,"的同学正在",sss)
#
#     def xue(self, sssb):
#         print("学号为",c.xuehao, "名字叫", a.name, "的同学正在", sssb)
# a = person()
# a.name = "韩聪"
# b = worker()
# b.play("工作")
# c=stude()
# c.xuehao="sb"
# c.chang("唱歌")
# c.xue("学习")
