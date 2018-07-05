def h():

    print ('Wen Chuan')

    yield 5#就是个生成器

    print ('Fighting!')
    print ("xxxxx")
    return 

c = h()
print(next(c))#第一次生成到yield就停止
print(next(c))#第二次从yield下面开始
#yield 的作用： yield可以看出是“暂停”了函数的执行，
#然后在调用函数的.next() 方法之后， 函数开始执行直到下一个 yield的表达式。



