#!/tools/bin/python
# Program to calculate Pay based on hours worked and pay per hour

hours = raw_input("Enter hours worked:")
rate  = raw_input("Enter pay per hour:")

hours = float(hours)
rate = float(rate)
pay = hours * rate
print "Your pay is:", pay
