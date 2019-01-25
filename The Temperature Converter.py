# Celsius to Fahrenheit and vice versa
import operator

def c_to_f(the_temp):
  the_temp *= 9/5
  the_temp += 32
  return the_temp
  
def f_to_c(the_temp):
  the_temp -= 32
  the_temp *= 5/9
  return the_temp

def k_to_c_back(temp, the_op):
  ans = the_op(temp, 273.15)
  return ans
  
def k_to_f(temp): 
  temp_in_f = 9/5 * (temp - 273) + 32
  return temp_in_f
  
finish = False 
print ("This is the Temperature Converter!")

while finish == False:
  print ()
  to_convert = input("Enter what type of temperature you want to convert ('c' for celsius, 'f' for fahrenheit and 'k' for kelvin): ").lower()
  to_make = input("Enter what you want to convert the above type to: ").lower() 
  if to_convert == to_make:
    print ("You entered the same thing. Please try again.")
    continue
  
  temp_to_change = input("Enter the temperature you wish to convert, or press ENTER to exit: ")
  if temp_to_change == "":
    print ("\nGame Over!")
    finish = True
  
  else:
    try:
      val = float(temp_to_change)
    except ValueError:
      print ("\nPlease enter a number only.") 
      continue
      
    print ()    
    if (to_convert == "k" or to_convert == "kelvin") and (to_make == "f" or to_make == "fahrenheit"):
      print (str(temp_to_change) + " Kelvin converts to " + str(c_to_f(k_to_c_back(float(temp_to_change), operator.sub))) + "°F.")
      
    elif (to_convert == "k" or to_convert == "kelvin") and (to_make == "c" or to_make == "celsius"):
      print (str(temp_to_change) + " Kelvin converts to " + str(k_to_c_back(float(temp_to_change), operator.sub)) + "°C.")
      
    elif (to_convert == "f" or to_convert == "fahrenheit") and (to_make == "k" or to_make == "kelvin"):
      print (str(temp_to_change) + "°F converts to " + str(k_to_c_back(f_to_c(float(temp_to_change)), operator.add)) + " Kelvin.")
    
    elif (to_convert == "f" or to_convert == "fahrenheit") and (to_make == "c" or to_make == "celsius"):
      print (str(temp_to_change) + "°F converts to " + str(f_to_c(float(temp_to_change))) + "°C.")
    
    elif (to_convert == "c" or to_convert == "celsius") and (to_make == "k" or to_make == "kelvin"):
      print (str(temp_to_change) + "°C converts to " + str(k_to_c_back(float(temp_to_change), operator.add)) + " Kelvin.")
    
    elif (to_convert == "c" or to_convert == "celsius") and (to_make == "f" or to_make == "fahrenheit"):
      print (str(temp_to_change) + "°C converts to " + str(c_to_f(float(temp_to_change))) + "°F.") 
      
    else:
      print ("I can't understand what you entered. Please try again.") 