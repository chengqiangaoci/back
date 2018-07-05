#Greenlet与python自带的yield相比可以使你在任意函数间随意切换，而不需把这个函数先声明为生成器
from greenlet import greenlet
def test1():
    print(12)
    gr2.switch()#在这保留，下一次打印下面的内容
    print(34)
    gr2.switch()

def test2():
    print(56)
    gr1.switch()
    print(78)

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()