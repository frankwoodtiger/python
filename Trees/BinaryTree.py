from Node import Node 

class BinaryTree(object):
	"""Binary tree class"""
	def __init__(self, rootNode):
		self._root = rootNode
		
	def getRoot(self):
		return self._root
	
	def insert(self, node):
		tempNode = self._root
		
		while tempNode is not None:
			parentNode = tempNode
			if node.load <= tempNode.load:
				tempNode = tempNode.leftNode
				if tempNode is None:
					parentNode.leftNode = node
					break
			else:
				tempNode = tempNode.rightNode
				if tempNode is None:
					parentNode.rightNode = node
					break
				
	def _preOrderTransversal_helper(self, root):
		if root is None:
			return None
		
		leftLoad = self._preOrderTransversal_helper(root.leftNode)
		leftLoad = " -> " +  leftLoad if leftLoad is not None else ""
		rightLoad = self._preOrderTransversal_helper(root.rightNode)
		rightLoad = " -> " +  rightLoad if rightLoad is not None else ""
		return root.load + leftLoad + rightLoad
	
	def preOrderTransversal(self):
		return self._preOrderTransversal_helper(self._root)
		
	def _inOrderTransversal_helper(self, root):
		if root is None:
			return None
		
		leftLoad = self._inOrderTransversal_helper(root.leftNode)
		leftLoad = leftLoad + " -> " if leftLoad is not None else ""
		rightLoad = self._inOrderTransversal_helper(root.rightNode)
		rightLoad = " -> " +  rightLoad if rightLoad is not None else ""
		return leftLoad + root.load + rightLoad
		
	def inOrderTransversal(self):
		return self._inOrderTransversal_helper(self._root)
		
	def _postOrderTransversal_helper(self, root):
		if root is None:
			return None
		
		leftLoad = self._postOrderTransversal_helper(root.leftNode)
		leftLoad = leftLoad + " -> " if leftLoad is not None else ""
		rightLoad = self._postOrderTransversal_helper(root.rightNode)
		rightLoad = rightLoad + " -> " if rightLoad is not None else ""
		return leftLoad + rightLoad + root.load
		
	def postOrderTransversal(self):
		return self._postOrderTransversal_helper(self._root)
		
if __name__=="__main__":
	btree = BinaryTree(Node('F'));
	btree.insert(Node('B'));
	btree.insert(Node('G'));
	btree.insert(Node('A'));
	btree.insert(Node('D'));
	btree.insert(Node('C'));
	btree.insert(Node('E'));
	btree.insert(Node('I'));
	btree.insert(Node('H'));
	
	root = btree.getRoot()
	
	print btree.preOrderTransversal()
	print btree.inOrderTransversal()
	print btree.postOrderTransversal()