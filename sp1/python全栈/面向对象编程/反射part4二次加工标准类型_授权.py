#授权是包装的一个特性，关键也在于定制
#授权的过程即是所有的更新的功能都是由新类的某部分来处理，但已存在的功能就授权给对象的默认属性
#授权的关键点就是覆盖__getattr__方法

#定制一个文件
class Open():
	def __init__(self,filename,mode="r",enconding="utf8"):
		self.file = open(filename,mode,enconding=enconding)
		self.mode = mode
		self.enconding = enconding

	def __getattr__(self,item):
		print(item)

f1 = Open("a.tex","w")
f1.read









