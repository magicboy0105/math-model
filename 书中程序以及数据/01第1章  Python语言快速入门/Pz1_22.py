#程序文件Pz1_22.py
from numpy import random  as rd   #从numpy库中导入模块random并设置别名为rd
from math import sin, cos     #导入模块中的正弦函数和余弦函数
from random import randint
a=rd.randint(0,10,(1,3))  #产生[0,10)的3个元素的随机整数数组
b=randint(0,10)  #产生[0,10]上的一个随机整数，不能产生向量
print("sin(b)=%6.4f"%sin(b))
print("cos(b)=%6.4f"%cos(b))

