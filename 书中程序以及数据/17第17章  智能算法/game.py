#程序文件game.py
import numpy as np
import numpy.random as nr
a=[1,2,3,4,5,6]*4   #构造列表
b=np.array(a)   #转换为数组
nr.shuffle(b)  #打乱数组b
s1=0; s2=0; n=0;
while s1<31 and s2<31 and len(b)>0:
    ind1=nr.randint(0,len(b))  #产生一个随机整数
    s1+=b[ind1]; np.delete(b,ind1) #第一个人加点，并删除对应的元素
    n+=1; ind2=nr.randint(0,len(b))  #产生随机整数
    s2+=b[ind2]; np.delete(b,ind2); n+=1;
    if s1==31 or s2>31: print("The first person win!"); break
    if s2==31 or s1>31: print("The second person win!"); break
else:
    if n%2==0: print("The second person win!")
    else: print("The first person win!")


