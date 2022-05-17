#程序文件Pex13_5_2.py
import numpy as np
import matplotlib.pyplot as plt

def fun(delta,*str):
    w=100; tw=[]
    for k in range(1,11):
        w=delta*w+2.5-0.125*k; tw.append(w)
    print(tw); w2=tw[-1]  #提取第二阶段的初值
    tw2=[]; k=0
    while w2>=75:
        k+=1; w2=delta*w2+1.25;
        tw2.append(w2); tw.append(w2)
    print("k=%d时,w(%d)=%.4f"%(k,k,w2))
    plt.plot(np.arange(1,len(tw)+1),tw,str[0])

def fun2(datas,labels):
    for data, style in datas:
        fun(data, style)
    plt.legend(labels, prop={'family': 'SimHei', 'size': 16})
    plt.show()

fun2([(0.975,"s-"),(0.97,"*-")],("正常代谢","增加运动"))
