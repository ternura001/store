from 工商银行完整版 import bank_addUser
import unittest
from ddt import ddt
from ddt import data
from ddt import unpack
import xlrd, xlwt
from xlutils.copy import copy

# username,password,country,province,street,door,money
da = xlrd.open_workbook("G:\\163组-python自动测试化\\python作业\\python\\HKR.xlsx")
table = da.sheets()[0]
rb = xlrd.open_workbook("G:\\163组-python自动测试化\\python作业\\python\\HKR.xlsx")
wb = copy(rb)
ws = wb.get_sheet(0)
li = []
l = []
for i in range(1, table.nrows):
    li = table.row_values(i, start_colx=0, end_colx=8)
    l.append(li)
i = 0


@ddt
class TestBank2(unittest.TestCase):

    @data(*l)
    @unpack
    def testAddUser(self, a, b, c, d, e, f, g, h):

        result = bank_addUser(a, b, c, d, e, f, g)
        global i
        i += 1
        if result != h:  # 将测试结果回写到excel表格中。
            ws.write(i, 8, "不通过")
            wb.save("G:\\163组-python自动测试化\\python作业\\python\\HKR.xlsx")
        else:
            ws.write(i, 8, "通过")
            wb.save("G:\\163组-python自动测试化\\python作业\\python\\HKR.xlsx")
        self.assertEqual(result, h)


if __name__ == '__main__':
    unittest.main()
