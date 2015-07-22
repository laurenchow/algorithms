import unittest

def find_missing_num(N, i):

 	num_list = i

	for i in range(0, N-2):
		diff_first_two = num_list[i+1]-num_list[i]
		diff_second_two = num_list[i+2]-num_list[i+1]

		if diff_first_two != diff_second_two:
			if diff_first_two > diff_second_two:
				common_difference = diff_second_two
				missing_element = num_list[i] + common_difference
			elif diff_first_two < diff_second_two:
				common_difference = diff_first_two
				missing_element = num_list[i+1] + common_difference

 	return missing_element

class FindMissingElement(unittest.TestCase):

	TEST_DATA = [
	(5, [3, 5, 7, 9, 13], 11),
	(4, [1, 3, 7, 9], 5),
	(4, [1, 3, 5, 9], 7),
	(5, [1, 9, 13, 17], 5),
	(8, [3, 5, 7, 9, 11, 13, 15, 19], 17 )
	] 

	def find_missing_element(self):
		for length, num_lst, expected_result in self.TEST_DATA:
			test_result = find_missing_num(length, num_lst)
			self.assertEqual(test_result, expected_result)

if __name__=="__main__":
	unittest.main()