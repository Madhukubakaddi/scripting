#!/tools/bin/python
# Program to calculate overtime pay using conditional statements and try/except. More than 40hrs pay 1.5 times the pay 

hours = raw_input("Enter hours worked:")
rate  = raw_input("Enter pay per hour:")

try :
  hours = float(hours)
except :
   print "Invalid input for hours"
   
try :
  rate = float(rate)
except :
   print "Invalid input for rate"

if hours > 40 :
   pay = 40 * rate + (hours - 40) * (1.5 * rate)
else :
  pay = hours * rate
  
print "Your pay is:", pay
