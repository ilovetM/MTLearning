```
6.1 遍历字符串
解决方案：笛卡尔积来生成行号，用来在该行中返回字符串中的每个字符。
SELECT SUBSTR(e.ename, iter.pos, 1) AS C
    FROM (SELECT ename FROM emp WHERE ename = 'KING') e,
         (SELECT id AS pos FROM t10) iter
  WHERE iter.pos <= length(e.ename)

```

```
6.2 字符串文字中包含引号
在使用引号时，一定要记住字符串是由两个引号来定义的，而在两个引号中没有任何字符时，表示 NULL。
```

```
6.3 计算字符在字符串中出现的次数
SEECT (LENGTH('10,CLARK,MANAFER') - length(replace('10,CLARK,MANAFER', ',', ' ')))/length(',') as cnt
FROM t1
使用减法。
```

```
6.4 从字符串中删除不需要的字符串
REPLACE TRANSLATE
```

```
6.5 将字符和数字数据分离
REPLACE TRANSLATE
```

```
6.6 判断字符串是不是字母数字型的
查出所有的字母与数字字符，这样就可以将它们转换为同一个字符，将所有的字母数字作为一个字符处理。
```

```
6.7 提取姓名的大写首字母缩写
# MySQL
CONCAT CONCAT_WS SUBSTRING SUBSTRING_INDEX
# PostgreSQL
REPLACE、TRANSLATE、RPAD
```

```
6.8 按字符串中的部分内容排序
# MySQL、PostgreSQL、DB2、Oracle
LENGTH SUBSTR

```

```
6.9 按字符串中的数值排序
REPLACE TRANSLATE
```

```
6.10 根据表中的行创建一个分隔列表
# MySQL
SELECT deptno,
       group_concat(ename order by  empno separator, ',) as emps
   FROM emp
GROUP BY deptno
```

```
6.11 将分隔数据转换为多列 IN 值
问题 IN ('a,b,c')
解决方案 实现分割
```

```
6.12 按字母顺序排列字符串
# MySQL
SELECT ename, group_concat(c order by c separator '')
    FROM (SELECT ename, substr(a.ename, iter.pos, 1) c
    FROM emp a,
    (SELECT id pos from t10) iter WHERE iter.pos <= length(a.ename) x
GROUP BY ename
```

```
6.13 判别可作为数值的字符串
REPLACE TRANSLATE ；将所有的数字转换成同一个字符
```

```
6.14 提取第 n 个分割的字串
split
```

```
6.14 分解 IP 地址
split
```
