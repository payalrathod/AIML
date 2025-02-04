import matplotlib.pyplot
import matplotlib.pyplot as plt
import numpy as np

'''
x = np.arange(0, 10)
y = np.arange(11, 21)

# scatter plot
#plt.scatter(x, y, c='r')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Graph in 2D')
#plt.savefig('test.png')
y = x*x
#plt.plot(x, y,'r--')
plt.plot(x, y, 'r*', linestyle='dashed', linewidth=2, markersize=12)

y = x*x
plt.subplot(2,2,1)
plt.plot(x,y,'r--')
plt.subplot(2,2,2)
plt.plot(x,y,'g*-')
plt.subplot(2,2,3)
plt.plot(x,y,'bo')
plt.subplot(2,2,4)
plt.plot(x,y,'b*')

y = 3*x+5
plt.title('sample')
plt.xlabel('x-axis')
plt.ylabel('y-label')
plt.plot(x,y)


x = np.arange(0, 4*np.pi, 0.1)
y = np.sin(x)
plt.subplot(2,1,1)
plt.title("sine wave")
plt.plot(x,y,'g')

x = np.arange(0, 4*np.pi, 0.1)
yy = np.cos(x)
plt.subplot(2,1,2)
plt.title("cos wave")
plt.plot(x,yy,'r--')

x = [2,8,10]
y = [11,16,9]
x1 = [1,5,11]
y2 = [12,14,5]
plt.bar(x,y)
plt.bar(x1,y2, color='r')
plt.title('bar plot')

a = np.array([22,45,54,23,76])
plt.hist(a)
plt.title('histogram')

#box plot
data = [np.random.normal(0, std, 100) for std in range(1,4)]
print(data)
plt.boxplot(data, vert=True, patch_artist=True)
plt.boxplot(data, vert=False, patch_artist=False)
'''

#pie chart
lab = 'Python', 'C++', 'Ruby', 'Java'
sizes = [215, 130, 245, 210]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.4, 0, 0, 0)
plt.pie(sizes, explode=explode, labels=lab, colors=colors, autopct='%1.1f%%', shadow=True)
plt.axis('equal')
plt.show()

matplotlib.pyplot.show()


