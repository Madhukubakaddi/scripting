#!/tool/bin/python
#Program to illustrate class inheritance

class party():
   x = 0
   def __init__(self,name):
      self.name=name
      print self.name,"Party started"
   
   def welcome(self):
      self.x = self.x + 1
      print "Welcome %d person to %s party"%(self.x,self.name)
      
## The below class is inheriting all the attributes of the party class and adding more to it      
class birth(party):
    def cake(self):
       # We are able to invoke the welcome() method from the parent class
       self.welcome()
       print "cut the cake"

## This invokes the __init__()/constructor method from the parent method
abhi = birth('birthday')
abhi.cake()
