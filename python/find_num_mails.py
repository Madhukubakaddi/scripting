#!/tools/bin/python
# Program to find the name of the mailer and the number of mails each person sent using dictionary w/o 'get' function

mail = raw_input("Enter mail to analyse:")

mail_handler = open(mail,'r')
name_dict = {}

### Without the 'get' function
for line in mail_handler :
   if line.startswith("From:") :
      split_line = line.split()
      email = split_line[1]
      name = email.split('@')[0]
      if name in name_dict:
         name_dict[name] = name_dict[name] + 1
      else :
         name_dict[name] = 0

### Using the 'get' function
for line in mail_handler :
   if line.startswith("From:") :
      split_line = line.split()
      email = split_line[1]
      name = email.split('@')[0]
      name_dict[name] = name_dict.get(name,0) + 1

print name_dict
