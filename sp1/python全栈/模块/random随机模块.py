#random随机模块
import random

#0-1之间随机浮点数
ret = random.random()
print(ret)

#1-3之间的整数，包括3
ret1 = random.randint(1,3)
print(ret1)

#1-3之间的整数，不包括3
ret2 = random.randrange(1,3)
print(ret2)

#随机抽取序列中的某一元素
ret3 = random.choice([11,22,33])
print(ret3)

#从序列中选择n个随机且独立的元素
ret4 = random.sample([11,33,44,55],2)
print(ret4)

#以长整型形式返回n个随机位
ret5 = random.getrandbits(3)
print(ret5)

#随机打断序列中的元素
test = [11,23,424,111,1,32,4]
random.shuffle(test)
print(test)

#取指定范围内的随机数
ret7 = random.uniform(1,4)
print(ret7)



































