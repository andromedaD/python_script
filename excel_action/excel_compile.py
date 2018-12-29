# #_*_coding:utf-8_*_
#
# import xdrlib,sys
# import xlrd
# #打开excel文件，输出二进制数据
# def open_excel(file='file.xls'):
#     try:
#         data=xlrd.open_workbook(file)
#         return data
#     except Exception as e:
#         print(str(e))
#
# #根据索引获取Excel表格中的数据，参数file：excel文件路径
# #定义方法，将excel中表标题和每行数据，以键值对方、方式建立数组，添加到list数组中
# def excel_table_byindex(file='file.xls',colnameindex=0,by_index=0):
#     data=open_excel(file)
#     table=data.sheets()[by_index]#获取sheet1表
#     nrows=table.nrows#总行数
#     ncols=table.ncols#总列数
#     coldatas=table.row_values(colnameindex)#第一行数据
#     list=[]
#     for rownum in range(1,nrows):
#         print(rownum)
#         row=table.row_values(rownum)
#         print(row)
#         if row:
#             app={}
#             for i in range(len(coldatas)):
#                 print(i)
#                 app[coldatas[i]]=row[i]
#                 print(app)
#             list.append(app)
#     return list
#
# #根据表名称获取Excle表格中数据
# # def excel_table_byname(file='file.xls',colnameindex=0,by_name=u'Sheet1'):
# #     data=open_excel(file)
# #     table=data.sheet_by_name(by_name)
# #     nrows=table.nrows#行数
# #     coldatas=table.row_values(colnameindex)
# #     list=[]
# #     for rownum in range(1,nrows):
# #         row=table.row_values(rownum)
# #
# #         if row:
# #             app={}
# #             for i in range(len(coldatas)):
# #                 app[coldatas[i]]=row[i]
# #             list.append(app)
# #     return list
# def main():
#     tables=excel_table_byindex()
#     for row in tables:
#         print(row)
#     # tables=excel_table_byname()
#     # for row in tables:
#     #     print(row)
#
# if __name__ == '__main__':
#     main()

#_*_coding:utf-8_*_

import xlrd
def open_xls(file='file.xls'):
    try:
        data=xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(str(e))
def xls_by_index(file='file.xls',colnameindex=0,by_index=0):
    data=open_xls(file)
    table=data.sheets()[by_index]
    nrows=table.nrows
    ncols=table.ncols
    colnametable=table.row_values(colnameindex)
    list = []
    for rownum in range(1,nrows):
        row=table.row_values(rownum)

        if row:
            app={}
            for i in range(len(colnametable)):
                app[colnametable[i]]=row[i]
            list.append(app)
    return list

def main():
    lists=xls_by_index()
    for list in lists:
        print(list)

if __name__ == '__main__':
    main()




