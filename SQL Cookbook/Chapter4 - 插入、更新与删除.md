```
4.1 插入新记录

INSERT INTO xx (field1, field2, field3) VALUES (value1, value2, value3)
```

```
4.2 插入默认值

INSERT INTO xx (field) values (default)

INSERT INTO D default values # PostgreSQL

```

```
4.3 使用NULL代替默认值
明确地指定 NULL 值
INSERT INTO (id, foo) VALUES (NULL, 'x')
```

```
4.4 从一个表向另外的表中复制行
INSERT INTO dept_east (deptno, dname, loc)
SELECT deptno, dname, loc
    FROM dept
  WHERE loc = 'New York'
```

```
4.5 复制表定义
问题：想创建一张表的副本，但只想复制表结构而不想要复制源表中的记录。
CREATE TABLE dept_2 LIKE dept # DB2
CREATE TABLE dept_2 AS 
  SELECT * FROM dept WHERE 1 = 0; # Oracle、MySQL、PostgreSQL
```

```
4.6 一次向多个表中插入记录
解决方案：将查询的结果插入到目标表中。
INSERT ALL / INSERT FIRST # ORACLE
```

```
4.7 阻止对某几列插入
问题：防止用户或是错误的软件应用程序对某几列插入数据。
解决方案：在表中创建一个视图，该视图将只允许用户进行操作的列，强制所有的插入操作都通过该视图进行。
CREATE VIEW news_emps AS
    SELECT empno, ename, job
    FROM emp;
```

```
4.8 在表中编辑记录
问题：要修改表中某些行的值。
UPDATE tmp SET sal = sal*1.10 WHERE deptno = 20;
```
```
4.9 当相应行存在更新时
问题：仅当另一个表中相应的行存在时，更新某表中的一些行。
UPDATE emp SET sal = sal * 1.20 
    WHERE empno IN (SELECT empno FROM emp_bonus)  # 可使用 EXISTS 代替 IN
```

```
4.10 用其他表中的值更新
问题：要用一个表中的值来更新另外一个表中的行。
解决方案：等值联结，子查询
UPDATE emp SET sal = ns.sal, comm = ns.sal/2 
    FROM new_sal ns WHERE ns.deptno = emp.deptno
```

```
4.11 合并记录
问题：根据表中记录存在状况，响应进行插入、更新或删除记录，条件为是否相应的数据。
解决方案：
书中只提到了 Oracle 在当时有解决方案。
 MERGE INTO emp_commission ec
 USING (SELECT * FROM emp) emp
    ON (ec.empno=emp.empno)
   WHEN MATCHED THEN
        UPDATE SET ec.comm = 1000
        DELETE WHERE sal < 2000
   WHEN not MATCHED THEN
        INSERT (ec.empno, ec.ename, ec.deptno, ec.comm)
        VALUES (emp,empno,emp.ename, emp.deptno,emp.comm)
```

```
4.12 从表中删除所有记录
问题：从表中删除所有记录。
DELETE FROM emp;
```

```
4.13 删除指定记录
4.14 删除单个记录
指定条件
```

```
4.15 删除违反参照完整性的记录
NOT EXISTS; NOT IN
```

```
4.16 删除重复记录
DELETE FROM dupes
  WHERE id not in (
    SELECT min(id) FROM dupes GROUP BY name 
  )
```

```
4.17 删除从其他表引用的记录
问题：从一个表中删除被另一个表引用的记录。
指定条件过滤 删除.
```