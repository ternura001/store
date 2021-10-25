# 实现输入十个数字并打印10个数求和的结果。
list=[]
for i in range(10):
    num=float(input("请输入第{}个数：".format(i+1)))
    list.append(num)
sum=0
for i in range (len(list)):
    sum+=list[i]
print(sum)

# 从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
list=[]
for i in range(10):
    num=int(input("请输入第{}个数：".format(i+1)))
    list.append(num)
sum=0
max=0
for i in range(len(list)):
    sum+=list[i]
    if list[i]>=max:
        max=list[i]
print(len(list))
average= sum/len(list)
print("总和：",sum)
print("最大：",max)
print("平均：",average)

# 使用random模块，如何产生 50~150之间的数
import random
randint=random.randint(50,150)
print(randint)
#
# 从键盘输入任意三边，判断是否能形成三角形，若可以，
# 则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
a = int(input('输入三角形第一边长: '))
b = int(input('输入三角形第二边长: '))
c = int(input('输入三角形第三边长: '))
print(a,b,c)
if a+b>c&a+c>b|b+c>a&c+a>b|a+c>b&b+c>a:
    print("可以形成三角形")
if a==b&a==c|b==a&b==c|c==a&c==b:
    print ("形成等腰三角形")
if a==b==c:
    print("形成等边三角形")
else:
    print("不可以形成三角形")



# 有以下两个数，使用+，-号实现两个数的调换
A=56
B=78
C=A+B
D=C-A
E=C-B
print("A转换为%d"%D)
print("B转换为%d"%E)

# 实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
count=0
uner = ("root")
mima=("admin")
while count<3:
    ming=input("请输入用户名：")
    mi =input("请输入密码:")
    if mi==mima and ming==uner:
        print("登录成功")
        break
    else:
        print("登录失败")
        count+=1
        continue
print("登录失败,错误超过三次，请联系管理员进行解锁")

编程实现下列图形的打印
a=7
for i in range(a):
    print(" "*(a-1-i)+'*'*(i+1)+'*'*i)

# 一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚+上下滑2米，
# 问第几天能出来？请编程求出
h=20
day=1
while True :
    if 3*day-2*(day-1)==h:
        break
    elif 3*day-2*day==h:
        break
    day=day+1
print("第%d天爬出"%day)


# 使用while循环实现NxN乘法表的打印
# 编程实现99乘法表的倒叙打印



# 判断下列变量命名是否合法
while True:
    s=input ('变量名：')
    if s=='exit':
        print('exit')
        break
    if s[0].isalpha()or s[0]=='_':
        for i in s[1:]:
            if not (i.isalpha() or i=='_'):
                print('%s变量名不合法'%(s))
                break
        else:
            print('%s变量名合法'%(s))
    else:
        print('%s变量名不合法'%(s))