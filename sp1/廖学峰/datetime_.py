#datetime是python处理日期和时间的标准库

#获取当前日期和时间
from datetime import datetime
test = datetime.now()
print(test)

# #获取指定日期和时间
# test1 = datetime(2011,11,11,11,11,11)
# print(test1)

# #获取制定秒数：timestamp，其中1970的第一天为初始时间
test2 = datetime.now()
print(test2.timestamp())
# #从秒数获取时间
# test3 = 11144444444.0
# print(datetime.fromtimestamp(test3))

# #获取UTC标准时区（北京时间为UTC+8）
# test4 = 11111111111.0
# print(datetime.fromtimestamp(test4))#本地时间
# print(datetime.utcfromtimestamp(test4))#UTC时间

#很多情况下用户输入的是字符串时间，将str转换为datetime
# test5 = datetime.strptime("2018-2-13 19:20:21","%Y-%m-%d %H:%M:%S")
# print(test5)
#将datetime转换为字符串
test6 = datetime.now()
print(test6.strftime("%Y,%b %d %H:%S"))

# #datetime加减，也是使用+和-，但是要导入timedelta
# from datetime import datetime,timedelta
# test7 = datetime.now()
# test8 = test7 + timedelta(days=1)
# print(test8)

