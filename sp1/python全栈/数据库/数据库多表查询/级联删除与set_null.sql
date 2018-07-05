如果在父表中找不到候选键，则不允许在子表上进行才insert和update


如果先删除父表某部分的内容，相对应删除子表关联的内容
CREATE TABLE Student3(
       id INT PRIMARY KEY auto_increment,
       name VARCHAR (20),
       charger_id TINYINT,
       foreign key (charger_id) references classcharger(id) on delete cascade
)

INSERT INTO Student3(name,charger_id) VALUES ("alvin1",2),
                                            ("alvin2",4),
                                            ("alvin3",1),
                                            ("alvin4",3),
                                            ("alvin5",1),
                                            ("alvin6",3),
                                            ("alvin7",2);



如果先删除父表某部分的内容，相对应子表关联的内容编程null
FOREIGN KEY (charger_id) REFERENCES ClassCharger(id)
                              ON DELETE SET NULL



拒绝对父表进行删除更新操作
No action方式
Restrict方式






















