#!/tools/bin/python
#Program to make a list of unique words in a file

file_name=raw_input("Enter file name:")
fh = open(file_name,'r')

list = []
for line in fh :
   words = line.split()
   for word in words :
      if word in list :
         continue
      list.append(word)

list.sort()
print list
