#程序文件Pex14_12.py
from numpy import array, piecewise, c_
d=array([[592.5,3,55,72,5],[529,2,38,105,3],[412,1,32,85,2]]); d=d.T
c1=lambda x: piecewise(x, [(350<x) & (x<600),  x>=600], [lambda x:(x-350)/250., 1])
c2=lambda x: piecewise(x, [(1.0<x) & (x<6.0), (x<=1.0)],[lambda x:1-(x-1)/5.0,1])
c3=lambda x: piecewise(x, [(20<x) & (x<60), x<=20], [lambda x:1-(x-20)/40., 1])
c4=lambda x: piecewise(x, [(50<x) & (x<130), x>=130], [lambda x:(x-50)/80., 1])
c5=lambda x: piecewise(x, [(1<x) & (x<6), x<=1], [lambda x:1-(x-1)/5., 1])
r=c_[c1(d[0]),c2(d[1]),c3(d[2]),c4(d[3]),c5(d[4])].T
w=array([0.2, 0.1, 0.15, 0.3, 0.25]);
A=w.dot(r); print('R=',r,'\n---------------------------\n','A=',A)
