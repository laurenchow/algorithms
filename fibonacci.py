def fibonacci(fib_number):
	fib_number = int(fib_number)

	while fib_number>=0:
		if fib_number == 1:
			return 1
		elif fib_number == 0:
			return 0
		else:
			fibval = fibonacci(fib_number-2) + fibonacci(fib_number-1)
			print "Here's what fibval is now %r" % fibval	
			return fibval
			#you can memoize this

fibonacci(5)