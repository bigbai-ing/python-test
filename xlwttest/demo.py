#!/usr/bin/env python
# coding=utf-8
import xlwt
#创建一个workbook并设置编码
workbook = xlwt.Workbook(encoding='utf-8')
#创建一个worksheet
worksheet = workbook.add_sheet('My Worksheet')

#写入excel
#参数对应行、列、值 , 单元格是从0,0 开始，所以下面的是对应2,1
worksheet.write(1, 0, label='this is test')

#保存
workbook.save('Excel_test.xls')
