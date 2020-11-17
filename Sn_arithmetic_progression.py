# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 14:08:24 2020

@author: TONG
"""
#!/usr/bin/python3

str = "等差数列前n项和计算器"
print (str.center(80, '*'))

b = a = int(input("请输入等差数列的首项："))
d = int(input("请输入等差数列的公差："))
n = int(input("请输入项数n："))
sum = 0
counter = 1

while counter <= n:
    sum = sum + a
    a = a + d
    counter += 1
    
str = "计算结果"
print (str.center(80, '*'))

print("首项为 %d 公差为 %d 的等差数列前 %d 项之和为: %d" % (b,d,n,sum)) #每个%d（十进制整数）对应后面一个数


    
