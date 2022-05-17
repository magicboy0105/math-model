#程序文件Pex2_16.py
import numpy as np, time, math
x=[i*0.01 for i in range(1000000)]
start=time.time()  #从公元纪年开始计时，到当前的秒
for (i,t) in enumerate(x): x[i]=math.sin(t)
print("math.sin:", time.time()-start)
y=np.array([i*0.01 for i in range(1000000)])
start=time.time()
y=np.sin(y)
print("numpy.sin:", time.time()-start)

