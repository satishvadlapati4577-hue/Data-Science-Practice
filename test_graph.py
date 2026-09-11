from matplotlib import pyplot as plt
import numpy as np

x = [8,5,4,6,9]
y = [3,5,7,9,6]
plt.plot(x,y)
plt.title('info')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

#polting without lines

xpoints = np.array([2,9,5,8,6])
ypoints = np.array([4,12,5,7,9])

plt.plot(xpoints,ypoints,'o')
plt.title('pltting without lines')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

x=np.array([85,67,87,98,78,101,40,55,90,100])
y=np.array([230,231,219,260,170,330,200,150,320,300])

plt.title('Running Time vs Distance')
plt.xlabel('distance')
plt.ylabel('Running Time')
plt.plot(x,y)
plt.show()

x=np.array([45,56,67,78,76])
y=np.array([101,120,150,131,121])
plt.title('Sports Watch Data')
plt.xlabel('average pulse rate')
plt.ylabel('calories burnage')
plt.plot(x,y)
plt.show()

#MARKERS

ypoints=np.array([7,8,4,10])
xpoints=np.array([12,14,16,18])
#plt.plot(xpoints,,markers='o')
plt.plot(xpoints,ypoints,marker='p')
plt.show()

plt.plot(ypoints,marker='*',ms=10,mec='r',mfc='w')
plt.show()

ypoints=np.array([84,6,8,10])

plt.plot(ypoints,linestyle='dotted')
plt.show()

plt.plot(ypoints,linestyle='dotted',marker='*',ms=12,mec='g',mfc='y')
plt.title('Dotted Line With Markers')
plt.show()

#LINE WIDTH

plt.plot(ypoints,linewidth='12',color='r')
plt.title('Line Width')
plt.show()

#SUBPLOT

#PLOT 1:

x=np.array([1,3,5,7,9])
y=np.array([3,8,9,12,15])
print(x)
print(y)
plt.subplot(1,2,1)
plt.plot(x,y)
plt.title('1st Graph')

#PLOT 2:

x=np.array([2,4,6,8,10])
y=np.array([4,9,11,15,19])
plt.subplot(1,2,2)
plt.plot(x,y)
plt.title('2nd Graph')
plt.show()

#BAR PLOT
#--Horizontal Bar Chart

activities=['sleeping','eating','working','playing']
frequency=[7,3,8,4]
plt.barh(activities,frequency,color='g')
plt.title('Horizontal Bar Chart')
plt.xlabel('frequency')
plt.ylabel('activities')
plt.show()

# "OR"
activities=['sports','phone','tv','friends','money','online','club','study']
frequency=[45,65,50,60,70,80,90,100]
plt.barh(activities,frequency,color='b')
plt.title('studentactivities')
plt.xlabel('activities')
plt.ylabel('no of students')
plt.show()

#VERTICAL BAR CHART 

languages=['python','java','c++','javascript','htms','css','sql','php']
students=[45,35,55,75,12,2,100,17]
plt.bar(languages,students,color='r')
plt.title('Vertical Bar Chart')
plt.show()




