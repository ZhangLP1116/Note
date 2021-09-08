> #### [412. Fizz Buzz](https://leetcode-cn.com/problems/fizz-buzz/)
>
> 难度简单96收藏分享切换为英文接收动态反馈
>
> 写一个程序，输出从 1 到 *n* 数字的字符串表示。
>
> \1. 如果 *n* 是3的倍数，输出“Fizz”；
>
> \2. 如果 *n* 是5的倍数，输出“Buzz”；
>
> 3.如果 *n* 同时是3和5的倍数，输出 “FizzBuzz”。
>
> **示例：**
>
> ```
> n = 15,
> 
> 返回:
> [
>     "1",
>     "2",
>     "Fizz",
>     "4",
>     "Buzz",
>     "Fizz",
>     "7",
>     "8",
>     "Fizz",
>     "Buzz",
>     "11",
>     "Fizz",
>     "13",
>     "14",
>     "FizzBuzz"
> ]
> ```
>
> 通过次数62,280
>
> 提交次数94,047

> 解法：时间复杂度O(n)，空间复杂度O(1)
>
> printf函数：将格式化字符串输出到屏幕
>
> sprintf函数：将格式化字符串输出到一个目标字符串中，可以用来构建一个字符串
>
> sprintf函数的原形：int sprintf( char *buffer, const char *format [, argument,...] );
>
> 用法与printf类似，第一个参数为目标字符串，第二个参数为格式化字符串，后续为可变个数的参数
>
> ```c
> /**
>  * Note: The returned array must be malloced, assume caller calls free().
>  */
> char ** fizzBuzz(int n, int* returnSize){
>     char **res=(char**)malloc(sizeof(char*)*n);
>     *returnSize=n;
>     char *F="Fizz";
>     char *B="Buzz";
>     char *FB="FizzBuzz";
>     for(int i=1;i<n+1;i++){
>         if(i%3==0 && i%5==0) res[i-1]=FB;
>         else{
>             if(i%3==0) res[i-1]=F;
>             else if(i%5==0) res[i-1]=B;
>             else{
>                 res[i-1]=(char*)malloc(sizeof(char)*10);
>                 sprintf(res[i-1],"%d",i);
>             }
>         }
>     }
>     return res;
> }
> ```
>
> 