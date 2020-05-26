# array = [1,2,2,2,2,2,3]
array = [3,2,3]

def majorityElement_moore(array):
	result = None
	count = 0

	for num in array:
		if count == 0:
			result = num
			count = 1
		elif num == result:
			count += 1
		else:
			count -= 1
	return result

print ("majority element by moore: "+str(majorityElement_moore(array)))