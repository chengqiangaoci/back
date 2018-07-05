查询所有记录select * from emp
查询某项记录select xx(如id,name....) from emp
查询某些记录select xx,xx from emp

create table ExamResult(
id int primary key auto_increment,
name varchar(20),
Js double,
Django double,
flask double
)

insert into ExamResult values (2,"xialv",35,93,92),
							  (3,"alex",99,23,72),
							  (4,"wusir",89,23,82),
							  (5,"alvin",29,63,92),
							  (6,"yuan",69,23,62)


去掉重复的记录 select distinct id from ExamResult(如id1，2,3重复，则去掉2和3)


过滤where
select name,js from ExamResult where js>80
包括between x and y  x到y之间
in(x,y,z)值是x或y或z
like "李%" 模糊匹配
like"李_" 模糊匹配一个字节
is null 空值



排序order by
select name,js from ExamResult order by js #默认升序
select name,js from examresult where js>70 order by js
select name,js from examresult order by js desc#降序



分组查询group by
按分组条件分组后每一组只会显示第一条记录(就是会过滤掉重复的)
select * from examresult group by name（可以变为第几组，如第一组是id，就用1） 按名字排序
select name,sum(JS) from examresult group by name#因为有重复的名字，因此将重复的名字的JS相加在分组
对分组后的过滤是having，对分组前的过滤是where
select name,sum(Django) from examresult group by name having sum(Django)>150
最好都用having



聚合函数
select count(name) from examresult where js>70#js大于70的名字个数 
select sum(js)/count(name) from examresult#JS的平均成绩，但是null值也计算在name中
select avg(js) from examresult#JS的平均成绩

ifnull(JS,0)如果js是null，则将其变为0

select max(js) from examresult
select min(js) from examresult


限制limit
select * from examresult limit 3     前3
select * from examresult limit 1,5   跟python索引一样，跳过第一条，然后选5条




