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

	def custom(self):
		lst = []
		print(f"Enter the list of parents {self.data} has:")
		parent_list = input().split()
		child_no = int(len(parent_list))
		if child_no:
			for index,child in enumerate(parent_list):
				lst.append(Tree(child))
				self.add_child(lst[(index)])
				lst[(index)].custom()

			
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

	root = Tree(input("Enter the Name of the root node:"))
	root.custom()
	root.pretty_print(3)
	root = build_product()
	root.pretty_print()
