class Stack:
	def __init__(self):
		self.stack = []

	def isEmpty(self):
		if self.stack == []:
			return 1
		else:
			return 0

	def push(self,data):
		self.stack.append(data)


	def pop(self):
		if self.stack == []:
			print("Stack is empty")
			return
		last = self.stack[-1]

		del self.stack[-1]

		return last

	def display(self):
		print(self.stack)

	def search(self,data):
		if data in self.stack:
			return self.stack.index(data)
		else:
			return -1

if __name__ == "__main__":
	obj = Stack()
	num = 30
	print("Is Stack empty--->"+str(obj.isEmpty()))
	obj.push(10)
	obj.push(20)
	obj.push(40)
	obj.push(30)
	obj.display()
	print("Is Stack empty--->"+str(obj.isEmpty()))
	print("The Index of number %d is %d"%(num,obj.search(30)))
	print("The poped element is %d"%obj.pop())
	print("The Index of number %d is %d"%(num,obj.search(30)))
	obj.display()


		 