#空调
import time
class aircondition:
    __brand=""
    __Price=0

    def setbrand(self,brand):
        if brand != "美的" and brand != "格力":
            print("没有这个品牌的空调？")
        else:
            self.__brand = brand
    def getbrand(self):
        return self.__brand

    def setprice(self,price):
        if price > 5000 or price < 2000:
            print("没有这个价位的空调")
        else:
            self.__Price =price
    def getprice(self):
        return self.__Price

    def mach(self):
        print("这是",self.__brand,"品牌的空调,价格为：",self.__Price,"元")

    def open(self,name):
        print("打开名为",name,"的空调")
        print ("【空调开机了",end="")
        for i in range(3):
            print(".", end="")
            time.sleep(1)
        print("】！")

    def shut(self,name):
        print("关闭名为",name,"的空调")
        print ("【空调将在",sd,"分钟后关闭",end="")
        for i in range(int(2)):
            print(".", end="")
            time.sleep(1)
        print("】！")

a=aircondition()
# a.brand = "美的"
# a.Price = 3000
a.setbrand("美的")
a.setprice(3000)
a.mach()
sd = int(30)
a.open("美的")
a.shut("美的")

#i.定义了一个学生类：属性:学号，姓名，年龄，性别，身高，体重，成绩，家庭地址，电话号码。
# 行为：学习（要求参数传入学习的时间），玩游戏（要求参数传入游戏名），编程（要求参数传入写代码的行数），
# 数的求和（要求参数用变长参数来做，返回求和结果）
import time
class student:
    __number=""
    __name=""
    __age=0
    __sex=""
    __high=0.00
    __weight=0.00
    __secore=0
    __address=""
    __phone=0
    def setnumber(self,number):
        if number != "s001"and number!="s002"and number !="s003" :
            print("没有这个学号？")
        else:
            self.__number = number
    def getnumber(self):
        return self.__number

    def setname(self,name):
        if name!="张三"and name !="李四" and name !="王五":
            print("没有这个学生")
        else:
            self.__name =name
    def getname(self):
        return self.__name

    def setage(self,age):
        if age > 23 or age < 18:
            print("没有这个年龄段的学生")
        else:
            self.__age =age
    def getage(self):
        return self.__age

    def setsex(self,sex):
        if sex!="男" and sex != "女":
            print("？？？")
        else:
            self.__sex =sex
    def getsex(self):
        return self.__sex

    def sethigh(self,high):
        if high > 2 or high<1.5:
            print("没有这个身高的人")
        else:
            self.__high =high
    def gethigh(self):
        return self.__high

    def setweight(self,weight):
        if weight>300 or weight < 60:
            print("没有这个体重的学生")
        else:
            self.__weight =weight
    def getweight(self):
        return self.__weight

    def setsecore(self,secore):
        if secore>100 or secore < 0 :
            print("???假的吧？？？")
        else:
            self.__secore =secore
    def getsecore(self):
        return self.__secore

    def setaddress(self,address):
        if address!="北京市":
            print("不是我们的学生")
        else:
            self.__address =address
    def getaddress(self):
        return self.__address

    def setphone(self,phone):
        if len(phone) != 11:
            print("电话号码错误")
        else:
            self.__phone =phone
    def getphone(self):
        return self.__phone

    def showMe(self):
        print("我叫", self.__name, "今年", self.__age, "岁，身高", self.__high, "米！体重",self.__weight,
        "我是", self.__sex,"生,学号",self.__number,"成绩",self.__secore,"住在",self.__address,
        "电话是",self.__phone)


    def study(self,subject,hour):
        print(self.__name,"学习了",subject,hour,"小时" )

    def game(self,gamename,hour):
        print(self.__name,"玩",gamename,"游戏",hour,"小时")
        print("【欢迎来到德莱联盟",end="")
        for i in range(2):
            print(".",end="")
            time.sleep(1)
        print("】！")

    def programming(self,programmingname,hour):
        print(self.__name,"学了",programmingname,"编程",hour,"小时")

s=student()

s.setnumber("s001")
s.setname("张三")
s.setage(21)
s.setsex("男")
s.sethigh(1.80)
s.setweight(180)
s.setsecore(90)
s.setaddress("北京市")
s.setphone("12058435521")
s.showMe()

s.study("英语",3)
s.game("英雄联盟",4)
s.programming("python",6)








































