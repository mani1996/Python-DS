from primitives import ListNode

__author__ = 'V Manikantan'

documentation = '''

DETAILS OF THE METHODS:

1) Push adds new value to queue at rear

2) Pop removes a value from queue at front if it exists, otherwise returns empty queue.

3) Front returns the front value of queue and Rear returns the rear value of quqeue

4) Logically non existing objects are implemented as NoneType objects.

'''

class Queue:
	def __init__(self):
		self.front = self.rear = None

	def __str__(self):
		if(self.front):
			v1 = self.front.key
		else:
			v1 = None

		if(self.rear):
			v2 = self.rear.key
		else:
			v2 = None

		return str([v1,v2])

	def Push(self,val):
		new_node = ListNode(key=val,next=None)
		if(not self.rear):
			self.front = self.rear = new_node
		else:
			self.rear.next = new_node
			self.rear = new_node

	def Pop(self):
		if(self.front):
			if(self.front==self.rear):
				self.front = self.rear = None
			else:
				self.front = self.front.next

	def Front(self):
		if(self.front):
			return self.front.key
		else:
			return None

	def Rear(self):
		if(self.rear):
			return self.rear.key
		else:
			return None


if __name__ == '__main__':
	pass