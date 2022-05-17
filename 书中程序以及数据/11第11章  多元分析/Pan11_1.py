#程序文件Pan11_1.py
import numpy as np; import pandas as pd
from sklearn import decomposition as dc
from scipy.stats import zscore
import matplotlib.pyplot as plt
c=pd.read_excel("Pan11_1_1.xlsx",usecols=np.arange(1,7))
c=c.values.astype(float)
d=zscore(c)          #数据标准化
r=np.corrcoef(d.T)   #求相关系数矩阵
f=pd.ExcelWriter('Pan11_1_2.xlsx')
pd.DataFrame(r).to_excel(f); f.save()
val,vec=np.linalg.eig(r)
cs=np.cumsum(val)  #求特征值的累加和
print("特征值为：",val,"\n累加和为：",cs)
fa = dc.FactorAnalysis(n_components = 2)  #构建模型
fa.fit(d)   #求解最大方差的模型
print("载荷矩阵为：\n",fa.components_)
print("特殊方差为：\n",fa.noise_variance_)
dd=fa.fit_transform(d)   #计算因子得分
w=val[:2]/sum(val[:2])  #计算两个因子的权重
df=np.dot(dd,w)        #计算每个评价对象的因子总分
tf=np.sum(c,axis=1)     #计算每个评价对象的实分总分
#构造pandas数据框,第1列到第5列数据分别为因子1得分，因子2得分，因子总分、实分总分和序号
pdf=pd.DataFrame(np.c_[dd,df,tf,np.arange(1,53)],columns=['f1','f2','yf','tf','xh'])
spdf1=pdf.sort_values(by='yf',ascending = False)  #y因子总分从高到低排序
spdf2=pdf.sort_values(by='tf',ascending=False)  #实分总分从高到低排序
print("排序结果为：\n",spdf1,'\n',spdf2)
s=['A'+str(i) for i in range(1,53)]
plt.rc('font',family='SimHei'); plt.rc('axes',unicode_minus=False)
plt.plot(dd[:,0],dd[:,1],'.')
for i in range(len(s)): plt.text(dd[i,0],dd[i,1]+0.03,s[i])
plt.xlabel("基础课因子得分"); plt.ylabel("开闭卷因子得分"); plt.show()
