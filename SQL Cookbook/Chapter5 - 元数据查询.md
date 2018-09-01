```
5.1 列出模式中的表
# PostgreSQL、MySQL、SQL Server
SELECT table_name
    FROM information_schema.tables
WHERE table_schema = 'SMEAGOL';
```

```
5.2 列出表的列
# PostgreSQL、MySQL、SQL Server
SELECT column_name, data_type, ordinal_position
    FROM information_schema.columns
  WHERE table_schema = 'SMEAGOL' and table_name = 'EMP';
```

```
5.3 列出表的索引
# PostgreSQL
SELECT a.tablename, a.indexname, b.column_name
    FROM pg_catalog.pg_indexes a,
         information_schema.columns b
    WHERE a.schemaname = 'SMEAGOL'
      and a.tablename = b.table_name;
# MySQL
SHHOW INDEX FROM emp;
```

```
5.4 列出表约束
# PostgreSQL、MySQL、SQL Server
SELECT a.table_name,
       a.constraint_name,
       b.column_name,
       a.constraint_type
  FROM information_schema.table_constraints a,
       information_schema.key_column_usage b
  WHERE a.table_name = 'EMP'
    and a.table_schema = 'SMEAGOL'
    and a.table_name = b.table_name
    and a.table_schema = b.table_schema
    and a.constraint_name = b.constraint_name
```

```
5.5 列出没有相应索引的外键
# MySQL
SHOW INDEX
```

```
5.6 使用 SQL 来生成 SQL
SELECT 'SELECT count(*) from '||table_name||';' cnts FROM user_tables;
```
