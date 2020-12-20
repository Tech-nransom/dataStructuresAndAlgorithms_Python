class Tree:
	def __init__(self,data):
		self.data = data
		self.parent = None
		self.childs = []

	def add_child(self,child):
		child.parent = self
		self.childs.append(child)

	def get_level(self):
		has_parent = self.parent
		level = 0
		while has_parent:
			level += 1
			has_parent = has_parent.parent
		return level

	def pretty_print(self,spacing = 2):
		prefix = " "*self.get_level() * spacing + ("!-->") if self.get_level() != 0 else ""
		print(prefix+ self.data)
		for child in self.childs:
			child.pretty_print(spacing)


	def UserInput(self):
		print("Enter the Root Element:")
		string = input()
		root = Tree(string)
		current = 0
		lst = []



		print("Enter the list of parents it has:")
		parent_list = input().split()
		child_no = int(len(parent_list))
		for child in parent_list:
			lst.append(Tree(child))
			print("Enter the list of parents it has:")	
			lst[-1].add_child()

			
def build_product():
	root = Tree("Gadgets")
	electronic = Tree("Electronics")
	Static = Tree("Static")

	electronic.add_child(Tree("Phone"))
	electronic.add_child(Tree("Laptop"))

	Static.add_child(Tree("Hand fan"))

	root.add_child(electronic)
	root.add_child(Static)


	return root



if __name__ == "__main__":
	root = build_product()
	root.pretty_print(4)
