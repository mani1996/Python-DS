__author__ = 'V Manikantan'

documentation = '''Implementation of a MaxHeap which can store objects of a single type. 
Comparison must be defined for the object in order to store based on priority.

1) Insert inserts given value into the max heap
2) GetMax returns the value of root node of heap (not deleted)
3) DeleteMax deletes root node and returns its value

NOTE: Tested functionality with Heap Sort algorithm.
'''


class MaxHeap:
	def __init__(self):
		self.nodes = []
		self.size = 0

	def Insert(self,val):
		self.nodes.append(val)
		self.size+=1
		n = self.size-1
		self.__sift_up__(self.nodes,n)

	def GetMax(self):
		if(self.nodes):
			return self.nodes[0]
		else:
			return None

	def DeleteMax(self):
		n = self.size
		if(n):
			res = self.nodes[0]
			v = self.nodes[n-1]
			self.nodes.pop(n-1)
			n,self.size = n-1,self.size-1

			if(self.nodes):
				self.nodes[0] = v
				self.__sift_down__(self.nodes,0,self.size)				

			return res
		else:
			return None


	def __sift_up__(self,a,index):
		while(index>0):
			if(a[index]>a[(index-1)/2]):
				a[index],a[(index-1)/2] = a[(index-1)/2],a[index]
				index = (index-1)/2
			else:
				break

	def __sift_down__(self,a,index,size):
		while(index<size):
			if((2*index+1>=size or a[index]>=a[2*index+1]) and (2*index+2>=size or a[index]>=a[2*index+2])):
				break
			elif(2*index+1<size and a[2*index+1]>a[index] and a[2*index+1]>a[2*index+2]):
				a[index],a[2*index+1] = a[2*index+1],a[index]
				index = 2*index+1
			else:
				if(2*index+2<size):
					a[index],a[2*index+2] = a[2*index+2],a[index]
				index = 2*index+2

