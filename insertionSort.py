# def insertionSort(array):
# # Using the 2nd array Method
# 	Array = []
# 	Array.append(array[0])
# 	for no in range(1,len(array)):
# 		flg = 1
# 		for numb in range(len(Array)):
		
# 			if array[no] < Array[numb]:
# 				Array.insert(numb,array[no])
# 				flg = 0
# 				break
# 		if flg:
# 			Array.append(array[no])

# 	return Array

def insertionSort(array):
# Using the Existing Array Only

	for index in range(1,len(array)):
		flg = 1
		for inner in range(index):
			if array[index] < array[inner]:
				array.insert(inner,array[index])
				array.pop(index+1)
				flg = 0
				break

	return array

if __name__ == '__main__':
	array = [int(no) for no in input("Enter the Array:").split()]
	# array = [1 ,2 ,3 ,4 ,5 ,6 ,6 ,7 ,99 ,88 ,77 ,66 ,3 ,2 ,4 ,5]
	# array = [88 ,66 ,44 ,3 ,1 ,4 ,87 ,5 ,3 ,78 ,99 ,44 ,3 ,7 ,32]
	print(insertionSort(array))