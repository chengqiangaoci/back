# class ParentClass1:
# 	pass
# class ParentClass2:
# 	pass

# class SubClass(ParentClass1):#单继承
# 	pass
# class SubClass(ParentClass1,ParentClass2):#多继承
# 	pass


# #父类与子类属性名相同是否会冲突或覆盖:不会覆盖，只是子类会优先使用自己的
# class Dad():
# 	money = 10
# 	def __init__(self,name):
# 		print("爸爸")
# 		self.name = name
# 	def hit_son(self):
# 		print("%s 打儿子" %self.name)
# class Son(Dad):
# 	money = 1000000
# test = Son("chengqian")
# print(test.money)


#当类之间显著不同，较小的类是较大的类所需的组件时，用组合
#如机器人有很多小类组成，如机械腿等

#当类之间有很多相同功能，提取这些共有功能作为基类，用继承比较好
#猫可以喵喵喵，吃喝拉撒
#狗可以汪汪汪，吃喝拉撒
#这样就可以提取吃喝拉撒作为基类

#上面那种继承不好，因为这样有强耦合，而程序最好不要有耦合


#以下较好
#接口继承——归一化式继承：规定好了所有的子类必须实现什么方法，但父类不实现这些方法
#写一个一切皆文件的类（以下是试验，不算真正的接口继承）
# class ALL_file():#父类规定子类必须由read和write，但是父类本身没有具体写明
# 	def read(self):
# 		pass
# 	def write(self):
# 		pass
# #这样就避免了子类与父类具有强耦合
# class Disk(ALL_file):#因为父类规定了，所以这里子类必须写明具体的方法
# 	def read(self):
# 		print("disk read")
# 	def write(self):
# 		print("disk write")
# class Cdrom(ALL_file):#C盘
# 	def read(self):
# 		print("cdrom read")
# 	def write(self):
# 		print("cdrom write")
# class Mem(ALL_file):#内存
# 	def read(self):
# 		print("mem read")#以下没有write方法
# test = Mem()
# test.read()
# test.write()#这里调用的是父类，因此没有东西


#以下是真正的接口继承
import abc#必须导入这个模块
class ALL_file(metaclass=abc.ABCMeta):#父类要起到限制作用
	@abc.abstractmethod#说明下面的方法不用具体实现
	def read(self):
		pass
	@abc.abstractmethod
	def write(self):
		pass
#这样就避免了子类与父类具有强耦合
class Disk(ALL_file):#因为父类规定了，所以这里子类必须写明具体的方法
	def read(self):
		print("disk read")
	def write(self):
		print("disk write")
class Cdrom(ALL_file):#C盘
	def read(self):
		print("cdrom read")
	def write(self):
		print("cdrom write")
class Mem(ALL_file):#内存
	def read(self):
		print("mem read")#以下没有write方法
	def write(self):
		pass
test = Mem()#这里会报错，无法实例化，因为Mem类没有write
#需要加上write方法



