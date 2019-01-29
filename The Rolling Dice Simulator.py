import sys
import time

from random import randint

def random_num(dice_sides):
  return randint(1, dice_sides)

print ()
print ("Welcome to the Rolling Dice Simulator!")
ended = False
total_roll_sum = 0

while ended == False:
  num_dice_faces = input("Enter the number of sides you want your dice to have: ") 
  
  if float(int(float(num_dice_faces))) != float(num_dice_faces) or int(num_dice_faces) <= 0:
    print ("Please enter a natural number. \n") 
  
  elif num_dice_faces == "":
    print ("You did not enter anything. Please try again. \n")
    
  else:
    print ()
    roll_num = 0
    print ("To end game, type anything other than 'again' or you can simply press the 'enter' button. \n")
    
    while ended == False:
      again = input("To roll dice again, type 'again': ").lower()  
    
      if again == "again" or again == "a":
        the_num = random_num(int(num_dice_faces))
        roll_num += 1
        print ("Roll " + str(roll_num) + ": " + str(the_num))
        total_roll_sum += the_num
        print ()
        
      else:
        print ()
        
        if roll_num == 1:
          print ("Your total is " + str(total_roll_sum) + " and you rolled the dice 1 time.")
        else:  
          print ("Your total is " + str(total_roll_sum) + " and you rolled the dice " + str(roll_num) + " times.")
        
        print ("Your average roll was " + str(total_roll_sum / roll_num))
        print ("\nThank you for playing. Game Over!") 
        ended = True