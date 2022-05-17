#程序文件Pex1_7.py
f=lambda n,m:sum([k**m for k in range(1,n+1)])
s=f(100,1)+f(50,2)+f(10,-1)
print("s=%10.4f"%(s))
