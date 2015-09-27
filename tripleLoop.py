

def countTripleLoop1(n):
	counter1 = 0
	for k in range(1,n+1):
		for j in range(k,n+1):
			for i in range(j,n+1):
				counter1 = counter1 + 1
				
	print "For n = {}, counter1: {}".format(n, counter1)
	
	print "For n = {}, by formula: {}".format(n, n*(n+1)*(n+2)/6)
	
if __name__=="__main__":
	countTripleLoop1(1)
	countTripleLoop1(2)
	countTripleLoop1(5)
	countTripleLoop1(6)
	countTripleLoop1(10)