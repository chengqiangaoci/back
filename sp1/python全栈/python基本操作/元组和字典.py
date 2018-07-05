#创建元组的时候，一般在最后加个逗号，与函数区分
# test = (1,2,3,"xxxxx",[33,34],[("chengqian","gaoci"),("qian","cew")])
# print(test)

#元组不可被删除、修改、增加。
#元组可以被for循环
#元组是有序的
#元组中列表的元素可以被修改


#列表、字典不能作为字典的key，元组可以为key
info = {
    "k1":19,
    "k2":True,
    "k3":[
    11,
    12,
    13,
    {
    "kk1":"vv1",
    "kk2":"vv2",
    }
    ],
    "k4":()
}
test = info["k1"]
print(test)
# print(info)#字典里可以有其它类型的元素
# v1 = info["k3"] #取value
# print(v1)
# del info["k1"]#删除键对
# print(info)

#获取键位对可以使用for循环
# for i,v in info.items():#获取键和值
# 	print(i,v)

for i,v in enumerate(info):#获取键和它所处的位置
	print(i,v)

#根据序列创建字典
# v = dict.fromkeys(["k1","222",222],3)#根据序列创建字典，第一个序列是key，第二个序列是value
# print(v)

#指定取值
# v = info.get("k1111","wrong")#指定取值，如果没找到的话会返回1111,如果这里没有指定参数，则返回none
# print(v)

#删除
# info.pop("k1")#删除键和值
# print(info)

#更新
# info.update({"k1":1111})#进行更新
# print(info)
# info.update(k1=123,k3=345)#也可以用这种方式写，得到的还是字典
# print(info)



