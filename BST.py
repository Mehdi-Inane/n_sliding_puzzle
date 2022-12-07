class Node():

	def __init__(self,node=None):
		self.left = None
		self.right = None
		self.node = node
		self.value = self.node.n
		
	def insert(self,value):
		if self is None:
			return Node(value)
		else:
			if self.node.n <= value.n:
				if self.right:
					self.right.insert(value)
				else:
					self.right = Node(value)
			else:
				if self.left:
					self.left.insert(value)
				else:
					self.left = Node(value)

def minValueNode(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current	
    			
def deleteNode(root, node):
	if root is None:
		return root
	if node.value < root.value:
		root.left = deleteNode(root.left,node)
		return root
	elif(node.value > root.value):
		root.right = deleteNode(root.right,node)
		return root
	else:
		if root.value == node.value:
			if root.left is None:
				temp = root.right
				root = None
				return temp
			elif root.right is None:
				temp = root.left
				root = None
				return temp
			temp = minValueNode(root.right)
			root.value = temp.value
			root.node = temp.node
			root.right = deleteNode(root.right, temp)
		else:
			root.left = deleteNode(root.left,node)
	return root

def inorder_reverse(root):
    return_list = []
    if root:
        return_list += inorder_reverse(root.right)
        return_list +=  [root.value]
        return_list += inorder_reverse(root.left)
    return return_list
    
class Test():

	def __init__(self,n,s):
		self.n = n
		self.s = s
	def __eq__(self,node):
		if self.s == node.s and self.n == self.n:
			print('ze here')
			return True
		return False
def pop(root):
	node_min = minValueNode(root)
	root = deleteNode(root,node_min)
	return node_min	
		
test = Test(1,'n')
root = Node(test)
root.insert(Test(6,'s'))
root.insert(Test(8,'p'))
root.insert(Test(4,'u'))
root.insert(Test(6,'k'))
root.insert(Test(9,'7'))
root.insert(Test(7,'j'))
root = deleteNode(root,Node(Test(6,'k')))
print(pop(root).value)
print(inorder_reverse(root))
