class Queue:
	def __init__(self):
		self.queue = []

	def isEmpty(self):
		if self.queue == []:
			return 1
		else:
			return 0

	def push(self,data):
		self.queue.append(data)


	def pop(self):
		if self.queue == []:
			print("Queue is empty")
			return
		last = self.queue[0]

		del self.queue[0]

		return last

	def display(self):
		print(self.queue[::-1])

	def search(self,data):
		if data in self.queue:
			return self.queue.index(data)
		else:
			return -1

if __name__ == "__main__":
	obj = Queue()
	num = 30
	print("Is Queue empty--->"+str(obj.isEmpty()))
	obj.push(10)
	obj.push(20)
	obj.push(40)
	obj.push(30)
	obj.display()
	print("Is Queue empty--->"+str(obj.isEmpty()))
	print("The Index of number %d is %d"%(num,obj.search(30)))
	print("The poped element is %d"%obj.pop())
	print("The Index of number %d is %d"%(num,obj.search(30)))
	obj.display()


		 