import random
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
print("*6、欢迎下次光临            *")
print("****************************")
#初始化银行
bank={}
#'Frank': {'account': 24275182, 'password': '123456', 'country': '中国', 'province': '山东', 'steert': '曹县', 'door': '001', 'money': 0, 'bank_name': '保熟银行'}
#定义一个开户银行
bank_name="保熟银行"

#定义添加到银行 定义函数元素对应元素  不是名称对名称
def bankadd(account,name,password,country,province,steert,door):
    if len(bank)>=100:
        return 3
    elif name in bank:
        return 2
    else:
        bank[name]={
            "account":account,
            "password":password,
            "country":country,
            "province":province,
            "steert":steert,
            "door":door,
            "money":0,
            "bank_name":bank_name
        }
        return 1
#存钱
def cunq(name1):
    if name1 in bank:
        print("用户金额%d"%bank[name1]["money"])
        money=int(input("请输入存款金额："))+bank[name1]["money"]
        bank[name1]["money"]=money
        return True
    else:
        return float
#取钱
def quq(name,password):
    if name in bank and password ==bank[name]["password"]:
        print("用户金额:%d"%bank[name]["money"])
        money2=bank[name]["money"]-int(input("请输入取款金额"))
        bank[name]["money"]=money2
        if money2 < 0:
            return 3
        if money2 >=0:
            money2=bank[name]["money"]
            return 0
    elif name not in bank:
        return 1
    elif name in bank:
        if password != bank[name]["password"]:
            return 2
#转帐
def zz(name3,password,name4):
    if name3 in bank and password==bank[name3]["password"] and name4 in bank:
        print("用户金额:%d"%bank[name3]["money"])
        money3=bank[name3]["money"]-int(input("请输入转出金额"))
        if money3<0:
            return 3
        if money3 >=0:
            bank[name3]["money"] = money3
            money4 = bank[name4]["money"] + money3
            return 0
    elif name3 not in bank:
        return 1
    elif name3 in bank :
        if password != bank[name3]["password"]:
            return 2
    elif name3 in bank and password==bank[name3]["password"]:
        if name4 not in bank :
            return 1
#查询
def xun(name5,password):
    if name5 in bank and password==bank[name5]["password"]:
        return 0
    elif name5 not in bank :
        return 1
    elif name5 in bank :
        if password !=bank[name5]["password"]:
            return 2





#定义用户入参
def useradd():
    account=random.randint(10000000,99999999)
    name=input("请输入您的名称")
    password=input("请输入您的密码")
    print("请输入你的详细信息")
    country=input("\t\t请输入您的国籍")#\t ==tab
    province=input("\t\t请输入您的省份")
    steert=input("\t\t请输入您的街道")
    door=input("\t\t请输入您的门牌号")
    num=bankadd(account,name,password,country,province,steert,door)
    if num ==3:
        print("本银行已满请到其他银行开户")
    elif num== 2:
        print("用户已存在")
    elif num==1:
        print("恭喜你开户成功，一下是您的相信信息")
        info = '''
                   ------------个人信息------------
                   用户名:%s
                   账号：%s
                   密码：*****
                   国籍：%s
                   省份：%s
                   街道：%s
                   门牌号：%s
                   余额：%s
                   开户行名称：%s
               '''
        # 每个元素都可传入%
        print(info % (name, account, country, province, steert, door, bank[name]["money"], bank_name))
#存钱
def cun ():
    name1=input("请输入账号")
    num1=cunq(name1)
    if num1==float :
        print("没有该用户")
    elif num1==True:
        info = '''
                   ------------个人信息------------
                   用户名:%s
                   密码：*****
                   余额：%s
                   开户行名称：%s
               '''
        print(info % (name1,bank[name1]["money"],bank_name))
#取钱
def qu():
    name = input("请输入账号")
    password=input("请输入密码：")
    num2 = quq(name,password)
    if num2 == 1 :
        print("没有该用户")
    elif num2==2 :
        print("密码错误")
    elif num2 == 3:
        print("余额不足")
    elif num2 == 0 :
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    密码：*****
                    余额：%s
                    开户行名称：%s
                '''
        print(info % (name, bank[name]["money"], bank_name))
#转账
def zhuan():
    name3 = input("请输入账号")
    password=input("请输入密码")
    name4=input("请输入转入账号")
    num2 = zz(name3, password,name4)
    if num2 == 1 :
        print("没有该用户")
    elif num2==2 :
        print("密码错误")
    elif num2 == 3:
        print("余额不足")
    elif num2 == 0 :
        info = '''
                            ------------个人信息------------
                            用户名:%s
                            密码：*****
                            余额：%s
                            开户行名称：%s
                        '''
        print(info % (name3, bank[name3]["money"], bank_name))
#查询
def cha():
    name5=input("请输入账号")
    password = input("请输入密码")
    num5=xun(name5,password)
    if num5 == 1 :
        print("没有该用户")
    elif num5 == 2 :
        print("密码错误")
    elif num5==0:
        info = '''
                          ------------个人信息------------
                          用户名:%s
                          账号：%s
                          密码：%s
                          国籍：%s
                          省份：%s
                          街道：%s
                          门牌号：%s
                          余额：%s
                          开户行名称：%s
                      '''
        print(info % (name5, bank[name5]['account'], bank[name5]['password'],bank[name5]['country'], bank[name5]['province'],bank[name5]['steert'], bank[name5]['door'], bank[name5]["money"], bank_name))

while False==0:
    index=int(input("请输入您需要的业务"))
    if index ==1:
        print("开户")
        useradd()
        print(bank)
    elif index ==2:
        print("存钱")
        cun()
        print(bank)
    elif index ==3:
        print("取钱")
        qu()
        print(bank)
    elif index ==4:
        print("转账")
        zhuan()
        print(bank)
    elif index ==5:
        print("查询")
        cha()
        print(bank)
    elif index ==6:
        print("下次光临")
        break

