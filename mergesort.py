
#base case 
def sort_array(array):
	#split array in half and return array recursively
	if len(array) == 1:
		# print array 
		return array

	else:
		array_length = int(len(array))//2
		#// floors it
		
		array1 = sort_array(array[0:array_length])
		array2 = sort_array(array[array_length:])

		sorted_array = merge(array1, array2)
		
	return sorted_array


# Runs in n log n

def merge(array1, array2):
	array1_counter = 0
	array2_counter = 0
	sorted_array = [] #sorted new/merged list
	while array1_counter < len(array1) or array2_counter <len(array2):
		if array1_counter >= len(array1):
			sorted_array.extend(array2[array2_counter:])
			array2_counter = len(array2)
			# import pdb; pdb.set_trace()
		elif array2_counter >= len(array2):
			sorted_array.extend(array1[array1_counter:])
			array1_counter = len(array1)
		elif array1[array1_counter] < array2[array2_counter]:
			sorted_array.append(array1[array1_counter])
			array1_counter += 1 
		elif array1[array1_counter] > array2[array2_counter]:
			sorted_array.append(array2[array2_counter])
			array2_counter += 1  

	# print sorted_array
	return sorted_array 

# Works but isn't most effective runtime

# def merge(array1, array2):
# 	sorted_array = []

# 	while array1 and array2:
# 		if array1 and not array2:
# 			sorted_array.extend(array1)
# 			array1 = []
# 		if array2 and not array1:
# 			sorted_array.extend(array2)
# 			array2 = []
# 		if array1[0] < array2[0]:
# 			sorted_array.append(array1[0])
# 			array1.pop(0) 
# 		elif array1[0] > array2[0]:
# 			sorted_array.append(array2[0])
# 			array2.pop(0)
			#deal with edge case of duplicates if not a distinct list

	# return sorted_array

if __name__ == "__main__":
	array = [5, 4, 1, 8, 12, 3, 9, 11] 
	sorted_array = sort_array(array)
	print sorted_array

