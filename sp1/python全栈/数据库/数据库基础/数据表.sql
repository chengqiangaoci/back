CREATE TABLE employee(
	id TINYINT primary key auto_increment, 
	name VARCHAR(25),#不定长字符串
	gender boolean,#布尔类型，实际上没指定数据类型,相当于0与1
	age INT,#数字型4字节
	department varchar(20),
	salary double(7,2)#浮点型八字节，eg:44444.44
)
#查看表信息
创建表 create table
主键   primary key
自动递增 auto_increment
显示表格 show tables
查看表格具体内容：desc xx
查看表创建信息 show create table xx

#修改表结构
增加字段 alter table xx add is_married tinyint(1)#布尔值
alter table xx add entry_date date not null

删除字段 alter table xx drop is_married 

修改字段信息 alter table tab_name(想修改的表格) modify 列名 类型（修改后的类型）
alter table employee modify age smallint not null default 18 after id#将age放在id后，default设置为18

修改列名 alter table tab_name change 先前 改后 

更改表名 rename table 旧名 to 新名

删除表 drop table xx


