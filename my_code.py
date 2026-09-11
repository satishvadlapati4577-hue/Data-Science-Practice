import pandas as pd
import numpy as np

s1=pd.Series([23,24,25,25,12,24])
print(s1)

s2=pd.Series([23,45,67,12,34],index=['a','b','c','d','e'])
print(s2)

s3=pd.Series([23,45,67,12,34],index=['a','b','c','d','e'],dtype='float')
print(s3)
# creation of series from dictionary

s4=pd.Series({'a':23,'b':45,'c':56})
print(s4)

s5=pd.Series({'telugu':66,'english':45,'maths':56,'science':78,'social':89})
print(s5)

s6=pd.Series({employee:salary for employee,salary in zip({'rajesh','satish','prameela','anusha'},{35000,45000,70000,90000})})
print(s6)

# @title:
d1=pd.DataFrame([43,44,43,56,66,34,])
print(d1)

d2=pd.DataFrame([[34,45,56,65,78],
                 [54,76,78,89,90],
                 [78,78,67,87,90]])
print(d2)

d2=pd.DataFrame(s2)
print(d2)

#Generate code with d2
d3=pd.DataFrame([[34,45,56,65,78],[54,76,78,89,90],[78,78,67,87,90]],index=['a','b','c'],columns=['maths','english','telugu','science','social'])
print(d3)

#createDataFrame from list of dictionaries

dic=[{'Nani':23,'mahesh':45},{ 'prameela':67,'anusha':87,'rajesh':90},{ 'satish':87,'nagulu':87,'ramesh':80}]
print (pd.DataFrame(dic,index=['a','b','c']))

#DataFrame operations
print(d3)
print(d3['maths'])
print(d3['english'])

print(d3.loc['a'])
print(d3.loc['b'])

d3['d']=d3['maths']*d3['english']
d3['e']=d3['english']+d3['maths']
print(d3)

#pop operation
d3.pop('maths')
print(d3)
d3.pop('d')
print(d3)
del d3['social']
print(d3)

#insert the data

d3.insert(1,'new1',[34,45,56])
print(d3)

#append operation
d3=pd.concat([d3,pd.DataFrame([[34,45,56,65],[45,65,65,77]],columns=['new1','english','telugu','science'])],ignore_index=True)
print(d3)

import numpy as np
d4=pd.DataFrame({'abc':np.random.randint(2,8,size=10),'xyz':np.random.randint(5,10,size=10),'bcd':np.random.randint(4,10,size=10)})
print(d4)