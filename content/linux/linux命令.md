Title: linux 常用命令 长期更新
Date: 2010-10-10 10:10
Category: linux
Tags: linux
Slug: linuxCLI
Author: EveBorn
Summary: linux 常用命令 长期更新

## make

```
<target> : <prerequisites>
[tab] <commands>
```
书：[跟我一起写Makefile-陈皓](https://github.com/Nigelzhf/PelicanBlog/blob/develop/content/书/跟我一起写Makefile-陈皓.pdf)--[Download](https://github.com/Nigelzhf/PelicanBlog/raw/develop/content/%E4%B9%A6/%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile-%E9%99%88%E7%9A%93.pdf)

## vagrant

测试环境搭建

[Vagrant简介和安装配置](http://rmingwang.com/vagrant-commands-and-config.html)

[使用Vagrant在Windows下部署开发环境](https://blog.smdcn.net/article/1308.html)

## iftop

命令监控连接的带宽：sudo iftop -i wlan0 -B -F 45.67.89.0/24
-B 设置 Byte 为单位。默认是 bit
-F 过滤指定网段
暂停监控显示，使用 P 按键
