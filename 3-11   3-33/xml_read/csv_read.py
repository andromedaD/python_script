import csv
#读取csv
# csv_file=csv.reader(open('stu_info.csv','r'))
# print(csv_file)
#
# for stu in csv_file:
#     print(stu[0],stu[2])

#写入csv
# stu=['alex',12,'shenzhen']
# stu1=['bbq',21,'tianjing']
# #打开文件
# out=open('stu_info.csv','a',newline='')
# #设置写入模式
# csv_write=csv.writer(out,dialect='excel')
# #写入具体内容
# csv_write.writerow(stu)
# csv_write.writerow(stu1)
# print("write over!!")

#csv读取方法二
# with open('stu_info.csv','r') as f:
#     result= csv.reader(f)
#     for res in result:
#         print(res)

#csv写入方法二
# stu=['weq','2312','sdasd']
# stu1=['weqrt','3123123','beijing']
# with open('stu_info.csv','a',newline='') as f:
#     csv_write=csv.writer(f,dialect='excel')
#     csv_write.writerow(stu)
#     csv_write.writerow(stu1)


with open('stu_info.csv','r') as f:
    result=csv.reader(f)
    for res in result:
        print(res)

# stu=['wuxie',19,'tianjing']
# stu1=['zahngqilin',20,'luoyang']
# with open('stu_info.csv','a',newline='') as f:
#     write_csv=csv.writer(f)
#     write_csv.writerow(stu)
#     write_csv.writerow(stu1)