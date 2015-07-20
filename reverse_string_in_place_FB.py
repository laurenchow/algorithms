def reverse_in_place(str_):

	#to print out string in reverse:
	print str_[::-1]

	#to reverse string in place:
	str_ = list(str_)

	for i in range(0, (len(str_)/2)+1):
		temp = str_[i]
		# import pdb; pdb.set_trace()
		str_[i] = str_[(len(str_)-i-1)]
		#to account for indices
		str_[(len(str_)-i-1)] = temp

	str_ = "".join(str_)
	return str_


if __name__=="__main__":
	str_=str(raw_input()).strip()
	res = reverse_in_place(str_)
	print res