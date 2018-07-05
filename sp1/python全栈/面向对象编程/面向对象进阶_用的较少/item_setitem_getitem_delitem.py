#.系列跟attr相关，字典的形式跟item相关
class Foo():
	def __getitem__(self,item):
		print("getitem",item)
		return self.__dict__[item]

	def __setitem__(self,key,value):
		print("setitem")
		self.__dict__[key] = value

	def __delitem__(self,key):
		print("delitem")
		self.__dict__.pop(key)
f1 = Foo()
#item只适用于字典的复制方式，如下，但是f.name = xxx这种方式不行
f1["name"] = "chengqian"#可以这样定义属性，直接触发setitem方法
print(f1.__dict__)


