#外键就是一种约束，会在你删除不应当删除的东西时提示，但并没什么实质的意义

---  每一个班主任会对应多个学生 , 而每个学生只能对应一个班主任
----主表
CREATE TABLE ClassCharger(
       id TINYINT PRIMARY KEY auto_increment,
       name VARCHAR (20),
       age INT ,
       is_marriged boolean

);

INSERT INTO ClassCharger (name,age,is_marriged) VALUES ("冰冰",12,0),
                                                       ("丹丹",14,0),
                                                       ("歪歪",22,0),
                                                       ("姗姗",20,0),
                                                       ("小雨",21,0);


----子表
表里面的某个字段与另外一个表的某个字段关联
作为外键一定要和关联主键的数据类型保持一致
CREATE TABLE Student2(
       id INT PRIMARY KEY auto_increment,
       name VARCHAR (20),
       charger_id TINYINT,
       FOREIGN KEY (charger_id) REFERENCES ClassCharger(id)
) 
INSERT INTO Student2(name,charger_id) VALUES ("alvin1",2),
                                            ("alvin2",4),
                                            ("alvin3",1),
                                            ("alvin4",3),
                                            ("alvin5",1),
                                            ("alvin6",3),
                                            ("alvin7",2);


查看已建立的外键信息 show create table Student2;


表已经创建好了后，再增加外键，并自定义外键名
ALTER TABLE student2  ADD CONSTRAINT abc
                     FOREIGN KEY(charger_id)
                     REFERENCES  classcharger(id);

删除外键
ALTER TABLE student DROP FOREIGN KEY abc;








