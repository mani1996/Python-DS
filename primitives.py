
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
    def __init__(self, key):
        self.__key = key
        self.__next = None
    def __init__(self, key, next):
        self.__key = key
        self.__next = next

    def setKey(self, key):
        self.__key = key
    def setNext(node):
        self.__next = node

    def getKey(self):
        return self.__key

    def getNext(self):
        return self.__next
