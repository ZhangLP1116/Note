### 常见的HTTP认证机制

#### 1、HTTP Basic Auth

最早期的认证方式，每次请求都要携带username、password。

缺点：有暴露分析



#### 2、Cookie Auth

使用Cookie和Session配合认证，每次请求只需要携带sessionID。

缺点：容易收到CSRF攻击，无法跨域



#### 3、Oauth2

开发授权协议，已经被广泛应用

缺点：过重，搭建麻烦



#### 4、Token Auth

工作机制和Cookie很相似，用户提交账号密码，后端生成token返回，每次请求携带token

后端根据token识别用户

优点：

1. 支持跨域：token可以设置在请求头中
2. 无状态：token本身包含了所有用户信息，不需要使用session
3. 更适合CDN
4. 去耦：
5. 更适合移动端：移动端一般不支持cookie
6. 没有csrf威胁：不依赖于cookie
7. 性能：一次加解密计算耗时小于一次数据库查询
8. 基于标准化：API可以使用标准化的JSON WEB TOKEN（JWT），已经被多种语言支持



### JWT

Json web token (JWT), 是为了在网络应用环境间传递声明而执行的一种基于JSON的开放标准（[(RFC 7519](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc7519)).该token被设计为紧凑且安全的，特别适用于分布式站点的单点登录（SSO）场景。JWT的声明一般被用来在身份提供者和服务提供者间传递被认证的用户身份信息，以便于从资源服务器获取资源，也可以增加一些额外的其它业务逻辑所必须的声明信息，该token也可直接被用于认证，也可被加密。



### 组成

JWT字符串由三部分组成，头部、载荷、签名



#### 头部

头部用于描述JWT的基本信息，例如类型、签名所用的算法，可以表示为一个json对象

```json
{
    "alg": "HS256",
    "typ": "JWT"
}
```

alg：表示使用的算法

typ：表示类型

头部使用Base64编码



#### 载荷

用来存放有效信息，这类信息分为三种，使用base64编码

- 标准中注册的声明：建议但不强制使用

  ```
  iss: jwt签发者
  sub：jwt锁面向的用户
  aud：接受jwt的一方
  exp：jwt的过期时间
  nbf：定义在声明时间之前jwt是不可用的
  iat：jwt签发时间
  jti：jwt的唯一身份标识
  ```

- 公共声明
  公共的声明可以添加任何的信息，一般添加用户的相关信息或其他业务需要的必要信息.但不建议添加敏感信息，因为该部分在客户端可解密.

- 私有声明
  私有声明是提供者和消费者所共同定义的声明，一般不建议存放敏感信息，因为base64是对称解密的，意味着该部分信息可以归类为明文信息。



示例

```json
{
  "sub": "1234567890",
  "name": "John Doe",
  "admin": true
}
```

sub：是标准声明，接收端可以根据标准去解读该字段

name：是是私有声明，需要告诉接收方如何解读该字段





#### 签名

签名由3部分组成：

- header：base64编码后的字符
- payload：base64编码后的字符
- secret：加密盐

该部分使用header的base64编码+payload的base64编码使用头部声明的算法配合加密盐进行加密得到。



完整的JWT=header：base64+payload：base64+签名



### JJWT库

定义JWT工具类：编写创建token，和解析token方法

```java
public class JWTUtils {
    private static final String secret = "zlp161232";

    // 创建token
    public static String createToken(Map<String,Object> map){

        // Jwts.builder用来构造JWT
        JwtBuilder jwtBuilder = Jwts.builder()
            // 设置加密算法、加密盐
                .signWith(SignatureAlgorithm.HS256,secret)
            // 标准声明字段值设置
                .setIssuer("zlp")
                .setIssuedAt(new Date())
                .setExpiration(new Date(System.currentTimeMillis()+ 60 * 1000))
            // 私有声明字段值设置，以添加形式，用set方式会覆盖上述设置
                .addClaims(map);
        
        // 使用加密算法和Base64编码，生成token
        String token = jwtBuilder.compact();
        return token;
    }

    public static void parseToken(String token){
        // Jwts.parser()返回一个默认的JWT解析对象
        // 设置解析用的加密盐，和token进行解析
        Claims body = (Claims) Jwts
                .parser()
                .setSigningKey(secret)
                .parse(token)
            // 获取载荷部分，可以强制转换成map类型
            // Claims类型继承了map，内置了一些获取公共声明字段的方法
            // 获取私有声明时室友map.get(key)，的形式获取
                .getBody();
        System.out.println(body.getIssuer());
        System.out.println(body.getIssuedAt());
        System.out.println(body.get("id"));
    }
}
```

#### 测试

1、生成token

```java
@SpringBootTest
class Demo3ApplicationTests {

    @Test
    void testJJWT() {
        Map<String, Object> map = new HashMap<>();
        map.put("id", 1116);
        String token = JWTUtils.createToken(map);
        System.out.println("token：" + token);
    }

}
```

```
token：eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ6bHAiLCJpYXQiOjE2MzU2NTQ5NzgsImV4cCI6MTYzNTY1NTAzOCwiaWQiOjExMTZ9.-gWuhAsTlnM8Hhb584A8zbz3IrtDHYdKWlSnbghYIMc

```

可以明显的看出token由3段组成



2、使用Base64获取header、payload部分

```java
@SpringBootTest
class Demo3ApplicationTests {

    @Test
    void testJJWT() {
        Map<String, Object> map = new HashMap<>();
        map.put("id", 1116);
        String token = JWTUtils.createToken(map);
        String[] split = token.split("\\.");
        System.out.println(TextCodec.BASE64.decodeToString(split[0]));
        System.out.println(TextCodec.BASE64.decodeToString(split[1]));
        System.out.println(TextCodec.BASE64.decodeToString(split[2]));
    }
}
```

```
{"alg":"HS256"}
{"iss":"zlp","iat":1635655620,"exp":1635655680,"id":1116}
��Lwu�4�qv���e*UA��sV�=���
```

前两端使用Base64编码可以直接解码获取明文，签名部分不行



3、解析token

```java
@SpringBootTest
class Demo3ApplicationTests {

    @Test
    void testJJWT() {
        Map<String, Object> map = new HashMap<>();
        map.put("id", 1116);
        String token = JWTUtils.createToken(map);
        JWTUtils.parseToken(token);
    }

}
```

```
zlp
Sun Oct 31 12:48:48 CST 2021
1116

成功解密，并获取payload部分信息
若解密失败则会抛出异常
若token过期也会抛出异常
```

> 加密盐不能过短，最少4个字符



### Oauth2使用JWT令牌

#### 整合JWT

配置认证服务器

```java
    @Override
    public void configure(AuthorizationServerEndpointsConfigurer endpoints) throws Exception {
        endpoints.authenticationManager(authenticationManager)
                .userDetailsService(userDetailsService);

        // 存储方式为JWT
        // 需要添加accessToken转换为JWT令牌的转换器
        endpoints.tokenStore(tokenStore)
                .accessTokenConverter(jwtAccessTokenConverter);
    }
```

配置TokenStore

```java
@Configuration
public class JwtTokenStoreConfig {
    // 注入jwtTokenStore
    @Bean
    public TokenStore jwtTokenStore(){
        return new JwtTokenStore(jwtAccessTokenConverter());
    }

    // 注入转换器，设置密钥
    @Bean
    public JwtAccessTokenConverter jwtAccessTokenConverter(){
        JwtAccessTokenConverter jwtAccessTokenConverter = new JwtAccessTokenConverter();
        jwtAccessTokenConverter.setSigningKey("test");
        return jwtAccessTokenConverter;
    }
}
```

测试

不使用JWT令牌

![image-20211031143925485](image/image-20211031143925485.png)

使用JWT令牌

![image-20211031143841636](image/image-20211031143841636.png)



#### 解析令牌

```java
@RestController
@RequestMapping("/user")
public class UserController {
    @GetMapping("/getUser")
    public Object getUser(Authentication authentication, HttpServletRequest request){
        String authorization = request.getHeader("Authorization");
        // 匹配前端格式，Authorization字段后会携带Bearer + 空格共7个字符
        // 去掉这七个字符就是完整的token
        String token = authorization.substring(authorization.lastIndexOf("Bearer") + 7);
        return Jwts.parser()
            // 一定要将密钥转换为字节流，不然会出现密钥不匹配的情况
                .setSigningKey("test".getBytes(StandardCharsets.UTF_8))
                .parse(token)
                .getBody();
    }

}
```

测试

从令牌中就可以获取到用户信息

![image-20211031150457272](image/image-20211031150457272.png)



#### 拓展令牌内容

原生JWT令牌可以直接使用addClaims方式添加信息，Oauth中整合的jwt添加信息的方式有所不同

继承`TokenEnhancer接口`，重写enhance，准备添加内容

```java
@Configuration
public class JwtTokenEnhancer implements TokenEnhancer {
    @Override
    public OAuth2AccessToken enhance(OAuth2AccessToken oAuth2AccessToken, OAuth2Authentication oAuth2Authentication) {
        // 自定义内容存放在Map中
        Map<String,Object> map = new HashMap<>();
        map.put("age",18);
        
        // 调用OAuth2AccessToken父接口的setAdditionalInformation方法设置添加内容
        ((DefaultOAuth2AccessToken) oAuth2AccessToken).setAdditionalInformation(map);
        
        // 返回OAuth2AccessToken对象
        return oAuth2AccessToken;
    }
}
```

配置认证服务器

```java
    @Override
    public void configure(AuthorizationServerEndpointsConfigurer endpoints) throws Exception {
        endpoints.authenticationManager(authenticationManager)
                .userDetailsService(userDetailsService);

        // 准备TokenEnhancerChain对象
        TokenEnhancerChain chain = new TokenEnhancerChain();
        // 准备List<TokenEnhancer>对象
        // 设置拓展内容，token转换器
        List<TokenEnhancer> enhancerList = new ArrayList<>();
        enhancerList.add(jwtTokenEnhancer);
        enhancerList.add(jwtAccessTokenConverter);
        
        // 设置属性，参数类型为List<TokenEnhancer>
        chain.setTokenEnhancers(enhancerList);

        
        endpoints.tokenStore(tokenStore)
            // 设置TokenEnhancerChain对象，进行内容添加
            // TokenEnhancerChain对象中已经设置了token转换器不需要再手动调用
            // .accessTokenConverter(jwtAccessTokenConverter)
                .tokenEnhancer(chain);
    }
```

测试

![image-20211031152923442](image/image-20211031152923442.png)