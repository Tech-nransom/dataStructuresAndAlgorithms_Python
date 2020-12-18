#Without collisions
class hashMap:
	
	def __init__(self):
		self.hash = [None for i in range(100)]
		

	def getHash(self,string):
		val = 0
		for char in string:
			val += ord(char)
		return val % 100

	def __setitem__(self,string,value):
		val = self.getHash(string)
		self.hash[val] =  value

	def __getitem__(self,string):
		val = self.getHash(string)
		return self.hash[val]

#Hashing using chaining(Covered Collisions)
class hashMapChaining:
	def __init__(self,size=100):
		self.hash = [[] for i in range(size)]

	def getHash(self,string):
		val = 0
		for char in string:
			val += ord(char)
		return val % 100

	def __setitem__(self,string,value):
		val = self.getHash(string)
		for index,items in enumerate(self.hash[val]):
			if items[0] == string:
				del self.hash[val][index]
				self.hash[val].append((string,value)) 
				print("Update successfull")
		if len(self.hash[val]) == 0 or (string in [i[0] for i in self.hash[val]]) == False:
			self.hash[val].append((string,value))
			print("New Added")

	def __getitem__(self,string):
		val = self.getHash(string)
		for items in (self.hash[val]):
			if string == items[0]:
				return items
		return []


if __name__ == "__main__":
	hm = hashMapChaining()
	print(hm.getHash("hello"))
	print(hm.getHash("randomString"))
	hm["hello"] = 1010
	hm["hello"] = 0000
	hm["germany"] = 111
	hm["england"] = 222
	hm["poland"] = 333
	hm["india"] = 444
	hm["america"] = 555
	hm["randomString"] = 666
	hm["whatsup"] = 234
	hm["all fine"] = 643
	print(hm["india"])
	print(hm["hello"])
	print(hm["america"])
	print(hm["unknown"])
	print(hm["randomString"])
