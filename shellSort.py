import time
import numpy as np
def gapSort(array,gap):
	for no in range(gap,len(array)):
		anchor = array[no]
		j = no
		while j>=gap and anchor < array[j-gap]:
			array[j] = array[j-gap]
			j -= gap
		array[j] = anchor
	return array

def shellSort(array,gap):
	if gap==0:
		return array
	array = gapSort(array,gap)
	return shellSort(array,gap//2)

if __name__ == '__main__':
	array = input("Enter the array:")#"234 25 778 899 223 667 7 3 2 56 8 6 11 933 8"#input("Enter the array:")
	array = [int(no) for no in array.split()]
	# array = list(np.random.randint(0,200000,7000))
	start = time.time()
	array = (shellSort(array,len(array)//2))
	stop = time.time()
	print(array)
	print(stop-start)
