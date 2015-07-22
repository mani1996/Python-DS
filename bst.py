from primitives import BSTNode
__author__ = 'V Manikantan'


class BST:
	def __init__(self):
		self.root = None

	def Insert(self,l):
		self.root = insert(self.root,val)

	def Check(self,val):
		return check(self.root,val)

	def Delete(self,val):
		self.root = delete(self.root,val)

	def Inorder(self):
		inorder(self.root)

	def Preorder(self):
		preorder(self.root)

	def Postorder(self):
		postorder(self.root)


#Insert into BST. 
#Takes root node and value to be inserted as parameters. 
#Returns new root node.
def insert(root,val):
	if(not root):
		node = BSTNode(val)
		return node
	else:
		if(val < root.value):
			root.left = insert(root.left,val)
		else:
			root.right = insert(root.right,val)
		return root

#Checks if given value exists in BST.
#Takes root node and value to be checked as parameters
#Returns True or False based on whether value exists or not
def check(root,val):
	if(root):
		if(root.value==val):
			return True
		else:
			return check(root.left,val) or check(root.right,val)
	else:
		return False

#Deletes particular node with given value in BST, if it exists
def delete(root,val):
	if(root):
		if(root.value==val):
			if(not root.left and not root.right):
				root = None
			elif(not root.left):
				root = root.right
			elif(not root.right):
				root = root.left
			else:
				suc = root.left
				temp = root.right
				if(root.left.right==None):
					root = root.left
					root.right = temp
				else:
					while(suc.right.right):
						suc = suc.right

					newval = suc.right.value
					suc.right = None
					root.value = newval
		elif(val<root.value):
			root.left = delete(root.left,val)
		else:
			root.right = delete(root.right,val)
		return root
	else:
		return None

#Inorder traversal of BST.
#Takes root node as parameter.
def inorder(root):
	if(root):
		inorder(root.left)
		print root.value,
		inorder(root.right)

#Preorder traversal of BST.
#Takes root node as parameter.
def preorder(root):
	if(root):
		print root.value,
		preorder(root.left)
		preorder(root.right)

#Postorder traversal of BST.
#Takes root node as parameter.
def postorder(root):
	if(root):
		postorder(root.left)
		postorder(root.right)
		print root.value,