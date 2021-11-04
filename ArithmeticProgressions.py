class ArithmeticProgression (object):  
  # Constructor
  def __init__(self, a, d):
    self.a = a
    self.d = d
    self.terms_list = [self.a]

  # Representation of object as a printable string
  def __repr__(self):
    return "This is an AP with first term as " + str(self.a) + " and the common difference as " + str(self.d)
    
  def addToSequence(self, num_terms):
    for x in range(num_terms):
      self.terms_list.append(self.terms_list[-1] + self.d)
  
  def getTermAtPos(self, pos_n):
    return self.a + self.d * (pos_n - 1)
    
  def getPosOfTerm(self, term):
    return int((term - self.a + self.d) / self.d)
    
  def contains(self, term):
    possible_pos = (term - self.a + self.d) / self.d
    return possible_pos == int(possible_pos)
  
  def getNextTerms(self, no_of_terms):
    answer = [self.terms_list[-1]]
    
    for x in range(no_of_terms):
      answer.append(answer[-1] + self.d)
      
    answer.pop(0)
    return answer
    
  def getSumNthTerm(self, n):
    return (n/2) * (2 * self.a + (n - 1) * self.d)
  
  def getTermSumSeq(self):
    return sum(self.terms_list)

# First term given as first param is automatically added to the series list
AP_new = ArithmeticProgression(1, 5)
print(AP_new) # runs __repr__

AP_new.addToSequence(90)
print("90 terms have been added to my sequence!\n")
print("Sum of terms till now is " + str(AP_new.getTermSumSeq()))
print("The term at position 1000 in my AP is " + str(AP_new.getTermAtPos(1000)))
print("The next five terms are " + str(AP_new.getNextTerms(5))) # Prints terms 92 to 96
print("Sum of terms till position 250 is " + str(AP_new.getSumNthTerm(250)))

check_num = input("\nEnter an integer: ")
int_check = int(check_num)

if AP_new.contains(int_check):
  print(check_num + " is at position " + str(AP_new.getPosOfTerm(int_check)) + " in my AP!")
else:
  print(check_num + " was not found in my AP!")
