#程序文件Pex16_10
from numpy.random import exponential, uniform, seed
from numpy import mean, array, zeros
seed(4)  #进行一致性比较,每次运行结果一样
def oneday():
    W=[0]  #第一个顾客的等待时间
    t0=exponential(10); c0=t0
    g0=c0+uniform(4,15); g=g0
    while g<480:
        t=exponential(10)  #下一个到达时间间隔
        c=c0+t  #下一个到达时刻
        w=max(0,g-c)  #下一个等待时间
        g=max(g,c)+uniform(4,15)  #下一个离开时刻
        c0=c  #把当前到达时刻保存起来
        W.append(w)  #把等待时间保存到列表中
    return len(W), mean(W)
W1=oneday(); print("服务人数和平均等待时间分别为：",W1)
d=1000  #模拟的天数
T=zeros(d); N=zeros(d)
for i in range(d):
    N[i],T[i]=oneday()
print("平均服务人数为：",round(N.mean()))
print("平均等待时间为：",T.mean())
