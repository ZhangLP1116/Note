> #### [535. TinyURL 的加密与解密](https://leetcode-cn.com/problems/encode-and-decode-tinyurl/)
>
> 难度中等117收藏分享切换为英文接收动态反馈
>
> TinyURL是一种URL简化服务， 比如：当你输入一个URL `https://leetcode.com/problems/design-tinyurl` 时，它将返回一个简化的URL `http://tinyurl.com/4e9iAk`.
>
> 要求：设计一个 TinyURL 的加密 `encode` 和解密 `decode` 的方法。你的加密和解密算法如何设计和运作是没有限制的，你只需要保证一个URL可以被加密成一个TinyURL，并且这个TinyURL可以用解密方法恢复成原本的URL。
>
> 通过次数13,379
>
> 提交次数15,960

> 异或操作，两遍结果不变
>
> 因为C语言以'\0'，作为字符串结束所以在异或过程中可能遇到key与字符串中某个字符相同导致字符串截断，所以用了长度为2的key。这也有可能导致结果为'\0'但是可能性较小。
>
> ```c
> /** Encodes a URL to a shortened URL. */
> char* encode(char* longUrl) {
>     char *key="zl";
>     for(int i=0;longUrl[i]!='\0';i++){
>     	longUrl[i]^=key[0];
>         longUrl[i]^=key[1];
> 	}
>     return longUrl;
> }
> 
> /** Decodes a shortened URL to its original URL. */
> char* decode(char* shortUrl) {
>     char *key="zlp";
>     for(int i=0;shortUrl[i]!='\0';i++){
>         shortUrl[i]^=key[1];
>         shortUrl[i]^=key[0];
> 	}
>     return shortUrl;
> }
> 
> // Your functions will be called as such:
> // char* s = encode(s);
> // decode(s);
> 
> ```

> 官方解答
>
> ![image-20210407150523705](image\image-20210407150523705.png)
>
> ![image-20210407150534851](image\image-20210407150534851.png)
>
> ![image-20210407150545197](image\image-20210407150545197.png)
>
> ![image-20210407150713381](image\image-20210407150713381.png)
>
> ![image-20210407150747504](image\image-20210407150747504.png)
>
> ![image-20210407150757989](image\image-20210407150757989.png)
>
> ![image-20210407150831251](image\image-20210407150831251.png)
>
> ![image-20210407150838121](image\image-20210407150838121.png)