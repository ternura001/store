#分析一个水杯的属性和功能，使用类描述并创建对象
class Cup:
    __high = 0.0
    __volume = 0.00
    __color = ""
    __wood=""
    def setHigh(self,high):
        if high > 30 or high < 10:
            print("高度输入错误")
        else:
            self.__high = high
    def getHigh(self):
        return self.__high

    def setvolume(self,volume):
        if volume > 1 or volume < 0.01:
            print("液体太少")
        else:
            self.__volume =volume
    def getvolume(self):
        return self.__volume

    def setcolor(self,color):
        if color !="绿色" and color!="红色" and color != "黑色":
            print("没有这个颜色的")
        else :
            self.__color =color
    def getcolor(self):
        return self.__color

    def setwood(self,wood):
        if wood != "玻璃" and wood !="铁" and wood != "木头":
            print("没有这个材质")
        else:
            self.__wood =wood
    def getwood(self):
        return self.__wood

    def water(self):
        print(self.__volume,"升的液体在杯中！")
    def showMe(self):
        print("这个杯子身高",self.__high,"厘米！存放液体",self.__volume,
              "颜色为：",self.__color,"材质为：",self.__wood)
# 造一个杯子
c = Cup()
# 给杯子赋值属性
# c.__high = 15.5
# c.__color = "绿色"
# c.__volume=0.50 # 1个多亿
# c.__wood ="玻璃"
c.setHigh(20)
c.setwood("木头")
c.setvolume(0.50)
c.setcolor("红色")
# 让杯子放液体
c.water()
c.showMe()


#有笔记本电脑（屏幕大小，价格，cpu型号，内存大小，待机时长），
# 行为（打字，打游戏，看视频）
import time
class computer:
    __computername=""
    __screen = 0.0
    __maney = 0.00
    __cpu=""
    __Memory=""
    __Standby=0.0

    def setcomputernume(self,computername):
        if computername  !="联想" and computername !="戴尔" and computername !="苹果":
            print("没有这台电脑")
        else:
            self.__computername = computername
    def getcomputername(self):
        return self.__computername

    def setscreen(self,screen):
        if screen < 12 or screen > 18:
            print("没有这种屏幕大小的笔记本")
        else:
            self.__screen =screen
    def getscreen(self):
        return self.__screen

    def setmaney(self,maney):
        if maney < 3000 or maney > 8000:
            print("没有这个价位的电脑")
        else:
            self.__maney =maney
    def getmaney(self):
        return self.__maney

    def setcup(self,cup):
        if cup !="i3" and cup !="i4" and cup!="i6" and cup!="i7":
            print("没有这个cup型号的电脑")
        else:
            self.__cpu =cup
    def getcup(self):
        return self.__cpu
    def setMemory(self,Memory):
        if Memory !="1000G" and  Memory != "2000G" and Memory !="3000G" and Memory !="500G" :
            print("没有这个大小内存的电脑")
        else:
            self.__Memory =Memory
    def getMemory(self):
        return self.__Memory

    def setStandby(self,Standby):
        if Standby < 6 or Standby > 12:
            print("没有这么长待机的电脑")
        else:
            self.__Standby =Standby
    def getStandby(self):
        return self.__Standby

    def type(self,typename):
        print(self.__computername, "电脑打字工具有：", typename)
    def game(self,gamename):
        print(self.__computername,"电脑下载的游戏有：",gamename)
        print("【植物大战僵尸",end="")
        for i in range(2):
            print(".",end="")
            time.sleep(1)
        print("植物大战僵尸】")
    def television(self,app):
        print(self.__computername,"电脑下载的视频APP有：",app)

    def showMe(self):
        print("笔记本电脑名为：", self.__computername , "cup型号为：", self.__cpu , "内存为：", self.__Memory,
              "价格为：", self.__maney,"人民币，屏幕大小为：",self.__screen,"待机时长：",self.__Standby)


c=computer ()

# c.computername ="联想"
# c.cpu ="i7"
# c.maney =5600
# c.Memory ="5000G"
# c.screen =15.6
# c.Standby =8.0
c.setcomputernume("联想")
c.setcup("i7")
c.setmaney(5600)
c.setMemory("1000G")
c.setscreen(15.6)
c.setStandby(8)

c.type("搜狗")
c.game("植物大战僵尸")
c.television("爱奇艺")
c.showMe()
