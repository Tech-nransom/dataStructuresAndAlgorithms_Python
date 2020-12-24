class Graph:

	def __init__(self, edges):
		self.edges = edges
		self.dict = {}
		self.cnt = 0
		for start,end in edges:
			if start in self.dict:
				if type(end) == type([]):
					self.dict.get(start).extend(end)
					self.dict[start] = list(set(self.dict.get(start)))
				else:
					if end not in self.dict.get(start):
						self.dict.get(start).append(end)


			else:
				if type(end) == type([]):
					self.dict[start] = end

				else:
					self.dict[start] = [end]

	def printGraph(self):
		print(self.dict)

	def get_paths(self, start, end, path=[]):
	        path = path + [start]

	        if start == end:
	            return [path]

	        if start not in self.dict:
	            return []

	        paths = []
	        for node in self.dict[start]:
	            if node not in path:
	                new_paths = self.get_paths(node, end, path)
	                for p in new_paths:
	                    paths.append(p)

	        self.cnt = len(paths)

	        return paths

	def noOfPaths(self,start,end,path=[]):
		return(self.cnt)		
if __name__ == '__main__':
	
	cities = [

	("Mumbai",["Paris","Dubai"]),
	("Paris",["NYC","Dubai"]),
	("Dubai","NYC"),
	("NYC","Toronto"),

	]

	graph = Graph(cities)
	graph.printGraph()
	start = input("Enter The Starting Point:")
	end = input("Enter the Ending Point:")
	print(graph.get_paths(start,end))
	print(f" Number of paths available to connect from {start} to {end} is {graph.noOfPaths(start,end)}")