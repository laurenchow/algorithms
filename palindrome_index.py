"""
Problem Statement

You are given a string of lower case letters. Your task is to figure out the index of the character on whose removal it will make the string a palindrome. There will always be a valid solution. 

In case the string is already a palindrome, then -1 is also a valid answer along with possible indices.

Input Format

The first line contains T, i.e. the number of test cases.
T lines follow, each containing a string.

Output Format

Print the position (0 index) of the letter by removing which the string turns into a palindrome. For a string, such as

bcbc
we can remove b at index 0 or c at index 3. Both answers are accepted.

Constraints 
T is between 1 and 20
length of stirng is under 100000
All characters are Latin lower case indexed.

Sample Input

3
aaab
baa
aaa
Sample Output

3
0
-1
Explanation

In the given input, T = 3,

For input aaab, we can see that removing b from the string makes the string a palindrome, hence the position 3.
For input baa, removing b from the string makes the string palindrome, hence the position 0.
As the string aaa is already a palindrome, you can output 0, 1 or 2 as removal of any of the characters still maintains the palindrome property. Or you can print -1 as this is already a palindrome.

"""
# Enter your code here. Read input from STDIN. Print output to STDOUT

#first line is how many test cases you need to process
#following n lines are test cases
import unittest

def palindrome_index(n, input_string):
	current_list = list(input_string)
	list_length = len(current_list)
	#check to see if you need to increment length here
 
	#does this work if you halve the lenght of hte list
	for letter in range(list_length/2):

		if current_list[letter]!=current_list[(list_length-1)-letter]:
			if current_list[letter]==current_list[(list_length-2)-letter]:
				if current_list[letter+1]==current_list[(list_length-2)-letter]:
					index_to_remove = (list_length-1)-letter
					#this 28/44case falls in here actually
					return index_to_remove
				elif current_list[letter+1]==current_list[(list_length-3)-letter]:
					#this handles the baaabc case
					index_to_remove = (list_length-1)-letter
					return index_to_remove
				elif current_list[letter-1]==current_list[list_length-1-letter+1]:
					#this handles 28/44
					index_to_remove = letter
					return index_to_remove
			else:
		
				index_to_remove = letter
				return index_to_remove
	

	index_to_remove = -1
	        
	
	return index_to_remove

class PalindromeIndexTest(unittest.TestCase):
	TEST_DATA = [
	(1, 'aaab', 3),
	(1, 'baaabc', 5),
	(1, 'baa', 0),
	(1, 'aaa', -1),
	(1, 'fyjwtatuieusvfqaeynaaiiaanyeaqfvsueutatwjyf', 8),
	(1, 'llhrxcreddwkcronujfkwbdswoowsdbwkfjunorckwdderxrhll', 5),
	(1, 'qasfhkfcojhntlfkaydtepsfsleipymwsopposwmypielsfspetdykfltnhjocfkhfsaq', 16),
	(1, 'broifqivnnvifiorb', 5),
	(1, 'bglgcwnmpobohqefrglsaaaaslgrfeqhobopmnwcglgb', -1),
	(1, 'bthvmywukfwrkslaiialskwfkuwymvhtb', 11),
	(1, 'uxxdlselxmwyiguugtpsypfudffswvwyswyyiiyywsywvsffdufpysptguugiywmxlesldxxu', 28),
	(1, 'qaaiyrpadovfjrmgkildtkseysejdtrpltptujlxxljutptlprtdjesyeskdlikgmrjfvodapryiaaq', 20),
	(1, 'rvscdpyljqglgmiktfndsmfnkgmubrruloqptgohsgneocoyyocoengshogtpqolurrbumgknfmsdntkimglgqjlypdcsvr', 17),
	(1, 'qmdpbsswvmqtyhkobqeijjieqbokhytqmvwssbdmq', 3)
	]

	def test_palindrome_index(self):
		for n, str_, expected_result in self.TEST_DATA:
			test_result = palindrome_index(n, str_)
			print "Result for {} is remove {} index".format(str_, test_result)
			self.assertEqual(test_result, expected_result)

if __name__=="__main__":
	unittest.main()
	# n = int(raw_input("How many test cases? "))

	# for i in range(0, n):
	# 	input_string = str(raw_input("Type in a string to check: "))
	# 	input_string = input_string.strip().replace(" ","").lower()
	# 	res = palindrome_index(n, input_string)
	# 	print "You need to remove the {} index".format(res)    

    
