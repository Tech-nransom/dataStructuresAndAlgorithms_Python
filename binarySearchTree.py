class BinaryTree:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

	def add_elements(self, data):
	        if data == self.data:
	            print("Ignore ",end="")
	            return 

	        if data < self.data:
	            if self.left:
	            	print("L",end="")
	            	self.left.add_elements(data)
	            else:
	            	print("L",end="")
	            	self.left = BinaryTree(data)
	        else:
	            if self.right:
	            	print("R",end="")
	            	self.right.add_elements(data)
	            else:
	            	print("R",end="")
	            	self.right = BinaryTree(data)

	        print(" ",end="")


	def inorder(self):
		elements= []

		if self.left:
			elements += self.left.inorder()


		elements.append(self.data)

		if self.right:
			elements += self.right.inorder()
			
		return elements

	def find_min(self):

		if self.left is None:
			return self.data
		return self.left.find_min()

	def find_max(self):

		if self.right is None:
			return self.data
		return self.right.find_max()


	def search(self,data):

		
		if data == self.data:
			return True

		if data< self.data:
			if self.left:
				return self.left.search(data)
			else: return False

		if data> self.data:
			if self.right:
				return self.right.search(data)

			else: return False

	def deletion(self,data):

		if data< self.data:
			if self.left:
				self.left =self.left.deletion(data)
		
		elif data> self.data:
			if self.right:
				self.right = self.right.deletion(data)


		else:
			if self.left is None and self.right is None:
				return None
			if self.left is None:
				return self.right#.find_min()

			if self.right is None:
				return self.right#.find_max()

			min_val = self.right.find_min()
			self.data = min_val
			self.right = self.right.deletion(min_val)




if __name__ == "__main__":
	numbers = [2,7,3,5,9,4,6,11,8]
	root = BinaryTree(2)
	print("Path--->",end="")
	for num in numbers:
		root.add_elements(num)
	print()
	print("Inorder->",str(root.inorder()))
	root.deletion(4)
	print("Inorder->",str(root.inorder()))
	# print("Inorder->",str(root.inorder()))
	# print("Inorder->",str(root.inorder()))
	# print("Inorder->",str(root.inorder()))
	print("Find Min-->",str(root.find_min()))
	print(root.search(0))
	print("Find Max-->",str(root.find_max()))
		
		