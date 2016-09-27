#!/tools/bin/python
# Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.

input = raw_input("Enter a string:")
str_len = len(input)
   
# Using 'for' loop and positive indices
for char in input:
    print input[str_len-1]
    str_len = str_len -1


# Using 'for' loop and negative indices
idx = -1
for char in input:
    print input[idx]
    idx = idx -1

# Using 'while' loop and positive indices
while str_len > 0 :
      print input[str_len-1]
      str_len = str_len -1
      
      
# Using 'while' loop and negative indices
idx = -1
while str_len > 0 :
    print input[idx]
    idx = idx -1
    str_len = str_len - 1

# Using math module
import math
idx = -1
while math.fabs(idx) <= str_len -1:
    print input[idx]
    idx = idx -1
