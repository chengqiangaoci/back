#CSV格式：以逗号分隔的值写入的文件
#获取数据集中的最高气温和日期
import csv
from datetime import datetime
with open("sitka_weather_07-2014.csv") as f:
	reader = csv.reader(f)#每一行
	next(reader)#将数据转移到文件中的下一项，在这里是第二行
	highs = []
	dates = []
	for row in reader:
		print(row)
		high = int(row[1])##每一行中的最高气温；将字符串转换为数字以便可视化
		highs.append(high)
		date = datetime.strptime(row[0],"%Y-%m-%d")
		dates.append(date)
#可视化最高气温,日期
from matplotlib import pyplot as plt
fig = plt.figure(dpi=128,figsize=(10,6))#调整尺寸以适应屏幕
plt.plot(dates,highs,c="red")
#设置图形格式
plt.title("Daily high temperatures,July 2014",fontsize=24)
plt.xlabel("",fontsize=16)
fig.autofmt_xdate()#自动调整日期标签，以免重叠
plt.ylabel("Temperature(F)",fontsize=16)
plt.tick_params(axis="both",which="major",labelsize=16)#设置刻度标记的大小
plt.show()



















