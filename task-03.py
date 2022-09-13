"""
Sum the numbers from 1 to 100 using a loop and the range statement
"""

total = 0                  # creating new variable (total) with initial value of zero 
for i in range(101):       # adding loop statment within the range of 101 since the range function counts until 100
    total = total + i      # the value of the iterator will be added to the variable (total) in repetitive way until the loop reach the last value of the range 100
print(total)               # printing the final value for the variable (total) after finishing the loop