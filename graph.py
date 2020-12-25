class Graph:

	def __init__(self, edges=[]):
		self.edges = edges
		self.dict = {}
		self.cnt = 0
		for start,end in edges:
			start = start.lower()
			if start in self.dict:
				if type(end) == type([]):
					self.dict.get(start).extend([Nodes.lower() for Nodes in end])
					self.dict[start] = list(set(self.dict.get(start)))
				else:
					end = end.lower()
					if end not in self.dict.get(start):
						self.dict.get(start).append(end)

			else:
				if type(end) == type([]):
					self.dict[start] = [Nodes.lower() for Nodes in end]

				else:
					self.dict[start] = [end.lower()]


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

	def shortestPath(self,start,end):
		
		try:
			return min(self.get_paths(start,end))
		except : return []


	def getInput(self):
		choice = 1
		while choice:
			start = input("Enter The Starting Node:").lower()
			end = [nodes.lower() for nodes in input(f"Enter the Nodes Linked to {start}:").split()]

			if start not in self.dict:
				self.dict[start] = end
			else:
				self.dict.get(start).extend(end)
				self.dict[start] = list(set(self.dict.get(start)))

			choice = int(input("Do you want to continue?? (0/1):"))




if __name__ == '__main__':
	
	cities = [

	("Mumbai",["Paris","Dubai"]),
	("Paris",["NYC","Dubai"]),
	("Dubai","NYC"),
	("NYC","Toronto"),

	]

	graph = Graph(cities)
	graph.printGraph()
	start = input("Enter The Starting Point:").lower()
	end = input("Enter the Ending Point:").lower()
	print(graph.get_paths(start,end))
	print(f"Number of paths available to connect from {start} to {end} is {graph.noOfPaths(start,end)}")
	print("The shortestPath from {0} to {1} is {2}".format(start,end,graph.shortestPath(start,end)))
	sample= Graph()
	sample.getInput()
	sample.printGraph()