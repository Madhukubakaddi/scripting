#!/tools/bin/python
# Program to count the occurrence of each word in a file

f_name = raw_input("Enter filename:")
try:
   f_handle = open(f_name,'r')
except :
   print "File does not exist"
   quit()

word_cnt = {}
for line in f_handle :
   words = line.split()
   for word in words :
      word_cnt[word] = word_cnt.get(word,0) + 1
    
print word_cnt
   
