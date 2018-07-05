事务指逻辑上的一组操作，组成这组操作的各个单元，要不全部成功，要不全部不成功。
create table account(id int,name varchar(20),balance double);
insert into account values(1,"chengqian",8000);
insert into account values(2,"gaoci",8000);

start transaction --开启事务
update account set balance=balance-5000 where id=1;--硬盘上实际上还没有扣5000，因为事务还没结束
发现上面那句有错误，于是回滚（回滚只能回滚insert delete update语句）

rollback;--撤销到事务开始的第一步

update account set balance=balance-5000 where id=1;--硬盘上还是没
update account set balance=balance+5000 where id=2;--这次事务正确

commit --提交事务，提交未存储的事务





savepoint--保留点，事务处理中设置的临时占位符，你可以对它发布回退，而不是整个事务回退
create table test2(id int PRIMARY KEY auto_increment,name VARCHAR(20)) engine=innodb;
INSERT INTO test2(name) VALUE ("alvin"),
                              ("yuan"),
                              ("xialv");
start transaction;
insert into test2 (name)values('silv');
select * from test2;
commit;

-- 保留点

start transaction;
insert into test2 (name)values('wu');
savepoint insert_wu;
select * from test2;

delete from test2 where id=4;
savepoint delete1;
select * from test2;

delete from test2 where id=1;
savepoint delete2;
select * from test2;

rollback to delete1;

