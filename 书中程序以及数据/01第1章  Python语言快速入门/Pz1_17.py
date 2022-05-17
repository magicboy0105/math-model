#程序文件Pz1_17.py
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30) 
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')
