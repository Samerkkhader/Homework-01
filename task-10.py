"""
Find the greatest common divisor between two numbers.
Write a function.
Make sure to put error checking in the function.
Both numbers must be positive integers for the function to work.
"""


def gcd (number_1, number_2):                                                                   # define new funtion , function name : gcd , Parameters : number_1, number_2                    
    if number_1 > 0 and type(number_1) == int and number_2 > 0 and type(number_2) == int :      # adding if statment to verify that both numbers are positive integers 
        smaller = min(number_1 ,number_2)                                                       # finding the smaller number between both inputs
        for i in range(1, smaller+1):                                                           # loop statement within the range of (from 1 to the smaller number itself)
                                                                                                # Note that if we write smaller alone, the loop cycle will finish at (smaller-1)
            if number_1 % i == 0 and number_2 % i == 0 :                                        # if the loop find a case where the remainder of division over the iterator equal zero for both numbers at the same time 
                gcd = i                                                                         # then the greatest common divisor = the iterator
        return gcd 
    else:                                                                                       # the function will return reatest common divisor value
        print("both numbers must be positive integers")                                         # print this error message in case on or both numbers are not positive integers 

print(gcd(10,16))                                                                               # run the function on 10,16 as test
