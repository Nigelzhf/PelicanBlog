Title: Orangeos基于qemu&bochs环境搭建及后续笔记
Date: 2016-07-21 11:15
Category: learning
Tags: learning, OS
Slug: OrangeOS
Author: EveBorn
Summary: Orange os 基于qemu&bochs环境搭建及后续笔记

# qemu&bochs环境搭建
为了宿主系统的干净，已经linux下各种工具比较方便，在这里使用ubuntu-16.04-amd64搭建环境。
偏好： make grep
## bochs

bochs用于完成书中的实验，自己移植到qemu中，继续增加其他的特性
> sudo apt-get install vgabios bochs bochs-x bximage

验证：
> test

## qemu

> sudo apt-get install qemu

没有发现如此安装有什么错误，暂时如此使用

## 需要调试环境 安装cgdb

> sudo apt-get install cgdb

## 在64位系统
首先安装libc6-dev-i386
> sudo apt-get install libc6-dev-i386

[bolg](http://blog.csdn.net/ricky_hust/article/details/7748779)
需要修改makefile，在cflags中添加-m32，在ldflags中添加-melf_i386可以解决兼容问题，不过修改完后先运行make clean将生成的.o文件去掉再运行make everything可以解决兼容问题，但还是有最后的klib.c问题，这是在cflags中添加-fno-stack-protector即可，这个原理不大明白，可以参见原始问答：http://forum.osdev.org/viewtopic.php?f=1&t=19434

# 实验笔记
## bootlorder
