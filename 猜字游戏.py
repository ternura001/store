#任务：开始金币有5个金币，每猜一次减一个为0就退出（or充钱）猜错3次也退出
import random
randint=random.randint(10, 20)#随机生成数字的范围：int   []
print(randint)
i=3
a=5
while i>=1:
    print("您还有机会%d次"%i)
    print("您还有金币%d个"%a)
    num=int(input("请输入您猜的数字"))
    if num==randint:
        print("恭喜你猜对了")
        a=a+3
        randint = random.randint(10, 20)
        print(randint)
        i=3
        continue
    elif num>randint:
        print("猜大了,再来一次")
    elif num<randint:
        print("猜小了，再来一次")

    else:
        print("再来一次")
    i=i-1
    a=a-1
    print("金币剩余%d"%a)
    if i == 0:
        a = a - 3
        i = i + 1
        if a<=0:
            break








