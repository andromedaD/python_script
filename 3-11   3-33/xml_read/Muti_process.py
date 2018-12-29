from time import ctime,sleep
import multiprocessing

#定义2个方法
def talk(content,loop):
    for i in range(loop):
        print("start talk:%s%s"%(content,ctime()))
        sleep(2)

def write(content,loop):
    for i in range(loop):
        print("start write: %s %s"%(content,ctime()))
        sleep(3)
#定义2个进程
multprocess=[]
p1=multiprocessing.Process(target=talk,args=('this is my best friend',2))
multprocess.append(p1)
p2=multiprocessing.Process(target=write,args=('wangjing',3))
multprocess.append(p2)

#调用进程

if __name__ == '__main__':
    for p in multprocess:
        p.start()
    for p in multprocess:
        p.join()
    print("all is the end!!")