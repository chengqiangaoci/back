#当局部变量和全局变量同名时，在定义局部变量的程序内，局部变量起作用，其他地方全局变量起作用。
# name = 111
# def test():
# 	name = "sjiaodeuon"
# 	print(name)
# test()#这里就打印的是局部变量
# print(name)#这里就是打印的全局变量

name = 111
print(name)
def test():
    global name#意味着下面的变量那么成为全局变量了，而外面的全局变量就无效了
    name = "sjiaodeuon"
    print(name)
print(name)
test()#这里就打印的是局部变量（实际上在这里局部变量已经被定义为全局变量）
print(name)#这也是打印的局部变量（同上）

#nonlocal跟global类似，但是他是指定上一级变量(外层非全局)
