#程序文件Pex2_34.py
import pandas as pd
import numpy as np
a=pd.read_excel("Pdata2_33.xlsx",usecols=range(1,4)) #提取第1列到第4列的数据
b=a.values  #提取其中的数据
#生成DataFrame类型数据
c=pd.DataFrame(b,index=np.arange(1,11),columns=["用户A","用户B","用户C"])
f=pd.ExcelWriter('Pdata2_34.xlsx')  #创建文件对象
c.to_excel(f,"sheet1")  #把c写入Excel文件
c.to_excel(f,"sheet2")  #c再写入另一个表单中
f.save()
