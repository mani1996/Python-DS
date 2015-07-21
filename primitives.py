
__author__='Rishi Rajasekaran'

documentation = '''
	The following contains the list of all
	primitive data structures which are
	necessary for building more generic
	ones.

	They are primarily the basic units
	of a given data structure, such as
	a node present in a linked list
'''

class ListNode:
    def __init__(self, key, next=None):
        self.key = key
        self.next = next 
