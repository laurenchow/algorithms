"""
Roy wanted to increase his typing speed for programming contests. So, his friend advised him to type the sentence "The quick brown fox jumps over the lazy dog" repeatedly, because it is a pangram. (Pangrams are sentences constructed by using every letter of the alphabet at least once.)

After typing the sentence several times, Roy became bored with it. So he started to look for other pangrams.

Given a sentence s, tell Roy if it is a pangram or not.

Input Format Input consists of a line containing s.

Constraints 
Length of s can be at most 10^3 and it may contain spaces, lower case and upper case letters. Lower case and upper case instances of a letter are considered the same.

Output Format Output a line containing pangram if s is a pangram, otherwise output not pangram.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import unittest

def pangram_checker(s1):

	pangram_result = False

	if len(s1)>=26:
	    
	    char_counter = {}
	    
	    #creates counter for all characters
	    for character in s1:
	        char_count = char_counter.get(character,0)+1
	        char_counter[character]=char_count
	    
	    #now check to see if all 26 letters are in the char_counter, if not it's not a pangram
	    if len(char_counter)==26:
	        for character in char_counter:
	            all_letters_checker = char_counter.get(character, -1) 
	            if all_letters_checker < 0:
	                return pangram_result
	            
	        #now you've checked entire string and it contains all 26 letters at least once
	        pangram_result = True
	        return pangram_result
	        
	    else:
	        return pangram_result
	else:
	    return pangram_result 

if __name__=="__main__":
	pangram_checker()