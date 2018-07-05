#使用scipy的genfromtxt读取数据
import scipy as sp
data = sp.genfromtxt("web_traffic.tsv",delimiter="\t")
print(data[:10])
print(data.shape)#shape是维度

#预处理和清洗数据
x = data[:,0]
y = data[:,1]
x = x[~sp.isnan(y)]#只选择有效值
y = y[~sp.isnan(y)]
wuxiaozhi = sp.sum(sp.isnan(y))#无效值
print(wuxiaozhi)

def error(f,x,y):
	return sp.sum((f(x)-y)**2)#计算误差
fp1,residuals,rank,sv,rcond = sp.polyfit(x,y,1,full=True)
print("Model parameters:%s"% fp1)#系数
print(residuals)#残差
f1 = sp.poly1d(fp1)
print(f1)#创建方程式
print(error(f1,x,y))#这个要重点理解


import matplotlib.pyplot as plt
fx = sp.linspace(0,x[-1],1000)
plt.plot(fx,f1(fx),linewidth=4)#线形图
plt.legend(["d=%i"%f1.order],loc="upper left")

plt.scatter(x,y)#散点图
plt.title("这是一个测试")
plt.xlabel("Time")      
plt.ylabel("Hits/Hour")
plt.xticks([w*7*24 for w in range(10)],["week %i" %w for w in range(10)])#显示每个星期
plt.autoscale(tight=True)
plt.grid()
plt.show()