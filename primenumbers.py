"""
Write a function that take an upper limit as a parameter and returns a list of prime numbers.
Put it in a module and use the function to generate all the prime number less than 200
"""


# creat new file and save it as primenumbers.py and save it in the same directory with other files

def check_prime(number):            # define new funtion , function name : check_prime , Parameter : number
    for i in range(2,number):       # adding iterator loop statment within the range (from 2 to the number)
                                    # The iterator should not include 1 and the number in the loop (refer to the definition of prime number )
        if (number % i) == 0:       # adding if statment to test dividing the number over the iterator cycle, if the loop find the remainder of division equal to zero, 
            return False            # which means the number can accept division over other numbers besides (1 and the number itself ), the function check_prime will return false 
            break                   # if the above condition happen, break the iterator cycle
    else:                           # else statment opposite to the for loop, in case the if loop finished without finding any remainder of zero 
        return True                 # the function check_prime will return true

def list_of_prime_numbers(upper_limit):
    # define new funtion , function name : list_of_prime_numbers , Parameter : upper_limit
    list_of_numbers = [j for j in range(3, upper_limit) if check_prime(j) == True] 
    # define new list named list_of_numbers and use loop with list comprehension within the range of ( from 3 to the argument of the function )
    # including if statment with the check_prime function we defined before
    print(list_of_numbers) 
    # print the output list after applying the new definded function list_of_prime_numbers

# save

