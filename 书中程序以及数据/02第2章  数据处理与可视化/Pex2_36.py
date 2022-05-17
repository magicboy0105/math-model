#程序文件Pex2_36.py
import numpy as np, pandas as pd
from matplotlib.pyplot import *
a=pd.read_excel("Pdata2_33.xlsx",usecols=range(1,4))  #提取第2列到第4列的数据
c=np.sum(a)  #求每一列的和
ind=np.array([1,2,3]); width=0.2
rc('font',size=16); bar(ind,c,width); ylabel("消费数据")
xticks(ind,['用户A','用户B','用户C'],rotation=20)  #旋转20度
rcParams['font.sans-serif']=['SimHei']   #用来正常显示中文标签
savefig('figure2_36.png',dpi=500)   #保存图片为文件figure2_36.png，像素为500
show()
