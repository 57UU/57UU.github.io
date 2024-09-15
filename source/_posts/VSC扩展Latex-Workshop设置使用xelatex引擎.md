---
title: VSC扩展Latex-Workshop设置使用xelatex引擎
date: 2024-08-27 11:30:04
tags:
    - Latex
    - Vscode
---

在网上看了一圈，使用的方法都是把默认的全局配置文件改掉，一点都不优雅
<!--more-->
使用magic语句是更好的方法，可以在文档开头写上
```tex
% !TEX program = xelatex
```

但是latex workshop默认会忽略这个属性，这就需要设置该扩展不忽略

如下图所示

![打开扩展设置](1.avif)
![设置forceRecipeUsage为false](2.png)





# 参考资料

[magic-comments](https://github.com/James-Yu/LaTeX-Workshop/wiki/Compile#magic-comments)

[latex-workshoplatexbuildforcerecipeusage](https://github.com/James-Yu/LaTeX-Workshop/wiki/Compile#latex-workshoplatexbuildforcerecipeusage)