### or

- 拼接 OR

    > 注意事项:
    >
    > 主动调用`or`表示紧接着下==一个==**方法**不是用`and`连接，不是接下来所有方法用or链接!(不调用`or`则默认为使用`and`连接)

- 例: `eq("id",1).or().eq("name","老王").eq("age","18")`
    --->`id = 1 or name = '老王 and age = 18'`



- OR 嵌套
- 例: `or(i -> i.eq("name", "李白").ne("status", "活着"))`
    --->`or (name = '李白' and status <> '活着')`



### and

```java
and(Consumer<Param> consumer)
and(boolean condition, Consumer<Param> consumer)
```

- AND 嵌套
- 例: `and(i -> i.eq("name", "李白").ne("status", "活着"))`
    --->`and (name = '李白' and status <> '活着')`



### nested（嵌套）

```java
nested(Consumer<Param> consumer)
nested(boolean condition, Consumer<Param> consumer)
```

- 正常嵌套 不带 AND 或者 OR
- 例: `nested(i -> i.eq("name", "李白").ne("status", "活着"))`
    --->`(name = '李白' and status <> '活着')`





###  apply（拼接sql）

```java
apply(String applySql, Object... params)
apply(boolean condition, String applySql, Object... params)
```

- 拼接 sql

    > 注意事项:
    >
    > 该方法可用于数据库**函数** 动态入参的`params`对应前面`applySql`内部的`{index}`部分.这样是不会有sql注入风险的,反之会有!

- 例: `apply("id = 1")`--->`id = 1`

- 例: `apply("date_format(dateColumn,'%Y-%m-%d') = '2008-08-08'")`
    --->`date_format(dateColumn,'%Y-%m-%d') = '2008-08-08'")`

- 例: `apply("date_format(dateColumn,'%Y-%m-%d') = {0}", "2008-08-08")`
    --->`date_format(dateColumn,'%Y-%m-%d') = '2008-08-08'")`



### func（动态SQL分支）

```java
func(Consumer<Children> consumer)
func(boolean condition, Consumer<Children> consumer)
```

- func 方法(主要方便在出现if...else下调用不同方法能不断链)
- 例: `func(i -> if(true) {i.eq("id", 1)} else {i.ne("id", 1)})`



###  select（设置查询字段）

```java
select(String... sqlSelect)
select(Predicate<TableFieldInfo> predicate)
select(Class<T> entityClass, Predicate<TableFieldInfo> predicate)
```

> 说明:
>
> 以上方法分为两类.
> 第二类方法为:过滤查询字段(主键除外),入参不包含 class 的调用前需要`wrapper`内的`entity`属性有值! 这两类方法重复调用以最后一次为准

- 例: `select("id", "name", "age")`
- 例: `select(i -> i.getProperty().startsWith("test"))`



### set（UpdateWrapper相关）

```java
set(String column, Object val)
set(boolean condition, String column, Object val)
```

- SQL SET 字段
- 例: `set("name", "老李头")`
- 例: `set("name", "")`--->数据库字段值变为**空字符串**
- 例: `set("name", null)`--->数据库字段值变为`null`



### setSql（UpdateWrapper相关）

```java
setSql(String sql)
```

- 设置 SET 部分 SQL
- 例: `setSql("name = '老李头'")`