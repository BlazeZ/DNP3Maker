
def send_dnp3_packet(the_sock=None, the_pkt='', pkt_id=0,sendOnly=False):
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