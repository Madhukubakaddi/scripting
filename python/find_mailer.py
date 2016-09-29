#!/tools/bin/python
#Program to find who sent the mail and how many mails were received

mail = raw_input("Enter mail to analyse:")

mail_handler = open(mail,'r')
name_lst = []
num_of_mail = 0
for line in mail_handler :
   if line.startswith("From:") :
      split_line = line.split()
      email = split_line[1]
      name = email.split('@')[0]
      name_lst.append(name)
      num_of_mail = num_of_mail + 1

print name_lst, num_of_mail
