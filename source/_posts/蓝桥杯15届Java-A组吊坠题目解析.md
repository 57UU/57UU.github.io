---
title: 蓝桥杯15届Java-A组吊坠题目解析
date: 2024-05-02 12:53:55
tags: [Coding,Algorithm,Java]
---

当时考蓝桥杯(java)的时候，也没怎么学过算法，一看这道题涉及到了图论，直接就放弃了。现在回过头来学了下，写个解析。
<!--more-->

## 题目
> **小蓝想制作一个吊坠，他手上有 n 个长度为 m 的首尾相连的环形字符串{s1, s2, · · · , sn} ，他想用 n − 1 条边将这 n 个字符串连接起来做成吊坠，要求所有的字符串连完后形成一个整体。连接两个字符串 si, sj 的边的边权为这两个字符串的最长公共子串的长度（可以按环形旋转改变起始位置，但不能翻转），小蓝希望连完后的这 n − 1 条边的边权和最大，这样的吊坠他觉得最好看，请计算最大的边权和是多少。**
# 分析
这道题涉及到两个问题
- 这很显然是一个涉及到图论的问题，可以采用与最小生成树类似的算法
- 对于两个节点，它们之间的边权的计算

# 边权计算
采用动态规划来计算
```java
    static int similarity(String a, String b) {
        a=a+a;//由于首尾相连，等效于将本身内容复制一遍再求最长公共子串
        int[][] dp=new int[a.length()+1][b.length()+1];
        for(int i=1;i<=a.length();i++){
            for(int j=1;j<=b.length();j++){
                if(a.charAt(i-1)==b.charAt(j-1)){
                    dp[i][j]=dp[i-1][j-1]+1;
                }else {
                    dp[i][j]=Math.max(dp[i-1][j],dp[i][j-1]);
                }
            }
        }
        return dp[a.length()][b.length()];
    }
```
# 构建边权数据结构
这个比较简单，就不解释了
```java
class Edge{
    int index1,index2,value;//index1 must < index2
    public Edge(int index1,int index2,int value){
        this.index2=index2;
        this.index1=index1;
        this.value=value;
    }
}

```

# 最大生成树
与最小生成树类似，先计算所有的边权
```java
ArrayList<Edge> list=new ArrayList<>();
for(int i=0;i<words_count-1;i++){
    for(int j=i+1;j<words_count;j++){
        list.add(new Edge(i,j,similarity(words[i],words[j])));//保证i<j
    }
}
list.sort((a,b)->-Integer.compare(a.value,b.value));
```
从大到小排序，逐个尝试添加，如果不会形成环，就继续。

使用int数组`root`来保存每个节点的的根节点，为了保证有序性，默认将index比较小的那一个作为根；若`root[index]==index`，则表明该节点就是根节点
```java
int[] root=new int[words_count];
for(int i=0;i<words_count;i++){
    root[i]=i;//初始化root数组，此时还没有添加边
}
int total=0;
for(var i:list){
    if(root[i.index1]!=root[i.index2]){//如果两个节点对应的根节点不同，表明连接这两个节点不会形成环
        root[i.index2]=getRoot(i.index1,root);//将这两个节点连上，默认将index较小的作为根
        total+=i.value;
    }
}
System.out.println(total);//输出
```

# 总代码
```java
import java.util.ArrayList;
import java.util.SortedSet;
import java.util.TreeSet;

public class Main {
    static int words_count;
    public static void main(String[] args){
        String[] words=new String[]{
                "aabb","abba","acca","abcd"
        };
        words_count=words.length;
        ArrayList<Edge> list=new ArrayList<>();
        for(int i=0;i<words_count-1;i++){
            for(int j=i+1;j<words_count;j++){
                list.add(new Edge(i,j,similarity(words[i],words[j])));//保证i<j
            }
        }
        list.sort((a,b)->-Integer.compare(a.value,b.value));

        int[] root=new int[words_count];
        for(int i=0;i<words_count;i++){
            root[i]=i;
        }
        int total=0;
        for(var i:list){
            if(root[i.index1]!=root[i.index2]){
                root[i.index2]=getRoot(i.index1,root);//默认将index较小的作为根
                total+=i.value;
            }
        }
        System.out.println(total);

    }
     static int getRoot(int index,int[] roots){
        return index==roots[index]?index:getRoot(roots[index],roots);
    }

    static int similarity(String a, String b) {
        a=a+a;
        int[][] dp=new int[a.length()+1][b.length()+1];
        for(int i=1;i<=a.length();i++){
            for(int j=1;j<=b.length();j++){
                if(a.charAt(i-1)==b.charAt(j-1)){
                    dp[i][j]=dp[i-1][j-1]+1;
                }else {
                    dp[i][j]=Math.max(dp[i-1][j],dp[i][j-1]);
                }
            }
        }
        return dp[a.length()][b.length()];
    }
}
class Edge implements Comparable<Edge>{
    int index1,index2,value;//index1 must < index2
    public Edge(int index1,int index2,int value){
        this.index2=index2;
        this.index1=index1;
        this.value=value;
    }
}

```



# 参考资料
- [最小生成树 克鲁斯卡尔（Kruskal）算法](https://zhuanlan.zhihu.com/p/337447019)
- [数据结构 并查集 管理分组](https://zhuanlan.zhihu.com/p/337189700)
- [最长公共子串](https://zhuanlan.zhihu.com/p/68409952)