# except FileNotFoundError
#  try:
#     fileName=input("please input fileName:")
#     open("%s.txt" %fileName)
# except FileNotFoundError:
#     print("%s.txt file not found" %fileName)
#


# except NameError
# try:
#     print(stu)
# except NameError:
#     print("stu not define!")
#


# try:
#     stu='jack'
#     print(stu)
# except BaseException as msg:
#     print(msg)
# else:
#     print("student is denfine!,name is %s" %stu)
# finally:
#     print("the end!")


#raise 只能接python标准异常类
# def division(x,y):
#     if y==0:
#         raise ZeroDivisionError("Zero is not allow")
#     return x/y
# try:
#     division(3,0)
# except BaseException as msg:
#     print(msg)
# finally:
#     print("the end!!")




