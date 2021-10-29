'''
xlrd 调用表格读取
xlwt 写
'''

import xlrd
import xlwt

yue=xlrd.open_workbook(filename="2020年每个月的销售情况.xlsx",encoding_override=True)
#
for j in range (0,12):
    name=yue.sheet_by_index(j)
# #计算总销售额
    num=0
    some=0
    for i in range (1, len(name.col(1))):
        rowd=name.cell_value(i,2)
        cold=name.cell_value(i,4)
        some+=cold
        num +=rowd * cold
    print("第{}月的总销额:".format(j+1),"%.2f"%num)
# #计算平均每日销售数量
    print("第{}月的平均销售数量:".format(j+1),"%.2f"%(some/(len(name.col(1))-1)),"总数：",some)
#计算每个种类月销售量占比
    some = 0
    yr=0
    nz=0
    fy=0
    tx=0
    pc=0
    mj=0
    for i in range(1, len(name.col(1))):
        rowd = name.cell_value(i, 1)
        cold = name.cell_value(i, 4)
        some += cold
        if rowd=="羽绒服":
            yr += cold
        if rowd=="牛仔裤":
            nz += cold
        if rowd=="风衣":
            fy += cold
        if rowd =="T血":
            tx += cold
        if rowd =="皮草":
            pc += cold
        else:
            mj += cold
    print("第{}月的羽绒服销售量占比:".format(j+1),yr/some)
    print("第{}月的牛仔裤销售量占比:".format(j+1),nz/some)
    print("第{}月的风衣销售量占比:".format(j + 1),fy/some)
    print("第{}月的T血销售量占比:".format(j + 1), tx/some)
    print("第{}月的皮草销售量占比:".format(j + 1),pc/some)
    print("第{}月的马甲销售量占比:".format(j + 1),mj/some)