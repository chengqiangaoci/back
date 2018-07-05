# pymysql.Connect()参数说明
# host(str):      MySQL服务器地址
# port(int):      MySQL服务器端口号
# user(str):      用户名
# passwd(str):    密码
# db(str):        数据库名称
# charset(str):   连接编码

# connection对象支持的方法
# cursor()        使用该连接创建并返回游标
# commit()        提交当前事务
# rollback()      回滚当前事务
# close()         关闭连接

# cursor对象支持的方法
# execute(op)     执行一个数据库的查询命令
# fetchone()      取得结果集的下一行
# fetchmany(size) 获取结果集的下几行
# fetchall()      获取结果集中的所有行
# rowcount()      返回数据条数或影响行数
# close()         关闭游标对象




import pymysql
#添加数据

conn = pymysql.connect(host='127.0.0.1', port=3306, user='chengqian', passwd='1889100b', db='test')#最后个是数据库名字

cursor = conn.cursor()


sql = """select * from emp"""
cursor.execute(sql)#执行
cursor.fetchall()
cursor.close()

#row_affected = cursor.execute("create table t1(id INT ,name VARCHAR(20))")

#row_affected=cursor.execute("INSERT INTO t1(id,name) values (1,'alvin'),(2,'xialv')")

#cursor.execute("update t1 set name = 'silv2' where id=2")




#查询数据
# row_affected=cursor.execute("select * from t1")
# one=cursor.fetchone()

# many=cursor.fetchmany(2)
# all=cursor.fetchall()



#scroll
#cursor.scroll(-1,mode='relative')  # 相对当前位置移动

#cursor.scroll(2,mode='absolute') # 相对绝对位置移动


#更改获取数据结果的数据类型,默认是元组,可以改为字典等:conn.cursor(cursor=pymysql.cursors.DictCursor)


# conn.commit()
# cursor.close()
# conn.close()











