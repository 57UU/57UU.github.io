---
title: 将Blazor-WASM-APP迁移到.Net8.0
date: 2023-11-29 19:19:38
tags:
    - [Coding]
    - [Blazor]
---
## 1
首先，要更改`TargetFramework`
```xml
<TargetFramework>net8.0</TargetFramework>
```
## 2
然后在Nuget包管理器中升级

![Nuget包管理器](nuget.png)

## 3
最后，最重要的

右键点击Blazor项目，点击清理，不然网页无法正常显示

![一定要清理](clear.png)

## 参考资料
[How to migrate your Blazor Server app to .NET 8](https://jonhilton.net/blazor-net8-migration/)

[Github Issue](https://github.com/dotnet/aspnetcore/issues/50755)