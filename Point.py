
class Point(object):
	def __init__(self,x=0, y=0):
		self.x = x
		self.y = y

	@property
	def x(self):
		return self.__x

	@x.setter
	def x(self, x):
		if x >= 0:
			self.__x = x
		else:
			self.__x = 0
			
	@property
	def y(self):
		return self.__y
		
	@y.setter
	def y(self, y):
		if y >= 0:
			self.__y = y
		else:
			self.__y = 0
			
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
	