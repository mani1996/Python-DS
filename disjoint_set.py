class Disjoint_Set:
	def __init__(self,n):
		self.parents = [i for i in range(n)]
		self.set_size = [1 for i in range(n)]
		self.size = n

	def Find(self,n):
		if(n>=1 and n<=self.size):
			return self.__find__(self.parents,n-1)+1
		else:
			return None

	def Union(self,x,y):
		if(x>=1 and x<=self.size and y>=1 and y<=self.size):
			self.__union__(self.parents,x-1,y-1)

	def Check(self,x,y):
		if(x>=1 and x<=self.size and y>=1 and y<=self.size):
			return Find(self,x-1)==Find(self,y-1)
		else:
			return None

	def Size(self,n):
		if(n>=1 and n<=self.size):
			return self.set_size[n-1]
		else:
			return None

	def __find__(self,parent,n):
		if(parent[n]==n):
			return n
		else:
			parent[n] = __find__(parent,parent[n])
			return parent[n]

	def __union__(parent,x,y):



