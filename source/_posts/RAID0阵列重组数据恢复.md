---
title: RAID0阵列重组数据恢复
date: 2024-02-14 15:12:49
tags: Utility
---


本文采用DiskGenius作为主要工具
<!--more-->
注意：似乎只有DiskGenius专业版有此功能

## Step1

将所有磁盘连接电脑
![](1.jpg)

## step2
![](3.png)
![](4.png)
Attention:一定要保证磁盘的添加顺序正确,`块大小`设置正确

根据经验，似乎当磁盘顺序调整正确时能够识别到损坏的分区，这时候再不断调整`块大小`，在设置正确后就能看到全部文件

## Step3
使用DiskGenius自带的分区备份功能即可备份该分区上的文件，或者直接拷贝文件也行（速度有点慢）
![](2.jpg)


# 参考资料

[DiskGenius Doc-RAID数据恢复](https://www.diskgenius.cn/exp/raid-recovery.php)