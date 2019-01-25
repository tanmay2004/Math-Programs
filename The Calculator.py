# Sequence of Steps:
# 1. Used float_or_not function to determine whther any of the user inputted numbers are floats, otherwise they are made to exist as integers.
# 2. Checks which operation the user wants to perform on the numbers. 
# 3. User is told to try again if no comprehensible info is found.
# 4. Equation and Answer is printed
# 5. Same things continue happening until sign input is found to be "".

import sys
import ThePalendromeChecker as PalChecker
import operator
import math
import time
  
print ("This is The Basic Calculator! To exit, press Ctrl + C.")

def float_or_not(x):
  if float(x) - int(float(x)) != 0:
    return True
  else:
    return False
    
def powers(base, exponent):
  if sign == "root" or sign == "ro":
    return float(base) ** (1 / float(exponent))
  else:  
    return float(base) ** float(exponent)
 
exit = False
correct = False 

while correct == False: 
  chances = 5
  for i in range(5):
    palendrome_try = input("Please enter any palindrome to continue: ")
    print ("Processing....")
    time.sleep(1)

    if palendrome_try != PalChecker.reverse(palendrome_try): 
      chances -= 1
      if chances == 0:
        print ("You couldn't enter a palindrome. Game Over!")
        correct = True
        exit = True
        break
        
      else:
        print ("Incorrect Palindrome. You have", chances, "chances remaining. \n")
        
    else:
      print ("That is a palindrome! Please proceed. Happy Calculating!")
      correct = True
      break
    
while exit == False:
  print ()
  num_1 = input("Enter your first number: ")
  num_2 = input("Enter your second number: ")
  sign = input("Enter the operation you wish to perform (It can be (a)dd, (s)ubtract, (d)ivide, (m)ultiply, (re)mainder, (exp)onent or (ro)ot), press ENTER to exit: ").lower()
  print () 
  op = ""
  
  if sign == "":
    exit = True
      
  else:
    if float_or_not(num_1) == True:
      input_1 = float(num_1) 

    else: 
      input_1 = int(float(num_1))
      
    if float_or_not(num_2) == True:
      input_2 = float(num_2) 

    else: 
      input_2 = int(float(num_2))

    if sign == "multiply" or sign == "m":
      sign = operator.mul
      op = "x"
      
    elif sign == "divide" or sign == "d":
      sign = operator.truediv
      op = "/"
      
    elif sign == "subtract" or sign == "s":
      sign = operator.sub
      op = "-"
      
    elif sign == "add" or sign == "a":
      sign = operator.add
      op = "+"
      
    elif sign == "exp" or sign == "exponent":
      print (input_1, "to the power", input_2, "is", str(powers(input_1, input_2)))

    elif sign == "root" or sign == "ro":
      if input_2 == 2 or input_2 == 2.0:
        print ("The square root of", input_1, "is", powers(input_1, input_2))
      elif input_2 == 3 or input_2 == 3.0:
        print ("The cube root of", input_1, "is", powers(input_1, input_2))
      else:
        print ("The " + str(input_2) + "th root of " + str(input_1) + " is " + str(powers(input_1, input_2)))
    
    else:
      print ("You did not enter a valid operation name. Please try again.")
      
    if op == "+" or op == "-" or op == "x" or op == "/":  
      try:
        print ("Equation:", input_1, op, input_2, "=", sign(input_1, input_2))
      
      except ZeroDivisionError:
        print ("No number can be divided by zero. The answer is 'not defined'. Please try again.")
        continue
      
      except:
        print ("Unexpected error:", sys.exc_info()[0], "Please try again.")  
        continue
      
      if op == "/":
        print ("The quotient and remainder of this problem is", math.floor(sign(input_1, input_2)), "and", input_1 % input_2, "respectively. \n") 
        percent_or_not = input("Type 'p' to find the percentage, otherwise press ENTER: ").lower()
        
        if percent_or_not == "p" or percent_or_not == "percent":
          print ("The percentage of the numbers you entered is " + str((input_1 * 100) / input_2) + "%.") 

# There is problem if the user enters 3.0 instead of 3 - FIXED
# Next Plan: Converting decimal output into fraction if user wants.