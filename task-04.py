"""
Sort a list of numbers using the sort function
And by code that you write yourself.
Please do a simple selection sort.

Find the minimum item on the original list and move to position 1
Repeat this until the list is sorted.
This algorithm is not effluent but is good for teaching.
If you can do this task you understand python lists and loops.
No need to place in a function.
Test on an example at least 5 integers in a list. 
"""



list = [5, 4, 3, 2, 1,]                                                   # creating a test list
list.sort()                                                               # sorting the test list using the build in sorting function in python 
print(list)                                                               # printing the list after sorting

def my_sort(list):                                                        # define new funtion , function name : my_sort , Parameter : list
    for i in range(len(list)):                                            # adding first iterator outer loop statment within the range of the list length
        minimum_index = i                                                 # set the first element as the minimum element
        for j in range(i+1, len(list)):                                   # adding second iterator inner loop statment within the range of first iterator plus 1 until the list length
            if list[j] < list[i]:                                         # compare the minimum with the second element. If the second element is smaller than the first, we assign it as a minimum
                minimum_index = j                                         # assign second element as minimum element
        list[i], list[minimum_index] = list[minimum_index], list[i]       # After each iteration, minimum element is swapped in front of the unsorted array   

my_sort(list)                                                             # run the funtion my_sort on the test list
print(list)                                                               # print the test result 