#json的转换:使用dumps转换为字符串
# import json
# dic = {"chengqian":"gaoci"}
# print(type(dic))
# test = json.dumps(dic)#将所有类型都转换为字符串
# print(test,type(test))

#loads读取json数据：转换为原来的数据类型
import json
test = (1,3,6,44)
test1 = json.dumps(test)
f = open("number","w")
f.write(test1)

with open("number","r") as f:
	data = json.loads(f.read())
	print(data)
	print(type(data))











