import sys

def prime_number(num):
  if num > 1:
    
    if num == 2:
      return True
    
    elif num % 2 == 0:
      return False
    
    else:
      half = (num / 2)
      if half > 2:
        for n in range(2, int(half)):
          remainder = num % n
          if remainder == 0:
            return False
        
        return True
      
      else:
        return True
  
  else:
    return False

def is_float(x):
  if float(x) - int(float(x)) != 0:
    return True
  
  else:
    return False

print ("Welcome to the COUNTING Machine!")
print ("To exit, press Ctrl + C at any time. \n")
done = False

while done == False:
  number_of_nums = 0
  type = input("Choose the type of counting you want to do ('p' for prime, 's' for squares, 'c' for cubes , 'b' for binary and 'n' for normal): ").lower()
  input_first_number = input("Please enter the number you wish to start from (default number is 0): ")
  input_last_number = input("Please enter the number you wish to end at: ") 

  if input_first_number == "":
    input_first_number = 0
    
  if input_last_number == "":
    print ("\nYou did not enter any number. Please try again.")
    continue
  
  if is_float(input_first_number) == True:
    input_first_number = float(input_first_number) 

  else: 
    input_first_number = int(float(input_first_number))
    
  if is_float(input_last_number) == True:
    input_last_number = float(input_last_number) 

  else: 
    input_last_number = int(float(input_last_number))
    
  if int(input_first_number) > int(input_last_number):
    print ("\nThe first number you entered is more than the second number. Please try again.")
    
  elif is_float(input_first_number) == True or is_float(input_last_number) == True:
    print ("One of the numbers you entered is a decimal. Please try again. \n")
  
  elif type == "s" or type == "squares" or type == "c" or type == "cubes":
    if type == "s" or type == "squares":
      thing = "perfect squares"
      power_num = 2
      
    else:
      thing = "perfect cubes"
      power_num = 3
    
    if int(input_first_number) < 0:
      print ("\nPlease enter a whole number.")
      continue

    if int(input_first_number) == 0:
      input_first_number = 1
      
    print ()
    nums = 0
    
    for i in range(int(input_first_number), int(input_last_number) + 1):
      if i ** power_num <= int(input_last_number):
        print (i ** power_num)
        nums += 1
      
    print ("\nCounting Complete!")
    print ("Thus, there are", nums, thing, "between", input_first_number, "and", input_last_number, "\n")
  
  elif type == "normal" or type == "n":
    input_first_number = int(input_first_number)
    input_last_number = int(input_last_number)
    
    print () 
    for i in range(input_first_number, input_last_number + 1):
      print (i) 
    print ("\nCounting complete!")  
            
  elif type == "prime" or type == "p":
    print ()
    for num in range(int(input_first_number), int(input_last_number) + 1):
      if prime_number(num) == True:
        print (num) 
        number_of_nums += 1
    
    print ("\nCounting Complete!") 
    print ("Thus, between " + str(input_first_number) + " and " + str(input_last_number) + ", there are " + str(number_of_nums) + " prime number(s). \n")
  
  elif type == "binary" or type == "b":
    if int(input_first_number) < 0:
      print ("I can't find binary numbers for negatives. Please enter a whole number. \n")
      continue
      
    else:
      for num in range(int(input_first_number), int(input_last_number) + 1):
        print (num, ">>>", bin(num)[2:]) 
      print ("\nCounting Complete!")
  
  else:
    print ("\nI can't understand the counting type you entered. Please try again. \n")
  
  again_or_not = input("To count again, press the 'enter' key: ")
  print () 
  if again_or_not != "":
    print ("You ended the game. Game Over!") 
    done = True