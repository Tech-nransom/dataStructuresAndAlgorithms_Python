#Without collisions
class hashMap:
	
	def __init__(self):
		self.hash = [None for i in range(100)]
		

	def getHash(self,string):
		val = 0
		for char in string:
			val += ord(char)
		return val % 100

	def add(self,string,value):
		val = self.getHash(string)
		self.hash[val] =  value

	def get(self,string):
		val = self.getHash(string)
		return self.hash[val]


if __name__ == "__main__":
	hashmap = hashMap()
	print(hashmap.getHash("hello"))
	print(hashmap.getHash("randomString"))
	hashmap.add("hello",101010)
	print(hashmap.get("hello"))