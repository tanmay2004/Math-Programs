# The GEB Sequence Printer

geb_seq = [1, 3]
diff_seq = [2]

print("What is a GEB Sequence?\n")
print("The GEB sequence 1, 3, 7, 12, . . . is defined by the following properties:")
print("(a) The GEB sequence is increasing (that is, each term is larger than the previous term)")
print("(b) The sequence formed using the differences between each pair of consecutive terms in the GEB sequence (namely, the sequence 2, 4, 5, . . .) is increasing too")
print("(c) Each positive integer that does not occur in the GEB sequence occurs exactly once in the sequence of differences in (ii)\n")

stopTermNum = input("Please enter your number (it should be more than 2): ")
print("")

if stopTermNum != "":
  stopTermNum = int(stopTermNum)
  
  while (len(geb_seq) < stopTermNum):
    
    if diff_seq[-1]+1 not in geb_seq:
      geb_seq.append(geb_seq[-1] + diff_seq[-1] + 1)
      
    else:
      geb_seq.append(geb_seq[-1] + diff_seq[-1] + 2)
      
    diff_seq.append(geb_seq[-1] - geb_seq[-2])
    
  for term in geb_seq:
    print(str(term))
  
  print("\nThus, the above are the first " + str(stopTermNum) + " terms occurring in the GEB Sequence!")
  
else:
  print("Please enter a positive integer only. Try again!")