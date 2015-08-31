class SuffixArray(object):

	def __init__(self,s):
		s = str(s)
		self.l = self.__suffix_array(s)

	def __suffix_array(self,s):
		try:
			l = len(s)
			rank = [[i,ord(s[i])-ord('a')] for i in range(l)]
			maps = [-1 for i in range(l)]
			for i in range(l-1):
				maps[i] = rank[i+1][1]
			for i in range(l):
				rank[i].append(maps[i])
			rank.sort(key = lambda t:(t[1],t[2])) #Comparison upto first 2 characters done
			k = 2
			while(k<l):	
				#print rank
				x = 0
				maps = [0 for i in range(l)]
				for i in range(1,l):
					if((rank[i][1],rank[i][2])!=(rank[i-1][1],rank[i-1][2])):
						x+=1
					maps[i] = x
			
				for i in range(l):
					rank[i][1] = maps[i]
				
				maps = [-1 for i in range(l)]
				for i in range(l):
					if(rank[i][0]>=k):
						maps[rank[i][0]-k] = rank[i][1]

				for i in range(l):
					if(maps[rank[i][0]]==-1):
						rank[i][2] = -1
					else:
						rank[i][2] = maps[rank[i][0]]
				rank.sort(key = lambda t:(t[1],t[2]))
				k*=2
			return map(lambda x:x[0],rank)
		except:
			return "Something wrong"

'''
s = raw_input('Enter the string:')
l = suffix_array(s)
print l
'''