import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
from random import randint
import sys

def getMNISTFromGrayscale(grayscale):
	lowerbound_mn = -1.0
	upperbound_mn = 1.0
	upperbound_gs = 255.0
	resolution = (upperbound_mn - lowerbound_mn) / upperbound_gs
	mnist_array = lowerbound_mn + grayscale * resolution
	return mnist_array

def getNormalizedMNist(mnist):
	return mnist.flattern()
	
if __name__=="__main__":
	