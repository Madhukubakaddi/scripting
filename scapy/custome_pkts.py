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

class VNTAG(Packet): 
   name = "VNTAG" 
   fields_desc =  [ BitField("dir", 0, 1), 
                    BitField("ptr", 0, 1), 
                    BitField("dst_vif", 0x123, 14), 
                    BitField("l", 0, 1),
                    BitField("rsvd", 0, 1), 
                    BitField("ver", 0, 2), 
                    BitField("src_vif", 0, 12) ] 
   
class ETAG(Packet): 
   name = "ETAG" 
   fields_desc =  [ BitField("pcp", 0, 3), 
                    BitField("de", 0, 1), 
                    BitField("svid", 0x123, 12), 
                    BitField("rr", 0, 2),
                    BitField("vid", 0, 14)]    

label = MPLS()
print hexdump(str(a))
