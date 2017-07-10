import binascii

''' Source and Dest of the packet ''' 
def Source_Dest():
	Source = -1
	while Source > 65535 or Source < 0:
		print "Enter Source (0-65535)"
		Source = int(raw_input())

	Dest = -1
	while Dest > 65535 or Dest < 0:
		print "Enter Destination must be different than the source (0-65535)"
		Dest = int(raw_input())

	Dest = binascii.unhexlify(str(format(Dest, '#06x').replace("0x","")))
	"reverse the order"
	Dest = Dest[1:]+Dest[0:1]
	Source = binascii.unhexlify(str(format(Source, '#06x').replace("0x","")))
	"reverse the order"
	Source = Source[1:]+Source[0:1]
	return  Dest + Source
''''''