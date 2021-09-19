### XML映射器

> 结构
>
> SQL 映射文件只有很少的几个顶级元素（按照应被定义的顺序列出）：
>
> - `cache` – 该命名空间的缓存配置。
> - `cache-ref` – 引用其它命名空间的缓存配置。
> - `resultMap` – 描述如何从数据库结果集中加载对象，是最复杂也是最强大的元素。
> - `sql` – 可被其它语句引用的可重用语句块。
> - `insert` – 映射插入语句。
> - `update` – 映射更新语句。
> - `delete` – 映射删除语句。
> - `select` – 映射查询语句。

#### select

> | 属性            | 描述                                                         |
> | :-------------- | :----------------------------------------------------------- |
> | `id`            | 在命名空间中唯一的标识符，可以被用来引用这条语句。           |
> | `parameterType` | 将会传入这条语句的参数的类全限定名或别名。这个属性是可选的，因为 MyBatis 可以通过类型处理器（TypeHandler）推断出具体传入语句的参数，默认值为未设置（unset）。 |
> | parameterMap    | 用于引用外部 parameterMap 的属性，目前已被废弃。请使用行内参数映射和 parameterType 属性。 |
> | `resultType`    | 期望从这条语句中返回结果的类全限定名或别名。 注意，如果返回的是集合，那应该设置为集合包含的类型，而不是集合本身的类型。 resultType 和 resultMap 之间只能同时使用一个。 |
> | `resultMap`     | 对外部 resultMap 的命名引用。结果映射是 MyBatis 最强大的特性，如果你对其理解透彻，许多复杂的映射问题都能迎刃而解。 resultType 和 resultMap 之间只能同时使用一个。 |
> | `flushCache`    | 将其设置为 true 后，只要语句被调用，都会导致本地缓存和二级缓存被清空，默认值：false。 |
> | `useCache`      | 将其设置为 true 后，将会导致本条语句的结果被二级缓存缓存起来，默认值：对 select 元素为 true。 |
> | `timeout`       | 这个设置是在抛出异常之前，驱动程序等待数据库返回请求结果的秒数。默认值为未设置（unset）（依赖数据库驱动）。 |
> | `fetchSize`     | 这是一个给驱动的建议值，尝试让驱动程序每次批量返回的结果行数等于这个设置值。 默认值为未设置（unset）（依赖驱动）。 |
> | `statementType` | 可选 STATEMENT，PREPARED 或 CALLABLE。这会让 MyBatis 分别使用 Statement，PreparedStatement 或 CallableStatement，默认值：PREPARED。 |
> | `resultSetType` | FORWARD_ONLY，SCROLL_SENSITIVE, SCROLL_INSENSITIVE 或 DEFAULT（等价于 unset） 中的一个，默认值为 unset （依赖数据库驱动）。 |
> | `databaseId`    | 如果配置了数据库厂商标识（databaseIdProvider），MyBatis 会加载所有不带 databaseId 或匹配当前 databaseId 的语句；如果带和不带的语句都有，则不带的会被忽略。 |
> | `resultOrdered` | 这个设置仅针对嵌套结果 select 语句：如果为 true，将会假设包含了嵌套结果集或是分组，当返回一个主结果行时，就不会产生对前面结果集的引用。 这就使得在获取嵌套结果集的时候不至于内存不够用。默认值：`false`。 |
> | `resultSets`    | 这个设置仅适用于多结果集的情况。它将列出语句执行后返回的结果集并赋予每个结果集一个名称，多个名称之间以逗号分隔。 |

#### insert、update、delete

> | `id`               | 在命名空间中唯一的标识符，可以被用来引用这条语句。           |
> | ------------------ | ------------------------------------------------------------ |
> | `parameterType`    | 将会传入这条语句的参数的类全限定名或别名。这个属性是可选的，因为 MyBatis 可以通过类型处理器（TypeHandler）推断出具体传入语句的参数，默认值为未设置（unset）。 |
> | `parameterMap`     | 用于引用外部 parameterMap 的属性，目前已被废弃。请使用行内参数映射和 parameterType 属性。 |
> | `flushCache`       | 将其设置为 true 后，只要语句被调用，都会导致本地缓存和二级缓存被清空，默认值：（对 insert、update 和 delete 语句）true。 |
> | `timeout`          | 这个设置是在抛出异常之前，驱动程序等待数据库返回请求结果的秒数。默认值为未设置（unset）（依赖数据库驱动）。 |
> | `statementType`    | 可选 STATEMENT，PREPARED 或 CALLABLE。这会让 MyBatis 分别使用 Statement，PreparedStatement 或 CallableStatement，默认值：PREPARED。 |
> | `useGeneratedKeys` | （仅适用于 insert 和 update）这会令 MyBatis 使用 JDBC 的 getGeneratedKeys 方法来取出由数据库内部生成的主键（比如：像 MySQL 和 SQL Server 这样的关系型数据库管理系统的自动递增字段），默认值：false。 |
> | `keyProperty`      | （仅适用于 insert 和 update）指定能够唯一识别对象的属性，MyBatis 会使用 getGeneratedKeys 的返回值或 insert 语句的 selectKey 子元素设置它的值，默认值：未设置（`unset`）。如果生成列不止一个，可以用逗号分隔多个属性名称。 |
> | `keyColumn`        | （仅适用于 insert 和 update）设置生成键值在表中的列名，在某些数据库（像 PostgreSQL）中，当主键列不是表中的第一列的时候，是必须设置的。如果生成列不止一个，可以用逗号分隔多个属性名称。 |
> | `databaseId`       | 如果配置了数据库厂商标识（databaseIdProvider），MyBatis 会加载所有不带 databaseId 或匹配当前 databaseId 的语句；如果带和不带的语句都有，则不带的会被忽略。 |

#### sql

> 用于创建可以复用的SQL语句
>
> sql标签定义
>
> ```xml
> <sql id="userColumns"> ${alias}.id,${alias}.username,${alias}.password </sql>
> ```
>
> include标签使用
>
> ```xml
> <select id="selectUsers" resultType="map">
>   select
>     <include refid="userColumns"><property name="alias" value="t1"/></include>,
>     <include refid="userColumns"><property name="alias" value="t2"/></include>
>   from some_table t1
>     cross join some_table t2
> </select>
> ```

#### cache

> 使用缓存的目的是减少重复查询带来的开销
>
> 应该被缓存的对象具有经常被查询且不经常修改的特点

> 缓存的配置和缓存实例会被绑定到 SQL 映射文件的命名空间中。 因此，同一命名空间中的所有语句和缓存将通过命名空间绑定在一起。 `每条语句可以自定义与缓存交互的方式`，或将它们完全排除于缓存之外，这可以通过在每条语句上使用两个简单属性来达成。 默认情况下，语句会这样来配置：
>
> ```xml
> <select ... flushCache="false" useCache="true"/>
> <insert ... flushCache="true"/>
> <update ... flushCache="true"/>
> <delete ... flushCache="true"/>
> ```

##### 一级缓存

> SqlSession级别，也叫本地缓存
>
> 它仅仅对一个会话中的数据进行缓存。在SqlSession存在期间有效，SqlSession调用close方法后失效

##### 二级缓存

>  namespace级别
>
>  要启用全局的二级缓存，只需要在你的 SQL 映射文件中添加一行：
>
>  ```xml
>  <cache/>
>  ```
>
>  效果
>
>  - 映射语句文件中的所有 select 语句的结果将会被缓存。
>  - 映射语句文件中的所有 insert、update 和 delete 语句会刷新缓存。
>  - 缓存会使用最近最少使用算法（LRU, Least Recently Used）算法来清除不需要的缓存。
>  - 缓存不会定时进行刷新（也就是说，没有刷新间隔）。
>  - 缓存会保存列表或对象（无论查询方法返回哪种）的 1024 个引用。
>  - 缓存会被视为读/写缓存，这意味着获取到的对象并不是共享的，可以安全地被调用者修改，而不干扰其他调用者或线程所做的潜在修改。
>
>  可以过cache标签的属性来改变缓存行为
>
>  ```xml
>  <cache
>   eviction="FIFO"
>   flushInterval="60000"
>   size="512"
>   readOnly="true"/>
>  ```
>
>  eviction：设置缓存清理算法，默认未LRU（最近少使用）
>
>  flushInterval：设置缓存刷新间隔
>
>  size：设置可缓存的最大``引用对象数量``
>
>  readOnly：设置缓存对象只读，可读写的缓存会（通过序列化）返回缓存对象的拷贝。 速度上会慢一些，但是更安全，因此默认值是 false。

> 注意
>
> - 二级缓存是事务性的。这意味着，当 SqlSession 完成并提交时，或是完成并回滚，但没有执行 flushCache=true 的 insert/delete/update 语句时，缓存会获得更新。
> - 缓存只作用于 cache 标签所在的映射文件中的语句。如果你混合使用 Java API 和 XML 映射文件，在共用接口中的语句将不会被默认缓存。你需要使用 @CacheNamespaceRef 注解指定缓存作用域。

##### 自定义缓存

> 1. 自定义缓存类，实现org.apache.ibatis.cache.Cache，且提供一个接受 String 参数作为 id 的构造器
>
> 2. 配置xml
>
>    ```xml
>    <cache type="com.domain.something.MyCustomCache"/>
>    ```
>
> 注意：缓存的配置（如清除策略、可读或可读写等），不能应用于自定义缓存。

#### cache-ref

> 对某一命名空间的语句，只会使用该命名空间的缓存进行缓存或刷新。 但你可能会想要在`多个命名空间中共享相同的缓存配置和实例`。要实现这种需求，你可以使用 cache-ref 元素来引用另一个缓存。
>
> ```xml
> <cache-ref namespace="com.someone.application.data.SomeMapper"/>
> ```

#### resultMap

> 将字段映射到对象属性，resultType可以实现自动映射是因为Mybatis自动创建了resultMap映射。
>
> result使用场景：
>
> - 对象名与列名不一致
> - 对象名与列名一部分不一致
> - 关联查询结果集
> - 嵌套查询结果集
>
> ```xml
>     <select id="getUid" resultMap="userResultMap">
>     select * from lol where uid = #{id}
>   </select>
> 
>     <resultMap id="userResultMap" type="com.zlp.pojo.lol">
>         <id property="uid" column="uid"/>
>         <result property="anchor" column="anchor"/>
>         <result property="room" column="room"/>
>         <result property="title" column="title"/>
>         <result property="hot" column="hot"/>
>     </resultMap>
> ```

##### resultMap结构

> - `constructor` - 用于在实例化类时，注入结果到构造方法中
>   - `idArg` - ID 参数；标记出作为 ID 的结果可以帮助提高整体性能
>   - `arg` - 将被注入到构造方法的一个普通结果
> - `id` – 一个 ID 结果；标记出作为 ID 的结果可以帮助提高整体性能
> - `result` – 注入到字段或 JavaBean 属性的普通结果
> - `association` – 一个复杂类型的关联；许多结果将包装成这种类型
>   - 嵌套结果映射 – 关联可以是 `resultMap` 元素，或是对其它结果映射的引用
> - `collection` – 一个复杂类型的集合
>   - 嵌套结果映射 – 集合可以是 `resultMap` 元素，或是对其它结果映射的引用
> - `discriminator` – 使用结果值来决定使用哪个 `resultMap`
>   - `case` – 基于某些值的结果映射
>     - 嵌套结果映射 – `case` 也是一个结果映射，因此具有相同的结构和元素；或者引用其它的结果映射

##### constructor标签

> 通过构造方法给实体类传入参数

##### association标签

> 实体类中存在以类为属性的字段时，使用该标签为其中的类赋值
>
> property：对应实体类中的属性名
>
> javaType：对应属性的类型
>
> ```xml
> <association property="teacher" javaType="com.zlp.pojo.Teacher">
>     <result property="id" column="t_id"/>
>     <result property="name" column="t_name"/>
> </association>
> ```

##### collection标签

> 实体类中存在以集合为属性的字段时，使用该标签为集合赋值
>
> property：对应实体类中的属性名
>
> javaType：该属性的java类型
>
> ofType：集合中包含元素的类型
>
> ```xml
> <collection property="courses" javaType="list" ofType="com.zlp.pojo.Course">
>     <result property="id" column="c_id"/>
>     <result property="name" column="c_name"/>
>     <result property="score" column="score" />
> </collection>
> ```

##### discriminator标签

> 用于处理复杂结构的结果映射
>
> discriminator就是在处理结果集有多种可能时正确的选择映射类型
>
> ```xml
> <resultMap id="vehicleResult" type="Vehicle">
>   <id property="id" column="id" />
>   <result property="vin" column="vin"/>
>   <result property="year" column="year"/>
>   <result property="make" column="make"/>
>   <result property="model" column="model"/>
>   <result property="color" column="color"/>
>   <discriminator javaType="int" column="vehicle_type">
>     <case value="1" resultMap="carResult"/>
>     <case value="2" resultMap="truckResult"/>
>     <case value="3" resultMap="vanResult"/>
>     <case value="4" resultMap="suvResult"/>
>   </discriminator>
> </resultMap>
> ```

##### 自动映射

> resultMap可以混合使用自动映射和手动映射。
>
> 当返回的结果集中有一部分列名和属性名相同，一部分不同，则resultMap标签中可以只手动配置那些名字不一致的映射，其他名字对应的可以省略将被自动映射。

> association、collection可以使用select标签关联一个查询，`其使用嵌套查询的形式表现出连接查询的结果`