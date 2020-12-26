def bubbleSort(array,ascending=True):
	for i in range(len(array)):
		for j in range(i,len(array)):
			if ascending:
				if array[i] > array[j]:
					array[i],array[j] = array[j],array[i]
			else:
				if array[i] < array[j]:
					array[i],array[j] = array[j],array[i]

	return array


# 9 2 5 1 3 7



if __name__ == '__main__':
	array = []
	for number in input("Enter The Array:").split():
		array.append(int(number))

	print(bubbleSort(array,ascending=False))