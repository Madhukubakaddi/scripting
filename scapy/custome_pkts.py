#!/tools/bin/python
from scapy.all import *

# BitField - 1bit integer field
# ByteField - 1Byte integer field
# ShortField - 2Byte integer field
# IntEnumField - 4Byte integer field (Has enumerated values)


# Layer2 headers
# TPID definitions for various tags
vntpid = 0x8838
etpid = 0x8839
cntpid = 0x8840

class VNTAG(Packet): 
   name = "VNTAG" 
   fields_desc =  [ BitField("dir", 0, 1), 
                    BitField("ptr", 0, 1), 
                    BitField("dst_vif", 0x123, 14), 
                    BitField("l", 0, 1),
                    BitField("rsvd", 0, 1), 
                    BitField("ver", 0, 2), 
                    BitField("src_vif", 0, 12)] 
bind_layers(Ether, VNTAG, type=vntpid)
   
class ETAG(Packet): 
   name = "ETAG" 
   fields_desc =  [ BitField("pcp", 0, 3), 
                    BitField("de", 0, 1), 
                    BitField("svid", 0x123, 12), 
                    BitField("rr", 0, 2),
                    BitField("vid", 0, 14)]  
   
bind_layers(Ether, ETAG, type=etpid)   
   
class CNTAG(Packet): 
   name = "CNTAG" 
   fields_desc =  [ ShortField("rpid", 0)]

bind_layers(Ether, CNTAG, type=cntpid)
   
class CNM(Packet): 
   name = "CNM" 
   fields_desc =  [ BitField("ver", 0, 4), 
                    BitField("rsvd", 0, 6), 
                    BitField("QntzFb", 0, 6), 
                    BitField("CPID", 0, 48),
                    ShortField("CNMQoffset", 0),
                    ShortField("CNMQDelta", 0),
                    BitField("DMAC", 0, 48),
                    ShortField("MSDUlen", 0)]  
class MiM(Packet): 
   name = "MiM" 
   fields_desc =  [ BitField("pcp", 0, 3), 
                    BitField("de", 0, 1), 
                    BitField("nca", 0, 1), 
                    BitField("ISID", 0,24)] 
   
bind_layers(Ether, MiM, type=0x88e7)

class MPLS(Packet): 
   name = "MPLS" 
   fields_desc =  [ BitField("label", 3, 20), 
                    BitField("cos", 0, 3), 
                    BitField("s", 1, 1), 
                    ByteField("ttl", 0)  ] 

bind_layers(Ether, MPLS, type=0x8847)


label = MPLS()
print hexdump(str(a))
