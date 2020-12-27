def binarySearch(array,number):
	left = 0
	right = len(array)-1
	mid = int((left+right)/ 2)
	flg = 1
	cnt = 1
	if array[left] == number:
		print(f"number found at location {left}")
		flg = 0
		return cnt
	if array[right] == number:
		print(f"number found at location {right}")
		flg = 0
		return cnt
	while (right-left)!=1:
		if array[mid] == number:
			print(f"number found at location {mid}")
			flg = 0
			return cnt

		if array[mid] > number:
			right = mid

		if array[mid] < number:
			left = mid

		mid = int((left+right)/ 2)

		cnt += 1

	print("number not found")
	return cnt


if __name__ == '__main__':
	array = [int(number) for number in input("Enter The Array:").split()]
	#array = [532 ,234 ,12 ,63 ,36 ,823 ,11 ,77 ,742 ,57]
	array.sort()

	print("Sorted Array-->",array)
	# number = 11 
	number = int(input("Enter the number to search:"))
	print("Number of Comparisions required %d"%binarySearch(array,number))