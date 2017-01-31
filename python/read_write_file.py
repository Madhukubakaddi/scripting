#!/tools/bin/python
#Program to read a file and convert to uppercase and write to another file

file_name = raw_input("Enter file name:")

try:
  fh = open(file_name,'r')
except :
  print "File not found"
  quit()

file_write = open("shout.txt",'w')
for line in fh:
  line = line.upper()
  file_write.write(line)

file_write.close()
