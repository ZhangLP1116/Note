### YAML配置文件

yaml是一种标记语言，与xml相比结构更加简单。与properties相比更加适合表示实体类数据

#### 基本语法

- key: value；kv之间有空格
- 大小写敏感
- 使用缩进表示层级关系

- 缩进的空格数不重要，只要相同层级的元素左对齐即可

- '#'表示注释
- 字符串无需加引号，如果要加，单引号中的特殊字符不会被转义，双引号中的字符会被转义

#### 表示的数据类型

- 字面量：单个的、不可再分的值。date、boolean、string、number、null

  ```yaml
  k: v
  ```

- 对象：键值对的集合。map、hash、set、object 

  ```yaml
  行内写法：  k: {k1:v1,k2:v2,k3:v3}
  #或
  k: 
    k1: v1
    k2: v2
    k3: v3
  ```

- 数组：一组按次序排列的值。array、list、queue

```yaml
行内写法：  k: [v1,v2,v3]
#或者
k:
 - v1
 - v2
 - v3
```

#### 示例

```java
@Data
@ToString
@ConfigurationProperties(prefix = "person")
public class User {
    private String userName;
    private Boolean boss;
    private Date birth;
    private Integer age;
    private String[] interests;
    private List<String> animal;
    private Map<String, Object> score;
    private Map<String, List<Pet>> allPets;
}


@Data
public class Pet {
	private String name;
	private Double weight;
}
```

application.yml

```yaml
# 绑定前缀
person:
  username: zlp
  boss: true
  birth: 1998/11/16
  age: 18
  interests:
    - 篮球
    - 足球
  animal:
    - 啊猫
    - 啊狗
  score:
    # 对象写法
    english:
      first: 30
      second: 40
      third: 50
    # 数组写法行内
    math: [131,140,148]
    # 对象行内写法
    chinese: {first: 128,second: 136}

# 数组嵌套对象，两种写法
  allPets:
    sick:
      - {name: 啊猫, weight: 80}
      - name: 啊狗
        weight: 90
```

测试

```java
    public static void main(String[] args) {
        ConfigurableApplicationContext run = SpringApplication.run(MyApplication.class, args);
        User bean = run.getBean(User.class);
        System.out.println(bean);
    }
```

输出

User(userName=zlp, boss=true, birth=Mon Nov 16 00:00:00 CST 1998, age=18, interests=[篮球, 足球], animal=[啊猫, 啊狗], score={english={first=30, second=40, third=50}, math={0=131, 1=140, 2=148}, chinese={first=128, second=136}}, allPets={sick=[Pet(name=啊猫, weight=80.0), Pet(name=啊狗, weight=90.0)]})



#### 配置yaml属性提示

添加依赖

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-configuration-processor</artifactId>
    <optional>true</optional>
</dependency>
```

设置打包输出时不需要打包这个依赖



```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <excludes>
                        <exclude>
                            <groupId>org.springframework.boot</groupId>
                            <artifactId>spring-boot-configuration-processor</artifactId>
                        </exclude>
                    </excludes>
                </configuration>
            </plugin>
        </plugins>
    </build>
```







