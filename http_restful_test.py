# from util.restful_util_test import Conmmon
# # con=Conmmon('ws://echo.websocket.org','ws')
# con=Conmmon('http://','http')
# result=con.get('www.baidu.com',params=None)
#
# print(result.cookies)
#
# # con.__del__()

import xlrd

#需要安装pyexcel-xls，否则报错不支持

#打开excel表格
workbook=xlrd.open_workbook('test11111.xlsx')
print(workbook)

#获取所有sheet名称
sheet_names=workbook.sheet_names()
print(sheet_names)

#获取所有或者某个sheet对象
#获取所有sheet对象
sheets_object=workbook.sheets()
print(sheets_object)

#通过index获取第一个sheet对象
sheet1_object=workbook.sheet_by_index(0)
print(sheet1_object)
#通过name获取第一个sheet对象
sheetn_object=workbook.sheet_by_name('新建1')
print(sheetn_object)

#判断某个sheet是否已经导入
#通过index判断
sheet_is_load=workbook.sheet_loaded(sheet_name_or_index=1)
print(sheet_is_load)

#通过名称判断
sheetn_is_load=workbook.sheet_loaded(sheet_name_or_index='xinjian')
print(sheetn_is_load)

#获取sheet1中的有效行数
nrows=sheet1_object.nrows
print(nrows)

#获取sheet1中第三行的数据
all_row_values=sheet1_object.row_values(rowx=2)
print(all_row_values)

row_values=sheet1_object.row_values(rowx=2,start_colx=0,end_colx=1)
print(row_values)

#获取sheet1中第三行的单元对象
row_object=sheet1_object.row(rowx=3)
print(row_object)

row_slice=sheet1_object.row_slice(rowx=3)
print(row_slice)

#获取sheet1中第三行的单元类型
'''
start_colx列到end_colx列的单元类型，返回值为array.array类型。
单元类型ctype：empty为0，string为1，number为2，date为3，
boolean为4， error为5（左边为类型，右边为类型对应的值）
'''
row_type=sheet1_object.row_types(rowx=3)
print(row_type)
#array('B', [2, 1])

#获取sheet1中第三行的长度
row_len=sheet1_object.row_len(rowx=3)
print(row_len)

#获取sheet1所有行的生成器
row_generator=sheet1_object.get_rows()
#print(row_generator.__next__())

#对sheet对象中的列执行操作

#获取sheet1中的有效列数
ncols=sheet1_object.ncols
print(ncols)

#获取sheet1中第col+1列的数据
col_values=sheet1_object.col_values(colx=0)
print(col_values)
col_values1=sheet1_object.col_values(1,1,3)
print(col_values1)

#获取sheet1中第2列的单元
col_slice=sheet1_object.col_slice(colx=1)
print(col_slice)
#获取sheet1中第二列的单元类型
'''
获取sheet对象中第rowx+1行，第colx+1列的单元数据类型值；
单元类型ctype：empty为0，string为1，number为2，
date为3，boolean为4， error为5
'''
col_types=sheet1_object.col_types(colx=0)
print(col_types)

#对sheet1对象中的单元执行操作
#获取sheet1中第rowx+1行，第colx+1列的单元对象
cell_info=sheet1_object.cell(rowx=1,colx=1)
print(cell_info)
print(type(cell_info))

#获取sheet1中第rowx+1行，第colx+1列的单元值
cell_value=sheet1_object.cell_value(rowx=1,colx=1)
print(cell_value)

#获取sheet1中第rowx+1行，第colx+1列的单元类型值
cell_type=sheet1_object.cell_type(rowx=2,colx=1)
print(cell_type)