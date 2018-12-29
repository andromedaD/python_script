#读取文本
# f=open("555.txt",'r')
# lines=f.readlines()
# print(lines)
# for line in lines:
#     print(line.split(',')[0])

#写入文本，方法一
# write_data =['\ntome',',','444']
# f=open("555.txt",'a')
# f.writelines(write_data)
# print("write is over!")
# f.close()

# #写入文本，方法二
# write_data =['\ntome',',','444']
# with open("555.txt",'a',newline='') as f:
#     f.writelines(write_data)
# print("write is over!!")
# f.close()

# with open('555.txt','r') as f:
#     lines=f.readlines()
#     for line in lines:
#         print(line)

# stu=['\ntom','22','shenzhen']
# with open('555.txt','a',newline='') as f:
#     f.writelines(stu)

# #99乘法表
# for i in range(1,11):
#     with open('555.txt', 'a')as fb:
#         fb.writelines("\n")
#     for j in range(1,11):
#         if i>=j:
#             cheng=i*j
#             cal="\t %d* %d=%d"%(i,j,cheng)
#             with open('555.txt','a')as fb:
#                 fb.writelines(cal)

# 加减乘除
# 定义方法判断运算规则
# def cal_rules(rule,int1,int2):
#     if rule=='+':
#         return(jia(int1,int2))
#
#     elif rule =='-':
#         jian(int1,int2)
#     elif rule == '*':
#         cheng(int1,int2)
#     elif rule=='/':
#         chu(int1,int2)
#
# def jia(int1,int2):
#     try:
#         data=int1+int2
#         return data
#     except Exception as e:
#         print(str(e))
#
# def jian(int1,int2):
#     try:
#         data=int1-int2
#         return data
#     except Exception as e:
#         print(str(e))
#
#
# def cheng(int1,int2):
#     try:
#         data=int1*int2
#         return data
#     except Exception as e:
#         print(str(e))
#
#
# def chu(int1,int2):
#     try:
#         data=int1/int2
#         return data
#     except Exception as e:
#         print(str(e))
#
# def main():
#     data=cal_rules('+',9,3)
#     print(data)
#
# if __name__ == '__main__':
#     main()

