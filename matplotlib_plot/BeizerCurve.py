import matplotlib.pyplot as plt
import matplotlib.collections as col
import math
import numpy as np

# program for Multivariable calculus, plot of Beizer curve
# A cubic Beizer curve can be determined by four control point:
# P0(x0, y0), P0(x1, y1), P0(x2, y2), P0(x3, y3)
# and it's defined by the parametric equation:
# x = x0*(1 - t)^3 + 3*x1*t*(1 - t)^2 + 3*x2*t^2*(1 - t) + x3*t^3
# y = y0*(1 - t)^3 + 3*y1*t*(1 - t)^2 + 3*y2*t^2*(1 - t) + y3*t^3
# where 0 <= t <= 1

# assume t is a numpy array
def ptsOnBeizer(P0, P1, P2, P3, t):
	temp1 = 1 - t
	temp2 = temp1**2
	temp3 = temp1**3
	return P0[0]*temp3 + 3*P1[0]*t*temp2 + 3*P2[0]*(t**2)*temp1 + P3[0]*(t**3), \
	       P0[1]*temp3 + 3*P1[1]*t*temp2 + 3*P2[1]*(t**2)*temp1 + P3[1]*(t**3)

r = 2

t = np.linspace(0, 1, 100)

# since d is a vector, ptOnCycloid returns a tuple of 2 for which 
# the 1st element is a vector of y's, and
# the 2nd element is a vector of y's
# the * here unpacks the vector of 2 vector into 2 vector as arguments

# plot control points
P0 = (4,1)
P1 = (28,48)
P2 = (50,42)
P3 = (40,5)
plt.scatter(*P0)
plt.annotate('P0', P0)
plt.scatter(*P1)
plt.annotate('P1', P1)
plt.scatter(*P2)
plt.annotate('P2', P2)
plt.scatter(*P3)
plt.annotate('P3', P3)

# plot lines between control pts

data = [P0, P1, P2, P3]
x = [pt[0] for pt in data]
y = [pt[1] for pt in data]
plt.plot(x, y)

plt.plot(*ptsOnBeizer(P0, P1, P2, P3, t))
plt.axis('equal')
plt.grid(True)
plt.show()