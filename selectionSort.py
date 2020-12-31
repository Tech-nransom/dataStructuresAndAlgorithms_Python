import numpy as np
import time
def selectionSort(array):
	for outer in range(len(array)):
		smallest = array[outer]
		small_ind = outer
		for inner in range(outer,len(array)):
			if array[inner] < smallest:
				smallest = array[inner]
				small_ind = inner
		array[outer],array[small_ind] = array[small_ind],array[outer]

	return array
if __name__ == '__main__':
	# array = input("Enter the array:")
	# array = [int(no) for no in array.split()]
	array = list(np.random.randint(0,20000,2000))
	# array = [63, 436, 1849, 1860, 638, 775, 1665, 336, 562, 84, 403, 555, 653, 525, 885, 485, 946, 1105, 342, 1224]
	start = time.time()
	print(selectionSort(array))
	stop = time.time()
	print(stop-start)