#!/tools/bin/python
# Set log level to benefit from Scapy warnings
import logging
from scapy.all import *

logging.getLogger("scapy").setLevel(1)

class Test(Packet):
    name = "Test packet"
    fields_desc = [ ShortField("test1", 1),
                    ShortField("test2", 2) ]

def make_test(x,y):
    return Ether()/IP()/Test(test1=x,test2=y)

if __name__ == "__main__":
    interact(mydict=globals(), mybanner="Test add-on v3.14")
