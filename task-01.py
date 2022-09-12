"""
Write a function that returns the letter grade based on an input number grade.
This is a simple if statement.
If x is greater than or equal to 90 return A and so on.
Write the function and demonstrate that it works with by running it.
Add assert statement after your demonstration to show how you can test something.
"""

def number_to_letter(grade):
    if grade >= 90 :
        return "A"
    elif 90 > grade >= 80 :
        return "B"
    elif 80 > grade >= 70 :
        return "C"
    elif 70 > grade >= 60 :
        return "D"
    else :
        return "F"

test = number_to_letter(90)
print(test)

assert number_to_letter(90) == "A", "90 should be an A"