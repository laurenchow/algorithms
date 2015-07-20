import unittest

def palindrome_checker(str_):
	input_list = list(str_)
	is_a_palindrome = True

	for letter in range(len(input_list)):
		if input_list[letter]!=input_list[(len(input_list)-1)-letter]:
			is_a_palindrome = False
			return is_a_palindrome

	return is_a_palindrome
class TestPalindromeChecker(unittest.TestCase):

	TEST_DATA = [
	('anna', True),
	('hannah', True),
	('lizard', False),
	('hgygsvlfcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcflvsgygh', True)
	('uxxdlselxmwyiguugtpsypfudffsvwyswyyiiyywsywvsffdufpysptguugiywmxlesldxxu', True)
	]

	def test_is_palindrome(self):
		for str_, expected_result in self.TEST_DATA:
			str_ = str_.strip().replace(" ","").lower()
			test_result = palindrome_checker(str_)
			self.assertEqual(test_result, expected_result)

if __name__=="__main__":
	# unittest.main()
	str_=  str(raw_input("Type in a string: "))
	str_ = str_.strip().replace(" ","").lower()
	res = palindrome_checker(str_)
	print "This {} is a palindrome: {}".format(str_, res)


"""
	orig:
	uxxdlselxmwyiguugtpsypfudffswvwyswyyiiyywsywvsffdufpysptguugiywmxlesldxxu

	minus 44
	uxxdlselxmwyiguugtpsypfudffswvwyswyyiiyywsywsffdufpysptguugiywmxlesldxxu

	minus 28 
	uxxdlselxmwyiguugtpsypfudffsvwyswyyiiyywsywvsffdufpysptguugiywmxlesldxxu