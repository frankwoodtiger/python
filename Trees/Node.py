
class Node(object):
	"""Node class serves the basis of tree node"""
	numOfNode = 0;
	def __init__(self, load=0, leftNode=None, rightNode=None):
		self._load=load
		self._leftNode=leftNode
		self._rightNode=rightNode
		self._numOfNode = self.numOfNode + 1
		
	def getLoad(self):
		return self._load

	def setLoad(self, load):
		self._load = load
	
	load = property(getLoad, setLoad)
	
	def getLeftNode(self):
		return self._leftNode
	
	def setLeftNode(self, leftNode):
		self._leftNode = leftNode
		
	leftNode = property(getLeftNode, setLeftNode)
	
	def getRightNode(self):
		return self._rightNode
	
	def setRightNode(self, rightNode):
		self._rightNode = rightNode
	
	rightNode = property(getRightNode, setRightNode)
	
	def __str__(self):
		return self._load
	
# Test for Node class
if __name__=="__main__":
	rootNode = Node("root")
	leftNode = Node("left")
	rightNode = Node("right")
	rootNode.leftNode = leftNode
	rootNode.rightNode = rightNode
	
	# normal test case
	print type(rootNode)
	print rootNode
	print rootNode.load
	
	print rootNode.leftNode
	print rootNode.rightNode

	# null test case
	print rootNode.leftNode.leftNode
	print Node.numOfNode
	
	