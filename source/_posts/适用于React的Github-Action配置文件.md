---
title: 适用于React的Github-Action配置文件
date: 2023-10-30 18:44:41
tags: 
    - [Coding]
    - [React]
    - [Github]
---

最近想给react配置一个自动构建，在网上查(chao)阅(xi)了许多资料,作为一个缝合怪，终于是把yml文件配置好了

```yml
# This workflow will do a clean installation of node dependencies, cache/restore them, build the source code and run tests across different versions of node
# For more information see: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-nodejs

name: Node.js CI

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
    strategy:
      matrix:
        node-version: [18.x]
        # See supported Node.js release schedule at https://nodejs.org/en/about/releases/
    steps:
    - uses: actions/checkout@v3
      with:
        token: ${{ secrets.GITHUB_TOKEN }}
        # If your repository depends on submodule, please see: https://github.com/actions/checkout
        submodules: recursive
    - name: Setup Node.js environment
      uses: actions/setup-node@v4.0.0
    - run: npm ci
    - run: CI=false npm run build
    #- run: npm test
    - name: Deploy to GitHub Pages
      uses: JamesIves/github-pages-deploy-action@v4.4.3
      with: 
       folder: build
            
```
有些东西我感觉是多余了，但是既然已经可以成功运行了，那最好还是不要动了

对了，还要设置github page从gh-pages分支中部署

 [React自动构建项目仓库](https://github.com/57UU/LiteratureMonth13)

 [文件示例](https://github.com/57UU/LiteratureMonth13/blob/master/.github/workflows/node.js.yml)
