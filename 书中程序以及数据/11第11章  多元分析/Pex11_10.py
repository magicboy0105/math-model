#程序文件Pex11_10.py
import numpy as np
from sklearn.decomposition import FactorAnalysis
r=np.array([[1, 1/5, -1/5],[1/5, 1, -2/5],[-1/5, -2/5, 1]])
fa=FactorAnalysis()
r_fa=fa.fit(r)
print(r_fa.get_params())
