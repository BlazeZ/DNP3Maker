
import binascii


def num_item():
    	print "Enter the number of item"
	Num = int(raw_input())
	Num =binascii.unhexlify(str(format(Num, '#04x').replace("0x","")))
	#Num = Num[1:]+Num[0:1]
	return Num