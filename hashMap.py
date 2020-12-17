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


if __name__ == "__main__":
	hm = hashMap()
	print(hm.getHash("hello"))
	print(hm.getHash("randomString"))
	hm["hello"] = 1010
	print(hm["404"])
	print(hm["hello"])