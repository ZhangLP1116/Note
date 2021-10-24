### 介绍

Jedis是java 操作redis库，实现了redis中所有API，并附加其他便利的API操作



### 常用操作

#### 1、连接redis

```java
public class demo1 {
    public static void main(String[] args) {
        Jedis jedis = new Jedis("localhost",6379);
        String ping = jedis.ping();
        // 连接成功返回PONE
        System.out.println(ping);
    }
}
```

#### 2、操作key

```java
    @Test
    public void demo1(){
        Jedis jedis = new Jedis("localhost",6379);
        jedis.set("name","zlp");
        jedis.get("name");
        // 查看所有key
        jedis.keys("*");
        // 查看是否存在某个key
        jedis.exists("name");
        // 查看key的类型
        jedis.type("name");
        // 设置key过期时间，单位秒
        jedis.expire("name",10L);
        // 查看key剩余过期时间
        jedis.ttl("name");
        // 删除key
        jedis.del("name");
        // 选中其他数据库
        jedis.select(1);
        // 清空当前数据库
        jedis.flushDB();
        // 清空所有数据库
        jedis.flushAll();
    }
}
```

#### 3、String操作

```java
    @Test
    public void demo2(){
        Jedis jedis = new Jedis("localhost",6379);
        // 设置k-v，可以带原生API参数PX、NX
        jedis.set("name","zlp");
        // 获取value
        jedis.get("name");
        // 在value后追加
        jedis.append("name","123");
        // 返回value的长度
        jedis.strlen("name");
        // 设置k-v，若存在则插入失败
        jedis.setnx("name", "zlp123");
        // 自增value
        jedis.incr("name");
        // 自减value
        jedis.decr("name");
        // 自增一定步长
        jedis.incrBy("name", 10);
        // 批量设置k-v
        jedis.mset("name","zlp","age","18");
        // 批量设置k-v，互斥
        jedis.msetnx("name","zlp","age","18");
        // 批量获取
        jedis.mget("name","age");
        // 获取value子串，包含开始和结束位置
        jedis.getrange("name",0,-1);
        // 在指定位置之前插入串
        jedis.setrange("name",1,"xx");
        // 先获取，在覆盖
        jedis.getSet("name","zlp123");
    }
}
```

#### 4、列表操作

参考原生API

#### 5、集合操作

参考原生API

#### 6、hash操作

参考原生API

#### 7、有序集合操作

参考原生API



### 模拟验证码

要求：
1、输入手机号，点击发送后随机生成6位数字码，2分钟有效
2、输入验证码，点击验证，返回成功或失败
3、每个手机号每天只能输入3次

```java
import org.junit.Test;
import redis.clients.jedis.Jedis;

import java.util.Random;


public class demo1 {
    public static void main(String[] args) {
        // verifyCode("138666");
        String res = verify("138666", "427158");
        System.out.println(res);
    }

    // 对比用户输入和redis中保存的验证码
    public static String verify(String phone, String code){
        Jedis jedis = new Jedis("localhost",6379);
        String codeKey = "VerifyCode" + phone + ":code";
        if (jedis.get(codeKey).equals(code)){
            return "成功";
        }
        return "失败";
    }

    // 创建6位验证码，设置2分钟过期时间
    // 如次数超过每日上限，则不创建
    // 以手机号作为参数拼接生成ridis的key
    public static void verifyCode(String phone){
        Jedis jedis = new Jedis("localhost",6379);
        String countKey = "VerifyCode" + phone + ":count";
        String codeKey = "VerifyCode" + phone + ":code";
        String count = jedis.get(countKey);
        if (count == null){
            jedis.setex(countKey,24*60*60,"1");

        }
        else if(Integer.parseInt(count) >=3 ){
            jedis.close();
            System.out.println("今日已经获取过3次");
            return;
        }
        else {
            jedis.incr(countKey);
        }
        jedis.setex(codeKey,2*60,getCode());
        jedis.close();
    }

    // 生成6位随机数
    public static String getCode(){
        Random random = new Random();
        String code = "";
        for(int i=0;i<6;i++){
            int i1 = random.nextInt(10);
            code += i1;
        }
        return code;
    }
}

```

