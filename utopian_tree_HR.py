# Enter your code here. Read input from STDIN. Print output to STDOUT

number_of_tests = raw_input()
number_of_tests = int(number_of_tests)

for i in range (0, number_of_tests):
    growth_cycles = raw_input()
    growth_cycles = int(growth_cycles)
    height = 1
    for i in range(1, growth_cycles+1):
        if i%2==0:
            height = height+1
        elif i%2!=0:
            height = height*2
   
    print height