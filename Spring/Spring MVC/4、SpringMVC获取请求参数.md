### 获取请求参数

#### 1、通过ServletAPI获取

> 使用原生ServledtAPI获取请求参数
>
> ```JAVA
> @RequestMapping("/testParam")
> public String testParam(HttpServletRequest request){
>     String username = request.getParameter("username");
>     String password = request.getParameter("password");
>     System.out.println("username:"+username+",password:"+password);
>     return "success";
> }
> ```

#### 2、通过控制器方法形参获取

> 在控制方法中设置与请求同名的形参，DispatcherServlet就会将请求参数赋值给相应的形参。
>
> 若没对应值则形参值为null
>
> ```HTML
> <a th:href="@{/testParam(username='admin',password=123456)}">测试获取请求参数-->/testParam</a><br>
> ```
>
> ```java
> @RequestMapping("/testParam")
> public String testParam(String username, String password){
>     System.out.println("username:"+username+",password:"+password);
>     return "success";
> }
> ```

#### 3、@RequestParam注解获取

> @RequestParam注解：将请求中的参数映射到控制方法的形参中
>
> @RequestParam注解一共有三个属性：
>
> value：指定为形参赋值的请求参数的参数名
>
> required：设置是否必须传输此请求参数，默认值为true
>
> 若设置为true时，则当前请求必须传输value所指定的请求参数，若没有传输该请求参数，且没有设置defaultValue属性，则页面报错400：Required String parameter 'xxx' is not present；若设置为false，则当前请求不是必须传输value所指定的请求参数，若没有传输，则注解所标识的形参的值为null
>
> defaultValue：不管required属性值为true或false，当value所指定的请求参数没有传输或传输的值为""时，则使用默认值为形参赋值

> ```JAVA
>     @RequestMapping("/testpojo")
>     public String testpojo(
>             @RequestParam(value = "username", defaultValue = "zlp", required = false) String name,
>             String pwd
>     ){
>         return "testpojo";
>     }
> ```

#### 4、@RequestHeader注解获取

> @RequestHeader是将请求头信息和控制器方法的形参创建映射关系
>
> @RequestHeader注解一共有三个属性：value、required、defaultValue，用法同@RequestParam

#### 5、@CookieValue注解获取

> @CookieValue是将cookie数据和控制器方法的形参创建映射关系
>
> @CookieValue注解一共有三个属性：value、required、defaultValue，用法同@RequestParam

#### 6、通过POJO获取

> 控制方法中设置实体类（bean），将请求参数封装到实体类中（bean）
>
> 若浏览器传输的请求参数的参数名和实体类中的属性名一致，那么请求参数就会为此属性赋值
>
> ```java
> package com.zlp;
> 
> import org.springframework.stereotype.Repository;
> 
> @Repository
> public class User {
>     private String username;
>     private String password;
>     private String age;
>     private String email;
>     private String sex;
> 
>     @Override
>     public String toString() {
>         return "User{" +
>                 "username='" + username + '\'' +
>                 ", password='" + password + '\'' +
>                 ", age='" + age + '\'' +
>                 ", email='" + email + '\'' +
>                 ", sex='" + sex + '\'' +
>                 '}';
>     }
> 
>     public void setUsername(String username) {
>         this.username = username;
>     }
> 
>     public void setPassword(String password) {
>         this.password = password;
>     }
> 
>     public void setAge(String age) {
>         this.age = age;
>     }
> 
>     public void setEmail(String email) {
>         this.email = email;
>     }
> 
>     public void setSex(String sex) {
>         this.sex = sex;
>     }
> 
>     public String getUsername() {
>         return username;
>     }
> 
>     public String getPassword() {
>         return password;
>     }
> 
>     public String getAge() {
>         return age;
>     }
> 
>     public String getEmail() {
>         return email;
>     }
> 
>     public String getSex() {
>         return sex;
>     }
> }
> ```
>
> ```HTML
> <form th:action="@{/testpojo}" method="post">
>     用户名：<input type="text" name="username"><br>
>     密码：<input type="password" name="password"><br>
>     性别：<input type="radio" name="sex" value="男">男<input type="radio" name="sex" value="女">女<br>
>     年龄：<input type="text" name="age"><br>
>     邮箱：<input type="text" name="email"><br>
>     <input type="submit">
> </form>
> ```
>
> ```java
> @RequestMapping("/testpojo")
> public String testPOJO(User user){
>     System.out.println(user);
>     return "success";
> }
> ```

#### 7、设置过滤器处理中文乱码

> 解决获取请求参数的乱码问题，可以使用SpringMVC提供的编码过滤器CharacterEncodingFilter，但是必须在web.xml中进行注册
>
> ```xml
> <!--配置springMVC的编码过滤器-->
> <filter>
>     <filter-name>CharacterEncodingFilter</filter-name>
>     <filter-class>org.springframework.web.filter.CharacterEncodingFilter</filter-class>
>     <init-param>
>         <param-name>encoding</param-name>
>         <param-value>UTF-8</param-value>
>     </init-param>
>     <init-param>
>         <param-name>forceResponseEncoding</param-name>
>         <param-value>true</param-value>
>     </init-param>
> </filter>
> <filter-mapping>
>     <filter-name>CharacterEncodingFilter</filter-name>
>     <url-pattern>/*</url-pattern>
> </filter-mapping>
> ```

> 注：
>
> SpringMVC中处理编码的过滤器一定要配置到其他过滤器之前，否则无效