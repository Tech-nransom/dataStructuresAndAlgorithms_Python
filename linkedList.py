class Node:
	def __init__(self, data=None,next = None):
		self.data = data
		self.next = next

class linkedList:
	def __init__(self):
		self.head = None

	def insert_beg(self,data):
		node  = Node(data,self.head)
		self.head = node

	def display(self):
		if self.head is None:
			return
		itr = self.head
		str_ll = ""
		while(itr):			
			str_ll += str(itr.data) + "-->"
			itr = itr.next
		print(str_ll)

	def insert_end(self,data):
		try:
			itr = self.head
			while itr.next:
				itr = itr.next
			itr.next = Node(data)
		except Exception as exc:
			print("linkedList not started")

      
	def get_length(self):

		if self.head is None:
			return -1
		itr = self.head
		cnt = 1

		while itr.next:
			cnt += 1
			itr = itr.next
		return cnt
	def update_at(self,data,position):
		if 0<position<=self.get_length():
			
			itr = self.head
			cnt= 1
			while cnt != position:
				cnt += 1
				itr = itr.next
			itr.data = data
		else:
			print("update at position %d not possible"%position)
			return 

	def insert_after(self,data,position):
		if 1<position<self.get_length():
			itr = self.head
			cnt = 1
			while cnt != position:
				cnt += 1
				itr = itr.next
			node = Node(data,itr.next)
			itr.next = node
		else:
			print("Insert is not in Middle")
			return

if __name__ == "__main__":

	ll = linkedList()
	print("The Length of the linkedList currently is "+str(ll.get_length()))
	ll.display()
	ll.insert_beg(10)
	ll.insert_beg(20)
	ll.insert_beg(30)
	ll.display()
	print("The Length of the linkedList currently is "+str(ll.get_length()))
	ll.insert_end(40)
	ll.display()
	print("The Length of the linkedList currently is "+str(ll.get_length()))
	ll.insert_beg(90)
	ll.display()
	ll.insert_end(100)
	ll.display()
	ll.update_at(77,2)
	ll.display()
	ll.insert_after(55,5)
	ll.display()
	print("The Length of the linkedList currently is "+str(ll.get_length()))
