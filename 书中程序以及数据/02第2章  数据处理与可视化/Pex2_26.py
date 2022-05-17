#程序文件Pex2_26.py
f1=open("Pdata2_26.txt","w")
str1=['Hello',' ','World!']; str2=['Hello','World!']
f1.writelines(str1); f1.write('\n')
f1.writelines(str2); f1.close()
f2=open('Pdata2_26.txt')
a=f2.read(); print(a)
