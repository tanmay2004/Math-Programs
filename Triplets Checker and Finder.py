import sys
from math import sqrt

print ("\nWelcome to the Pythagorean Triplet Finder and Checker! To exit, press Ctrl + C. \n")
find_or_check_again = ""

while find_or_check_again == "":
  find_or_check = input("Type 'find' to find the hypotenuse of a right triangle and 'check' to test if a triangle has a right angle or not: ").lower()
  if find_or_check == "check" or find_or_check == "find":
    print () 
    base = float(input("Please enter the base of your triangle: ")) 
    perpendicular = float(input("Please enter the perpendicular of your triangle: ")) 

    perpendicular_squared = perpendicular ** 2
    base_squared = base ** 2
    
    if find_or_check == "check":
      hypotenuse = float(input("Please enter the hypotenuse of your triangle: ")) 
      print () 
      
      if perpendicular > 0 and base > 0 and hypotenuse > 0:
        hypotenuse_squared = hypotenuse ** 2
        
        if base_squared + perpendicular_squared == hypotenuse_squared:
          print ("You entered " + str(int(base)) + ", " + str(int(perpendicular)) + " and " + str(int(hypotenuse)) + ". That is a Pythagorean Triplet! \n")
        else:
          print ("You did not enter a Pythagorean Triplet. \n") 
      
      else:
        print ("You entered an invalid value for the length of the side of a triangle. Please try again! \n")
       
    else:
      if find_or_check == "find":
        num = perpendicular_squared + base_squared
        maybe_hypotenuse = sqrt(num)
        
        if maybe_hypotenuse - int(maybe_hypotenuse) == 0:
          print ("According to the measurements that you entered, the hypotenuse of the triangle is " + str(int(maybe_hypotenuse)) + ". \n")
        
        else:
          print ("According to the measurements that you entered, the hypotenuse of the triangle is " + str(maybe_hypotenuse) + ". \n")
    
    find_or_check_again = input("To test or find for any other values, press the 'enter' key, to exit, type anything: ")
    
  else: 
    print ("You did not enter 'check' or 'find'. Please try again. \n") 