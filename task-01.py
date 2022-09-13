"""
Write a function that returns the letter grade based on an input number grade.
This is a simple if statement.
If x is greater than or equal to 90 return A and so on.
Write the function and demonstrate that it works with by running it.
Add assert statement after your demonstration to show how you can test something.
"""

def number_to_letter(grade):                                   # define new funtion , function name : number_to_letter , Parameter : grade
    if grade >= 90 :                                           # adding if statment with the condition grade>=90
        return "A"                                             # in case the condition was true, the function will return "A"
    elif 90 > grade >= 80 :                                    # adding else if statment with the condition 90 > grade >= 80
        return "B"                                             # in case the condition was true, the function will return "B"
    elif 80 > grade >= 70 :                                    # adding else if statment with the condition 80 > grade >= 70
        return "C"                                             # in case the condition was true, the function will return "C"
    elif 70 > grade >= 60 :                                    # adding else if statment with the condition 70 > grade >= 60
        return "D"                                             # in case the condition was true, the function will return "D"
    else :                                                     # adding else statment if all the above condtions were fales
        return "F"                                             # in case the condition was true, the function will return "F"
assert number_to_letter(85) == "B", "85 should be an B"        # test the funtion with assert statment, if the test value was true, nothing will happen, if fales, the error messege "85 should be an B" will appear

test_grade = number_to_letter(90)                              # enter the value 90 as test argument to the funtion, and assign the funtion result to the variable test_grade    
print(test_grade)                                              # print the funtion test result