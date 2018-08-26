```
1.1 从表中检索所有行和列
问题：查看表中的所有数据。
显式地指定列，便于所有人理解。
```

```
1.2 从表中检索部分行
问题：从表中查看满足特定条件的行。
使用 WHERE
```

```
1.3 查找满足多个条件
问题：要返回满足多个条件的行。
使用 WHERE 字句以及 OR 和 AND 子句。
```

```
1.4 从表中检索部分列
问题：要查看一个表中特定列的值，而不是所有列的值。
SELECT 指定列名
```

```
1.5 为列取有意义的名称
问题：改变查询所返回的列名，使它们更具有可读性。
AS
```

```
1.6 在 WHERE 子句中引用取别名的列
WHERE 后 直接使用 ALIAS 的名称
```

```
1.7 连接列值
问题：拼接字段及字符串
MySQL 使用 CONCAT;
SELECT CONCAT(name + ' WORK AS A ' + job AS msg) FROM <TableName>;

DB2, Oracle, PostgreSQL 使用 ||
SELECT name||' WORK AS A '||job as msg
```

```
1.8 在 SELECT 语句中使用条件逻辑
CASE WHEN ... THEN ... ELSE ... END
SELECT ename, sal,
        CASE WHEN sal <= 2000 then 'UNDERPAID'
            WHEN sal >= 4000 then 'OVERPAID'
            ELSE 'OK'
        END AS status
    FROM emp
```

```
1.9 限制返回的行数
MySQL 、PostgreSQL
LIMIT OFF
```

```
1.10 从表中随机返回 n 条记录
查阅相关 RAND 函数
```

```
1.11 查找空值
IS NULL
```

```
1.12 将空值转换为实际值
SELECT COALESCE(comm, 0) FROM emp
也可以使用 CASE WHEN ... THEN ... ELSE ... END
```

```
1.13 按模式搜索
LIKE
```