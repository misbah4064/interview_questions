from random import randint

def create_array(size, max):
	array = []
	for i in range(size):
		array.append(randint(0,max))
	return array

def nbubble_sort(array,n): #n.k
	l = len(array)
	greatest_array = []
	for i in range(n):     # n
		for j in range(l-i-1):    # length of the array l
			if array[j+1] < array[j]:
				temp = array[j]
				array[j] = array[j+1]
				array [j+1] = temp
	print(array)
	i = l-1
	while i >l-n-1:
		greatest_array.append(array[i])
		i -= 1
	return greatest_array

def nMerge_sort(array,n): #nlogn
	array.sort()
	l = len(array)
	greatest_array = []
	i = l-1
	while i >l-n-1:
		greatest_array.append(array[i])
		i -= 1
	return greatest_array

qArray = create_array(10,100)
print("Question")
print(qArray)
print("using Bubble Sort")
print(nbubble_sort(qArray,3))
print("using Merge Sort")
print(nMerge_sort(qArray,3))