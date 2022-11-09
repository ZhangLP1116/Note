收集为Map

```java
public Map<Long, String> getIdNameMap(List<User> users) {
    return accounts.stream().collect(Collectors.toMap(User::getId, User::getUserName));
}
//第二种：将id和实体Bean做为K,V account -> account是一个返回本身的lambda表达式，后面的使用Function接口中的一个默认方法代替，使整个方法更简洁优雅。
public Map<Long, Account> getIdAccountMap(List<Account> accounts) {
    return accounts.stream().collect(Collectors.toMap(Account::getId, account -> account));
}
public Map<Long, Account> getIdAccountMap(List<Account> accounts) {
    return accounts.stream().collect(Collectors.toMap(Account::getId, Function.identity()));
}
//第三种： key存在重复记录时处理,如果使用第一种方法会出错，所以这里只是简单的使用后者覆盖前者来解决key重复问题
public Map<String, Account> getNameAccountMap(List<Account> accounts) {
    return accounts.stream().collect(Collectors.toMap(Account::getUsername, Function.identity(), (key1, key2) -> key2));
}
//第四种： 使用某个具体的Map类来保存，如保存时使用LinkedHashMap
public Map<String, Account> getNameAccountMap(List<Account> accounts) {
    return accounts.stream().collect(Collectors.toMap(Account::getUsername, Function.identity(), (key1, key2) -> key2, LinkedHashMap::new));
}

```

