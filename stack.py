from singlyLL import push_at_beg,del_at

__author__ = 'V Manikantan'

documentation = '''

DETAILS OF THE METHODS:

1) push accepts the current top node and value to be pushed. It returns the new top node.

2) pop accepts the current top node. It returns the new top node after peforming pop operation.

3) top accepts the current top node. It returns the value on top of the stack.

NOTE:

1) If push or pop operation cannot be performed, the stack remains in the same state and doesn't raise any
   exception.

2) If the stack is empty, the top node will/should be a NoneType object.   

'''

#Pushes element on top of stack
def push(top,val):
	top = push_at_beg(top,val)
	return top

#Pops element from top of stack
def pop(top):
	top = del_at(top,0)
	return top

#Returns value of top element in stack
def top(top):
	if(top==None):
		#print 'Error : Stack is empty'
		return None
	else:
		return top.data



if __name__ == '__main__':
	pass