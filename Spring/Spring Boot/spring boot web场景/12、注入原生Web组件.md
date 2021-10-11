### 注入原生Web组件

相关官方文档地址：https://docs.spring.io/spring-boot/docs/current/reference/html/features.html#features.developing-web-applications.embedded-container

原生Web组件有：Servlet、Filter、Listener



#### 1、扫描组件方式

@ServletComponentScan(basePackages = "package") :扫描原生web组件所在包

@WebServlet：标识为servlet

@WebFilter：标识为filter

@WebListener：标识为listener

servlet示例

`注意注入的servlet不会被拦截器拦截`

```java
@WebServlet(urlPatterns = "/myServlet")
public class MyServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        resp.getWriter().write("/myServlet");
    }
}
```

filter示例

```java
@Slf4j
@WebFilter(urlPatterns = "/myServlet")
public class MyFilter implements Filter {
    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        log.info("MyFilter init");
    }

    @Override
    public void destroy() {
        log.info("MyFilter destroy");
    }

    @Override
    public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {
        log.info("MyFilter doFilter");
        filterChain.doFilter(servletRequest,servletResponse);
    }
}
```

listener示例

```java
@Slf4j
@WebListener
public class MyListener implements ServletContextListener {
    @Override
    public void contextInitialized(ServletContextEvent sce) {
        log.info("MyListener init");
    }

    @Override
    public void contextDestroyed(ServletContextEvent sce) {
        log.info("MyListener destroy");
    }
}
```

启动类

```java
// 扫描要注入的原生组件所在包
@ServletComponentScan(basePackages = "com.zlp.boot.servlet")
@SpringBootApplication
public class SpringBootDemo2Application {

    public static void main(String[] args) {
        SpringApplication.run(SpringBootDemo2Application.class, args);
    }

}
```



#### 2、作为Spring Bean方式

在配置类中以Bean的形式注入原生web组件

ServletRegistrationBean：原生Servlet类型存在spring中的类型

FilterRegistrationBean：原生Filter类型存在spring中的类型

ServletListenerRegistrationBean：原生Listener类型存在spring中的类型

示例

```java
@Configuration
public class MyRegistConfig {

    // 注册Servlet
    @Bean
    public ServletRegistrationBean myServlet(){
        MyServlet myServlet = new MyServlet();

        return new ServletRegistrationBean(myServlet,"/myServlet");
    }


    // 注册Filter
    @Bean
    public FilterRegistrationBean myFilter(){

        MyFilter myFilter = new MyFilter();
//        return new FilterRegistrationBean(myFilter,myServlet());
        FilterRegistrationBean filterRegistrationBean = new FilterRegistrationBean(myFilter);
        filterRegistrationBean.setUrlPatterns(Arrays.asList("/myServlet"));
        return filterRegistrationBean;
    }

    // 注册listener
    @Bean
    public ServletListenerRegistrationBean myListener(){
        MySwervletContextListener myListener = new MyListener();
        return new ServletListenerRegistrationBean(myListener);
    }
}
```



### DispatcherServlet注册过程

注册过程发生在`DispatcherServletAutoConfiguration`类下

1. 创建DispatcherServlet，此时只是设置好DispatcherServlet对象的属性，spring boot还没有将它当作一个Servlet使用

   ```java
   // 在DispatcherServletConfiguration配置类中
   
   public static final String DEFAULT_DISPATCHER_SERVLET_REGISTRATION_BEAN_NAME = "dispatcherServletRegistration";
   
   	@Configuration(proxyBeanMethods = false)
   	@Conditional(DefaultDispatcherServletCondition.class)
   	@ConditionalOnClass(ServletRegistration.class)
   	@EnableConfigurationProperties(WebMvcProperties.class)
   	protected static class DispatcherServletConfiguration{
   
   
   		@Bean(name = DEFAULT_DISPATCHER_SERVLET_BEAN_NAME)
   		public DispatcherServlet dispatcherServlet(WebMvcProperties webMvcProperties) {
   			DispatcherServlet dispatcherServlet = new DispatcherServlet();
   			dispatcherServlet.setDispatchOptionsRequest(webMvcProperties.isDispatchOptionsRequest());
   			dispatcherServlet.setDispatchTraceRequest(webMvcProperties.isDispatchTraceRequest());
   			dispatcherServlet.setThrowExceptionIfNoHandlerFound(webMvcProperties.isThrowExceptionIfNoHandlerFound());
   			dispatcherServlet.setPublishEvents(webMvcProperties.isPublishRequestHandledEvents());
   			dispatcherServlet.setEnableLoggingRequestDetails(webMvcProperties.isLogRequestDetails());
   			return dispatcherServlet;
   		}
   ```

2. 注册DispatcherServlet

   ```java
   // 在DispatcherServletRegistrationConfiguration配置类中
   
   	@Configuration(proxyBeanMethods = false)
   	@Conditional(DispatcherServletRegistrationCondition.class)
   	@ConditionalOnClass(ServletRegistration.class)
   	@EnableConfigurationProperties(WebMvcProperties.class)
   	@Import(DispatcherServletConfiguration.class)
   	protected static class DispatcherServletRegistrationConfiguration {
   
   		@Bean(name = DEFAULT_DISPATCHER_SERVLET_REGISTRATION_BEAN_NAME)
   		@ConditionalOnBean(value = DispatcherServlet.class, name = DEFAULT_DISPATCHER_SERVLET_BEAN_NAME)
   		public DispatcherServletRegistrationBean dispatcherServletRegistration(DispatcherServlet dispatcherServlet,
   				WebMvcProperties webMvcProperties, ObjectProvider<MultipartConfigElement> multipartConfig) {
               
               // 将dispatcherServlet注册为Servlet
               // 设置dispatcherServlet作用路径，从配置文件中获得
   			DispatcherServletRegistrationBean registration = new DispatcherServletRegistrationBean(dispatcherServlet,
   					webMvcProperties.getServlet().getPath());
   			
              // 设置Servlet名
              registration.setName(DEFAULT_DISPATCHER_SERVLET_BEAN_NAME);
   			registration.setLoadOnStartup(webMvcProperties.getServlet().getLoadOnStartup());
   			multipartConfig.ifAvailable(registration::setMultipartConfig);
   			return registration;
   		}
   
   	}
```
   
   DispatcherServletRegistrationBean，实际上是一个ServletRegistrationBean
   
   ```java
   public class DispatcherServletRegistrationBean extends ServletRegistrationBean<DispatcherServlet>
   ```
   
   