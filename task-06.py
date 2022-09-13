"""
Write a function that computes the volume of a sphere when passed the radius.
Use an assert statement to test the function.
"""

def sphere_volume(radius):                       # define new funtion , function name : sphere_volume , Parameter : radius
    return (4/3) * (22/7) * (radius**3)          # the function calculate and return the value of the sphere volume
assert sphere_volume(5) == 523.8095238095237 , "the sphere volume for a sphere with radius 5 equal to 523.8095238095237"
# test the funtion with assert statment, if the test value was true, nothing will happen, if fales, the error messege "the sphere volume for a sphere with radius 5 equal to 523.8095238095237" will appear


print(sphere_volume(5))                          # run the function with radius value 5

