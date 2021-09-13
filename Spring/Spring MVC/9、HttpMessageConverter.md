### Http报文转换

> HttpMessageConverter，报文信息转换器，将请求报文转换为Java对象，或将Java对象转换为响应报文
>
> HttpMessageConverter提供了两个注解和两个类型：@RequestBody，@ResponseBody，RequestEntity，ResponseEntity
>
> 这四个方式中两个请求相关的使用较少，获取请求的方法有很多种
>
> 响应的类和注解使用较多

#### 1、@RequestBody

> @RequestBody可以获取请求体，需要在控制器方法设置一个形参，使用@RequestBody进行标识，当前请求的请求体就会为当前注解所标识的形参赋值
>
> ```html
> <form th:action="@{/testRequestBody}" method="post">
>     用户名：<input type="text" name="username"><br>
>     密码：<input type="password" name="password"><br>
>     <input type="submit">
> </form>
> ```
>
> ```java
> @RequestMapping("/testRequestBody")
> public String testRequestBody(@RequestBody String requestBody){
>     System.out.println("requestBody:"+requestBody);
>     return "success";
> }
> ```
>
> 输出结果：
>
> requestBody:username=admin&password=123456

#### 2、RequestEntity

> RequestEntity封装请求报文的一种类型，需要在控制器方法的形参中设置该类型的形参，当前请求的请求报文就会赋值给该形参，可以通过getHeaders()获取请求头信息，通过getBody()获取请求体信息
>
> ```java
> @RequestMapping("/testRequestEntity")
> public String testRequestEntity(RequestEntity<String> requestEntity){
>     System.out.println("requestHeader:"+requestEntity.getHeaders());
>     System.out.println("requestBody:"+requestEntity.getBody());
>     return "success";
> }
> ```
>
> 输出结果：
> requestHeader:[host:"localhost:8080", connection:"keep-alive", content-length:"27", cache-control:"max-age=0", sec-ch-ua:"" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"", sec-ch-ua-mobile:"?0", upgrade-insecure-requests:"1", origin:"http://localhost:8080", user-agent:"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"]
>
> 
>
> requestBody:username=admin&password=123

#### 3、@ResponseBody

> @ResponseBody用于标识一个控制器方法，可以将该方法的返回值直接作为响应报文的响应体响应到浏览器（默认报文类型：text）
>
> ```java
> @RequestMapping("/testResponseBody")
> @ResponseBody
> public String testResponseBody(){
>     return "success";
> }
> ```
>
> 结果：浏览器页面显示success
>
> HttpServletResponse原生API实现
>
> ```java
>     @RequestMapping("/testResponseBody")
>     @ResponseBody
>     public void testResponseBody(HttpServletResponse response) throws IOException {
>         response.getWriter().println("success");
>     }
> ```
>
> 

#### 4、SpringMVC处理json

> 1. 导入依赖
>
>    ```xml
>    <dependency>
>        <groupId>com.fasterxml.jackson.core</groupId>
>        <artifactId>jackson-databind</artifactId>
>        <version>2.12.1</version>
>    </dependency>
>    ```
>
> 2. 在SpringMVC的核心配置文件中开启mvc的注解驱动
>
>    ```xml
>    <mvc:annotation-driven />
>    ```
>
> 3. 在处理器方法上使用@ResponseBody注解进行标识
>
> 4. 将Java对象直接作为控制器方法的返回值返回，就会自动转换为Json格式的字符串
>
>    ```java
>    @RequestMapping("/testResponseUser")
>    @ResponseBody
>    public User testResponseUser(){
>        return new User(1001,"admin","123456",23,"男");
>    }
>    ```

#### 5、SpringMVC处理ajax

> 1. 请求地址
>
>    ```html
>    <div id="app">
>    	<a th:href="@{/testAjax}" @click="testAjax">testAjax</a><br>
>    </div>
>    ```
>
> 2. vue.js代码
>
>    ```html
>    <script type="text/javascript" th:src="@{/static/js/vue.js}"></script>
>    <script type="text/javascript" th:src="@{/static/js/axios.min.js}"></script>
>    <script type="text/javascript">
>        var vue = new Vue({
>            el:"#app",
>            methods:{
>                testAjax:function (event) {
>                    axios({
>                        method:"post",
>                        url:event.target.href,
>                        params:{
>                            username:"admin",
>                            password:"123456"
>                        }
>                    }).then(function (response) {
>                        alert(response.data);
>                    });
>                    event.preventDefault();
>                }
>            }
>        });
>    </script>
>    ```
>
> 3. 后端处理
>
>    ```java
>    @RequestMapping("/testAjax")
>    @ResponseBody
>    public String testAjax(String username, String password){
>        System.out.println("username:"+username+",password:"+password);
>        return "hello,ajax";
>    }
>    ```

#### 6、@RestController注解

> @RestController注解是springMVC提供的一个复合注解，标识在控制器的类上，就相当于为类添加了@Controller注解，并且为其中的每个方法添加了@ResponseBody注解

#### 7、ResponseEntity

> ResponseEntity用于控制器方法的返回值类型，该控制器方法的返回值就是响应到浏览器的响应报文
>
> （用于控制响应到浏览器的报文）

