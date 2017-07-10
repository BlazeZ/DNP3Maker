import struct
from CRC import * 

"constant"
sequenceT = 191
sequenceA = 191

''' sequence code for dnp3 '''
def T_seq():
	global sequenceT
	sequenceT = sequenceT + 1
	return hex(sequenceT)[2:].decode('hex')

def A_seq():
	global sequenceA
	sequenceA = sequenceA + 1
	#print (hex(sequenceA),"in hexadecimal.")
	return hex(sequenceA)[2:].decode('hex')
''''''
def update_seq(header,nonSeqPayload):
    	payload = T_seq() + A_seq() + nonSeqPayload
	packet = """%s%s%s%s""" % (header, struct.pack('>H', CRC16DNP().calculate(header)), payload, struct.pack('>H', CRC16DNP().calculate(payload)))
	return packet
