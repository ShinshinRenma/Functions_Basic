"""
Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, 
from the number (as the 0th element) down to 0 (as the last element).
"""
# def countdown(num):
#    while(num>0):
#        print(num)
#        num -= 1

#countdown(5) 

"""
Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
Example: print_and_return([1,2]) should print 1 and return 2
"""

#def print_and_return(list):
#    print(list[0])
#    return list[1]

#x = print_and_return([1,2])
#print(x)

"""
First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
"""

#def first_plus_length(list):
#    return (list[0] + len(list))

#example = [5, 4, 3, 2, 1, 0]
#x = first_plus_length(example)
#print(x)

"""
Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from 
the original list that are greater than its 2nd value. Print how many values this is and then return the new list. 
If the list has less than 2 elements, have the function return False
"""

#def values_greater_than_second(list):
#    if(len(list)<2):
#        return False
#    print(list[1])
#    new_list = []
#    for x in range(0, (len(list)), 1):
#        if(list[x] > list[1]):
#            new_list.append(list[x])
#    return new_list

#example_list = [5,2,3,2,1,4]
#x = values_greater_than_second(example_list)
#print(x)

"""
This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and 
return a list whose length is equal to the given size, and whose values are all the given value.
"""

#def this_length_that_value(num1, num2):
#    new_list = []
#    for x in range (0, num1, 1):
#        new_list.append(num2)
#    return new_list

#y = this_length_that_value(10,3)
#print(y)