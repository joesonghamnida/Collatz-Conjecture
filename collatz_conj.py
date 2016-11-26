#collatz conjecture program: n/2, 3n + 1

number = int(input("please enter a whole number greater than one: "))
number_list = []
max_number = 0
steps = 0

#loop to apply conjecture
while number > 1:
    test_number = number
    if (test_number % 2) == 0:
            number = number / 2
    else:
            number =  (3 * number) + 1
    if max_number <= number:
            max_number = number
    steps = steps + 1
    print (number)
    #section to store numbers in list, problem with this so far
    #number_list = number_list.append(number)

#end of loop    
print ("The number of steps required was ", steps)
print ("The greatest number reached was ", max_number)

#reverse conjecture, 2n, (n-1) / 3
print (number_list.reverse())
"""
number = int(input("Please enter a number you wish to find: "))
reverse = 1
steps = 0
#logic/runtime error, works fine for even numbers, not so much odd. probably breaks on zero too.
while reverse != number:
    test_reverse = reverse
    #gets us out of initial loop
    if test_reverse == 1:
        test_reverse = test_reverse * 2
    #initiates rest of loop
    if (test_reverse % 2) == 0:
        reverse = 2 * reverse
        if reverse > number:
            reverse = (reverse - 1) / 3
    else:
        reverse = (reverse - 1) / 3
    steps = steps + 1
    print (reverse)
print ("\nThe final product is ", reverse)
print ("The number of steps required to find the reverse number was ", steps)
"""    
