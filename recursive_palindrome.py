import unittest

def is_palindrome(some_string):

    if len(some_string) == 1:
        return True
    else:
        lst = list(some_string)
        if lst[0]==lst[-1]:
            lst.pop(-1)
            lst.pop(0)
            some_string = "".join(lst)
            # import pdb; pdb.set_trace() 
            return is_palindrome(some_string)
        else:
            return False 

class IsPalindromeTest(unittest.TestCase):
    TEST_DATA = [
    ("hello", False),
    ("a", True),
    ("aba", True)
    ]

    def test_palindrome(self):
        for str_, expected_result in self.TEST_DATA:
            test_result = is_palindrome(str_)
            self.assertEqual(test_result, expected_result)

if __name__=="__main__":
    unittest.main()
    # res = is_palindrome('oho')
    # print res