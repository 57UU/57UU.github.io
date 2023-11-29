---
title: 初步上手Flask 完成一个提交页面
date: 2023-11-29 09:44:16
tags: [Coding,Python]
---

最近需要通过网络收集一些资料，有不想用腾讯文档这些臃肿的东西，就自己写了一个Web服务来收集信息

python用来写服务端非常简单
<!--more-->

其实前端核心也就是这句话
```js
fetch("/add?add=" + t.value)
```
和服务端的这句话
```python
@app.route('/add')
def add():
    add = request.args.get('add')
    print("Add: ",add)
    save(add)
    return "成功"
```
以下是全部代码

```python
from flask import Flask, request

app = Flask(__name__) 


def save(t):
    with open("sayings.txt","a",encoding='utf8') as f:
        f.write(t+"\n")

with open("index.html",encoding='utf-8') as f:
    html=f.read()

@app.route('/')
def index():
    return html
@app.route('/add')
def add():
    add = request.args.get('add')
    print("Add: ",add)
    save(add)
    return "成功"


if __name__ == '__main__':
    from waitress import serve
    print("Running--")
    serve(app, host="0.0.0.0", port=25523)
    

```
而这个`index.html`也是非常简单的

```html
<html>
    <script>
    function f() {
        let t = document.getElementById('input');
        if(t.value==""){
            alert("请输入")
            return
        }
        fetch("/add?add=" + t.value).then(() => { alert("成功"); });
    }
    </script>
<head>
    <meta charset="utf-8">
    <meta name="viewport"
        content="width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no">
    <title>
        增加锐言
    </title>
    <link href="https://cdn.staticfile.org/twitter-bootstrap/5.1.1/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.staticfile.org/twitter-bootstrap/5.1.1/js/bootstrap.bundle.min.js"></script>
</head>

<body>
    <div class="container-fluid p-5 bg-primary text-white text-center">
        <h1>提交‘锐言’</h1>
    </div>
    <div class="container p-5">
        <p>可以在下面输入‘锐言’，然后提交</p>
        <textarea class="mo-textarea" id="input" placeholder="Input here..."></textarea>
        <button type="button" class="btn btn-primary" onclick="f()">Submit</button>
    </div>

</body>

</html>
```
如果要美观一点的，还可以加入一点CSS
```html


<style>
    /* 去除默认样式 */
    textarea {
        border: none;
        outline: none;
        padding: 0;
        margin: 0;
        -webkit-appearance: none;
        -moz-appearance: none;
        appearance: none;
        background-image: none;
        background-color: transparent;
        font-size: inherit;
        width: 100%;
        height: 50%;
    }

    textarea:focus {
        outline: none;
    }

    /* 自定义样式 */
    .mo-textarea {
        display: inline-block;
        resize: vertical;
        padding: 5px 15px;
        line-height: 1.5;
        box-sizing: border-box;
        color: #606266;
        background-color: #fff;
        border: 1px solid #dcdfe6;
        border-radius: 4px;
        transition: border-color 0.2s cubic-bezier(0.645, 0.045, 0.355, 1);
    }

    /* 提示文字 */
    .mo-textarea::placeholder {
        color: #c0c4cc;
    }

    /* 鼠标hover */
    .mo-textarea:hover {
        border-color: #c0c4cc;
    }

    /* 获得焦点 */
    .mo-textarea:focus {
        border-color: #3677f0;
    }
</style>
```


## 提示
请不要使用非https传输敏感信息