## Python不用学，用用你就会

Python是最接近“说人话”的计算机编程语言。基本上看看就能懂，拿来就能用。所以我们说“Python不用学，用用你就会”。

举个栗子。所有计算机编程语言的第一课都是一个打印“Hello World!”的程序，那么用C语言编程长这样：
```
#include <stdio.h>
int main()
{
    printf("Hello World! \n");
    return 0;
}
```
用Java编程长这样：
```
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
```
显然，它们都不是“说人话”，没有学过编程的人是很难看懂的，更不用说马上就能用。

那么Python呢？长什么样？Python只有一句话：
```
  print("Hello World!")
```
是不是只有一句话而且非常好理解？

下面是Python最基本的一些语句的示例，相信你都是一看就懂，没什么问题。
```
print("Hello World!")       
print(3+4)
print("5 除以 3 等于", 5/3)
print()                        #打印一个空行

x = 4
y = 3
print("x * y =", x*y)
a = x**y
print(x, "的", y, "次方等于", a)
print()

name = "小强"
print("你好,",name,"!")
```
运行结果如下，相信效果都是你想象的那样自然：
```
Hello World!
7
5 除以 3 等于 1.6666666666666667

x * y = 12
4 的 3 次方等于 64

你好, 小强 !
```
可能唯一要注意的是：上述代码中所有的引号，用单引号双引号都可以，但要保证成对使用，并且千万不要用中文的全角引号。另外#表示注释，是给自己或别人提示的，运行时自动被忽略。

这里是

