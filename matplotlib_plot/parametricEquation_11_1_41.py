import matplotlib.pyplot as plt
import matplotlib.collections as col
import math
import numpy as np

# program for Multivariable calculus, Question 42 on 11.1

def ptOnCircle(r, theta):
	return [r*math.cos(theta), r*math.sin(theta)]

a = 4
b = 2

math.sec = lambda x: 1.0 / math.cos(x)

# d = [-math.pi, -math.pi/2.5, -math.pi/2.75, -math.pi/3.0, -math.pi/3.2, -math.pi/3.5, -math.pi/4.0, 0, math.pi/4.0, math.pi/3.5, math.pi/3.2, math.pi/3.0, math.pi/2.75, math.pi/2.5, math.pi]
d = [math.pi/16.0*i for i in range(-16,17)]

	
x = [a*math.cos(d[i]) for i in range(len(d))]
y = [b*math.sin(d[i]) for i in range(len(d))]

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