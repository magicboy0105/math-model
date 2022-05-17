#程序文件Pex16_6.py
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font',size=16); N=10000;
x,y=np.random.uniform(-1,1,size=(2,N))
inside=(x**2+y**2)<=1
mpi=inside.sum()*4/N  #求pi的近似值
error=abs((mpi-np.pi)/np.pi)*100
outside=np.invert(inside)
plt.plot(x[inside],y[inside],'b.')
plt.plot(x[outside],y[outside],'r.')
plt.plot(0,0,label='$\hat\pi$={:4.3f}\nerror={:4.3f}%'.
         format(mpi,error),alpha=0)
plt.axis('square'); plt.legend(); plt.show()



