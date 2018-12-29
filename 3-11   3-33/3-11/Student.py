# #定义这个类
# class Student():
# #属性初始化
#     def __init__(self,name,city):
#         self.name=name
#         self.city=city
#         print("my name is %s and city is %s" %(name,city))
#
# #定义方法
#     def talk(self):
#         print("hello 51zxw")
# #生成实例对象
# '''
# stu1=Student('jack','beijing')
# stu1.talk()
#
# stu2=Student('marry','shanghai')
# stu2.talk()
# '''
# #定义这个类
# class Student():
#
# #属性初始化
#     def __init__(self,name,city):
#         self.name=name
#         self.city=city
#         print("my name is%s and city is %s"%(name,city))
# #定义方法
#     def talk(self):
#         print("hello world!!!")


#定义这个类
class Student():
    def __init__(self,name,city):
        self.name=name
        self.city=city
        print("%s%s"%(name,city))
    def talk(self):
        print(self.name)