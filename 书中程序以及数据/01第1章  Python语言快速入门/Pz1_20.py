#程序文件Pz1_20.py
def fun(a,b,c): print("三个数的和为：",a+b+c)
seq=[1,2,3]; fun(*seq)                  #输出：三个数的和为： 6
tup=(1,2,3); fun(*tup)                  #输出：三个数的和为： 6
dic={1:'a', 2:'b', 3:'c'}; fun(*dic)    #输出：三个数的和为： 6
set={1,2,3}; fun(*set)                  #输出：三个数的和为： 6
