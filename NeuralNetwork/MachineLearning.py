import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
from random import randint
import sys

class MachineLearning:
	figureNum = 0
	EPSILON = 0.0001
	lambda_reg = 1          # for regularization term
	learningRate = 20.0
	input_layer_size  = 400 # 20x20 Input Images of Digits with 5000 training sample
	hidden_layer_size = 25  # 25 hidden units
	output_layer_size = 10
	num_labels = 10         # 10 labels, from 0 to 9   
	
	def readMat(self, fileName):
		return sio.loadmat(fileName)
		
	def displaySampleByIndex(self, SampleMatrix, indx):
		self.figureNum = self.figureNum + 1
		plt.figure(self.figureNum)
		if indx <= SampleMatrix.shape[0]:
			plt.imshow(np.transpose(SampleMatrix[indx]), interpolation='none')
			
			
	def displayRandomSixSamples(self, SampleMatrix):
		self.figureNum = self.figureNum + 1
		plt.figure(self.figureNum)
		indx = randint(0,SampleMatrix.shape[0]-1)
		X = np.reshape(SampleMatrix[indx:indx+4].flatten(), (40, 40)) # randomly display handwritten digit sample
		plt.imshow(np.transpose(X), interpolation='none')
		print np.transpose(X)
		
	def displayCostVsIter(self, J_array):
		max_cost = J_array.max()
		min_cost = J_array.min()
		delta = J_array[-1] - J_array[0]
		delta_percent = (delta / J_array[0])*100
		print 'max cost: {:.3f}\nmin cost: {:.3f}\ndelta: {:.3f}\ndelta %: {:.3f}%'.format(max_cost, min_cost, delta, delta_percent)
		self.figureNum = self.figureNum + 1
		plt.figure(self.figureNum)
		plt.plot(J_array)
		plt.ylabel('J(theta)')
		
	# display theta i.e. the neuron
	def displayTheta(self, theta1, theta2):
		# dim(theta1) = 25x401
		# dim(theta2) = 10x26
		theta1 = np.reshape(theta1[:,1:].flatten(), (100, 100))
		self.figureNum = self.figureNum + 1
		plt.figure(self.figureNum)
		plt.imshow(theta1.T)
		
		self.figureNum = self.figureNum + 1
		plt.figure(self.figureNum)
		plt.imshow(theta2.T)
	
	def showAllGraphs(self):
		plt.show()
		
	def setEPSILON(self, Linput, Loutput):
		# 6.0 is important here as it make the expression as float
		self.EPSILON = np.sqrt(6.0 / (Linput + Loutput))
			
	def sigmoid(self, z):
		return 1.0 / (1.0 + np.exp(-z))
	
	def linearCombo(self, theta, X):
		# Theta1: 25x401
		# X: 401x1
		return theta.dot(X)
		
	def computeActivation(self, a_vector, theta):
		z = self.linearCombo(theta, a_vector)
		return self.sigmoid(z)
		
	# we have 1 hidden layer. Hence, we have theta1 and theta2
	def costFunction(self, X, y, theta1, theta2, debug):
		m = X.shape[0]
		J = 0
		X_b = np.append(np.ones((X.shape[0],1)), X, 1) # add bias term in the input vectors
		THETA1_grad = np.zeros(theta1.shape)
		THETA2_grad = np.zeros(theta2.shape)
		for i in range(0, m):
			# forward propagation
			a1 = np.reshape(X_b[i], (X_b[i].shape[0],1)) # transform from (401,) to (401,1) dimension-wise
			a2 = self.sigmoid(self.linearCombo(theta1, a1))
			a2 = np.append(1, a2)                        # append bias term in a2
			a2 = np.reshape(a2, (a2.shape[0], 1))        # transform from (26,) to (26,1) dimension-wise
			h = self.sigmoid(self.linearCombo(theta2, a2))
			
			# transform the y vector be logical vector
			y_vec = np.zeros((self.num_labels, 1))
			y_vec[y[i][0]-1] = 1
			
			# back propagation 
			d3 = h - y_vec
			d2 = np.multiply(theta2.T.dot(d3), np.multiply(a2, 1-a2))
			THETA2_grad = THETA2_grad + d3.dot(a2.T)
			THETA1_grad = THETA1_grad + d2[1:].dot(a1.T)
			
			# Compute cost: J(theta)
			J = J + np.sum(np.multiply(y_vec, np.log(h)) + np.multiply(1 - y_vec, np.log(1 - h)))
			
			if debug == True and i == 0:
				print 'dim(a1): {}'.format(a1.shape)
				# print a1
				print 'dim(a2): {}'.format(a2.shape)
				# print a2
				print 'dim(h): {}'.format(h.shape)
				# print h
				print 'dim(y_vec): {}'.format(y_vec.shape)
				# print y_vec
				
			# non-vectorized implementation
			# for k in range(0, self.num_labels):
			# 	J = J + y_vec[k]*np.log(h[k]) + (1-y_vec[k])*np.log(1-h[k])
		
		# add the regularization term (3 layers implementation)
		regTerm = 0
		for j in range(theta1.shape[0]):
			for k in range(theta1.shape[1]-1): # ignoring bias
				regTerm = regTerm + np.power(theta1[j,k+1], 2)
		for j in range(theta2.shape[0]):
			for k in range(theta2.shape[1]-1): # igno1ring bias
				regTerm = regTerm + np.power(theta2[j,k+1], 2)
		regTerm = self.lambda_reg*regTerm/(2*m)
		J = -1.0 * J/m + regTerm
		
		
		# calculate theta term for further gradient descent/optimization term
		reg_grad_1 = np.multiply(self.lambda_reg, theta1)
		reg_grad_1[:,0] = 0
		THETA1_grad = np.divide(THETA1_grad + reg_grad_1, m)
		
		reg_grad_2 = np.multiply(self.lambda_reg, theta2)
		reg_grad_2[:,0] = 0
		THETA2_grad = np.divide(THETA2_grad + reg_grad_2, m)
		
		if debug == True:
			print 'dim(THETA1_grad): {}'.format(THETA1_grad.shape)
			print 'dim(THETA2_grad): {}'.format(THETA2_grad.shape)
				
		
		# return a Python dict with all parameters
		return {
			'J': J,
			'THETA1_grad': THETA1_grad,
			'THETA2_grad': THETA2_grad
		}
	
	def trainNN(self, X, y, iter, isThetaExist):
		m = X.shape[0]
		J_array = np.zeros((iter,))
		
		# see if there are old thetas to use
		if isThetaExist == True:
			thetaDict = self.readMat('theta.mat')
			theta1 = thetaDict['theta1']
			theta2 = thetaDict['theta2']
		else:
			self.setEPSILON(self.input_layer_size, self.output_layer_size)
			theta1 = 2*self.EPSILON*np.random.random((self.hidden_layer_size,self.input_layer_size + 1)) - self.EPSILON # 400 input, 25 hidden unit, 10 output
			theta2 = 2*self.EPSILON*np.random.random((self.output_layer_size,self.hidden_layer_size + 1)) - self.EPSILON # 400 input, 25 hidden unit, 10 output
			# dim(theta2) = 10x26
			# dim(theta1) = 25x401
			
		for i in range(iter):
			print i
			# gradient descent
			dataSet = self.costFunction(X, y, theta1, theta2, False)
			J_array[i] = dataSet['J']
			THETA1_grad = dataSet['THETA1_grad']
			THETA2_grad = dataSet['THETA2_grad']
			theta1 = theta1 - np.multiply(self.learningRate/m, THETA1_grad)
			theta2 = theta2 - np.multiply(self.learningRate/m, THETA2_grad)
		
		if (J_array[-1] - J_array[0]) < 0:
			# only save the weighted matrix when cost is decreasing
			self.saveMat(theta1, theta2)
		else:
			print 'cost is increasing'
			
		# return a Python dict with all parameters
		return {
			'J_array': J_array,
			'theta1': theta1,
			'theta2': theta2
		}
			
	
	# X is a matrix with multiple samples (row per sample)
	def batchPredict(self, theta1, theta2, X):
		m = X.shape[0]
		num_labels = theta2.shape[0]
		
		p = np.zeros((m,1))
		X_b = np.append(np.ones((m,1)), X, 1)
		for i in range(m):
			h1 = self.sigmoid(self.linearCombo(theta1, X_b[i]))
			h1 = np.append(1, h1)
			h2 = self.sigmoid(self.linearCombo(theta2, h1))
			# take the index of max value, which is the actual value
			# note that y is matrix (5000 x 1) with value from 1 to 10, need to take the offset
			# so need to make the prediction scaled from 0 - 9 to 1 - 10 to meet the given y value
			p[i] = np.argmax(h2) + 1 
		return p
	
	# prediction over a single sample, it's actually a feed forward step
	def singlePredict(self, theta1,  theta2, x):
		x_b = np.append(1, x)
		h1 = self.sigmoid(self.linearCombo(theta1, x_b))
		h1 = np.append(1, h1)
		h2 = self.sigmoid(self.linearCombo(theta2, h1))
		return np.argmax(h2) + 1 
	
	def measureAccurancy(self, theta1, theta2, X, y):
		p = self.batchPredict(theta1, theta2, X) # (m, 1=num_labels) e.g (5000, 10)
		return np.mean(p == y)*100
	
	def saveMat(self, theta1, theta2):
		sio.savemat('theta.mat', dict(theta1=theta1, theta2=theta2))
	
	def getDataSet(self):
		imageData = self.readMat('ex4data1.mat')
		imageWeight = self.readMat('ex4weights.mat')
		dataSet = {}
		dataSet['Theta1'] = imageWeight['Theta1']
		dataSet['Theta2'] = imageWeight['Theta2']
		dataSet['y'] = imageData['y'] # 5000 x 1
		dataSet['X_pre'] = imageData['X'] # 5000 x 400 (5000 image with size 20 x 20 images)
		return dataSet

if __name__=='__main__':
	np.set_printoptions(suppress=True)
	ml = MachineLearning()
	imageData = ml.readMat('ex4data1.mat')
	imageWeight = ml.readMat('ex4weights.mat')
	Theta1 = imageWeight['Theta1']
	Theta2 = imageWeight['Theta2']
	y = imageData['y'] # 5000 x 1
	X_pre = imageData['X'] # 5000 x 400 (5000 image with size 20 x 20 images)
	
	iter = int((sys.argv)[1])
	dataSet = ml.trainNN(X_pre, y, iter, True)
	J_array =  dataSet['J_array']
	J_default = (ml.costFunction(X_pre,y,Theta1, Theta2, False))['J']
	print 'With supplied Weight: {}% accurancy with cost of {}'.format(ml.measureAccurancy(Theta1, Theta2, X_pre, y), J_default)
	print 'With Weight trained from scratch: {}% accurancy'.format(ml.measureAccurancy(dataSet['theta1'], dataSet['theta2'], X_pre, y))
	print 'y[538]: {}, feed forwad with X[538]: {}'.format(y[538][0], ml.singlePredict(dataSet['theta1'], dataSet['theta2'], X_pre[538]))
	ml.displayCostVsIter(J_array)
	
	# ml.displayTheta(dataSet['theta1'], dataSet['theta2'])
	# ml.displayTheta(Theta1, Theta2)
	# print ml.linearCombo(Theta1, np.append(1, X_pre[0])).shape
	
	# ml.displaySampleByIndex(np.reshape(X_pre, (5000, 20, 20)), 4900)
	# ml.displayRandomSixSamples(X_pre)
	# print ml.sigmoid(np.array([-10,0,10]))
	
	ml.showAllGraphs()
	
