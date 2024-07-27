---
title: windows的CLSID与ProgID对应关系
date: 2024-07-28 00:22:46
tags: 
    - Windows
    - Coding
---


前几天要写个程序，要用到windows的CLSID（~~虽然最后程序没写出来~~），发现网上没有特别全的对应关系，于是就查询资料，自己导出了一份。
<!--more-->

## 先说结果
结果在这里[CLSID.json](CLSID.json)

## 过程
查询资料得知，windows将CLSID放在注册表如下位置
- LOCAL_MACHINE\SOFTWARE\Classes\CLSID
- CLASSES_ROOT\CLSID

于是用一个C#脚本很快就导出了，代码如下

```csharp
List<CLSID> pairs = new();
{
    var reg = Registry.ClassesRoot.OpenSubKey("CLSID");
    var subs = reg.GetSubKeyNames();
    foreach (var i in subs)
    {
        var name = reg.OpenSubKey(i).GetValue("")?.ToString();
        pairs.Add(new CLSID
        {
            guid = i,
            name = name
        });
    }
}
{
    var reg = Registry.LocalMachine.OpenSubKey("SOFTWARE\\Classes\\CLSID");
    var subs = reg.GetSubKeyNames();
    foreach (var i in subs)
    {
        var name = reg.OpenSubKey(i).GetValue("")?.ToString();
        pairs.Add(new CLSID
        {
            guid = i,
            name = name
        });
    }
}

var json= JsonSerializer.Serialize(pairs,options:new JsonSerializerOptions() {WriteIndented=true });

File.WriteAllText("CLSID.json", json, encoding: Encoding.UTF8);


struct CLSID
{
    public string guid { set; get; }
    public string name { set; get; }
}
```