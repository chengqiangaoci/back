#绘制简单的折线图,数字一般都在列表中
# import matplotlib.pyplot as f
# squares = [1,4,5,6,7,8]
# f.plot(squares)#plot函数根据数字绘制有意义的函数
# #设置图表标题，并给坐标轴加标签
# f.title("测试",fontsize=24)
# f.xlabel("x轴",fontsize=14)
# f.ylabel("y轴",fontsize=14)
# f.show()




#同时指定x和y轴的值
# import matplotlib.pyplot as f
# x_label = [1,3,5,7,9]
# y_label = [1,9,25,49,81]
# f.plot(x_label,y_label)
# f.title("test")
# f.xlabel("xzhou")
# f.ylabel("yzhou")
# f.show()



#自动计算数据
import matplotlib.pyplot as f
x_label = list(range(1,1001))
y_label = [x**2 for x in x_label]
f.plot(x_label,y_label)
f.title("test")
f.xlabel("xzhou")
f.ylabel("yzhou")
f.show()





#使用scatter绘制散点图
# import matplotlib.pyplot as f
# f.scatter(2,4,s=200)

# f.title("test title",fontsize=24)
# f.xlable("xzhou",fontsize=14)
# f.ylabel("yzhou",fontsize=14)
# f.show()






















