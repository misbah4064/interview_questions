array = [2,-4,66,-27,11,6,-54,-87,12,56,96,16,18]
#array = [.........................66, 87, 96]

def maxProduct(array):
	array.sort()
	print(array)
	n = len(array)
	product = array[n-1]*array[n-2]*array[n-3]
	return product

def n_maxProduct(array):
	array.sort(reverse = True)
	return max(array[0]*array[1]*array[2],
		array[0]*array[-1]*array[-2])
print(array)
print("max product: "+str(maxProduct(array)))
print("max product: "+str(n_maxProduct(array)))






