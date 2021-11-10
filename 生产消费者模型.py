import time
from threading import Thread
ticket = 500
class Basket(Thread):
    username = ""
    count = 0
    name = ""
    shop = 0
    money = 5000

    def run(self) -> None:
        while True:
            global ticket
            if ticket > 0:
                self.count = self.count + 1
                ticket = ticket - 1
                print("还要做",ticket,"就满了")
                if ticket == 500:
                    time.sleep(4)
                    continue
            else:
                print(self.username, "总共做了", self.count, "个")

            if ticket > 0:
                ticket = ticket + 1
                self.shop = self.shop + 1
                self.money = self.money - 3
                print(self.name, "买了", self.shop, "剩余金额", self.money)
                if self.money < 3:
                    break
                if ticket == 0:
                    time.sleep(4)
            else:
                print(self.name, "总共买了", self.shop)
                continue



p1 = Basket()
p2 = Basket()
p3 = Basket()
S1 = Basket()
S2 = Basket()
S3 = Basket()
S4 = Basket()
S5 = Basket()
S6 = Basket()

p1.username = "张三"
p2.username = "李四"
p3.username = "王五"

S1.name = "金克斯"
S2.name = "阿卡丽"
S3.name = "卡莎"
S4.name = "伊芙兰"
S5.name = "斯特林"
S6.name = "拉克丝"

p1.start()
p2.start()
p3.start()
S1.start()
S2.start()
S3.start()
S4.start()
S5.start()
S6.start()






















