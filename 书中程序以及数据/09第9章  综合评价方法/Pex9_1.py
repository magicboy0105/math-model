#程序文件Pex9_1.py
import numpy as np
import pandas as pd
a=np.loadtxt("Pdata9_1_1.txt",)
R1=a.copy(); R2=a.copy(); R3=a.copy()  #初始化
#注意R1=a,它们的内存地址一样，R1改变时，a也改变
for j in [0,1,2,4,5]:
    R1[:,j]=R1[:,j]/np.linalg.norm(R1[:,j]) #向量归一化
    R2[:,j]=R1[:,j]/max(R1[:,j])     #比例变换
    R3[:,j]=(R3[:,j]-min(R3[:,j]))/(max(R3[:,j])-min(R3[:,j]));
R1[:,3]=1-R1[:,3]/np.linalg.norm(R1[:,3])
R2[:,3]=min(R2[:,3])/R2[:,3]
R3[:,3]=(max(R3[:,3])-R3[:,3])/(max(R3[:,3])-min(R3[:,3]))
np.savetxt("Pdata9_1_2.txt", R1); #把数据写入文本文件，供下面使用
np.savetxt("Pdata9_1_3.txt", R2); np.savetxt("Pdata9_1_4.txt", R3)
DR1=pd.DataFrame(R1)  #生成DataFrame类型数据
DR2=pd.DataFrame(R2); DR3=pd.DataFrame(R3)
f=pd.ExcelWriter('Pdata9_1_5.xlsx')  #创建文件对象
DR1.to_excel(f,"sheet1")  #把DR1写入Excel文件1号表单中,方便做表
DR2.to_excel(f,"sheet2"); DR3.to_excel(f, "Sheet3"); f.save()


