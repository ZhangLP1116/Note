### RESTful

> REST：**Re**presentational **S**tate **T**ransfer，表现层资源状态转移。
>
> 它是一种url设计规范
>
> REST 风格提倡 URL 地址使用统一的风格设计，从前到后各个单词使用斜杠分开，不使用问号键值对方式携带请求参数，而是将要发送给服务器的数据作为 URL 地址的一部分，以保证整体风格的一致性。

#### 1、RESTful示例

> | 操作     | 传统方式         | REST风格             |
> | -------- | ---------------- | -------------------- |
> | 查询操作 | getUserById?id=1 | user/1（Get请求）    |
> | 保存操作 | saveUser         | user（Post请求）     |
> | 删除操作 | deleteUser?id=1  | user/1（delete请求） |
> | 更新操作 | updateUser       | user（put请求）      |

#### 2、HiddenHttpMethodFilter

> 由于浏览器只支持发送get和post方式的请求，那么该如何发送put和delete请求呢？
>
> SpringMVC 提供了 **HiddenHttpMethodFilter** 帮助我们**将 POST 请求转换为 DELETE 或 PUT 请求**
>
> **HiddenHttpMethodFilter** 处理put和delete请求的条件：
>
> a>当前请求的请求方式必须为post
>
> b>当前请求必须传输请求参数_method（使用隐藏域传输）
>
> 满足以上条件，**HiddenHttpMethodFilter** 过滤器就会将当前请求的请求方式转换为请求参数_method的值，因此请求参数\_method的值才是最终的请求方式
>
> 在web.xml中注册**HiddenHttpMethodFilter** 
>
> ```xml
> <filter>
>     <filter-name>HiddenHttpMethodFilter</filter-name>
>     <filter-class>org.springframework.web.filter.HiddenHttpMethodFilter</filter-class>
> </filter>
> <filter-mapping>
>     <filter-name>HiddenHttpMethodFilter</filter-name>
>     <url-pattern>/*</url-pattern>
> </filter-mapping>
> ```
>
> ```html
> <input type="hidden" name="_method" value="PUT">
> ```

> 注：
>
> 目前为止，SpringMVC中提供了两个过滤器：CharacterEncodingFilter和HiddenHttpMethodFilter
>
> 在web.xml中注册时，必须先注册CharacterEncodingFilter，再注册HiddenHttpMethodFilter
>
> 原因：
>
> - 在 CharacterEncodingFilter 中通过 request.setCharacterEncoding(encoding) 方法设置字符集的
> - request.setCharacterEncoding(encoding) 方法要求前面不能有任何获取请求参数的操作
> - 而 HiddenHttpMethodFilter 恰恰有一个获取请求方式的操作：
> - String paramValue = request.getParameter(this.methodParam);

> 源码
>
> ```java
>     protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException {
>         HttpServletRequest requestToUse = request;
>         // 是否为POST请求
>         if ("POST".equals(request.getMethod()) && request.getAttribute("javax.servlet.error.exception") == null) {
>             // 获取_method属性参数
>             String paramValue = request.getParameter(this.methodParam);
>             if (StringUtils.hasLength(paramValue)) {
>                 String method = paramValue.toUpperCase(Locale.ENGLISH);
>                 if (ALLOWED_METHODS.contains(method)) {
>                     // 重新生成请求
>                     requestToUse = new HiddenHttpMethodFilter.HttpMethodRequestWrapper(request, method);
>                 }
>             }
>         }
> 
>         filterChain.doFilter((ServletRequest)requestToUse, response);
>     }
> ```
>
> 