# 计算半周长
# -*- coding: UTF-8 -*-

# Filename : 02-math.py
# author by : （学员ID)

a = float(input('输入三角形第一边长: '))
b = float(input('输入三角形第二边长: '))
c = float(input('输入三角形第三边长: '))
p = (a + b + c) / 2

# 计算面积
# 掌握 python 开根号的写法
area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print('三角形面积为 %0.2f' % area)
