#!/tools/bin/python
# Program to illustrate class, class attributes,methods and instances/objects of a class

class party():
  x = 5
  # 'self' acts like an reference/pointer to the instance/object. All the attributes of the class are stored with reference to self
  def __init__(self,name):
    self.name = name
    print "Party starts in %d seconds"%self.x
    
  def start(self):
    self.x = self.x -1
    print "%s party starts in %d seconds"%(self.name,self.x)
    
  def __del__(self):
     print "Party ends now"

# Creating two instances/objects of the same class, where state of each instance/object is maintained independently
birthday = party("birthday")
marriage = party("marriage")
# The below method call is can be interpreted as party.start(birthday)
birthday.start()
birthday.start()
marriage.start()
birthday.start()
