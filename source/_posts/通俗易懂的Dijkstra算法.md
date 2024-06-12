---
title: 通俗易懂的Dijkstra算法
date: 2024-05-14 20:28:53
tags: 
- Coding
- Rust
---

看了下网上的一些讲的这个算法，有的说的太复杂了
<!--more-->
我们假设有A、B、C、D、E四个节点，我们想找到从A到E的最短路径（边权和最小）

我们定义$D_A(x)$表示**当前**计算出来的从A到X的最短距离

定义$C(X,Y)$表示从X**直接**到Y的距离

```
A——8——B
| ╲     ╲ 
2  18    15
|    ╲     ╲
C——9——D——11——E
```
## 文字描述
记全部节点所在的集合为U
先构建一个映射$f: x \rightarrow D_A(x),x\in\{B、C、D、E\}$，再构建一个集合$C:\{\}$来存放已经寻找过了的节点。
### 初始化
初始从A开始直接寻找，然后将结果直接存放在$f$中，$C:\{A\}$

### 循环迭代
寻找$f$值域中值最小的项对应的节点，且该节点没有被搜索过。记该节点为$N$

从该节点作为桥梁进行搜索
对于$\{x|x\in U,x\notin C\}$
更新值
$D_A(X)=min\{D_A(X),D_A(N)+C(N,X)\}$
然后将N放入C中

## 图表描述
我们可以构建如下表,B、C、D列表示当前计算出的最短距离，即$D_A(X)$
，然后一步一步迭代计算
|已经搜索了的节点|B|C|D|E|说明|
|:---:|:---:|:---:|:---:|:---:|:---|
|A|8|2|18|$\infty$|从A开始直接寻找，发现C距离最短，下一步从C开始搜索
|AC|8|-|**11**|$\infty$|发现$D_A(C)+C(C,D)$比$D_A(D)$更小，遂更新$D_A(D)$的值；此时未搜索的节点中B的距离最短
|ACB|-|-|11|**23**|发现$D_A(B)+C(B,E)$比$D_A(E)$更小，遂更新
|ACBD|-|-|-|**22**|发现$D_A(D)+C(D,E)$比$D_A(E)$更小，遂更新

注意，每次迭代时找出的`未被搜索的`、`最短的`路径就是$D_A(X)$的最短路径，所以不需要再次更新数值，上图中使用减号`-`表示。

## Rust实现

```rust
use std;

static INF: usize =0xFFF;

fn main() {
    let mut graph:Vec<[usize; 5]>=vec![
        [0,8,2,18, INF],
        [0,0, INF, INF,15],
        [0,0,0,9, INF],
        [0,0,0,0,11],
        [0,0,0,0,0]
    ];
    
    //上三角阵，转化为对称矩阵
    for i in 0..5{
        for j in 0..i{
            graph[i][j]=graph[j][i];
        }
    }
    let mut dij =Dijkstra::new(graph);
    let min_path=dij.find(0,4);
    print!("min path:{}",min_path)

}
struct Dijkstra{
    graph:Vec<[usize; 5]>,
    not_find:Vec<usize>,
    distance:Vec<usize>,
}

impl Dijkstra {
    fn new(graph: Vec<[usize; 5]>)->Dijkstra{
        return  Dijkstra{
            graph,
            not_find: vec![0,1,2,3,4,],
            distance: vec![INF,INF,INF,INF,INF,],
        };
    }
    fn d(&self, dst:usize) ->usize{
        self.distance[dst]
    }
    fn c(&self, src:usize, dst:usize) ->usize{
        self.graph[src][dst]
    }
    fn init(&mut self, src:usize){
        for i in 0..5{
            self.distance[i]=self.c(src, i as usize);
        }
    }
    fn find(&mut self, src:usize, dst:usize)->usize{
        self.init(src);//initialize
        for _i in 0..5{
            let mut min:usize=self.not_find[0];
            let mut index_at_not_find =0;
            let mut index=0;
            for node in &self.not_find{
                if self.distance[*node]<self.distance[min]{
                    min= *node;
                    index_at_not_find=index;
                }
                index += 1;
            }
            self.not_find.remove(index_at_not_find);

            for node in &self.not_find{
                if self.d(min)+self.c(min, *node)<self.d(*node) {
                    self.distance[*node]=self.d(min)+self.c(min, *node);
                }
            }
        }
        return self.distance[dst];

    }
}
```


