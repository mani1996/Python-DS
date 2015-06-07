__author__ = 'V Manikantan'

class Node(object):
	__slots__ = 'data','next'

	def __init__(self,data=None,next=None):
		self.data,self.next = data,next #Link is set to None by default

	def __str__(self):
		if(not self==None):
			return self.data
		else:
			return 'NULL'


# Adds an element at end of linked list and returns new head pointer
def push_at_end(head,val):

	if(type(val)=='None'):
		#print 'Error : Data cannot be a NoneType object'
		#print 'List is restored to the state before this command.'
		return head

	if(head==None):
		temp = Node(data = val,next = None)
		head = temp
		return head
	else:
		temp1 = head
		while(temp1.next!=None):
			temp1 = temp1.next

		temp = Node(data = val, next = None)
		temp1.next = temp
		return head

# Adds an element at beginning of linked list and returns head pointer
def push_at_beg(head,val):

	if(type(val)=='None'):
		#print 'Error : Data cannot be a NoneType object'
		#print 'List is restored to the state before this command.'
		return head

	if(head==None):
		temp = Node(data = val,next = None)
		head = temp
		return head
	else:
		temp = Node(data = val,next = head)
		return temp


# Receives position of node to be deleted ( 0 - indexing )
def del_at(head,pos=0,is_end = False):
	if(pos<0): #Indices to the left of 0 handled here
		#print 'Error : Invalid index. Index starts from 0 (inclusive).'
		#print 'List is restored to the state before this command.'
		pass
	elif(head==None):
		#print 'Error : Linked list is empty'
		#print 'List is restored to the state before this command.'
		pass
	else:

		if(not is_end):
			if(pos):
				ctr = 1;
				temp = head.next;
				temp1 = head;

				while(not temp==None and not ctr==pos):
					temp = temp.next
					temp1 = temp1.next
					ctr = ctr+1

				if(temp==None):
					#print 'Error : Invalid index. Position value is higher than maximum permissible index.'
					#print 'List is restored to the state before this command.'
					pass
				else:
					temp1.next = temp.next
			else:
				head = head.next

		else:
			if(head.next==None):
				head = None
			else:
				temp = head
				while(temp.next.next!=None):
					temp = temp.next

				temp.next = temp.next.next

	return head


# Traverses the linked list starting from head node
def traverse(head):
	temp = head
	
	while(temp!=None):
		print temp.data,
		temp = temp.next



if __name__=='__main__':
	pass


