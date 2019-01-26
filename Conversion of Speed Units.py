# The Speed Units Converter!

def ms_to_kmph(m, sec):
  the_speed = (m / sec) * 3.6  
  if sec == 1:
    return str(m) + " metres per second is the same as " + str(the_speed) + " kmph"
  else:
    return str(m) + " metres per " + str(sec) + " seconds (i.e. " + str(m / sec) + " m/s) is the same as " + str(the_speed) + " kmph"

def kmph_to_ms(km, hr):
  metres = km * 1000
  timesec = hr * 3600
  object_speed = str(metres / timesec)
  
  if hr == 1:
    return str(km) + " kmph is the same as " + object_speed + " m/s"
  else:
    return str(km) + " km per " + str(hr) + " hours (i.e. " + str(km / hr) + " kmph) is the same as " + str(object_speed) + " m/s"
    
units = input("Please enter the units you want to convert ('kmph' or 'ms'): ").lower()
speed_dis_units = input("Enter the numerator of the speed that you wish to convert: ")
speed_time_units = input("Enter the time of the denominator that you wish to convert (default is 1): ")
  
try:
  val = float(speed_time_units)
except ValueError:
  speed_time_units = 1
  
try:
  value = int(speed_dis_units)
except ValueError:
  print ("\nYour distance value is not a number. Please try again.")
else:
  if units == "m/s" or units == "ms":
    print ("\n" + ms_to_kmph(float(speed_dis_units), float(speed_time_units)))

  elif units == "kmph":
    print ("\n" + kmph_to_ms(float(speed_dis_units), float(speed_time_units)))
    
  else:
    print ("\nI can't understand what units you entered.")