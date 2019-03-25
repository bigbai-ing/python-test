#python使用xlwt模块操作Excel和xlrd读取已存在的xls文件

二、xlrd使用介绍

   1、导入模块
        import xlrd 
   2、打开Excel文件读取数据
        data = xlrd.open_workbook('excelFile.xls')
   3、使用技巧
        获取一个工作表
        table = data.sheets()[0]          #通过索引顺序获取
        table = data.sheet_by_index(0) #通过索引顺序获取
        table = data.sheet_by_name(u'Sheet1')#通过名称获取
链接：https://www.jianshu.com/p/4e39444d5ebc
简单demo：demo.py
设置样式：style.py

