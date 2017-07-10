from Function import *
from Group import *
from Variation import *
from Qualifer import *
from CRC import * 
from Sequence import *
from AttackType import *
from Control import *
from Source import *
from CustomPayload import *
from Number import *
from Detail import *

''' the heart of the program ''' 
def custum_payload():
    #control of dnp3 function need works here
	'''
	try:
		control = dnp3_control()
	except TypeError:
		control = dnp3_control()
	'''
	data ,function_check, = dnp3_function()

	print "what user choose : " ,function_check
	if (function_check > 11 and function_check < 18) or function_check == 1:
		data = T_seq()  + A_seq() + data
	else:
		group_check = set_group(function_check-1)
		data += group_check
		#use for mutilpy run 
		
		nonSeqPayload = data + Variation(function_check-1,group_check) + qulifier_code(function_check-1,group_check) + num_item()
		data = T_seq()  + A_seq() + nonSeqPayload
	total_cnt = len(data) + 5
	header = "\x05\x64"+ chr(total_cnt)+"\xc4"+Source_Dest()
	packet = """%s%s%s%s""" % (header, struct.pack('>H', CRC16DNP().calculate(header)), data, struct.pack('>H', CRC16DNP().calculate(data)))
	return packet , header , nonSeqPayload
''''''

''' for fun '''
def custum_control():
	print "Enter control mode (192-196 and 201)"
	control = Num = int(raw_input())
	control =binascii.unhexlify(str(format(Num, '#04x').replace("0x","")))
	header = "\x05\x64"+ chr(5)+control+Source_Dest()
	packet = """%s%s""" % (header, struct.pack('>H', CRC16DNP().calculate(header)))
	return packet

''''''
