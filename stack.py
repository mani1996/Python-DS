from primitives import ListNode

__author__ = 'V Manikantan and Rishi Rajasekaran'

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

class Stack:
    def __init__(self):
        self.top = None

    def push(self, key):
        self.top = ListNode(key, self.top)

    def pop(self):
        if (self.top != None):
            self.top = self.top.next
    
    def top(self):
        return self.top
    
    def empty(self):
        return (self.top == None)

    def print_stack(self):
        print "Contents of stack: "
        it = self.top
        while (it != None):
            print it.key
            it = it.next

if __name__ == '__main__':
	pass
