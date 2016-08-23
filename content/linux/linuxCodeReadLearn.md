Title: linux源代码阅读&相关资源
Date: 2016-08-17 10:10
Category: linux 学习
Tags: learning, linux, 操作系统, Source
Slug: linuxCodeReadLearn
Author: EveBorn
Summary: linux源代码阅读&相关资源，资源整理

# linux history

* linux 0.11
* linux 0.95    实现虚拟文件系统
* linux 0.96    实现网络接口

# linux

linux采用分段+分页机制结合管理内存

# linux 调试方法 

* [linux0.11 调试方法](https://wwssllabcd.github.io/blog/2012/08/03/compile-linux011/)
```
gdb tools/system
target remote localhost:1234


gdb常用命令
b: 下中斷點
info b :u 列出目前中断点，也可简写成"i b"
continue(c) 继续执行直到下一个中断点或结束
list(l): 列出目前上下文
step(s): 单步 (会进入 funciton)
next(n) : 单步 (不会进入 funciton)
until(u) 跳离一个 while for 循环
print(p): 显示某变量，如 p str
info register(i r) : 显示 CPU 的 register

GDB 打印出内存中的內容，格式為 x/nyz，其中
n: 要印出的數量
y: 显示的格式，可为C( char), d(整数), x(hex)
z: 单位，可为 b(byte), h(16bit), w(32bit)
```


# source

* [80386保护模式的本质](http://www.jianshu.com/p/1cea7dc5d6b7)
* [Intel 80386 程序员参考手册](http://www.kancloud.cn/wizardforcel/intel-80386-ref-manual/123838)
* [linux0.11内核之文件系统](http://harpsword.leanote.com/post/Untitled-563d6103ab6441584f000164)

