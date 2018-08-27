```
2.1 以指定的次序返回查询结果
问题：按字段排序
ORDER BY
```

```
2.2 按多个字段排序
ORDER BY A, B DESC/ASC
```

```
2.3 按子串排序
问题：按字符串的某一部分对查询结果排序。
ORDER BY SUBSTR(a, len(a) - 2)  # DB2、MySQL、Oracle、PostgreSQL

ORDER BY SUBSTRING(a, len(a) -  2) # SQL SERVER
```

```
2.4 对字母数字混合的数据排序
问题：现有字母和数字混合的数据，希望按照数字或字符部分来排序
使用函数 REPLACE 和 TRANSLATE 修改要排序的字符串 # Oracle 和 PostgreSQL
```

```
2.5 处理空值排序
问题：空值排序到最后
使用 CASE WHEN ... THEN ... ELSE ... END
```

```
2.6 根据数据项的键排序
问题：根据某些条件逻辑来排序。
ORDER BY CASE WHEN job = 'SALESMAN' THEN commm ELSE sal END
```