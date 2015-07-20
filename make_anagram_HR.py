def makeAnagram(s1, s2):
	s1 = s1.strip().replace(" ","").lower()
	s2 = s2.strip().replace(" ", "").lower()

	set_s1 = set(s1)
	set_s2 = set(s2)

	#identify common letters
	common_characters = set_s1.intersection(set_s2) 
 
	#this doesn't work because you don't account for the count of each character
	#so it will think hide and hidddeee are the same thing or l and llll 

	char_counter_s1 = {}

	#identify how many of each common letters are in each string
	for character in s1:
		char_count = char_counter_s1.get(character, 0) + 1
		char_counter_s1[character] = char_count

	char_counter_s2 = {}

	for character in s2:
		char_count = char_counter_s2.get(character,0) +1
		char_counter_s2[character]=char_count

	#identify which string has a smaller amount of common characters as that's what you'll need
	#to create the anagram (if one has 3 e's and one has 5, you can only use 3)

	count_shared_letters = 0

	for character in common_characters:
		common_count_s1 = char_counter_s1.get(character, 0)
		common_count_s2 = char_counter_s2.get(character, 0)
		if common_count_s2 > common_count_s1:
			count_shared_letters = count_shared_letters + common_count_s1
		elif common_count_s1 > common_count_s2:
			count_shared_letters = count_shared_letters + common_count_s2
		elif common_count_s1 == common_count_s2:
			count_shared_letters = count_shared_letters + common_count_s1

	deletions_to_make = (len(s1) - count_shared_letters) + (len(s2)-count_shared_letters)

	return deletions_to_make 


if __name__=="__main__":
	s1 = raw_input("Give me a string: ")
	s2 = raw_input("Give me another string: ")
	result = makeAnagram(s1, s2)
	print "You need to make {} deletions".format(result)