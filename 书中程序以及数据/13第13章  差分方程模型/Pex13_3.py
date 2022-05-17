#程序文件Pex13_3.py
x0=1000000; r=0.005; N=500; n=0; xm=8000
x1=x0*(1+r)-xm
while n<=N and x1>0:
    n+=1;
    if n%12==0: print("第%d个月末欠钱：x(%d)=%.4f"%(n,n,x1))
    x0=x1; x1=x0*(1+r)-xm
print("还款月数n=",n+1)
print("还款%d年%d个月"%((n+1)//12,n+1-12*((n+1)//12)))



