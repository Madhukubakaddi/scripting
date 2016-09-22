#!/tools/bin/python
# Program to read user input of numbers, exit on 'Done' and return the average of numbers
# This program uses the following concepts learnt in class
# 1. print 2. variable assignment 3. 

def catch_error(num):
  try :
    num = float(num)
  except:
    print "Not a number"
    return
  return num

total = 0
count = 0
smallest = None
while True:
  num = raw_input("Enter number:")
  if num == 'Done':
    break
  if catch_error(num) is None :
    continue
  else :
    num = float(num)
    if smallest is None :
      smallest = num
    elif num < smallest :
      smallest = num
    total = total + num
    count = count + 1

print "Average is:", total/count
print "Smallest number is:", smallest
