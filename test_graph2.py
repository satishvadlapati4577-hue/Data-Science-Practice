from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as s
import seaborn as sns

 #MATPLOTLIB 

plt.bar([0.25,1.25,2.25,3.25,4.25],[50,45,66,66,55,],label='Bmw',color='r',width=.6)
plt.bar([0.75,1.75,2.75,3.75,4.75],[80,40,20,40,20],label='Audi',color='b',width=.6)
plt.legend()
plt.xlabel('Days')
plt.ylabel('Distance(klm)')
plt.title('Information')
plt.show()

x=[1,2,3,4,5]
y=[11,12,13,14,15]
labels=['data1','data2','data3','data4','data5']
plt.plot(x,y)
plt.xticks(x,labels)
plt.show()

#HISTOGRAM PLOT

a=np.array([22,44,24,12,14,15,12,55,58,99])
plt.hist(a,bins=[0,25,35,45,75,100],color='b')
plt.title('histogram of result')
plt.xticks([0,25,35,45,75,100])
plt.xlabel('marks')
plt.ylabel('no of students')
plt.show()


marks=[55,75,68,3,67,12,23,35,84,75,90,]
plt.hist(marks,bins=5,color='skyblue',)
plt.title('student marks distribution')
plt.xlabel('marks range')
plt.ylabel('no of students')
plt.show()

#PIE PLOT

data=[1234542332,2354324532,2314233323,4354323243,1213131415]
i=['Chaina','Indai','Unitedstate','Indonesia','Germany']
e=[0.1,0,0,0,0]
colors=['red','orange','blue','green','#733278']
plt.pie(data,labels=i,explode=e,shadow=True,startangle=180,autopct='%1.1f%%',wedgeprops={'edgecolor':'black','linewidth':2},colors=colors)
plt.title('Population Pie Chart')
plt.show()

#SCATTER PLOT

students_id=[1,2,3,4,5,6,7,8,9,10]
students_marks=[85,89,90,75,65,58,78,53,32,25]
plt.scatter(students_id,students_marks)
plt.show()

#Maths Marks
students_id=([1,2,3,4,5,6,7,8,9,10])
students_marks=([45,67,77,88,68,88,98,77,89,93])
plt.scatter(students_id,students_marks,label='Blue=Maths')
#Science Marks
students_id=([1,2,3,4,5,6,7,8,9,10])
students_marks=([56,78,78,67,98,67,56,67,87,43])
plt.scatter(students_id,students_marks,label='orange=Science')
plt.legend()
plt.title('Students Marks')
plt.show()

#Box Plot
i=[0,1,50,900,1000,101,105]
df=pd.DataFrame(i,columns=['a'])
print(df)

i=[0,1,50,900,1000,101,105]
df=pd.DataFrame(i,columns=['a'])
print(df)
s.boxplot(df['a'])
plt.show()

#HeatMap
data=np.random.randint(low=1,high=100,size=(10,10))
print('The Data To Be Plotted:\n')
print(data)
hm=sns.heatmap(data=data)
plt.show()

#Student Marks Data
data=pd.DataFrame(
    [[58,67,86],
     [67,78,45],
     [88,67,80]],
   index=['student A','student B','student C'],
   columns=['Maths','Science','English'])
#Create Heatmap
sns.heatmap(data,annot=True,cmap='YlGnBu',linewidths=0.6)
plt.title('student marks heatmap')
plt.show()
