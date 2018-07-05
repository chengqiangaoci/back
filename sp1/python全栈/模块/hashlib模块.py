import hashlib#加密模块
# obj = hashlib.md5()#md5算法
# obj.update("hello".encode("utf-8"))#对字符串进行加密
# print(obj.hexdigest())#加密后的hello
#但是以上还是可能会被破解，比如大数据库

#通过加料的方式使得密文具有特色化
obj = hashlib.md5("sb".encode("utf-8"))
obj.update("hello".encode("utf-8"))
print(obj.hexdigest())































