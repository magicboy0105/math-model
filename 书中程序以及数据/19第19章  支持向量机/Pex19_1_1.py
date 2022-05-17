#程序文件Pex19_1.py
from sklearn import datasets, svm, metrics
from sklearn.model_selection import GridSearchCV
import numpy as np
iris=datasets.load_iris()
x=iris.data; y=iris.target
parameters = {'kernel':('linear','rbf'), 'C':[1,10,15]}
svc=svm.SVC(gamma='scale')
clf=GridSearchCV(svc,parameters,cv=5)  #cv为交叉验证参数，为5折
clf.fit(x,y)
print("最佳的参数值:", clf.best_params_)
print("score：",clf.score(x,y))
yh=clf.predict(x); print(yh) #显示分类的结果
print("预测准确率：",metrics.accuracy_score(y,yh))
print("误判的样本点为:",np.where(yh!=y)[0]+1)
