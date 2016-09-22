#!/tools/bin/python
# Program to read user input of numbers, exit on 'Done' and return the average of numbers

def catch_error(num):
  try :
    num = float(num)
  except:
    print "Not a number"
    return
  return num

total = 0
count = 0
while True:
  num = raw_input("Enter number:")
  if num == 'Done':
    break
  if catch_error(num) is None :
    continue
  else :
    total = total + num
    count = count + 1

print "Average is:", total/count

