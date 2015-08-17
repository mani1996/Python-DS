from collections import deque

class Graph:
	def __init__(self,directed = False,weighted = False):
		self._graph = {}
		self.directed = bool(directed)
		self.weighted = bool(weighted)
		self.edgeCount = 0
		self.vertexCount = 0
	
	
	def addVertex(self,node):
		if node not in self._graph:
			self._graph[node] = []
			self.vertexCount += 1
	
	
	def addEdge(self,src,dst,weight = None):
		try:
			for adj in self._graph[src]:
				if dst == adj['dst']:
					print "Edge already exists."
					return
		except KeyError:
			pass
		if src not in self._graph:
			self.addVertex(src)
		if dst not in self._graph:
			self.addVertex(dst)
		if self.weighted:
			if weight is None:
				print "Please enter some weight."
				return
			edge = {'dst':dst,
					'weight':weight}
			
			self._graph[src].append(edge)
			if not self.directed:
				backedge = {'dst':src,
							'weight':weight}
				self._graph[dst].append(backedge)
				self.edgeCount += 1
		else:
			edge = {'dst':dst}
			if edge not in self._graph[src]:
				self._graph[src].append(edge)
				if not self.directed:
					self._graph[dst].append({'dst':src})
					self.edgeCount += 1
			else:
				print "Edge already exists."
				return
		self.edgeCount += 1
		print "Edge Added."
	

	def BFS(self,node):
		q = deque([])															
		q.append(node)
		visited = {}
		visited[node] = True
		while q:
			subnode = q.popleft()
			print subnode
			for adj in self._graph[subnode]:
				if adj['dst'] not in visited:
					visited[adj['dst']] = True
					q.append(adj['dst'])
				
				
	def DFS(self,node):
		s = []
		s.append(node)
		visited = {}
		visited[node] = True
		while s:
			subnode = s.pop()
			for i in self._graph[subnode]:
				if i['dst'] not in visited:
					visited[i['dst']] = True
					s.append(i['dst'])
			print subnode
					
					
	def DFSRecursive(self,node,visited):
		visited[node] = True
		count = 0
		for i in self._graph[node]:
			if i['dst'] not in visited:
				count += 1
				count += self.DFSRecursive(i['dst'],visited)
		print str(node) + " " + str(count)
		return count 
			
			
	def getEdges(self):
		if self.weighted:
			return 	[{'src':vertex,
					'dst':edge['dst'],
					'weight':edge['weight']} 
					for vertex in self._graph.keys() for edge in self._graph[vertex]]
		else:
			return 	[{'src':vertex,
					'dst':edge['dst']} 
					for vertex in self._graph.keys() for edge in self._graph[vertex]]
						
	def getVertices(self):
		vertices = []
		for vertex in self._graph.keys():
			if vertex not in vertices:
				vertices.append(vertex)
			for neighbor in self._graph[vertex]:
				if neighbor['dst'] not in vertices:
					vertices.append(neighbor['dst'])
		return vertices 
			
	def shortestPath(self,source):
		if not self.weighted:
			print "Graph is not weighted."
			return
		vertices = self.getVertices()
		if source not in vertices:
			print "Source not in graph."
			return 
		Queue = {}
		distances = {}
		Queue[source] = 0
		distances[source] = 0
		for vertex in vertices:
			if vertex != source:
				Queue[vertex] = 1000000
				distances[vertex] = 1000000
		while Queue:
			u = min(Queue,key =  Queue.get)
			for adj in self._graph[u]:
				try:
					if Queue[adj['dst']] > Queue[u] + adj['weight']:
						Queue[adj['dst']] = Queue[u] + adj['weight']
						distances[adj['dst']] = Queue[u] + adj['weight']
				except KeyError:
					pass
			del Queue[u]
		return distances
		
		