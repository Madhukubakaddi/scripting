#!/tools/bin/python
# Program to extract the portion of the string after the colon

str = 'X-DSPAM-Confidence: 0.8475'
colon_pos = str.find(':')
#extract till end of string
num = str[colon_pos + 1:]
num = num.lstrip()
print float(num)

#Program to extract the date of mailing
str = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
if @ in str:
  at_pos = str.find('@')
  #Start searching for space from the postion of '@'
  sp_pos = str.find(' ',at_pos)
  date = str[sp_pos+1:]
