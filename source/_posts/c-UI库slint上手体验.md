---
title: c++UI库slint上手体验
date: 2024-03-25 21:49:39
tags: CPP
---

首先这个玩意需要安装`Rust`开发环境
<https://www.rust-lang.org/learn/get-started>
<!--more-->
然后需要`Rust`的某个工具链
```cmd
rustup target add --toolchain stable-x86_64-pc-windows-msvc x86_64-pc-windows-gnu
```

但是这玩意在国内由于网络原因根本动不了，所以先要为`Rustup`设置镜像仓库
可以参考下文设置环境变量
<https://www.jianshu.com/p/876b1cca26d8>


弄好之后，运行cmake就好了

# 体验感受
## 遗憾
- 没有多窗口支持
- 由于界面脚本与程序不同，接口都需要从UI暴露出来
- 缺少路由等支持