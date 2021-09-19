### 动态Sql

> 动态 SQL 是 MyBatis 的强大特性之一。如果你使用过 JDBC 或其它类似的框架，你应该能理解根据不同条件拼接 SQL 语句有多痛苦，例如拼接时要确保不能忘记添加必要的空格，还要注意去掉列表最后一个列名的逗号。利用动态 SQL，可以彻底摆脱这种痛苦。

> 相关标签
>
> - if
> - choose (when, otherwise)
> - trim (where, set)
> - foreach

#### If

> 根据条件包含where子句
>
> ```xml
> <select id="findActiveBlogWithTitleLike"
>      resultType="Blog">
>   SELECT * FROM BLOG
>   WHERE state = ‘ACTIVE’
>   <if test="title != null">
>     AND title like #{title}
>   </if>
> </select>
> ```

#### Choose、when、otherwise

> 有时候，我们不想使用所有的条件，而只是想从多个条件中选择一个使用。针对这种情况，MyBatis 提供了 choose 元素，它有点像 Java 中的 switch 语句。
>
> ```xml
> <select id="findActiveBlogLike"
>      resultType="Blog">
>   SELECT * FROM BLOG WHERE state = ‘ACTIVE’
>   <choose>
>     <when test="title != null">
>       AND title like #{title}
>     </when>
>     <when test="author != null and author.name != null">
>       AND author_name like #{author.name}
>     </when>
>     <otherwise>
>       AND featured = 1
>     </otherwise>
>   </choose>
> </select>
> 
> ```
>
> title查找后不会进行author查找
>
> 传入了 “title” 就按 “title” 查找，传入了 “author” 就按 “author” 查找的情形。若两者都没有传入，就返回标记为 featured 的 BLOG（这可能是管理员认为，与其返回大量的无意义随机 Blog，还不如返回一些由管理员精选的 Blog）。

#### where

> 问题示例
>
> ```xml
> <select id="findActiveBlogLike"
>      resultType="Blog">
>   SELECT * FROM BLOG
>   WHERE
>   <if test="state != null">
>     state = #{state}
>   </if>
>   <if test="title != null">
>     AND title like #{title}
>   </if>
>   <if test="author != null and author.name != null">
>     AND author_name like #{author.name}
>   </if>
> </select>
> ```
>
> 若if test="state != null"不成立，则sql将会出错
>
> ```sql
> SELECT * FROM BLOG
> WHERE
> 
> SELECT * FROM BLOG
> WHERE
> AND title like ‘someTitle’
> ```
>
> 使用where标签可以避免这样的问题，*where* 元素只会在子元素返回任何内容的情况下才插入 “WHERE” 子句。而且，若子句的开头为 “AND” 或 “OR”，*where* 元素也会将它们去除。
>
> ```xml
> <select id="findActiveBlogLike"
>      resultType="Blog">
>   SELECT * FROM BLOG
>   <where>
>     <if test="state != null">
>          state = #{state}
>     </if>
>     <if test="title != null">
>         AND title like #{title}
>     </if>
>     <if test="author != null and author.name != null">
>         AND author_name like #{author.name}
>     </if>
>   </where>
> </select>
> ```

#### set

> set标签用于动态更新语句，忽略其它不更新的列
>
> ```xml
> <update id="updateAuthorIfNecessary">
>   update Author
>     <set>
>       <if test="username != null">username=#{username},</if>
>       <if test="password != null">password=#{password},</if>
>       <if test="email != null">email=#{email},</if>
>       <if test="bio != null">bio=#{bio}</if>
>     </set>
>   where id=#{id}
> </update>
> ```
>
> *set* 元素会动态地在行首插入 SET 关键字，并会删掉额外的逗号

#### trim

> 该标签可以实现上述where、set标签功能，自由度更高
>
> 实现where标签功能
>
> ```xml
> 子元素返回内容则添加前缀，并删除不合理的前缀and和or，这里的空格是必须的
> <trim prefix="WHERE" prefixOverrides="AND |OR ">
>   ...
> </trim>
> ```
>
> 实现set标签功能
>
> 子元素返回内容时添加前缀，删除多余的后缀逗号
>
> ```xml
> <trim prefix="SET" suffixOverrides=",">
>   ...
> </trim>
> ```

#### foreach

> 动态遍历
>
> ```xml
> <select id="selectPostIn" resultType="domain.blog.Post">
>   SELECT *
>   FROM POST P
>   WHERE ID in
>   <foreach item="item" index="index" collection="list"
>       open="(" separator="," close=")">
>         #{item}
>   </foreach>
> </select>
> ```

#### script

> 注解使用动态sql是使用script标签
>
> ```xml
>    @Update({"<script>",
>       "update Author",
>       "  <set>",
>       "    <if test='username != null'>username=#{username},</if>",
>       "    <if test='password != null'>password=#{password},</if>",
>       "    <if test='email != null'>email=#{email},</if>",
>       "    <if test='bio != null'>bio=#{bio}</if>",
>       "  </set>",
>       "where id=#{id}",
>       "</script>"})
>     void updateAuthorValues(Author author);
> ```

#### bind

> `bind` 元素允许你在 OGNL 表达式以外创建一个变量，并将其绑定到当前的上下文
>
> ```xml
> <select id="selectBlogsLike" resultType="Blog">
>   <bind name="pattern" value="'%' + _parameter.getTitle() + '%'" />
>   SELECT * FROM BLOG
>   WHERE title LIKE #{pattern}
> </select>
> ```

#### 多数据库支持

> 如果配置了 databaseIdProvider，你就可以在动态代码中使用名为 “`_databaseId`” 的变量来为不同的数据库构建特定的语句。比如下面的例子：
>
> ```xml
> <insert id="insert">
>   <selectKey keyProperty="id" resultType="int" order="BEFORE">
>     <if test="_databaseId == 'oracle'">
>       select seq_users.nextval from dual
>     </if>
>     <if test="_databaseId == 'db2'">
>       select nextval for seq_users from sysibm.sysdummy1"
>     </if>
>   </selectKey>
>   insert into users values (#{id}, #{name})
> </insert>
> ```

