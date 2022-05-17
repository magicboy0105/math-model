#程序文件Pex17_5.py
from sklearn.neural_network import MLPRegressor
from numpy import array, loadtxt
from pylab import subplot, plot, show, xticks,rc,legend
rc('font',size=15); rc('font',family='SimHei')
a=loadtxt("Pdata17_5.txt"); x0=a[:,:3]; y1=a[:,3]; y2=a[:,4];
md1=MLPRegressor(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=10)
md1.fit(x0, y1); x=array([[73.39,3.9635,0.988],[75.55,4.0975,1.0268]])
pred1=md1.predict(x); print(md1.score(x0,y1)); 
print("客运量的预测值为：",pred1,'\n----------------'); 
md2=MLPRegressor(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=10)
md2.fit(x0, y2); pred2=md2.predict(x); print(md2.score(x0,y2)); 
print("货运量的预测值为：",pred2); yr=range(1990,2010)
subplot(121); plot(yr,y1,'o'); plot(yr,md1.predict(x0),'-*')
xticks(yr,rotation=55); legend(("原始数据","网络输出客运量"))
subplot(122); plot(yr,y2,'o'); plot(yr,md2.predict(x0),'-*')
xticks(yr,rotation=55)
legend(("原始数据","网络输出货运量"),loc='upper left'); show()
