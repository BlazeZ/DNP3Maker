import binascii

def Detail():
    	try:
		print "Enter payload qualifer->range Field"
		payload = binascii.unhexlify(str(raw_input()))
		return payload
	except TypeError:
		return Detail()