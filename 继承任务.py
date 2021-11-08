# #1、定义老手机类，有品牌属性，且属性私有化，提供相应的getXxx与setXxx方法，
# # 提供无返回值的带一个Str类型参数的打电话的方法，内容为：“正在给xxx打电话...”
# #2、定义新手机类，继承老手机类，重写父类的打电话的方法，内容为2句话：“语音拨号中...”、“正在给xxx打电话...”
# # 要求打印“正在给xxx打电话...”这一句调用父类的方法实现，不能在子类的方法中直接打印；提供无返回值的无参数的手机介绍的方法，
# # 内容为：“品牌为：xxx的手机很好用...”
# import time
# class OldPhone:
#     __phoneNumber = ""
#     __voice = ""
#     __address = ""
#     __brand = ""
#     def setphonenumber(self,number):
#         if len(number) != 11:
#             print("号码输入错误")
#         else:
#             self.__phoneNumber =number
#     def getphonenumber(self):
#         return self.__phoneNumber
#
#     def setbrand(self,name):
#         if name != "诺基亚":
#             print("品牌错误")
#         else:
#             self.__brand = name
#     def getbrand(self):
#         return self.__brand
#
#     def call(self,number):
#         print("品牌是",self.__brand,"的手机",self.__phoneNumber,"正在给",number,"打电话！")
#         for i in range(4):
#             print("叮~",end=" ")
#             time.sleep(1)
#         print("对方已接通！")
#
# class NewPhone(OldPhone):
#     def call(self,number):
#         print("语音拨号中",end="")
#         for i in range(3):
#             print(".",end="")
#             time.sleep(1)
#         print("正在给",number,"打电话")
#         for i in range(3):
#             print(".",end="")
#             time.sleep(1)
#         print("对方已接通！")
# phone = NewPhone()
# phone.setphonenumber("13552648187")
# phone.setbrand("诺基亚")
# phone.call("13888465492")

# #1、定义厨师类，有姓名和年龄的属性，且属性私有化，提供相应的getXxx与setXxx方法，提供无返回值的无参数的蒸饭方法；
# #2、定义厨师的子类，该类中要求只能写一个无返回值的无参数的炒菜的方法，其他的方法不能写；
# #3、定义厨师的子类的子类，重写所有父类的方法，每个方法的内容只需打印一句话描述方法的功能即可；(蒸饭，炒菜)
# #4、定义测试类，创建厨师的子类的子类（厨师的孙子类）对象，使用该对象，对厨师类中的姓名和年龄属性赋值，并获取赋值后的属性值打印到控制台上；
#
# class cook:
#     __name = ""
#     __age = 0
#     def setcookname(self,name):
#         if len(name) > 4 and len(name) <= 1 :
#             print("姓名错误")
#         else:
#             self.__name =name
#     def getcookname(self):
#         return self.__name
#     def setage(self,age):
#         if age > 65 and age < 30:
#             print("错误")
#         else:
#             self.__age =age
#     def getage(self):
#         return self.__age
#
#     def steam(self,name):
#         print("这个",self.__age,"岁名叫",self.__name,"的厨师正在蒸",name)
#
# class son (cook):
#
#     def steam(self,name):
#         super().steam(name)
#     def fry(self,name):
#         print("炒",name)
#
# class grandson(son):
#     def steam(self, name):
#         super().steam(name)
#
#     def fry(self,name):
#         super().fry(name)
#
# cook = grandson()
# cook.setcookname("张三")
# cook.setage(40)
# cook.steam("米饭")
# cook.fry("白菜")
# print(cook.getage(),cook.getcookname())


#i.人：年龄，性别，姓名。
class people :
    __age = 0
    __name=""
    __sex =""
    def setage(self,age):
        if age > 100 or age < 0:
            print("？？？")
        else:
            self.__age =age
    def getage(self):
        return self.__age

    def setname(self,name):
        if len(name) > 4 or len(name) < 2:
            print("查无此人")
        else:
            self.__name =name
    def getname(self):
        return self.__name

    def setsex(self,sex):
        if sex !="男" and sex != "女":
            print("？？？")
        else:
            self.__sex =sex
    def getsex(self):
        return self.__sex


#ii.现在有个工种，工人：年龄，性别，姓名 。
# 行为：干活。请用继承的角度来实现该类。
class worker(people):
    def work(self,subject,hour):
        print("我叫", p.getname(), "性别", p.getsex(), "今年", p.getage(),
              "岁,我的职业是",subject,"每天工作",hour,"小时")
#iii.现在有学生这个工种，学生：年龄，性别，姓名，学号。
# 行为：学习，唱歌。请结合上面的几个题目用继承的角度来实现。
class students(people):
    def student(self,subject,number):
        print("我叫", p.getname(), "性别", p.getsex(), "今年", p.getage(), "岁,职业:",
              subject,"学号:",number)
    def study(self,name,hour):
        print(p.getname(),"学习",name,"学了",hour,"小时")
    def sing(self,name,hour):
        print(p.getname(),"唱",name,"歌,唱了",hour,"小时")
p = students()
#1.
p.setage(25)
p.setsex("女")
p.setname("小红")
print("我叫", p.getname(), "性别", p.getsex(), "今年", p.getage(), "岁了")
#2.
# p.work(subject="工人",hour=12)
#3.
p.study("英语",6)
p.sing("黄河",2)
p.student("学生","S001")


























