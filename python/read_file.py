#!/tools/bin/python
#Program to read a file and convert to uppercase 

file_name = raw_input("Enter file name:")

try:
  fh = open(file_name,'r')
except :
  print "File not found"
  quit()

for line in fh:
  line = line.upper().rstrip()
  print line
