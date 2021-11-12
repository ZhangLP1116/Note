> ![image-20210808135527110](image\image-20210808135527110.png)

### 线程创建

> #### 继承Thread
>
> ```java
>//继承Tread，重写run方法，使用start方法创建一个线程。run是进程的主要功能函数
> 
> public class t extends Thread{
> int x;
> public t(int x){
>    this.x=x;
>  }
>    public void run(){
>    while(true){
>        System.out.println(x);
>      }
>    }
>    public static void main(String[] args){
>    t t1 = new t(1);
>    t1.start();
>      System.out.println(t1.getId());
>    }
>    }
>  ```
> 
> #### 实现Runable接口
>
> ```java
>// 如果一个类已经继承另一个类，则可以继承Runable接口创建线程
> // Thread类实际上是一个实现了Runable接口的类
> public class t implements Runnable{
> int x;
> public t(int x){
>    this.x=x;
>  }
>    public void run(){
>    while(true){
>        System.out.println(x);
>      }
>    }
>    public static void main(String[] args){
>    t t1 = new t(1);
>    Thread r = new Thread(t1); // 传入一个Runnable target参数
>      r.start(); // start实际调用target.run，也就是t1.run
>    }
>    }
>  }
> ```
> 
> #### 实现Callable接口
>
> ```java
>import java.util.concurrent.Callable;	// 重写call方法
> import java.util.concurrent.ExecutionException;
> import java.util.concurrent.FutureTask;	
> // Call接口无法直接作为Thread类参数需要借助Fture接口
> 
> public class t implements Callable<Integer>
> {
> 
> public static void main(String[] args)
> {
>    t ctt = new t();
>    FutureTask<Integer> ft = new FutureTask<>(ctt);
>      for(int i = 0;i < 100;i++)
>      {
>          System.out.println(Thread.currentThread().getName()+" 的循环变量i的值"+i);
>          if(i==20)
>          {
>              new Thread(ft,"有返回值的线程").start();
>          }
>      }
>      try
>      {
>          System.out.println("子线程的返回值："+ft.get());
>      } catch (InterruptedException e)
>      {
>          e.printStackTrace();
>      } catch (ExecutionException e)
>      {
>          e.printStackTrace();
>      }
>    
>    }
> 
>  @Override
> public Integer call() throws Exception
>  {
>    int i = 0;
>    for(;i<100;i++)
>      {
>          System.out.println(Thread.currentThread().getName()+" "+i);
>      }
>      return i;
>    }
>    
>  }
> ```
> 
> 需要获取返回值的情况应该使用Callable接口
>
> ![image-20210808155212685](image\image-20210808155212685.png)

### Thread、Runable、Futrue、FutrueTask、Callable关系

> ![image-20210808154307728](image\image-20210808154307728.png)
>
> #### Thread类
>
> ​		是实现Runable接口的实现类。
>
> #### Futrue接口
>
> ​		用于获取线程的返回值
>
> ![image-20210808160920698](image\image-20210808160920698.png)
>
> #### FutrueTask类
>
> ![image-20210808161314277](image\image-20210808161314277.png)
>
> ![image-20210808161249813](image\image-20210808161249813.png)
>
> ​	FutrueTask构造方法，可以接收Callable或Runnable
>
> ![image-20210808161504971](image\image-20210808161504971.png)
>
> #### FutrueTask与Futrue
>
> ​	FutrueTask类是Futrue接口的实现类，可以实例化对象作为Thread类的Runnable target参数创建线程
>
> ​	Futrue无法实例化对象，它作为线程的返回值类型，被用于获取线程结果

### 总结

> 从底层创建线程的方式有两种，有一种是Thread类start方法，一种是线程池submit方法
>
> Runnable接口、callable接口都是用于编写线程主体的功能的方式
>
> Futrue接口：用于获取线程运行结果
>
> FutrueTask类：可以作为Thread类或线程池的线程创建参数，同时能获取线程运行结果
>
> ```java
>// Callable与Futrue
> 
> // 创建线程池
> ExecutorService es = Executors.newSingleThreadExecutor();  
> //创建线程主体任务
> CallableDemo calTask=new CallableDemo();  
> //创建获取线程结果的变量，提交任务创建线程执行，结果是Futrue类型
> Future<Integer> future =es.submit(calTask);  
> //关闭线程池  
> es.shutdown();  
> ```
> 
> ```java
>// Callable与Futrue
> 
> //创建线程池  
> ExecutorService es = Executors.newSingleThreadExecutor();  
> //创建线程任务主体
> CallableDemo calTask=new CallableDemo();  
> //创建FutureTask，将线程主体封装到Futrue
> FutureTask<Integer> futureTask=new FutureTask<>(calTask);  
> //提交FutrueTask变量，创建线程执行
> es.submit(futureTask);  
> //关闭线程池  
> es.shutdown();  
> ```

### Thread主要方法

> ![image-20210808165503600](image\image-20210808165503600.png)
>
> ![image-20210808165516698](image\image-20210808165516698.png)

