# import xlwt
# # 创建工作簿
# wb = xlwt.Workbook()
# # 创建表单
# sh=wb.add_sheet('test')
# # 创建字体对象
# font=xlwt.Font()
# # 字体加粗
# font.bold=True
# alm=xlwt.Alignment()
# # 设置左对齐
# alm.horz=0x01
# # 创建样式对象
# style1=xlwt.XFStyle()
# style2 = xlwt.XFStyle()
# style1.font = font
# style2.alignment = alm
# # write 方法参数1：行，参数2：列，参数3：内容
# sh.write(0,1,'姓名',style1)
# sh.write(0, 2, '年龄', style1)
# sh.write(1, 1, '张三')
# sh.write(1, 2, 50, style2)
# sh.write(2, 1, '李四')
# sh.write(2, 2, 30, style2)
# sh.write(3, 1, '王五')
# sh.write(3, 2, 40, style2)
# sh.write(4, 1, '赵六')
# sh.write(4, 2, 60, style2)
# sh.write(5, 0, '平均年龄', style1)
# # 保存
# wb.save('test.xls')

import xlrd

import xlrd

# # 读取Excel文件
# data = xlrd.open_workbook("test.xls")
# # print(data.sheet_loaded(0)) # 加载索引为0的工作表  True
# # data.unload_sheet(0) # 卸载
# # print(data.sheet_loaded(0))  # 未被加载，False
# # print(data.sheet_loaded(1))  # True
# print(data.sheets()) # 获取全部sheet  [Sheet  0:<Sheet1>, Sheet  1:<Sheet2>, Sheet  2:<Sheet3>]
# print(data.sheets()[0]) # 获取指定索引的工作表对象  Sheet  0:<Sheet1>
# print(data.sheet_by_index(0)) # 根据索引获取工作表 Sheet  0:<Sheet1>
# print(data.sheet_by_name('Sheet1'))  # 根据名字sheetname（区分大小写）获取工作表 Sheet  0:<Sheet1>
# print(data.sheet_names()) # 获取所有工作表的name ['Sheet1', 'Sheet2', 'Sheet3']
# # 查看共有多少个工作表
# print(len(data.sheet_names())) # 返回所有工作表的名称组成的list的长度 3
# print(data.nsheets) # 返回excel工作表的数量 3

import xlrd

data = xlrd.open_workbook("test.xls")

# 操作excel单元格
sheet1 = data.sheet_by_index(0) # 获取第一个工作表



