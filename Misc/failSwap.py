
def failSwap(a, b):
	temp = a
	a = b
	b = temp

def swap(a, b):
	return b, a
	
if __name__=="__main__":
	a = 'a'
	b = 'b'
	
	print "before failSwap, a = '{}', b = '{}'".format(a, b)
	failSwap(a, b)
	print "After failSwap, a = '{}', b = '{}'".format(a, b)
	# It fails because Python is pass by value
	
	print "before swap, a = '{}', b = '{}'".format(a, b)
	a, b = swap(a, b)
	print "After swap, a = '{}', b = '{}'".format(a, b)
	