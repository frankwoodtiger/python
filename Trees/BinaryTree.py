from Node import Node 
import time
from math import log
from math import ceil
from collections import deque

class BinaryTree(object):
	"""Binary tree class"""
	def __init__(self, rootNode=None):
		self._root = rootNode
		
	def getRoot(self):
		return self._root
		
	def searchNodeByLoad(self, load):
		if self._root is None:
			return None
			
		tempNode = self._root
		while tempNode is not None:
			if load == tempNode.load:
				return tempNode
			elif load < tempNode.load:
				tempNode = tempNode.leftNode
			else:
				tempNode = tempNode.rightNode
		return tempNode
		
	def getMinNode(self):
		if self._root is None:
			return None
			
		tempNode = self._root
		while tempNode.leftNode is not None:
			tempNode = tempNode.leftNode
				
		return tempNode
	
	def getMinParentChildTupleFromNode(self, node):
		if node is None:
			return (None, None)
		
		# special case when node has no childs so that parentNode is None and node is not
		parentNode = None
		while node.leftNode is not None:
			parentNode = node
			node = node.leftNode
		
		return (parentNode, node)
		
	def getMaxNode(self):
		if self._root is None:
			return None
			
		tempNode = self._root
		while tempNode.rightNode is not None:
			tempNode = tempNode.rightNode
				
		return tempNode
	
	def countImmediateChild(self, node):
		if node is None:
			return
		count = 2
		if node.leftNode is None:
			count = count - 1
		if node.rightNode is None:
			count = count - 1
		return count
		
	def countChildsFromNode(self, node):
		if node == None:
			return 0
		if self.countImmediateChild(node) == 0:
			return 1
		return 1 + self.countChildsFromNode(node.leftNode) + self.countChildsFromNode(node.rightNode)
	
	def countTreeNode(self):
		return self.countChildsFromNode(self._root)
		
	def insert(self, node):
		if type(node) is not Node:
			node = Node(node)
			
		if self._root is None:
			self._root = node
			return
			
		tempNode = self._root
		while tempNode is not None:
			if node.load <= tempNode.load:
				if tempNode.leftNode is None:
					tempNode.leftNode = node
					break;
				else:
					tempNode = tempNode.leftNode
			else:
				if tempNode.rightNode is None:
					tempNode.rightNode = node
					break;
				else:
					tempNode = tempNode.rightNode
					
	def recursiveInsert(self, insertNode):
		if type(insertNode) is not Node:
			insertNode = Node(insertNode)
			
		self._recursiveInsert_helper(insertNode, self._root)
	
	def _recursiveInsert_helper(self, insertNode, currentNode):	
		if self._root is None:
			self._root = insertNode
			return
			
		if insertNode.load <= currentNode.load:
			if currentNode.leftNode is None:
				currentNode.leftNode = insertNode
			else:
				self._recursiveInsert_helper(insertNode, currentNode.leftNode)
		else:
			if currentNode.rightNode is None:
				currentNode.rightNode = insertNode
			else:
				self._recursiveInsert_helper(insertNode, currentNode.rightNode)
	
	def popRoot(self):
		if self._root == None:
			return None
			
		load = self._root.load
		successorParent, successor = self.getMinParentChildTupleFromNode(self._root.rightNode)
		
		# successor of B is C, the next node that is greater than itself
		#            F
		#           / \
		#          /   \
		#        |B|    G
		#        / \     \
		#       A   D     I
		#          / \   /
		#        |C|  E H
		
		if successor is None:
			self._root = self._root.leftNode
		else: 
			self._root.load = successor.load
			if successorParent is None: 
				# special case when the successor's parent is the passing node 
				self._root.rightNode = successor.rightNode
			else:	
				successorParent.leftNode = successor.rightNode
		return load
					
	def deleteNodeByLoad(self, load):
		if load == self._root.load:
			self.popRoot() # popRoot takes care the empty tree case
			return True
			
		tempNode = self._root		
		while tempNode is not None:
			if load < tempNode.load:
				isLeft = True # isLeft notifies whether the next layer's node is a left or right node
				parentNode = tempNode
				tempNode = tempNode.leftNode
			elif load > tempNode.load:
				isLeft = False
				parentNode = tempNode
				tempNode = tempNode.rightNode
			else:
				if self.countImmediateChild(tempNode) == 0:
					# case 1: deleted node has no child (trivial case)
					if isLeft is True:
						parentNode.leftNode = None
					else:
						parentNode.rightNode = None
				elif tempNode.leftNode is None:
					# case 2.1: deleted node has a right child (just swap with replace with child node)
					if isLeft is True:
						parentNode.leftNode = tempNode.rightNode
					else:
						parentNode.rightNode = tempNode.rightNode
				elif tempNode.rightNode is None:
					# case 2.1: deleted node has a right child (just swap with replace with child node)
					if isLeft is True:
						parentNode.leftNode = tempNode.leftNode
					else:
						parentNode.rightNode = tempNode.leftNode
				else:
					# case 3: deleted node has two children (get successor node, swap and delete 
					# the dangling swapped child)
					successorParent, successor = self.getMinParentChildTupleFromNode(tempNode.rightNode)
					tempNode.load = successor.load
					if successorParent is None:
						tempNode.rightNode = successor.rightNode
					else:
						successorParent.leftNode = successor.rightNode
				return True
		return False
	
	def _preOrderTransversal_helper(self, root):
		if root is None:
			return None
		
		leftLoad = self._preOrderTransversal_helper(root.leftNode)
		leftLoad = " -> " +  str(leftLoad) if leftLoad is not None else ""
		rightLoad = self._preOrderTransversal_helper(root.rightNode)
		rightLoad = " -> " +  str(rightLoad) if rightLoad is not None else ""
		return str(root.load) + str(leftLoad) + str(rightLoad)
	
	def preOrderTransversal(self):
		return self._preOrderTransversal_helper(self._root)
		
	def _inOrderTransversal_helper(self, root):
		if root is None:
			return None
		
		leftLoad = self._inOrderTransversal_helper(root.leftNode)
		leftLoad = str(leftLoad) + " -> " if leftLoad is not None else ""
		rightLoad = self._inOrderTransversal_helper(root.rightNode)
		rightLoad = " -> " +  str(rightLoad) if rightLoad is not None else ""
		return str(leftLoad) + str(root.load) + str(rightLoad)
		
	def inOrderTransversal(self):
		return self._inOrderTransversal_helper(self._root)
		
	def _postOrderTransversal_helper(self, root):
		if root is None:
			return None
		
		leftLoad = self._postOrderTransversal_helper(root.leftNode)
		leftLoad = str(leftLoad) + " -> " if leftLoad is not None else ""
		rightLoad = self._postOrderTransversal_helper(root.rightNode)
		rightLoad = str(rightLoad) + " -> " if rightLoad is not None else ""
		return str(leftLoad) + str(rightLoad) + str(root.load)
		
	def postOrderTransversal(self):
		return self._postOrderTransversal_helper(self._root)

	def bfsTraversal_oneline(self): # also same as level order
		if self._root is None:
			return None
		dq = deque([self._root])
		strList = []
		while dq:  # while dq is not empty
			if dq[0].leftNode is not None:
				dq.append(dq[0].leftNode)
			if dq[0].rightNode is not None:
				dq.append(dq[0].rightNode)
			# You know you have visited all children at this point so we can de-queue our queue
			# We use list and later join list to form str, this is easier than the
			# above string concatenation approach in other transversal
			strList.append(dq.popleft().load)
		return " ".join(strList)
	
	def bfsTraversal_with_newline(self):
		currentLevel = [self._root]
		strList = []
		while currentLevel:
			nextLevel = []
			for node in currentLevel:
				if node is None:
					strList.append("( )") # show the empty node as well
					continue              # skip this node as this is actually not a real node
					
				strList.append('(' + node.load + ')')
				if node.leftNode is not None: 
					nextLevel.append(node.leftNode)
				else:
					nextLevel.append(None)
				if node.rightNode is not None: 
					nextLevel.append(node.rightNode)
				else:
					nextLevel.append(None)
			strList.append('\n')
			currentLevel = nextLevel
		str = " " + " ".join(strList)
		return str[0:str.rfind('\n', 0, len(str)-1)] # rfind is used to remove the last empty layer
		
	def toInOrderList(self):
		return self._toInOrderList_helper(self._root)
	
	def _toInOrderList_helper(self, root):
		if root is None:
			return []
		
		lt = []
		lt.extend(self._toInOrderList_helper(root.leftNode))
		lt.extend([root.load])
		lt.extend(self._toInOrderList_helper(root.rightNode))
		return lt

	def balance(self):
		if self._root is None:
			return
		lt = self.toInOrderList()
		self._root = None # Hand it to gc to clear the tree first
		self._balance_helper(lt, 0, len(lt) - 1)
		
	def _balance_helper(self, lt, lowIndex, highIndex):
		# 1. call toInOrderList to construct a sorted list, and pass the list as argument in here - O(n)
		# 2. insert back the list to a new tree, by insert the middle of the list recursively - O(n)
		# Thus, O(n) + O(n) = O(2n) => O(n)
		# Eg: let say we have the following tree
		#            5
		#           /
		#          4
		#         /
		#        3
		#       /
		#      2
		#     /
		#    1
		# toInOrder will get a sorted list whatever: [ 1 2 3 4 5 ]
		
		# indx:   0 1 2 3 4
		# list: [ 1 2 3 4 5 ]
		
		# 1st iter: mid = (4+0)/2 = 2
			# indx:   0 1    |2|                   3 4
			# list: [ 1 2 ] [ 3 (inserted 1st) ] [ 4 5 ]
		
		# 2nd iter: mid = (1+0)/2 = 0                                       |    mid = (4+3)/2 = 3    
			# indx:  |0|                   1                                |     |3|                   4
			# list: [ 1 (inserted 2nd) ] [ 2 (inserted 3rd as base case)]   |    [ 4 (inserted 4th) ] [ 5 (inserted 5th as base case) ]
		
		# Thus, We should get inserted order: 3, 1, 2, 4, 5 which produce the tree below
		#            3
		#           / \
		#          1   4
		#           \   \
		#            2   5
		
		if lowIndex == highIndex:
			self.insert(lt[lowIndex])
			return
		elif lowIndex >= highIndex:
			return
		
		midIndex = (lowIndex + highIndex) / 2
		self.insert(lt[midIndex])
		self._balance_helper(lt, lowIndex, midIndex-1)
		self._balance_helper(lt, midIndex+1, highIndex)
		
if __name__=="__main__":
	# Tree example from tree transversal wiki
	#            F
	#           / \
	#          /   \
	#         B     G
	#        / \     \
	#       A   D     I
    #          / \   /
	#         C   E H
	btree = BinaryTree()
	start_time = time.clock()
	btree.insert('F')
	btree.insert(Node('B'))
	btree.insert(Node('G'))
	btree.insert(Node('A'))
	btree.insert(Node('D'))
	btree.insert(Node('C'))
	btree.insert(Node('E'))
	btree.insert(Node('I'))
	btree.insert(Node('H'))
	elapse_time_sec = (time.clock() - start_time)
	print "insert takes {:f} sec".format(elapse_time_sec) 
	
	print " preorder transversal: %s" % btree.preOrderTransversal()
	print "  inorder transversal: %s" % btree.inOrderTransversal()
	print "postorder transversal: %s" % btree.postOrderTransversal()
	print "BFS transversal oneliner:%s" % btree.bfsTraversal_oneline()
	print "BFS transversal level:\n%s" % btree.bfsTraversal_with_newline()
	
	print "Num of node: %d" % btree.countTreeNode()
	print "Min node: {}".format(btree.getMinNode())
	print "Min node using getMinParentChildTupleFromNode: {}".format(btree.getMinParentChildTupleFromNode(btree.getRoot().rightNode)[1])
	print "Max node: {}".format(btree.getMaxNode())
	print "'B' in tree?: {}".format(btree.searchNodeByLoad('B'))
	print "'Z' in tree?: {}".format(btree.searchNodeByLoad('Z'))
	print "toInOrderList: {}".format(btree.toInOrderList())
	
	for i in range(btree.countTreeNode()):
		print "After deleting poping root of {}:".format(btree.popRoot())
		print btree.inOrderTransversal()
	
	btree_r = BinaryTree()
	start_time = time.clock()
	btree_r.recursiveInsert('F')
	btree_r.recursiveInsert(Node('B'))
	btree_r.recursiveInsert(Node('G'))
	btree_r.recursiveInsert(Node('A'))
	btree_r.recursiveInsert(Node('D'))
	btree_r.recursiveInsert(Node('C'))
	btree_r.recursiveInsert(Node('E'))
	btree_r.recursiveInsert(Node('I'))
	btree_r.recursiveInsert(Node('H'))
	elapse_time_sec = (time.clock() - start_time)
	print "recursive insert takes {:f} sec".format(elapse_time_sec) 
	
	print btree_r.inOrderTransversal()
	print "Deleting 'D': {}".format(btree_r.deleteNodeByLoad('D'))
	print btree_r.inOrderTransversal()
	print "Deleting 'G': {}".format(btree_r.deleteNodeByLoad('G'))
	print btree_r.inOrderTransversal()
	print "Deleting 'H': {}".format(btree_r.deleteNodeByLoad('H'))
	print btree_r.inOrderTransversal()
	print "Deleting 'F': {}".format(btree_r.deleteNodeByLoad('F'))
	print btree_r.inOrderTransversal()
	print "Deleting 'A': {}".format(btree_r.deleteNodeByLoad('A'))
	print btree_r.inOrderTransversal()
	print "Deleting 'I': {}".format(btree_r.deleteNodeByLoad('I'))
	print btree_r.inOrderTransversal()
	print "Deleting 'B': {}".format(btree_r.deleteNodeByLoad('B'))
	print btree_r.inOrderTransversal()
	print "Deleting 'E': {}".format(btree_r.deleteNodeByLoad('E'))
	print btree_r.inOrderTransversal()
	print "Deleting 'C': {}".format(btree_r.deleteNodeByLoad('C'))
	print btree_r.inOrderTransversal()
	
	btree_ub = BinaryTree()
	for i in reversed(range(1,6)): # reversed return an iterator rather than a pure list
		btree_ub.insert(i)
	
	# pre order is the insert sequence
	print btree_ub.preOrderTransversal()
	btree_ub.balance()
	print btree_ub.preOrderTransversal()
	