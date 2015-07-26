__author__ = 'V Manikantan'

documentation = '''
Helper Class for Disjoint Set data structure

1)  Instantiate object by calling

	obj = Disjoint_Set(n) 

	where n is the number of elements in total. This creates n Disjoint sets with 1 element each.


2)	Find takes n as parameter and returns representative element of set to which element number 'n' belongs.

	Function Call: set_rep = obj.Find(n)

3)	Union takes x,y as parameters and merges the sets (if disjoint), such that set containing y becomes child
	of set containing x.

	Function Call: obj.Union(x,y)

4)	Check takes x,y as parameters and returns True/False based on whether they belong to same set or not.

	Function Call: same_set = obj.Check(x,y)

5)	Size takes n as parameter and returns size of set containing n.

	Function Call: size = obj.Size(n)

6)  Groups returns the total number of Disjoint Sets at present.
	
	Function Call: groups = obj.Groups()


NOTE: Invalid parameters to functions => No change is done / NoneType objects returned

'''

class Disjoint_Set:
	def __init__(self,n):
		self.parents = [i for i in range(n)]
		self.set_size = [1 for i in range(n)]
		self.size = n
		self.groups = n

	def Find(self,n):
		if(n>=1 and n<=self.size):
			return self.__find__(self.parents,n-1)+1
		else:
			return None

	def Union(self,x,y):
		if(x>=1 and x<=self.size and y>=1 and y<=self.size and not self.Check(x,y)):
			self.__union__(self.parents,self.Find(x)-1,self.Find(y)-1)
			self.groups-=1

	def Check(self,x,y):
		if(x>=1 and x<=self.size and y>=1 and y<=self.size):
			return self.Find(x)==self.Find(y)
		else:
			return None

	def Size(self,n):
		if(n>=1 and n<=self.size):
			return self.set_size[self.Find(n)-1]
		else:
			return None

	def __find__(self,parent,n):
		if(parent[n]==n):
			return n
		else:
			parent[n] = self.__find__(parent,parent[n])
			return parent[n]

	def __union__(self,parent,x,y):
		self.set_size[x]+=self.set_size[y]
		parent[y] = x
	
	def Groups(self):
		return self.groups
