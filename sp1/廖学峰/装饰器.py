#函数也是对象，可以被赋值给变量，因此可以通过变量调用该函数
# def test():
# 	print("this is a test")

# a = test
# a()

#假设要增强上面函数的功能，但是又不改变函数test的定义
#这种在代码运行期间动态增加功能的方式，成为装饰器
def logger(func):
    def inner(*args, **kwargs): #1
        print "Arguments were: %s, %s" % (args, kwargs)
...     return func(*args, **kwargs) #第一步返回主函数的形参，
... return inner#第二步返回内函数