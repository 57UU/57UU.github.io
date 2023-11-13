---
title: 适用于Blazor_Webassembly的Github-action配置文件
date: 2023-11-12 18:43:19
tags:    
    - [Coding]
    - [Blazor]
    - [Github]
---
Github-action实在是太好用了，最近在搞Blazor Webassembly,去网上抄袭了一圈，得到了以下config
<!--more-->
```yml
name: .NET

on:
  push:
    branches: [ "master" ]
  pull_request:
    branches: [ "master" ]

permissions:
  contents: write

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Setup .NET
      uses: actions/setup-dotnet@v3
      with:
        dotnet-version: 7.x.x
    - name: Publish with dotnet
      run: dotnet publish --configuration Release --output build
      
    - name: Deploy to GitHub Pages
      uses: JamesIves/github-pages-deploy-action@v4.4.3
      with: 
       folder: build/wwwroot
```

## 由于Github-pages的特殊情况,还需要添加.nojekyll文件

在第一次生成完成后，转到gh-pages分支，添加.nojekyll空文件

![如图所示](1.png)

## 最后再多说一嘴Blazor的坑
Blazor倾向于使用缓存，这可能会导致应用不能及时更新,需要使用Ctrl+F5强制刷新