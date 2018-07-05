import time
print(time.time())#获取当前时间与1970.1.1之差的秒数，时间戳

print(time.localtime())#具体的时间结构（年月日天。。。），结构化时间

# t = time.localtime()
# print(t.tm_year)#单单打印年
# print(t.tm_wday)#星期几（5的话是周六）

# print(time.gmtime())#获取原始时区UTC

# #结构化时间转换为时间戳
# print(time.mktime(time.localtime()))#必须给一个结构化时间的参数

# #将结构化时间转换为字符串时间
# print(time.strftime("%Y-%m-%d %X",time.localtime()))#X是时分秒的意思

# #将字符串时间转换为结构化时间
# print(time.strptime("2016:12:24:17:50:36","%Y:%m:%d:%X"))

#直接看时间
print(time.ctime())

#系统定义的
# import datetime
# print(datetime.datetime.now())








