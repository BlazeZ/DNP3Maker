import binascii

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