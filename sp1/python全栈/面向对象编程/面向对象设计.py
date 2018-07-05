# dog1 = {
# 	"name":"xx",
# 	"gender":"公",
# 	"type":"泰迪"
# }
# def jiao(dog):
# 	print("%s,汪汪" %dog["name"])
# def chi(dog):
# 	print("吃粑粑")
# jiao(dog1)

#类：把一类事物的相同特征和动作整合到一起
#对象：就是具体的存在


#学校类：特征：name,addr,type
#学校类：动作:考试，招生，开除学生
# def school(name,addr,type):
# 	def exam(school):
# 		print("%s 考试" %school)
# 	def recruit(school):
# 		print("%s %s 正在招生" %(school["type"],school["name"]))
# 	sch = {
# 		"name":name,
# 		"addr":addr,
# 		"type":typ,
# 		"recruit":recruit,
# 		"exam":exam,
# 	}
# 	return sch
# s1 = school("oldboy","shahe","公立")
# print(s1)
# s1["recruit"](s1)#这里传入的s1就是sch

#初始化（包括特征和动作）、动作、返回初始化
def school(name,addr,type):
	def init(name,addr,type):
		sch = {
			"name":name,
			"addr":addr,
			"type":type,
			"recruit":recruit,
			"exam":exam,
		}
		return sch
	def exam(school):
		print("%s 考试" %school)
	def recruit(school):
		print("%s %s 正在招生" %(school["type"],school["name"]))
	return init(name,addr,type)
s1 = school("oldboy","shahe","公立")
print(s1)
s1["recruit"](s1)#这个函数要的参数是school,而这个参数要的是字典











