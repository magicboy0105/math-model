#程序文件Pex14_7.py
import numpy as np
a=np.array([[0.4,0.3,0.5,0.3],[0.3,0.3,0.4,0.4],[0.2,0.3,0.3,0.3]])
b=np.array([0.2,0.3,0.4,0.3]); N=[]
for i in range(len(a)): N.append(1-(np.linalg.norm(a[i]-b))/2)
print("贴近度分别为：",N)
           
