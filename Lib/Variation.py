import binascii

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