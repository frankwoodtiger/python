
class Node:
	"""Node class serves the basis of tree node"""
	def __init__(self, load=0, leftNode=None, rightNode=None)
		self.load=load
		self.leftNode=leftNode
		self.rightNode=rightNode
		
	def setLoad(self, load)
		self.load = load
		
	def getLoad(self):
		return self.load
		
	def setLeftNode(self, leftNode):
		self.leftNode = leftNode
		
	def getLeftNode(self):
		return self.leftNode
		
	def setRightNode(self, rightNode):
		self.rightNode = rightNode
		
	def getRightNode(self):
		return self.rightNode