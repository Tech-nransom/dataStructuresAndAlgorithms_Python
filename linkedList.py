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
		itr = self.head
		while itr.next:
			itr = itr.next
		itr.next = Node(data)

	def get_length(self):

		if self.head is None:
			return -1
		itr = self.head
		cnt = 1

		while itr.next:
			cnt += 1
			itr = itr.next
		return cnt


if __name__ == "__main__":

	ll = linkedList()
	print(ll.get_length())
	ll.display()
	ll.insert_beg(10)
	ll.insert_beg(20)
	ll.insert_beg(30)
	ll.display()
	print(ll.get_length())
	ll.insert_end(40)
	ll.display()
	print(ll.get_length())
	ll.insert_beg(90)
	ll.display()
	ll.insert_end(100)
	ll.display()
