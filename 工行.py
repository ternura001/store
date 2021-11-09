from DBUtils import update
from DBUtils import select
import random

class bank:
    __name = ""
    __password = ""
    __country=""
    __province=""
    __steert=""
    __door=""
    __money=0

def setname(self, name):
    if len(name) > 4 or len(name) < 2:
        print("？？？")
    else:
        self.__name = name

def getname(self):
    return self.__name

def setpassword(self, password):
    if type(password) != int and len(password) != 6:
        print("密码输入错误")
    else:
        self.__password = password

def getpassword(self):
    return self.__password

def setcountry(self, country):
    self.__country = country

def getcountry(self):
    return self.__country

def setprovince(self, province):
    self.__province = province

def getprovince(self):
    return self.__province

def setsteertce(self, steertce):
    self.__steertce = steertce

def getsteertce(self):
    return self.__steertce

def setdoorce(self, doorce):
    self.__doorce = doorce

def getdoorce(self):
    return self.__doorce

def setmoney(self, money):
    if money<0:
        print("???")
    else:
        self.__money = money

def getmoney(self):
    return self.__money

def showtime():
        print("***************************")
        print("*    中国工商银行          *")
        print("*     账户管理系统         *")
        print("***************************")
        print(" ")
        print("*1、开户                   *")
        print("*2、存钱                   *")
        print("*3、取钱                   *")
        print("*4、转账                   *")
        print("*5、查询                   *")
        print("*6、欢迎下次光临             *")
        print("***************************")
#初始化银行
# bank={}
#'Frank': {'account': 24275182, 'password': '123456', 'country': '中国', 'province': '山东', 'steert': '曹县', 'door': '001', 'money': 0, 'bank_name': '保熟银行'}
#定义一个开户银行
bank_name="保熟银行"

#定义添加到银行 定义函数元素对应元素  不是名称对名称
def bankadd(self,account):
    sql = "select count(*) from user"
    param = []
    data = select(sql,param,mode="one")
    if data[0] >= 100:
        return 3


    sql1 = "select * from user where name = %s"
    param1 = [self.__name]
    data1 = select(sql1, param1)  # ((),)
    if len(data1) >= 1:
        return 2

    sql2 = "insert into user value(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param2 = [account,self.__name,self.__password,self.__country, self.__province, self.__steert, self.__door, self.__money, self.__bank_name]
    update(sql2, param2)
    return 1

def cqadd(self):
    sql1 = "select * from user where name = %s"
    param1 = [self.__name]
    data1 = select(sql1, param1)
    if len(data1) >= 1:
        sql2 = "update user set money=money+%s where name=%s "
        song=int(input("请输入您要存入的金额："))
        param2 = [song,self.__name]
        update(sql2, param2)
        return True
    else:
        return False

def qxadd(self):
    sql3 = "select * from user where name = %s and password=%s"
    param3 = [self.__name,self.__password]
    data3 = select(sql3, param3)  # ((),)
    if len(data3) >= 1:
        sql4="select money from user where name = %s"
        param4=[self.__name]
        data4=select(sql4,param4)
        for i in data4:
            print(i)

        song1=int(input("请输入您要取出的金额："))

        sql1="select money from user where money>%s"
        param1=[song1]
        data1=select(sql1,param1)
        if len(data1)==0:
            return 3
        elif len(data1)>=1:
            sql5 = "update user set money=money-%s where name = %s"
            param5 = [song1,self.__name]
            update(sql5, param5)
            return 0
    sql6 = "select * from user where name = %s "
    param6 = [self.__name]
    data6 = select(sql6, param6)  # ((),)
    if len(data6)==0:
        return 1
    sql7 = "select * from user where password = %s "
    param7 = [self.__password]
    data7 = select(sql7, param7)  # ((),)
    if len(data7) == 0:
        return  2

def zzadd(self):
    sql3 = "select * from user where name = %s "
    param3 = [self.__zhuanchuname]
    data3 = select(sql3, param3)
    sql1 = "select * from user where name = %s "
    param1 = [self.__zhuanruname]
    data1 = select(sql1, param1)
    sql2 = "select * from user where password = %s "
    param2 = [self.__password]
    data2 = select(sql2, param2)
    if len(data3)>=1 and len(data1)>=1:
        if len(data2)>=1:
            zhuanrumoney = int(input("请输入您要转出的金额："))
            sql7 = "select * from user where money>%s "
            param7 = [zhuanrumoney]
            data7 = select(sql7, param7)
            if len(data7) < 0:
                return 3
            elif len(data7) >=1:
                sql4 = "update user  set money=money+%s where name=%s "
                param4 = [zhuanrumoney,self.__zhuanruname]
                update(sql4, param4)
                sql5 = "update user set money=money-%s where name=%s "
                param5 = [zhuanrumoney,self.__zhuanchuname]
                update(sql5, param5)
                return 0
    if len(data3)< 1 and len(data1) < 1:

        return 1
    if len(data2) <1:
        return 2

def cxadd(self):
    sql3 = "select * from user where name = %s "
    param3 = [self.__name]
    data3 = select(sql3, param3)
    sql2 = "select * from user where password = %s "
    param2 = [self.__password]
    data2 = select(sql2, param2)
    if len(data3)>=1 and len(data2)>=1:
        return 0
    elif len(data3)==0:
        return 1
    elif len(data2)==0:
            return 2

#定义用户入参
def useradd(self):
    p=bank()
    account=random.randint(10000000,99999999)
    p.setname=(input("请输入您的名称"))
    p.setpassword=(int(input("请输入您的密码")))
    print("请输入你的详细信息")
    p.setcountry=(input("\t\t请输入您的国籍"))
    p.setprovince=(input("\t\t请输入您的省份"))
    p.setsteert=(input("\t\t请输入您的街道"))
    p.setdoor=(input("\t\t请输入您的门牌号"))
    p.setmoney=(0)
    num = bankadd(self.__name,account)
    if num ==3:
        print("本银行已满请到其他银行开户")
    elif num== 2:
        print("用户已存在")
    elif num==1:
        print("恭喜你开户成功，以下是您的相信信息")
        sql3 = "select account 账号,name 姓名,password 密码,country 国家,province 省份,steert 街道,door 门牌号,money 货币,bankename 银行名称 from user where name = %s"
        param3 = [self.__name]
        data3 = select(sql3, param3)
        print("账号:",account
          ,"姓名:",self.__name
          ,"密码:",self.__password
          ,"国家:",self.__country
          ,"省份:",self.__province
          ,"街道:",self.__steert
          ,"门牌号:",self.__door
          ,"货币:",self.__money
          ,"银行名称:",bank_name
          )
def cunqianadd(self):
    p=bank()
    p.setname=(input("请输入您的姓名："))
    num1=cqadd(self.__name)
    if num1==False:
        print("银行没有该用户信息")
    elif num1==True:
        sql3 = "select * from user where name = %s "
        param3 = [self.__name]
        data3 = select(sql3, param3)
        for i in data3:
            print(i)

def quxianadd(self):
    p=bank()
    p.name = (input("请输入您的姓名："))
    p.password = (int(input("请输入您的用户密码：")))
    num2 = qxadd(self.__name)

    if num2==1:
        print("账户信息不存在")
    elif num2==2:
        print("密码输入错误")
    elif num2==3:
        print("您的余额不足")
    elif num2==0:
        sql3 = "select * from user where name = %s "
        param3 = [self.__name]
        data3 = select(sql3, param3)
        for i in data3:
            print(i)

def zhuanzhangadd(self):
    p=bank()
    p.setzhuanchuname=(input("请输入您转出账户的姓名："))
    p.setzhuanruname=(input("请输入您转入账户的姓名："))
    p.setpassword =( int(input("请输入您的用户密码：")))
    num3=zzadd(self.__name)

    if num3==1:
        print("转出或转入的账号不存在")
    elif num3==2:
        print("转出账户的密码输入错误")
    elif num3==3:
        print("转出账户的余额不足")
    elif num3==0:
        sql3 = "select * from user where name = %s "
        param3 = [self.__zhuanchuname]
        data3 = select(sql3, param3)
        for i in data3:
            print(i)
        sql2 = "select * from user where name = %s "
        param2= [self.__zhuanruname]
        data2 = select(sql2, param2)
        for i in data2:
            print(i)

def chaxunadd(self):
    p=bank()
    p.setname =(input("请输入您的姓名："))
    p.setpassword = (int(input("请输入您的用户密码：")))
    num4 = cxadd(self.__name)

    if num4==1:
        print("账户信息不存在")
    elif num4==2:
        print("密码输入错误")
    elif num4==0:
        sql3 = "select * from user where name = %s "
        param3 = [self.__name]
        data3 = select(sql3, param3)
        for i in data3:
            print( i )

while False==0:
    index=int(input("请输入您需要的业务"))
    if index ==1:
        print("开户")
        useradd()
        print(bank)
    elif index ==2:
        print("存钱")
        cunqianadd()
    elif index ==3:
        print("取钱")
        quxianadd()
    elif index ==4:
        print("转账")
        zhuanzhangadd()
    elif index ==5:
        print("查询")
        chaxunadd()
    elif index ==6:
        print("下次光临")
        break