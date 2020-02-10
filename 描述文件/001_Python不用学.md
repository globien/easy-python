## Python不用学，用用你就会

Python是一种新型的计算机编程语言，它去掉了传统编程语言中晦涩难懂的语法规则，尽最大可能地接近我们的自然语言，基本上做到了看看就能懂、拿来就能用的水平。所以我们说“Python不用学，用用你就会”。

举个简单的例子。几乎所有计算机编程语言的第一个示范程序都是打印“Hello World!”这句话，那么如果用最经典的C语言编程是长这个样子的：
```
#include <stdio.h>
int main()
{
    printf("Hello World! \n");
    return 0;
}
```
是不是很麻烦、很奇怪、很难懂的样子？而用当下很流行的另外一种编程语言Java来编程则是长这样子的：
```
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
```
似乎更难懂了。显然，它们都不是“说人话”的，没有学过编程的人是很难看懂的，更不用说马上就能用了。

那么用Python编程长什么样呢？Python是最接近“讲人话”的计算机编程语言，它的第一个示范程序只需要一句话：
```
print("Hello World!")
```
就这样一句话，运行结果就是显示“Hello World!"。是不是很自然，非常好理解？它跟自然语言如此相似，所以基本上不需要什么解释就能看明白。

下面是更多的一些Python基本语句的示例，相信你都是一看就懂，没什么问题。
```
print("Hello World!")       
print(2+3)
print("2 + 3 =", 2+3)

x = 3
y = 4
a = x - y
b = x * y
c = x / y
print("a =", a)
print("b =", b)
print("c =", c)

first_name = "Harry"
last_name = "Potter"
print("Hi", first_name, last_name, "!")
```
运行结果如下，相信效果都是你想象的那样自然：
```
Hello World!
5
2 + 3 = 5
a = -1
b = 12
c = 0.75
Hi Harry Potter !
```
>可能唯一要注意的是：上述代码中所有的引号，用单引号双引号都可以，但要保证成对使用，并且千万不要用中文的全角引号。另外#表示注释，是给自己或别人提示的，运行时自动被忽略。

上述例子看懂了，基本也就记住了，也就等于你已经基本上学会了Python这门计算机编程语言。当然，这不等于你已经完全掌握，完全熟练了。Python还有很多高深的内容，我们要做的就是，把Python当工具直接拿来用，解决日常工作、生活、学习中遇到的一些有趣的小问题，比如算算概率啦、解决几个数学运算啦，在使用中自然越来越熟悉，逐步掌握。这个过程跟你接触和掌握Word、Excel、PowerPoint等工具的过程并没有太大差别。本专栏就是专门收集和整理这些趣味问题，并把它们编程Python程序，供大家参考。

还有一点很重要，很多Python教程第一课就是教你如何安装Python，因为安装Python还是有点儿麻烦的。其实，初学者并不需要安装Python运行环境，你把代码直接拷贝到这个网站就可以在线运行和调试了： https://www.programiz.com/python-programming/online-compiler 。（这是作者找到的目前最好用的免费平台；如果不能用了，请查看本栏目主页Readme中推荐的其它平台。）

本文对应的代码文件为：[001_Python基本语句示例.py](../代码文件/001_Python基本语句示例.py)

这里是《好玩不用学的Python》栏目，我们的口号是“Python不用学，用用你就会”。欢迎关注！
