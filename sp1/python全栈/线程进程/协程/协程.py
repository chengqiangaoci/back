
import time
import queue

def consumer(name):#这是一个生成器
    print("--->ready to eat baozi...")
    while True:
        new_baozi = yield#等待send进来数据
        print("[%s] is eating baozi %s" % (name,new_baozi))
        #time.sleep(1)

def producer():

    r = con.__next__()
    r = con2.__next__()
    n = 0
    while 1:
        time.sleep(1)
        print("[32;1m[producer][0m is making baozi %s and %s" %(n,n+1) )
        con.send(n)#发送到上面的yield
        con2.send(n+1)

        n +=2


if __name__ == '__main__':
    con = consumer("c1")#生成了生成器，没有执行函数
    con2 = consumer("c2")
    producer()
