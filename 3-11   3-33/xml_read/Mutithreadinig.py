# from time import ctime,sleep
# import threading
#
# def talk(content,loop):
#     for i in range(loop):
#         print("start talk %s %s"%(content,ctime()))
#         sleep(2)
#
# def write(content,loop):
#     for i in range(loop):
#         print("start write %s%s" %(content,ctime()))
#         sleep(3)
#
#
# #定义加载线程
# threads=[]
# t1=threading.Thread(target=talk,args=('hello 51zxw',2))
# threads.append(t1)
# t2=threading.Thread(target=write,args=('you are good',4))
# threads.append(t2)
#
# #执行多线程
# if __name__ == '__main__':
#     for t in threads:
#         t.start()
#     for t in threads:
#         t.join()
#     print("all ends time: %s"%ctime())
#


from time import ctime,sleep
import threading

#定义方法
def talk(content,loop):
    for i in range(loop):
        print("start talk  is:%s%s"%(content,ctime()))
        sleep(2)

def write(content,loop):
    for i in range(loop):
        print("start write is:%s%s"%(content,ctime()))
        sleep(3)


#定义线程，并装载
threads=[]
t1=threading.Thread(target=talk,args=('hello baby',2))
threads.append(t1)
t2=threading.Thread(target=write,args=('listen to me',3))
threads.append(t2)

#运行守护
if __name__ =='__main__':
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("this is the end!!")