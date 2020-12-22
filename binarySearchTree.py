class BinaryTree:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

	def add_elements(self, data):
	        if data == self.data:
	            return 

	        if data < self.data:
	            if self.left:
	                self.left.add_elements(data)
	            else:
	                self.left = BinaryTree(data)
	        else:
	            if self.right:
	                self.right.add_elements(data)
	            else:
	                self.right = BinaryTree(data)


	def inorder(self):
		elements= []

		if self.left:
			elements += self.left.inorder()

		elements.append(self.data)

		if self.right:
			elements += self.right.inorder()


		return elements


if __name__ == "__main__":
	numbers = [2,7,3,5,9,4,6,11,8]
	root = BinaryTree(2)
	for num in numbers:
		root.add_elements(num)

	print("Inorder->",str(root.inorder()))

		
		