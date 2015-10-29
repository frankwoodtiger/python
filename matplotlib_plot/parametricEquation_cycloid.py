import matplotlib.pyplot as plt
import matplotlib.collections as col
import math
import numpy as np

# program for Multivariable calculus, plot of cycloid

def ptOnCircle(r, h, k, theta):
	return h + r*np.cos(theta), k + r*np.sin(theta)

def ptOnCycloid(r, theta):
	return r*(theta - np.sin(theta)), r*(1 - np.cos(theta))

r = 2

d = np.linspace(0, 4*np.pi, 100)

# since d is a vector, ptOnCycloid returns a tuple of 2 for which 
# the 1st element is a vector of x's, and
# the 2nd element is a vector of y's
# the * here unpacks the vector of 2 vector into 2 vector as arguments
plt.plot(*ptOnCycloid(r, d))
plt.plot(*ptOnCircle(r, r, r, np.linspace(0, 2*np.pi, 100)))
plt.plot(*ptOnCircle(r, 3*r, r, np.linspace(0, 2*np.pi, 100)))
plt.plot(*ptOnCircle(r, 5*r, r, np.linspace(0, 2*np.pi, 100)))
plt.plot(*ptOnCircle(r, 7*r, r, np.linspace(0, 2*np.pi, 100)))
plt.plot(*ptOnCircle(r, 9*r, r, np.linspace(0, 2*np.pi, 100)))
plt.plot(*ptOnCircle(r, 11*r, r, np.linspace(0, 2*np.pi, 100)))
plt.plot(*ptOnCircle(r, 13*r, r, np.linspace(0, 2*np.pi, 100)))

plt.plot(*ptOnCircle(r, r*10*np.pi/2, r, np.linspace(0, 2*np.pi, 100)))
plt.axis('equal')
plt.grid(True)
plt.show()