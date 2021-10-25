# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
names = [
    ["曹操","56","男","106","IBM", "500","50"],
    ["大乔","19","女","230","微软", "501","60"],
    ["小乔","19","女","210","Oracle","600","60"],
    ["许褚","45","男","230","Tencent","700","10"]]
# print(names)
#统计每个人的平均薪资
# i=0
# sum=0
# for i in range(0,len(names)):
#     sum=sum+int(names[i][5])
# print("平均为：",sum/len(names))

#统计每个人的平均年龄
# s=0
# for i in range(0,len(names)):
#     s=s+int(names[i][1])
# print("平均为",s/len(names))
#公司新来一个员工
names.append(["刘备","45","男","220","alibaba","500","30"])
# print(names)
#统计公司男女人数
# man=0
# women=0
# for i in range(0,len(names)):
#     if names[i][2]=="男":
#         man=man+1
#     else:
#         women+=1
# print("男的有:",man,"女的有:",women)
#每个部门的人数
# i=0
# a=0
# b=0
# c=0
# d=0
# while i<5:
#     if names[i][6]=="50":
#         a=a+1
#     elif names[i][6]=="60":
#         b=b+1
#     elif names[i][6]=="10":
#         c=c+1
#     elif names[i][6]=="30":
#         d=d+1
#     i=i+1
# print("部门为50的有%d"%a)
# print("部门为60的有%d"%b)
# print("部门为10的有%d"%c)
# print("部门为30的有%d"%d)
#现在魔法学院有赫敏、哈利、罗恩、马尔福四个人的几次魔法作业的成绩。
#但是呢，因为有些魔法作业有一定难度，教授不强制同学们必须上交，所以大家上交作业的次数并不一致。
#求每个人的总成绩？
# name=[["罗恩", 23 ,35 ,44],
# ["哈利",60, 77 ,68 ,88, 90],
# ["赫敏", 97 ,99 ,89 ,91, 95, 90],
# ["马尔福",100,85,90]]
# i=0
# j=0
# num=0
# for i in range(0,len(name)) :
#     for j in range(1,len(name[i])):
#         num=num+name[i][j]
#     else:
#         print(name[i][0],num)
#         num=0

#当输入是54321时，写出下面程序的执行结果。
# num=int (input("请输入一个数："))
# while num !=0:
#     print(num % 10)
#     num = num //10

# 请对下列列表进行冒泡排序（网易测试开发笔试题）
# a=[5,2,4,7,9,1,3,5,4,0,6,1,3]
# def dubble (a):
#     for i in range(0,len(a)):
#         for j in range (0, len(a)- 1 - i):
#           if  a [j]> a [j+1]:
#               a[j],a[j + 1]=a [j + 1],a [j]
#         print(a)
# dubble (a)