
def bubble_sort(array):
	pointer1 = 0
	pointer2 = 1
	end = len(array)
	
	while end > 0: 

		for i in range(0, len(array)):

			while pointer1 < len(array) and pointer2 < len(array):
				# for i in range(0, len(array)):
				if array[pointer1] <= array[pointer2]:
					pointer1 += 1
					pointer2 += 1
				elif array[pointer2] < array[pointer1]:
					array = swap(array, pointer1, pointer2)
					pointer1 += 1
					pointer2 += 1
			# import pdb; pdb.set_trace()
			pointer1 = 0
			pointer2 = 1
			end -= 1
	return array

def swap(array, pointer1, pointer2):
	temp = array[pointer1]
	array[pointer1] = array[pointer2]
	array[pointer2] = temp
	
	return array

if __name__ == "__main__":
	array = [5, 4, 1, 3, 7, 6, 9, -2, 13, 2]
	sorted_array = 	bubble_sort(array)
	print array
	print "Sorted array: {}".format(sorted_array)
