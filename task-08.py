"""
Write a function that computes the average of numbers input by the user and displays the average, minimum, maximum and the numbers in a nice format (using print statement).
"""


user_input = input("please insert your numbers seperated by comma")    # ask the user to insert inputs with explain message 

def avg_min_max(user_input):                                           # define new funtion , function name : avg_min_max , Parameter : user_input
    str_list = user_input.split(",")                                   # covert the user input from string to list of strings
    int_list = [int(i) for i in str_list ]                             # covert the user input from list of strings to list of integers
    print("Your number list is ", int_list)                            # diplay the user input numbers
    average = sum(int_list)/len(int_list)                              # calculate the average of the user input numbers
    print("Average = ", average)                                       # display the average of the user input numbers
    print("Minimum value = ", min(int_list))                           # find and display the minimum between the user input numbers
    print("Maximum value = ", max(int_list))                           # find and display the maximum between the user input numbers


avg_min_max (user_input)                                               # run the function
