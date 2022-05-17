#程序文件Pex14_10.py
import numpy as np
import matplotlib.pyplot as plt
from skfuzzy.cluster import cmeans
a=np.array([[1,3],[1.5,3.2],[1.3,2.8],[3,1]])
cntr,u, _, _, _, _, _ = cmeans(a.T,c=2,m=2,error=0.005, maxiter=1000)
#cntr的每一行是一个聚类中心，u的每一列是一个对象的隶属度
print(cntr,'\n-------------------------\n',u)

