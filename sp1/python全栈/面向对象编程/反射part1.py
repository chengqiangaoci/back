#反射就是自己检查自己
#hasattr（object,name）判断对象中有没有name字符串对应的方法和属性
class BlackMedium():
	feture = "Ugly"
	def __init__(self,name,addr):
		self.name = name
		self.addr = addr

	def sell_house(self):
		print("[%s] 正在卖房子" %self.name)

	def rent_house(self):
		print("[%s] 正在出租房子" %self.name)
b1 = BlackMedium("万成置地","天露园")
# b1.sell_house()
# print(hasattr(b1,"name"))#检验b1中有没有name属性,true和false
# print(hasattr(b1,"sell_house"))

#print(getattr(b1,"sell_house"))#获取b1中的sell_house属性，找不到会报错

setattr(b1,"sb","True")#设置属性
print(b1.__dict__)#这里就多了一个属性

delattr(b1,"sb")#与上面的相对，是删除
print(b1.__dict__)#这里的话相对于上面那个属性就删除了