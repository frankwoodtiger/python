import matplotlib.pyplot as plt
import matplotlib.collections as col
import math
import numpy as np

# program for Multivariable calculus, Question 42 on 11.1

def ptOnCircle(r, theta):
	return [r*np.cos(theta), r*np.sin(theta)]

a = 4
b = 2

np.sec = lambda x: 1.0 / np.cos(x)

# d = [-np.pi, -np.pi/2.5, -np.pi/2.75, -np.pi/3.0, -np.pi/3.2, -np.pi/3.5, -np.pi/4.0, 0, np.pi/4.0, np.pi/3.5, np.pi/3.2, np.pi/3.0, np.pi/2.75, np.pi/2.5, np.pi]
d = [np.pi/4.0, np.pi/3.5, np.pi/3.2, np.pi/3.0, np.pi/2.75, np.pi/2.5, np.pi/1.5]

	
x = [a*np.sec(d[i]) for i in range(len(d))]
y = [b*np.sin(d[i]) for i in range(len(d))]

pts_a = [ptOnCircle(a, d[i]) for i in range(len(d))] # line from origin
i = 0
for pt in pts_a:
	plt.plot([0,pt[0],x[i]], [0, pt[1],0])
	i=i+1

pts_b = [ptOnCircle(b, d[i]) for i in range(len(d))]
i = 0
for pt in pts_b:
	plt.plot([pt[0],x[i], x[i]], [pt[1],y[i],0], c='red')
	i=i+1

	
print x
print y
plt.scatter(x, y)

x_c = np.linspace(-4.0, 4.0, 100)
y_c = np.linspace(-4.0, 4.0, 100)
X_c, Y_c = np.meshgrid(x_c,y_c)
F = X_c**2 + Y_c**2 - 16.0
plt.contour(X_c,Y_c,F,[0])

F = X_c**2 + Y_c**2 - 4.0
plt.contour(X_c,Y_c,F,[0])

plt.axis('equal')
plt.grid(True)
plt.show()