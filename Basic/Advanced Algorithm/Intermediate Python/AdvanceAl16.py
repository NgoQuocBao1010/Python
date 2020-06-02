def countInversions(arr):
	result = 0

	for index in range(len(arr) - 1):
		for index2 in range(index + 1, len(arr)):
			if arr[index] > arr[index2]:
				result += 1

	return result


print(countInversions([4, 6, 2, 9, 7, 14, 3, 8, 15]))