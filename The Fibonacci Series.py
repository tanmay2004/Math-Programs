# Fibonacci Series

def is_float(x):
  if float(x) - int(float(x)) != 0:
    return True
  
  else:
    return False

def next_num(num_1, num_2):
  sum = num_1 + num_2 
  return sum
  
stop_asking = False

while stop_asking == False:
  all_nums_in_series = [1, 1]
  series_till_num = input("Please enter how many fibonacci numbers you want (Press ENTER to exit): ")

  if series_till_num == "":
    stop_asking = True 
    
  else:
    try:
      as_a_float = float(series_till_num)
    
    except ValueError:
      print ("You did not enter a number. Try again. \n")
      continue
    
    else:
      if is_float(series_till_num) == True:
        print ("You entered a decimal. Please try again. \n")
        
      else:
        print ()
        series_till_num = int(float(series_till_num))
        
        if series_till_num > 0:
          thing1 = 1
          thing2 = 1
          print (thing1)
          
          if series_till_num >= 2:
            print (thing2)
            for i in range(2, series_till_num):
              the_num = next_num(thing1, thing2)
              print (the_num)
              all_nums_in_series.append(the_num)
              thing1 = thing2
              thing2 = the_num
              
          print ("\nFibbonaci Series Complete!")
          print ("The average of the numbers in the above series is", (sum(all_nums_in_series) / len(all_nums_in_series)), "\n")
          
        else:
          print ("You can only enter a natural number. Please try again.")  