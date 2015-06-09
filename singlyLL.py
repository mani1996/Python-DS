__author__ = 'V Manikantan'


documentation = '''

DETAILS OF THE METHODS:

1) class SinglyLLNode defines the structure of each node in the singly linked list. Each node has a value and a link to the
   next element.

2) push_at_end accepts head node and value to be pushed at end. It returns the value of new head pointer after
   insertion.

3) push_at_beg accepts head node and value to be pushed at beginning . It returns the new head pointe after
   insertion.

4) del_at accepts the head node(compulsory) , position of node to be deleted(optional, 0 by default) and a parameter
   is_end (optional, deletes the last node if set to True, irrespective of position argument). It returns the new 
   head pointer after deletion.

NOTE:

1) If insertion or deletion cannot be performed, the linked list remains in the same state and doesn't raise any
   exception.

2) If the linked list is empty, the head node will/should be a NoneType object.   

'''

class SinglyLLNode(object):
	__slots__ = 'data','next'

	def __init__(self,data=None,next=None):
		self.data,self.next = data,next #Link is set to None by default

	def __str__(self):
		if(not self==None):
			return self.data
		else:
			return 'NULL'


def push_at_end(head,val):

	if(type(val)=='None'):
		#print 'Error : Data cannot be a NoneType object'
		#print 'List is restored to the state before this command.'
		return head

	if(head==None):
		temp = SinglyLLNode(data = val,next = None)
		head = temp
		return head
	else:
		temp1 = head
		while(temp1.next!=None):
			temp1 = temp1.next

		temp = SinglyLLNode(data = val, next = None)
		temp1.next = temp
		return head


def push_at_beg(head,val):

	if(type(val)=='None'):
		#print 'Error : Data cannot be a NoneType object'
		#print 'List is restored to the state before this command.'
		return head

	if(head==None):
		temp = SinglyLLNode(data = val,next = None)
		head = temp
		return head
	else:
		temp = SinglyLLNode(data = val,next = head)
		return temp



def del_at(head,pos=0,is_end = False):
	if(pos<0):
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



def traverse(head):
	temp = head
	while(temp!=None):
		print temp.data,
		temp = temp.next



if __name__=='__main__':
	pass


