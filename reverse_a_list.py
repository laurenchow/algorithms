import unittest

def reverse(lst):
	lst = list(lst)
	size = len(lst)

	for i in range(0, size/2):
		temp = lst[i]
		lst[i]=lst[(len(lst)-1)-i] #you need to do (len(lst)-1) to address range so you start at last index, not count of size
		lst[(len(lst)-1)-i] = temp 
	
	print lst
	return lst

class TestReverseList(unittest.TestCase):
	TEST_DATA = [
		((1,2,3,4,5,6,7,8,9),[9,8,7,6,5,4,3,2,1]),
		((1,3,5,7,9),[9,7,5,3,1]),
		('alleyoop', ['p', 'o', 'o', 'y', 'e', 'l', 'l', 'a'])
		]

	def test_list_reversal(self):
		for test_list, expected_result in self.TEST_DATA:
			test_result = reverse(test_list)
			self.assertEqual(test_result, expected_result)

if __name__=="__main__":
	unittest.main()
