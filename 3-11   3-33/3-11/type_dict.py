# student={1:'jack',2:'bob',3:'mary',4:'micle'}
# print(student[3])
#
# #添加元素
# student[5]='mick'
# print(student)
#
# #修改元素
# student[2]='harry'
# print(student)
#
# #删除元素
# del student[2]
# print(student)
#
# #清空元素
# student.clear()
# print(student)
#
# #彻底销毁字典
# del student
# print(student)

student={'tom':'beijing','katty':'shanghai','jerry':'tianjing'}
print(student['tom'])

#添加元素
student['alex']='zhenjiang'
print(student)

#修改元素
student['tom']='shenzhen'
print(student['tom'])

#删除元素
del student['alex']
print(student)

#清除元素
student.clear()
print(student)