#!/tools/bin/python
#Count number of characters in string using function
input = raw_input("Enter the string:")
ch = raw_input("Enter the charater to be searched")

def cnt_char(string, char):
  str_len = len(string)
  cnt = 0
  for c in string :
    if c == char:
      cnt = cnt+1
  return cnt
  
cnt = cnt_char(input,ch)
print cnt
