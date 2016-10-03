#!/tools/bin/python
from scapy.all import *

# BitField - 1bit integer field
# ByteField - 1Byte integer field
# ShortField - 2Byte integer field
# IntEnumField - 4Byte integer field (Has enumerated values)
class MPLS(Packet): 
   name = "MPLS" 
   fields_desc =  [ BitField("label", 3, 20), 
                    BitField("cos", 0, 3), 
                    BitField("s", 1, 1), 
                    ByteField("ttl", 0)  ] 

bind_layers(Ether, MPLS, type=0x8847)

label = MPLS()
print hexdump(str(a))
