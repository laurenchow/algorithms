"""
Print fizzbuzz with as few letters as possible.
"""
import regex


#Solution 1:
# for i in range(1, 101):
#     if i%15==0:
#         print 'FizzBuzz'
#     elif i%5==0:
#         print 'Buzz'
#     elif i%3==0:
#         print 'Fizz'
#     else:
#         print i


#Solution 2:
for x in range(101):print'Fizz'*(x%3==0)+'Buzz'*(x%5==0) or x

# for x in range(101):print'Fizz'*(x%3==0)+'Buzz'*(x%5==0) or x) 
