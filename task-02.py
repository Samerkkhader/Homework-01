"""
Take generic input with the input command.
Use an if statement to write a function that returns “Lamar is a great school” if the sentence passed has the word Lamar. 
"""

def Lamar_finder(user_input):                              # define new funtion , function name : Lamar_finder , Parameter : user_input
    if "Lamar" in user_input or "lamar" in user_input :    # adding if statment with the condition if ("Lamar" or "lamar") found in the function argument
        return "Lamar is a great school"                   # return "Lamar is a great school" if the value of if statment condition was true


print(Lamar_finder(input()))                               # run the funtion




# Another way to type the if statment
# if user_input.find("Lamar") != -1 or user_input.find("lamar") != -1 :