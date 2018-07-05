多表查询：
		连接查询：
				内连接：inner join
				外连接：left join    right join
				全连接：full join

-- 准备两张表
-- company.employee
-- company.department

      create table employee(
      emp_id int auto_increment primary key not null,
      emp_name varchar(50),
      age int,
      dept_id int
      );

      insert into employee(emp_name,age,dept_id) values
        ('A',19,200),
        ('B',26,201),
        ('C',30,201),
        ('D',24,202),
        ('E',20,200),
        ('F',38,204);


    create table department(
       dept_id int,
       dept_name varchar(100)
      );

    insert into department values
      (200,'人事部'),
      (201,'技术部'),
      (202,'销售部'),
      (203,'财政部');
mysql> select * from employee;
+--------+----------+------+---------+
| emp_id | emp_name | age  | dept_id |
+--------+----------+------+---------+
|      1 | A        |   19 |     200 |
|      2 | B        |   26 |     201 |
|      3 | C        |   30 |     201 |
|      4 | D        |   24 |     202 |
|      5 | E        |   20 |     200 |
|      6 | F        |   38 |     204 |
+--------+----------+------+---------+

mysql> select * from department;
+---------+-----------+
| dept_id | dept_name |
+---------+-----------+
|     200 | 人事部    |
|     201 | 技术部    |
|     202 | 销售部    |
|     203 | 财政部    |
+---------+-----------+



笛卡尔积查询
mysql> SELECT * FROM employee,department;
+--------+----------+------+---------+---------+-----------+
| emp_id | emp_name | age  | dept_id | dept_id | dept_name |
+--------+----------+------+---------+---------+-----------+
|      1 | A        |   19 |     200 |     200 | 人事部    |
|      1 | A        |   19 |     200 |     201 | 技术部    |
|      1 | A        |   19 |     200 |     202 | 销售部    |
|      1 | A        |   19 |     200 |     203 | 财政部    |
|      2 | B        |   26 |     201 |     200 | 人事部    |
|      2 | B        |   26 |     201 |     201 | 技术部    |
|      2 | B        |   26 |     201 |     202 | 销售部    |
|      2 | B        |   26 |     201 |     203 | 财政部    |
|      3 | C        |   30 |     201 |     200 | 人事部    |
|      3 | C        |   30 |     201 |     201 | 技术部    |
|      3 | C        |   30 |     201 |     202 | 销售部    |
|      3 | C        |   30 |     201 |     203 | 财政部    |
|      4 | D        |   24 |     202 |     200 | 人事部    |
|      4 | D        |   24 |     202 |     201 | 技术部    |
|      4 | D        |   24 |     202 |     202 | 销售部    |
|      4 | D        |   24 |     202 |     203 | 财政部    |
|      5 | E        |   20 |     200 |     200 | 人事部    |
|      5 | E        |   20 |     200 |     201 | 技术部    |
|      5 | E        |   20 |     200 |     202 | 销售部    |
|      5 | E        |   20 |     200 |     203 | 财政部    |
|      6 | F        |   38 |     204 |     200 | 人事部    |
|      6 | F        |   38 |     204 |     201 | 技术部    |
|      6 | F        |   38 |     204 |     202 | 销售部    |
|      6 | F        |   38 |     204 |     203 | 财政部    |
+--------+----------+------+---------+---------+----------


内连接和左外连接最重要
内连接
查询两张表中都有的关联数据,相当于利用条件从笛卡尔积结果中筛选出了正确的结果。
select * from employee,department where employee.dept_id = department.dept_id;
--select * from employee inner join department on employee.dept_id = department.dept_id;
+--------+----------+------+---------+---------+-----------+
      | emp_id | emp_name | age  | dept_id | dept_id | dept_name |
      +--------+----------+------+---------+---------+-----------+
      |      1 | A        |   19 |     200 |     200 | 人事部    |
      |      2 | B        |   26 |     201 |     201 | 技术部    |
      |      3 | C        |   30 |     201 |     201 | 技术部    |
      |      4 | D        |   24 |     202 |     202 | 销售部    |
      |      5 | E        |   20 |     200 |     200 | 人事部    |
      +--------+----------+------+---------+---------+-----------+


左外连接：在内连接的基础上增加左边有右边没有的结果
select * from employee left join department on employee.dept_id = department.dept_id;
 +--------+----------+------+---------+---------+-----------+
    | emp_id | emp_name | age  | dept_id | dept_id | dept_name |
    +--------+----------+------+---------+---------+-----------+
    |      1 | A        |   19 |     200 |     200 | 人事部    |
    |      5 | E        |   20 |     200 |     200 | 人事部    |
    |      2 | B        |   26 |     201 |     201 | 技术部    |
    |      3 | C        |   30 |     201 |     201 | 技术部    |
    |      4 | D        |   24 |     202 |     202 | 销售部    |
    |      6 | F        |   38 |     204 |    NULL | NULL      |
    +--------+----------+------+---------+---------+-----------+




右外连接：在内连接的基础上增加右边有左边没有的结果

select * from employee RIGHT JOIN department on employee.dept_id = department.dept_id;

+--------+----------+------+---------+---------+-----------+
| emp_id | emp_name | age  | dept_id | dept_id | dept_name |
+--------+----------+------+---------+---------+-----------+
|      1 | A        |   19 |     200 |     200 | 人事部    |
|      2 | B        |   26 |     201 |     201 | 技术部    |
|      3 | C        |   30 |     201 |     201 | 技术部    |
|      4 | D        |   24 |     202 |     202 | 销售部    |
|      5 | E        |   20 |     200 |     200 | 人事部    |
|   NULL | NULL     | NULL |    NULL |     203 | 财政部    |
+--------+----------+------+---------+---------+-----------+


全外连接：在内连接的基础上增加左边有右边没有的和右边有左边没有的结果
-- mysql不支持全外连接 full JOIN
    -- mysql可以使用此种方式间接实现全外连接
    
   select * from employee RIGHT JOIN department on employee.dept_id = department.dept_id
   UNION
   select * from employee LEFT JOIN department on employee.dept_id = department.dept_id;

        

        +--------+----------+------+---------+---------+-----------+
        | emp_id | emp_name | age  | dept_id | dept_id | dept_name |
        +--------+----------+------+---------+---------+-----------+
        |      1 | A        |   19 |     200 |     200 | 人事部    |
        |      2 | B        |   26 |     201 |     201 | 技术部    |
        |      3 | C        |   30 |     201 |     201 | 技术部    |
        |      4 | D        |   24 |     202 |     202 | 销售部    |
        |      5 | E        |   20 |     200 |     200 | 人事部    |
        |   NULL | NULL     | NULL |    NULL |     203 | 财政部    |
        |      6 | F        |   38 |     204 |    NULL | NULL      |
        +--------+----------+------+---------+---------+-----------+

      -- 注意 union与union all的区别：union会去掉相同的纪录




































































































