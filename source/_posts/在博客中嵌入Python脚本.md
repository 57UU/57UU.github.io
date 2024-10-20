---
title: 在博客中嵌入Python脚本
date: 2024-10-12 13:59:29
tags:
    - Python
    - Web
---
之前看友链博客做了这样的一个test，刚好今天就有同学在研究怎么在网页上跑py，于是我就写了这样一个示例。

# Example

<script src="https://cdn.jsdelivr.net/pyodide/v0.26.2/full/pyodide.js"></script>
<script type="text/javascript">
    function callback(){
        let code=document.getElementById("code").value;
        document.getElementById("result").innerText="Code is running"
        loadPyodide().then((pyodide) => {
            let result=pyodide.runPython(code);
            document.getElementById("result").innerText=result;
        });
    }
</script>

<textarea id="code" style="width:80%;height:5rem;">
def get_num():
    return (114514+114514)*(11-4+5/1-4)+(114*514+(114*51*4+(1145*(1+4)+11-4+5+1-4)))
get_num()
</textarea>

<button onclick="callback()" style="background-color: #4CAF50;padding: 15px 32px;text-align: center;border-radius: 5px;">Run code</button>

Result:

<p id="result"></p>


# 博客代码
实现起来非常简单，只需要一点前端知识就能看懂。
```html
<script src="https://cdn.jsdelivr.net/pyodide/v0.26.2/full/pyodide.js"></script>
<script type="text/javascript">
    function callback(){
        let code=document.getElementById("code").value;
        document.getElementById("result").innerText="Code is running"
        loadPyodide().then((pyodide) => {
            let result=pyodide.runPython(code);
            document.getElementById("result").innerText=result;
        });
    }
</script>

<textarea id="code" style="width:80%;height:5rem;">
def get_num():
    return (114514+114514)*(11-4+5/1-4)+(114*514+(114*51*4+(1145*(1+4)+11-4+5+1-4)))
get_num()
</textarea>

<button onclick="callback()" style="background-color: #4CAF50;padding: 15px 32px;text-align: center;border-radius: 5px;">Run code</button>

Result:

<p id="result"></p>
```

# 一点解释
其实就是加载了一个py的web实现，把代码丢到这个环境中跑。

# 问题
测试发现，若没有加速器，加载py引擎的时间可能会过长；且这个引擎的效率不高，运行也慢。