#程序文件Pex16_9_2.py
import numpy as np
a=2; b=3; lamda=10; M1=0;
u=1; n=10000;
for i in range(1,2*lamda):
    d=np.random.poisson(lamda,n)  #产生n个服从Poiss分布的需求量数据
    M2=np.mean(((b-a)*u*(u<=d)+((b-a)*d-a*(u-d))*(u>d)))  #求平均利润
    if M2>M1: M1=M2; u=u+1;
    else: print('最佳购进量:',u-1); break


