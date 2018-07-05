增加一条记录insert into emp (id,name,xx,xx) values(1,"chengqian",xx,xx)
增加多条记录insert into emp (id,name,xx,xx),(id,name,xx,xx) .....
insert into emp values()这里面必须全部变量
insert into emp set 变量=xx

修改一条记录update emp set salary=salary+20000,xx=xx+20000 where name="xx"

删除记录delete from emp(后面要是什么都没有的话就是清空！！！) where id=2 or(2和3)id=3

清空表 delete from emp

直接删除表truncate table emp

查询所有字段 select * from xx(表格名)










