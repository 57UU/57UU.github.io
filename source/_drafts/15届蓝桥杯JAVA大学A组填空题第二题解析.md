---
title: 15届蓝桥杯国赛JAVA大学A组填空题第二题解析
date: 2024-11-12 21:10:07
tags: 
    - Algorithm
    - Java
---


# 注意
以下数组下标均以0开始。
# 题目
列表$A=[a_0,a_1,a_2...a_{2023}]$ ，其中$a_i$互不相同

列表$B=[b_0,b_1,b_2...b_{2023}]$ ,其中**整数** $b_i$ $\in$ [0,2023]且互不相同。

定义变换$T$ : $A[b_i]=A[i]$，对于A中元素同时完成该操作，等效于以下CPP代码。
```cpp
int[] temp=int[2024];
for(int i=0;i<2024;i++){
    temp[B[i]]=A[i];
}
A=temp;
```

现在有一$B$使得发生2024次 $T$ 变换后A**第一次**完全与初始值相同,也就是说A第一次回到了$[a_0,a_1,a_2...a_{2023}]$。求：这样的B有多少种。
## 注意
时间过了这么久了，记忆不一定准确，题目可能与官方的有出入，（我在网上也没找到这道题2024/11/12）

# 解析
最近学了离散数学，了解到了置换变换，看到了循环置换表示法，对这个问题有了启发。

我们定义若$置换R与最小的n使得R^n=I$，则称这个置换的周期为$n$。

这道题的意思也就是说，我们需要找到一种置换，所有元素都在环上（每个元素的位置都要改变），且必须保证这些环的最小公倍数是2024(在2024次操作后A才第一次与初始值相同)

如何找到所有的置换呢，只需要找到$\{L|\sum L=2024\land lcm(L)=2024\}$，其中$L$是一个关于数字的集合，代表每个环的长度。

如果一个环的长度为$n$，那么这个环有$A_{n-1}^{n-1}$种排列方式。为什么不是$n$呢，因为环可以旋转，比如$ABCD=BCDA$

# 未完待续。。。


