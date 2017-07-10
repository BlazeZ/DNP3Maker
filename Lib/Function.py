"Constant"
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