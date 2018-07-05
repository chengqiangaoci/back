from random import randint
class Die():
	"""一个骰子的类"""
	def __init__(self,num_sides=6):
		"""骰子有六面"""
		self.num_sides =num_sides

	def roll(self):
		#随机返回一个值
		return randint(1,self.num_sides)

die = Die()
results = []
for roll_num in range(100):#重复100次
	result = die.roll()
	results.append(result)
print(results)

#计算每个点数出现的频率
frequencies = []
for value in range(1,die.num_sides+1):
	frequency = results.count(value)
	frequencies.append(frequency)

#进行可视化
import pygal
hist = pygal.Bar()#实例化

hist.title = "结果图"
hist.x_labels = ["1","2","3","4","5","6"]
hist.x_title = "Result"
hist.y_title = "frequencies"

hist.add("D6",frequencies)#两个实参，分别是标签和要传入值的列表
hist.render_to_file("test.svg")#这里并不能显示出来，目录必须要是中文的







