import numpy as np
import time
def mergeTwoArrays(arr1,arr2):
	index = 0
	Array = []
	while (len(arr1) and len(arr2)):
		if arr1[index] < arr2[index]:
			Array.append(arr1.pop(index))
		elif arr2[index] < arr1[index]:
			Array.append(arr2.pop(index))
		else:
			Array.append(arr1.pop(index))

	if len(arr1)!=0:
		Array.extend(arr1)
	if len(arr2)!=0:
		Array.extend(arr2)
	return Array

def seprateArrays(array):
	half = len(array)//2
	return array[:half],array[half:]

def mergeSort(array):
	if len(array) < 2:
		return array
	arr1,arr2 = seprateArrays(array)
	arr1 = mergeSort(arr1)
	arr2 = mergeSort(arr2)
	return (mergeTwoArrays(arr1,arr2))
	


if __name__ == '__main__':
	# array = "5 6 43 7 8 3 9 55 44 0"
	# array = [int(no) for no in array.split()]
	array = list(np.random.randint(0,2000,500))
	start = time.time()
	array = (mergeSort(array))
	end = time.time()
	print(end-start)

	