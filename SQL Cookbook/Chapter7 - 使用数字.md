```
7.1 计算平均值
avg
```

```
7.2 求某列中的最小/最大值
SELECT min(sal) as min_sal, max(sal) as max_sal from emp;
```

```
7.3 对某列的值求和
sum
```

```
7.4 求一个表的行数
count
```

```
7.5 求某列值得个数
SELECT count() from emp # count(cloumn) cloumn 指定后悔统计不会空的个数
```

```
7.6 生成累计和
# MySQL 、PostgreSQL
SELECT e.name, e.sal,
    (SELECT sum(d.sal) from emp d)
    WHERE d.empno <= e.empno) as running_total
    FROM emp e
ORDER BY 3
```

```
7.7 生成累乘积
标量子查询
```

```
7.8 计算累积差
标量子查询
```

```
7.9 计算模式（找出出现最频繁的元素）
子查询
```

```
7.10 计算中间值
自连结
```

```
7.11 求总和的百分比
先除后乘。
```

```
7.12 对可空列做聚集
avg(coalesce(comm, 0))
```

```
7.13 计算不包含最大值和最小值的均值
子查询
```

```
7.14 把字母数字串转换为数值
TRANSLATE REPLACE
```

```
7.15 更改累计和中的值
标量子查询，创建累计和， CASE WHEN
```

```
```
