---
title: C++：狗屎语言
date: 2024-05-02 18:43:00
tags: 
    - Coding
    - CPP
---

这段时间在写CPP大作业，才算真正被CPP恶心到
<!--more-->

# 狗屎的include设计
这个是我觉得做的最垃圾的地方，c的include是真的给你include,明明是个编译型语言，必须要我指定包含哪些文件，这还需要是单向的，否则动不动就死递归include了。虽说有头文件卫士这玩意，这还是容易编译出错。

这些include还是传递性的，给代码分析器造成了不小的麻烦，导致代码提示不是慢就是质量差。



# 垃圾的std标准库
连个最基础的string都搞不好，考虑到当年没unicode,这个就不说了，但是为什么连个最基础的`split`、`replace`$^*$都不提供.

随便找一个成熟的第三方库，基本上都是自己实现了一个string

注：
`replace` 指的是像py中的用一个字符串替换一个字串

除此之外，像什么vector也是跟屎一样，没有`contain`、`remove` 函数

# 乱七八糟的包管理
其实我这句话就是错的，这种垃圾语言连包管理器都没有，使用第三方包的方式简直“百花齐放”，什么静态链接动态链接的，写一个大一点的项目还要把别人的代码放进来，把一个项目膨胀几百倍。

# 弱智的编译器
我在下文定义了一个函数，我在上文调用你不知道自己去找吗？

我在两个class之间交叉引用，你tm不知道自己去找找，还要我自己预先定义，处理CPP的交叉引用真令人头大。

# 愚蠢的错误提示
你写错了点啥语法，那些错误提示真的不是人能看懂的

```output
E:/Projects//src/Utils.h:79:35: error: variable 'std::istringstream iss' has initializer but incomplete type
   79 |         std::istringstream iss(str);
      |                                   ^
```
这是我没有include这个文件的报错😅

## 意义不明的缩写
我问下大家`cout`中的`c`是什么意思，`c++`、`console`? 哈哈，是`charactor`😅.

什么time缩写成tm，可以看下面这个表
|word|abbr.|
|:---:|:---:|
|time|tm|
|month day|mday|
|input file stream|ifstream|
|seek get|seekg|

这些糟糕透顶的缩写遍地都是，就不举例了

## 糟糕的语法设计
那些特殊语法使得程序十分丑陋，我们常见的语法如下：

```
Type varible= ...
```
而CPP表示函数指针却是别出心裁
```cpp
int (*functionPointer)() = ...;
```

这就导致了如果你的一个函数要返回一个函数指针的代码相当丑陋
```cpp
int (*f(bool condition))(int, int) {
    return condition?functionPointer1:functionPointer2;
}
int main(){
    int (*func)(int,int)=f(true);
    return 114514;
}
```

模糊的语法也是一堆：
你看现在的c++标准，好多都是为以前的undefined擦屁股的，比如`expilct`关键字

还有什么这些乱七八糟的代码都能编译
```cpp
i=(++i)+(++i)+(++i)+(++i);
```

## [引经据典](https://medium.com/nerd-for-tech/linus-torvalds-c-is-really-a-terrible-language-2248b839bee3)

<h3 align="center">C++ is really a terrible language!</h3>

<h4 align="end">——Linus Torvalds</h4>
