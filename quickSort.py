def partition(array,start,end):
	pivot_index = start
	pivot_no = array[pivot_index]

	while start<end:

		while array[start]<=pivot_no:
			start += 1

		while array[end] > pivot_no:
			end-=1

		if start<end:
			array[start],array[end] = array[end],array[start]

	array[pivot_index],array[end] = array[end],array[pivot_index]

	return end



def quickSort(array,start,end):
	if start < end:
		parti = partition(array,start,end)
		quickSort(array,start,parti-1)
		quickSort(array,parti+1,end)

# Method 2

# def quickSort(array,start=0,end):
# 	pIndex = start
# 	i = pIndex
# 	pivot_index = end
# 	if len(array[start:end+1]) <= 1:
		
# 		return
# 	pivot_no = array[pivot_index]

# 	initial = True
# 	while pIndex < pivot_index and i < pivot_index:

# 		while array[pIndex] < array[pivot_index] and pIndex<pivot_index:
# 			pIndex += 1
# 		if initial:
# 			i = pIndex

# 		while array[i] >= array[pivot_index] and i<pivot_index:
# 			i += 1
# 			initial = False
# 		array[pIndex],array[i] = array[i],array[pIndex]
# 	left = array[:array.index(pivot_no)]
# 	right = array[array.index(pivot_no)+1:]
# 	# quickSort(array[:array.index(pivot_no)])
# 	# quickSort(array[array.index(pivot_no)+1:])
# 	quickSort(array,start=(array.index(pivot_no)-1) if (array.index(pivot_no)-1)>0 else 0)


if __name__ == '__main__':

	# print(quickSort(array),0,end=len(array)-1)
	# array = [5 ,6 ,3 ,7 ,1 ,8 ,4]
	array = [int(no) for no in input("Enter the array:").split()]
	quickSort(array,0,len(array)-1)
	print(array)
