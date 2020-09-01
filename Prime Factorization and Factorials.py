# Finding All Prime Factors or the Factorial of a Number

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

def divisibility_check(dividend, divisor):
  return dividend % divisor == 0

def prime_factors(x):
  factors_list = []
  if prime_number(x) == True:
    return "You entered a prime number. So, its prime factorization is 1 x " + str(int(x))
    
  elif x > 1:
    # ALGORITHM:
    # 1. Think about each number till half of 'x'
    # 2. Check for each's divisibility by 'x' till no longer possible
    # 3. Each time, append it to the list
    # 4. In the end, sort through it and print it.
    # Thus, I must make a function to check the divisibility of any two numbers! >> DONE
    divided_x = x
    
    for i in range(2, int(x / 2) + 1):
      if prime_number(i) == True:
        while (divisibility_check(divided_x, i)):
          factors_list.append(str(i))
          divided_x = divided_x // i
          
    return "\nThe Prime Factorization of " + str(x) + " is " + ' x '.join(factors_list)
    
  elif x < 1:
    return "The number you entered can't be prime factorized. Please try again."
    
  else:
    return "You did not enter a number. Please try again."

def factorial(x):
  if x > 0:
    if x == 1:
      return 1
    else:
      return x * factorial(x - 1)

user_number = "Unknown"

while user_number != "":
  mode_type = input("Enter 'pf' to find the prime factorization of a number and 'f' to find the number's factorial: ").lower()
  user_number = input("Please enter your number (To exit, simply press ENTER): ")
  
  if user_number != "":
    the_number = int(user_number)
    
    if (mode_type == "factorial") or (mode_type == "f"):
      if the_number > 0:
        print ("\nThe factorial of " + str(the_number) + " is " + str(factorial(the_number)) + "\n")
      else:
        print ("The number you entered does not have a factorial.\n")
      
    elif (mode_type == "prime factorization") or (mode_type == "pf"):
      print (prime_factors(the_number) + "\n") 
      
    else:
      print ("I didn't understand what you entered. Please try again.\n")
      
  else:
    print ("You ended the game. Game Over!")
