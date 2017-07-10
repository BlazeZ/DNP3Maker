import binascii

''' set dnp3 control TODO: '''
def dnp3_control():
	try:
		print "Enter DNP3 control"
		control = binascii.unhexlify(str(raw_input()))
		return control
	except TypeError:
		return dnp3_control()

''''''
