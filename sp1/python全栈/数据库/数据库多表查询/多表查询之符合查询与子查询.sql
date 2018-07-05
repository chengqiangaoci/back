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


符合查询
查询员工年龄大于等于25岁的部门
SELECT DISTINCT department.dept_name--这里本来有两个技术部的结果，因为distinct过滤，最后剩一个
    FROM employee,department
    WHERE employee.dept_id = department.dept_id
    AND age>25;



以内连接的方式查询employee和department表，并且以age字段的升序方式显示

    select employee.emp_id,employee.emp_name,employee.age,department.dept_name
    from employee,department
    where employee.dept_id = department.dept_id
    order by age asc;






子查询:算并集
-- 子查询是将一个查询语句嵌套在另一个查询语句中。
-- 内层查询语句的查询结果，可以为外层查询语句提供查询条件。
-- 子查询中可以包含：IN、NOT IN、ANY、ALL、EXISTS 和 NOT EXISTS等关键字
-- 还可以包含比较运算符：= 、 !=、> 、<等


-- 1. 带IN关键字的子查询

   ---查询employee表，但只显示在department表中出现过dept_id

   select * from employee
            where dept_id IN
            (select dept_id from department);


+--------+----------+------+---------+
| emp_id | emp_name | age  | dept_id |
+--------+----------+------+---------+
|      1 | A        |   19 |     200 |
|      2 | B        |   26 |     201 |
|      3 | C        |   30 |     201 |
|      4 | D        |   24 |     202 |
|      5 | E        |   20 |     200 |
+--------+----------+------+---------+
5 rows in set (0.01 sec)



2. 带比较运算符的子查询
=、!=、>、>=、<、<=、<>
查询员工年龄大于等于25岁的部门
     select * from department
           where dept_id IN
          (select DISTINCT dept_id from employee where age>=25);

3. 带EXISTS关键字的子查询

-- EXISTS关字键字表示存在。在使用EXISTS关键字时，内层查询语句不返回查询的记录。
-- 而是返回一个真假值。Ture或False
-- 当返回Ture时，外层查询语句将进行查询；当返回值为False时，外层查询语句不进行查询

     select * from employee
              WHERE EXISTS
              (SELECT dept_name from department where dept_id=203);

      --department表中存在dept_id=203，Ture


     select * from employee
                WHERE EXISTS
              (SELECT dept_name from department where dept_id=205);

     -- Empty set (0.00 sec)


    ps:  create table t1(select * from t2);
