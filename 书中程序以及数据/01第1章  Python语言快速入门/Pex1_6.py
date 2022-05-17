#程序文件Pex1_6.py
f=lambda a,b=2,c=5: a-b+c        #使用默认值参数
print("f=",f(10,20))             #输出: f=-5
print("f=",f(10,20,30))          #输出：f=20
print("f=",f(c=20,a=10,b=30))    #使用关键字实参，输出：f=0

