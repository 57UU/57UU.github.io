---
title: 在C语言中使用奇技淫巧判断一个浮点数是不是整数
date: 2024-10-27 16:41:19
tags:
    - CPP
---

起因是同学在群里问了一个相关的问题，恰好我当时在上计组。于是我就想到了使用IEEE754的规范来检测这个数是否为整数

```cpp
int isRealFloat(float  num){
    unsigned int a=*(unsigned int*)&num;//将浮点数的二进制表示以int方式读取
    unsigned int exp=((a<<1)>>24)-127;//读取指数
    unsigned int fraction=a&0x007FFFFF;//取出尾数
    return (0x007FFFFF>>exp)&fraction;//指数有多少位，就覆盖多少位尾数。若尾数有没有剩余，那么这个值就是0，表示假；否则尾数有剩余，就说明这的确是小数，这个值本身就不是0，表示真。
}
```

当然用易读的标准代码表示如下
```cpp
int isRealFloat2(float num){
    return (num-(int)num)!=0;
}
```

在x86指令集,o3优化条件下，利用奇技淫巧的函数`isRealFloat`有9条汇编代码；`isRealFloat2`函数有10条汇编代码。

~~虽然在性能测试中还是标准写法的速度快些~~



