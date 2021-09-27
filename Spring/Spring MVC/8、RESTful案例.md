### REFSful使用案例

#### 1、准备

> 和传统 CRUD 一样，实现对员工信息的增删改查。
>
> - 搭建环境
>

##### 准备实体类

> ```java
> package com.atguigu.mvc.bean;
> 
> public class Employee {
> 
>    private Integer id;
>    private String lastName;
> 
>    private String email;
>    //1 male, 0 female
>    private Integer gender;
>    
>    public Integer getId() {
>       return id;
>    }
> 
>    public void setId(Integer id) {
>       this.id = id;
>    }
> 
>    public String getLastName() {
>       return lastName;
>    }
> 
>    public void setLastName(String lastName) {
>       this.lastName = lastName;
>    }
> 
>    public String getEmail() {
>       return email;
>    }
> 
>    public void setEmail(String email) {
>       this.email = email;
>    }
> 
>    public Integer getGender() {
>       return gender;
>    }
> 
>    public void setGender(Integer gender) {
>       this.gender = gender;
>    }
> 
>    public Employee(Integer id, String lastName, String email, Integer gender) {
>       super();
>       this.id = id;
>       this.lastName = lastName;
>       this.email = email;
>       this.gender = gender;
>    }
> 
>    public Employee() {
>    }
> }
> ```
>

##### 准备dao模拟数据

> ```java
> package com.atguigu.mvc.dao;
> 
> import java.util.Collection;
> import java.util.HashMap;
> import java.util.Map;
> 
> import com.atguigu.mvc.bean.Employee;
> import org.springframework.stereotype.Repository;
> 
> 
> @Repository
> public class EmployeeDao {
> 
>    private static Map<Integer, Employee> employees = null;
>    
>    static{
>       employees = new HashMap<Integer, Employee>();
> 
>       employees.put(1001, new Employee(1001, "E-AA", "aa@163.com", 1));
>       employees.put(1002, new Employee(1002, "E-BB", "bb@163.com", 1));
>       employees.put(1003, new Employee(1003, "E-CC", "cc@163.com", 0));
>       employees.put(1004, new Employee(1004, "E-DD", "dd@163.com", 0));
>       employees.put(1005, new Employee(1005, "E-EE", "ee@163.com", 1));
>    }
>    
>    private static Integer initId = 1006;
>    
>    public void save(Employee employee){
>       if(employee.getId() == null){
>          employee.setId(initId++);
>       }
>       employees.put(employee.getId(), employee);
>    }
>    
>    public Collection<Employee> getAll(){
>       return employees.values();
>    }
>    
>    public Employee get(Integer id){
>       return employees.get(id);
>    }
>    
>    public void delete(Integer id){
>       employees.remove(id);
>    }
> }
> ```

##### pom.xml配置

> ```xml
> <?xml version="1.0" encoding="UTF-8"?>
> <project xmlns="http://maven.apache.org/POM/4.0.0"
>          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>          xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
>     <modelVersion>4.0.0</modelVersion>
> 
>     <groupId>com.zlp.rest</groupId>
>     <artifactId>springMVC-REST</artifactId>
>     <version>1.0-SNAPSHOT</version>
>     <packaging>war</packaging>
> 
>     <dependencies>
>         <dependency>
>             <groupId>org.springframework</groupId>
>             <artifactId>spring-webmvc</artifactId>
>             <version>5.3.7</version>
>         </dependency>
> 
>         <dependency>
>             <groupId>ch.qos.logback</groupId>
>             <artifactId>logback-classic</artifactId>
>             <version>1.2.5</version>
>         </dependency>
> 
>         <dependency>
>             <groupId>javax.servlet</groupId>
>             <artifactId>javax.servlet-api</artifactId>
>             <version>3.1.0</version>
>             <scope>provided</scope>
>         </dependency>
> 
>         <dependency>
>             <groupId>org.thymeleaf</groupId>
>             <artifactId>thymeleaf-spring5</artifactId>
>             <version>3.0.12.RELEASE</version>
>         </dependency>
>     </dependencies>
> 
> </project>
> ```

##### web.xml配置

> ```xml
> <?xml version="1.0" encoding="UTF-8"?>
> <web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
>          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>          xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
>          version="4.0">
> 
>     <servlet>
>         <servlet-name>zlp</servlet-name>
>         <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
>         <init-param>
>             <param-name>contextConfigLocation</param-name>
>             <param-value>classpath:springMVC.xml</param-value>
>         </init-param>
>         <load-on-startup>1</load-on-startup>
>     </servlet>
>     <servlet-mapping>
>         <servlet-name>zlp</servlet-name>
>         <url-pattern>/</url-pattern>
>     </servlet-mapping>
> 
>     <filter>
>         <filter-name>filter</filter-name>
>         <filter-class>org.springframework.web.filter.CharacterEncodingFilter</filter-class>
>         <init-param>
>             <param-name>encoding</param-name>
>             <param-value>UTF-8</param-value>
>         </init-param>
>         <init-param>
>             <param-name>forRequestEncoding</param-name>
>             <param-value>true</param-value>
>         </init-param>
> 
>     </filter>
>     <filter-mapping>
>         <filter-name>filter</filter-name>
>         <url-pattern>/*</url-pattern>
>     </filter-mapping>
> 
>     <filter>
>         <filter-name>HiddenHttpMethodFilter</filter-name>
>         <filter-class>org.springframework.web.filter.HiddenHttpMethodFilter</filter-class>
>     </filter>
>     <filter-mapping>
>         <filter-name>HiddenHttpMethodFilter</filter-name>
>         <url-pattern>/*</url-pattern>
>     </filter-mapping>
> 
> 
> </web-app>
> ```

##### spring.xml配置

> ```java
> <?xml version="1.0" encoding="UTF-8"?>
> <beans xmlns="http://www.springframework.org/schema/beans"
>        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>        xmlns:context="http://www.springframework.org/schema/context"
>        xmlns:mvc="http://www.springframework.org/schema/mvc"
>        xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd http://www.springframework.org/schema/context https://www.springframework.org/schema/context/spring-context.xsd http://www.springframework.org/schema/mvc https://www.springframework.org/schema/mvc/spring-mvc.xsd">
> 
>     <!--配置thymeleaf解析类-->
>     <bean id="zlp" class="org.thymeleaf.spring5.view.ThymeleafViewResolver">
>         <!--解析类优先级-->
>         <property name="order" value="1"/>
>         <property name="characterEncoding" value="utf-8"/>
>         <property name="templateEngine">
>             <!--内部bean 解析引擎-->
>             <bean class="org.thymeleaf.spring5.SpringTemplateEngine">
>                 <property name="templateResolver">
>                     <!--内部bean 解析资源-->
>                     <bean class="org.thymeleaf.spring5.templateresolver.SpringResourceTemplateResolver">
>                         <!--资源路径前缀-->
>                         <property name="prefix" value="/WEB-INF/templates/" />
>                         <!--资源路径后缀-->
>                         <property name="suffix" value=".html" />
>                         <property name="templateMode" value="HTML5" />
>                         <property name="characterEncoding" value="utf-8" />
>                     </bean>
>                 </property>
>             </bean>
>         </property>
>     </bean>
> 
>     <mvc:view-controller path="/" view-name="index" />
>     <mvc:view-controller path="/toAdd" view-name="add"/>
>     <context:component-scan base-package="com.zlp.rest"/>
> 
>     <!--配置默认servlet，处理静态资源请求-->
>     <mvc:default-servlet-handler/>
>     <!--开启注解驱动,xml中配置的视图控制器会使注解的控制器失效，需要手动开启-->
>     <mvc:annotation-driven/>
> 
> </beans>
> ```

##### 功能要求

> | 功能                | URL 地址    | 请求方式 |
> | ------------------- | ----------- | -------- |
> | 访问首页√           | /           | GET      |
> | 查询全部数据√       | /employee   | GET      |
> | 删除√               | /employee/2 | DELETE   |
> | 跳转到添加数据页面√ | /toAdd      | GET      |
> | 执行保存√           | /employee   | POST     |
> | 跳转到更新数据页面√ | /employee/2 | GET      |
> | 执行更新√           | /employee   | PUT      |

#### 2、具体功能：访问首页

> 控制器
>
> ```xml
> <mvc:view-controller path="/" view-name="index" />
> ```
>
> 视图
>
> ```html
> <!DOCTYPE html>
> <html lang="en" xmlns:th="http://www.thymeleaf.org">
> <head>
>     <meta charset="UTF-8">
>     <title>首页</title>
> </head>
> <body>
> <a th:href="@{/employee}">员工信息表</a>
> </body>
> </html>
> ```

#### 3、具体功能：查询所有员工数据

> 控制器（需要使用request共享域给视图传递数据）
>
> ```java
>     @RequestMapping(value = "/employee", method = RequestMethod.GET)
>     public String employee(Model m){
>         Collection<Employee> coll = dao.getAll();
>         m.addAttribute("employees",coll);
>         return "employee";
>     }
> ```
>
> 视图
>
> ```html
> <table border="1" cellpadding="0" cellspacing="0" style="text-align: center;" id="dataTable">
>     <tr>
>         <th colspan="5">Employee Info</th>
>     </tr>
>     <tr>
>         <th>id</th>
>         <th>lastName</th>
>         <th>email</th>
>         <th>gender</th>
>         <th>options(<a th:href="@{/toAdd}">add</a>)</th>
>     </tr>
>     <tr th:each="employee : ${employees}">
>         <td th:text="${employee.id}"></td>
>         <td th:text="${employee.lastName}"></td>
>         <td th:text="${employee.email}"></td>
>         <td th:text="${employee.gender}"></td>
>         <td>
>             <a class="deleteA" @click="deleteEmployee" th:href="@{'/employee/'+${employee.id}}">delete</a>
>             <a th:href="@{'/employee/'+${employee.id}}">update</a>
>         </td>
>     </tr>
> </table>
> ```

#### 4、具体功能：跳转到添加数据页面

> 控制器
>
> ```xml
> <mvc:view-controller path="/toAdd" view-name="add"/>
> ```
>
> 视图
>
> ```html
> <!DOCTYPE html>
> <html lang="en" xmlns:th="http://www.thymeleaf.org">
> <head>
>     <meta charset="UTF-8">
>     <title>增加员工</title>
> </head>
> <body>
> <form th:action="@{/employee}" method="post">
>     lastName：<input type="text" name="lastName"/><br/>
>     email：<input type="text" name="email" /><br/>
>     gender：<input type="radio" name="gender" value="1" />man：
>     <input type="radio" name="gender" value="0" />woman：<br/>
>     <input type="submit" value="submit" />
> </form>
> </body>
> </html>
> ```

#### 5、具体功能：执行保存

> 控制器（POJO方法获取请求参数）
>
> ```java
>     @RequestMapping(value="/employee", method=RequestMethod.POST)
>     public String employeeSave(Employee employee){
>         dao.save(employee);
>         return "redirect:/employee";
>     }
> ```

#### 6、具体功能：跳转到更新数据页面

> 控制器（从url中获取参数，通过request共享域传递数据）
>
> ```java
> @RequestMapping(value = "/employee/{id}", method = RequestMethod.GET)
> public String employeeUpdate(@PathVariable("id") Integer id, Model m){
>     Employee employee = dao.get(id);
>     m.addAttribute("id",employee.getId());
>     m.addAttribute("lastName",employee.getLastName());
>     m.addAttribute("email", employee.getEmail());
>     m.addAttribute("gender",employee.getGender());
>     return "update";
> }
> ```
>
> 视图
>
> ```html
> <!DOCTYPE html>
> <html lang="en" xmlns:th="http://www.thymeleaf.org">
> <head>
>     <meta charset="UTF-8">
>     <title>更新员工信息</title>
> </head>
> <body>
> <form th:action="@{/employee}" method="post">
>     <input type="hidden" name="_method" value="PUT" />
>     <input type="hidden" name="id" th:value="${id}"/>
>     lastName： <input type="text" name="lastName" th:value="${lastName}" /><br/>
>     email：<input type="text" name="email" th:value="${email}" /><br/>
>     gender：<input type="radio" name="gender" value="1" />man
>     <input type="radio" name="gender" value="0" />woman<br/>
>     <input type="submit" value="submit"/>
> </form>
> </body>
> </html>
> ```

#### 7、具体功能：执行更新

> 控制器（POJO方法获取请求参数）
>
> ```java
> @RequestMapping(value = "/employee" ,method = RequestMethod.PUT)
> public String employeeUpdate(Employee employee){
>     dao.save(employee);
>     return "redirect:/employee";
> }
> ```

#### 8、具体功能：删除

> 控制器（从url中获取参数）
>
> ```java
> @RequestMapping(value = "/employee/{id}" ,method=RequestMethod.DELETE)
> public String employeeDelete(@PathVariable("id") Integer id){
>     dao.delete(id);
>     return "redirect:/employee";
> }
> ```
>
> 视图
>
> ```html
> <form id="delete_form" method="post">
>     <!-- HiddenHttpMethodFilter要求：必须传输_method请求参数，并且值为最终的请求方式 -->
>     <input type="hidden" name="_method" value="delete"/>
> </form>
> ```
>
> vue.js
>
> ```html
> <script th:src="@{/static/js/vue.js}"></script>
> <script type="text/javascript">
>     var vue = new Vue({
>         el:"#dataTable",
>         methods:{
>             //event表示当前事件
>             deleteEmployee:function (event) {
>                 //通过id获取表单标签
>                 var delete_form = document.getElementById("delete_form");
>                 //将触发事件的超链接的href属性为表单的action属性赋值
>                 delete_form.action = event.target.href;
>                 //提交表单
>                 delete_form.submit();
>                 //阻止超链接的默认跳转行为
>                 event.preventDefault();
>             }
>         }
>     });
> </script>
> ```

#### 9、静态资源访问

> 1、静态资源必须被打包
>
> 2、开启默认servlet对静态资源请求进行处理，DispatcherServlet前端控制器没有对静态支援请求进行处理
>
> （默认的servlet在Tomcat的web.xml配置，项目中的web.xml中与Tomcat的web.xml相同的配置会被项目中的web.xml覆盖，`与css特性类似最靠近的生效`）

> 配置springMVC相当于在配置DispatcherServlet控制器的各个属性