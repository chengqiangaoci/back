#基本操作
f = open("",encoding="utf-8")
test = f.read()#readable是否可读，readline一行行读
# readlines是一行行一次性读出来
# print(test)
# f.close()

#一行行写
# f = open("","w",encoding="utf-8")#w会整个覆盖
# f.write("1111111111\n")
# f.writelines(["5555\n","6666\n"])#可以写列表
#a模式不会覆盖，而是追加在最后

#r+既能读也能写

#with
# with open("","w") as f:
# 	f,write("11111\n")

#b模式，进制模式
# f = open("","rb")#b模式不能指定编码,
# data = f.read()
# print(data)#这是读取的是进制
# print(data.decode("utf-8"))#可以显示字节

#b模式，wb,写入的时候格式的问题
# f = open("","wb")
# f.write(bytes("",encoding="utf-8"))#写入为字节
# f.write("",encode("utf-8"))#跟上面一样

























