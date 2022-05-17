#程序文件Pex4_9.py
import numpy as np
import matplotlib.pyplot as plt
a=np.loadtxt("Pdata4_9.txt")  #读入两行的数据
b=a.T  #转置成两列的数据
plt.rc('font',size=16); plt.rc('font',family='SimHei')
plt.boxplot(b,labels=['女子','男子'])
plt.savefig('figure4_9.png', dpi=500); plt.show()
