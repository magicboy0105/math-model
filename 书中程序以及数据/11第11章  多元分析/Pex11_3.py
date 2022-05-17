#程序文件Pex11_3.py
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
x0=np.array([[1.24,1.27], [1.36,1.74], [1.38,1.64], [1.38,1.82], [1.38,1.90], [1.40,1.70],
    [1.48,1.82], [1.54,1.82], [1.56,2.08], [1.14,1.78], [1.18,1.96], [1.20,1.86],
    [1.26,2.00], [1.28,2.00], [1.30,1.96]])   #输入已知样本数据
x=np.array([[1.24,1.80], [1.28,1.84], [1.40,2.04]])  #输入待判样本点数据
y0=np.hstack([np.ones(9),2*np.ones(6)])  #y0为已知样本数据的类别
clf = LDA()
clf.fit(x0, y0)
print("判别结果为：",clf.predict(x))
print("已知样本的误判率为：",1-clf.score(x0,y0))

