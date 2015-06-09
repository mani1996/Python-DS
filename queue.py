from singlyLL import push_at_end,del_at

__author__ = 'V Manikantan'

documentation = '''

DETAILS OF THE METHODS:

1) enqueue accepts the current front,rear nodes and value to insert in queue. It returns the new front and rear
   nodes after insertion.

2) dequeue accepts the current front,rear nodes. It returns the new front and rear nodes after deletion.

3) values accepts the current front,rear nodes. It returns the values of the current front and rear nodes.  

'''


#Inserts element at the end of queue
def enqueue(front,rear,val):
	if(front==None):
		front = push_at_end(front,val)
		rear = front
	else:
		rear = push_at_end(rear,val)
		rear = rear.next
	return front,rear

#Removes element from the front of queue
def dequeue(front,rear):
	if(front!=None):
		if(front.next==None):
			front = rear = None
		else:
			front = del_at(front,0)
	else:
		#print 'Queue is empty'
		pass
	return front,rear

#Returns value of element at the ends of queue
def values(front,rear):
	v1 = v2 = 0

	if(front==None):
		v1 = None
	else:
		v1 = front.data

	if(rear==None):
		v2 = None
	else:
		v2 = rear.data

	return v1,v2


if __name__ == '__main__':
	pass