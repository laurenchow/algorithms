"""
Given a number N, return the number of primes within 1 to N.

"""

import math 
import unittest

def  getNumberOfPrimes( N):
    prime_counter = 1
    #we'll include 2 here for convenience so start loop at 3
   
    for num in range(3,N+1):
        prime = True 
        # if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
        if num % 2 != 0:
            #need to make it +1 because the int just cuts off the float so will not reflect
            #actual square root          
            for i in range(3, int(math.sqrt(num)+1), 2):
                if num % i == 0:
                    prime = False
                    break
            if prime==True: 
                prime_counter = prime_counter + 1        

    return prime_counter

class PrimeCounterTest(unittest.TestCase):
    TEST_DATA = [
    (100, 25),
    (1000, 168),
    (5, 3),
    (100000, 9592)
    ]

    def test_prime_counter(self):
        for num_, expected_result in self.TEST_DATA:
            test_result = getNumberOfPrimes(num_)
            self.assertEqual(test_result, expected_result)

if __name__=="__main__":
    unittest.main()