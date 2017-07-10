import binascii

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