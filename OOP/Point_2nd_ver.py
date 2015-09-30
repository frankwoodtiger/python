
class Point(object):
	"""Demonstrate the alternate use of property in Python 2"""
	def __init__(self,x=0, y=0):
		self._x = x
		self._y = y

	def getx(self):
		return self._x

	def setx(self, x):
		if x >= 0:
			self._x = x
		else:
			self._x = 0
	
	x = property(getx, setx, "This is 'x' property.")
	
	def gety(self):
		return self._y
		
	def sety(self, y):
		if y >= 0:
			self._y = y
		else:
			self._y = 0
			
	y = property(gety, sety, "This is 'x' property.")
	
	def __str__(self):
		return "Point: ({}, {})".format(self.x, self.y)

if __name__=='__main__':
	pt_a = Point()
	print pt_a
	
	pt_b = Point(1.0, 2.0)
	print pt_b
	
	pt_a.x = -1
	pt_a.y = 10.0
	print pt_a
	