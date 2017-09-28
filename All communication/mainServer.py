import sys
import time
import Queue
import threading
from pc_communication import *
from bt_communication import *
#from sr_communication import *



__author__ = 'Sim Long Siang'

action_status =  " "
explored_map = " "
explored_obstacles = " "
movement = " "
robot_pos_dir = " "
is_complete = " "
way_point = " "
sensor_info =" "
terminated = 0

class Main(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

        self.pc_thread = PcAPI()
        print("PC - PC thread created.")
	self.bt_thread = BluetoothAPI()
        print("BT - Bluetooth thread created.")
	#self.sr_thread = SerialAPI()

	# Initialize the connections
        self.pc_thread.init_pc_comm()
        print("PC - PC connected completed.")
	self.bt_thread.connect_bluetooth()
	print("BT - Bluetooth connected completed.")
	#self.sr_thread.connect_serial()
        time.sleep(1)	# wait for 1 secs before starting


################ PC Functions #####################################

    def writePC(self, msg_to_pc):
    # Write to PC. Invoke write_to_PC()
    
        print ("PC - Inside writePC")
        #while True:
            #msg_to_pc = raw_input("Enter text: ")
        self.pc_thread.write_to_PC(msg_to_pc)
            #print "WritePC: Sent to PC: %s" % msg_to_pc

    def readPC(self):
    # Read from PC. Invoke read_from_PC() and send
    # data according to action status

        print ("PC - Inside readPC")
        while True:
            read_pc_msg = self.pc_thread.read_from_PC()
            #print(read_pc_msg)
            self.writeBT(read_pc_msg)
    
##            pc_msg = read_pc_msg.split("|")
##            action_status = pc_msg[0]
##            explored_map = pc_msg[1]
##            explored_obstacles = pc_msg[2]
##            movement = pc_msg[3]
##            robot_pos_dir = pc_msg[4]
##            is_complete = pc_msg[5]
##
##            # Check action_status for destination
##            # Action_status: EX, TE, FP, MV(Move_robot), SS(sensor_info), DONE
##
##            if(action_status.lower() == 'ex'):		# send to all
##                
##                #self.writeSR(read_pc_msg[1:])
##                ToAndroid = []
##                ToAndroid.extend([action_status, explored_map, explored_obstacles, robot_pos_dir])
##                Android_Msg= "|".join(ToAndroid)
##                self.writeBT(Android_Msg)
##                #print ("PC send to Android : %s" % Android_Msg)
##
##		ToArduino = []
##		action_status = "MV"
##                ToArduino.extend([action_status, movement])
##                Arduino_Msg= "|".join(ToArduino)
##                print ("PC send to Arduino : %s" % Arduino_Msg)

##
##            #if(action_stat.lower() == 'fp'):		# send to all
##                #self.writeBT(read_pc_msg[1:])
##                #self.writeSR(read_pc_msg[1:])
##                #ToAndroid = []
##                #ToAndroid.extend([action_stat, ex_map, ex_obs, position])
##                #Android_Msg= "|".join(ToAndroid)
##                #print ("PC send to Arduino : %s" % movement)
##                #print ("PC send to Android : %s" % Android_Msg)
##
##            #if(action_stat.lower() == 'te'):		# send to all
##                #self.writeBT(read_pc_msg[1:])
##                #self.writeSR(read_pc_msg[1:])
##                #ToAndroid = []
##                #ToAndroid.extend([action_stat, ex_map, ex_obs, position])
##                #Android_Msg= "|".join(ToAndroid)
##                #print ("PC send to Arduino : %s" % movement)
##                #print ("PC send to Android : %s" % Android_Msg)

################### Android/BT functions ###################################

    def writeBT(self, msg_to_bt):
        #Write to BT. Invoke write_to_bt()
        print ("BT - Inside writeBT")
        #while True:
            #msg_to_bt = raw_input("RPI: ")
        self.bt_thread.write_to_bt(msg_to_bt)
            #print ("Value sent to Android: %s" % msg_to_bt)

    def readBT(self):
        #Read from BT. Invoke read_from_bt() and send data to PC
        print ("BT - Inside readBT")
        while True:
            read_bt_msg = self.bt_thread.read_from_bt()
##          #print(read_bt_msg)
            self.writePC(read_bt_msg)
##            bt_msg = read_bt_msg.split("|")
##            action_status = bt_msg[0]
##            robot_pos_dir = bt_msg[1]
##            # Check header and send to arduino
##            if(action_status.lower() == 'ex'):	# send to PC
##                # Construct string to send to Arduino
##                action_status = 'SS'
##                command = action_status + "|"
##                self.writeSR(command)
##
##            elif(action_status.lower() == 'te'):
##                # Construct string to send to Arduino
##                terminated = '1'

#################### Serial Comm functions ##################################

##    def writeSR(self, msg_to_sr):
##        # Write to Serial. Invoke write_to_serial()
##	   self.sr_thread.write_to_serial(msg_to_sr)
##       #print ("Message sent to arduino: %s" % msg_to_sr)
##
##    def readSR(self):
##        # Read from SR. Invoke read_from_serial() and send data to PC
##	   print ("Inside readSR")
##       while True:
##           print ("Inside readSR")
##           try:
##               read_sr_msg = self.sr_thread.read_from_serial()
##               sr_msg = read_sr_msg.split("|")
##		# Write straight to Bluetooth and PC without any checking
##		# self.writeBT(read_sr_msg)
##		# self.writePC(read_sr_msg)
##                # print ("Value received from arduino: %s" % read_sr_msg)
##                # time.sleep(1)
##
##	# Remember to comment this out and use direct communication with PC
##
##	# Check header and send data to PC
##                if(sr_msg[0].lower() == 'ss'):	# sensor info send to PC
##                    sensor_info = sr_msg[1]
##                    if (terminated == 1):
##                        action_status = "TE"
##                    else:
##                        action_status = "EX"
##                    ToPC = []
##                    ToPC.extend([action_status, robot_pos_dir, sensor_info, way_point])
##                    PC_Msg= "|".join(ToPC)
##                    self.writePC(PC_Msg)
##                    print ("Sensor_info written to PC from SR: %s" % PC_Msg)
##
##                elif(sr_msg[0].lower() == 'done'):	# movement is completed
##        		    action_status = "SS"
##        		    self.writeSR(action_status + "|")
##        		    print ("Movement completed. Sending Sensor_Info." )
##                else:
##                    print ("incorrect header received from SR: [%s]" % sr_msg[0])
##                    time.sleep(1)
##            except serial.serialutil.SerialException:
##                pass

####################### Thread Initialization ################################################

    def initialize_threads(self):

	# PC read and write thread
        rt_pc = threading.Thread(target = self.readPC, name = "pc_read_thread")
	# print "created rt_pc"
        wt_pc = threading.Thread(target = self.writePC, args = ("",), name = "pc_write_thread")
	# print "created wt_pc"

	# Bluetooth (BT) read and write thread
    	rt_bt = threading.Thread(target = self.readBT, name = "bt_read_thread")
	# print "created rt_bt"
	wt_bt = threading.Thread(target = self.writeBT, args = ("",), name = "bt_write_thread")
	# print "created wt_bt"

	# Serial (SR) read and write thread
	# rt_sr = threading.Thread(target = self.readSR, name = "sr_read_thread")
	# print "created rt_sr"
	# wt_sr = threading.Thread(target = self.writeSR, args = ("",), name = "sr_write_thread")
	# print "created wt_sr"


	# Set threads as daemons
        rt_pc.daemon = True
        wt_pc.daemon = True

	rt_bt.daemon = True
	wt_bt.daemon = True

	#rt_sr.daemon = True
	#wt_sr.daemon = True

        print ("All threads initialized successfully\n")


	# Start Threads
        rt_pc.start()
        wt_pc.start()

	rt_bt.start()
	wt_bt.start()

	#rt_sr.start()
	#wt_sr.start()

        print ("Starting rt and wt threads\n")


    def close_all_sockets(self):
    # Close all sockets

        pc_thread.close_all_pc_sockets()
	bt_thread.close_all_bt_sockets()
	#sr_thread.close_all_sr_sockets()
        print ("end threads\n")

    def keep_main_alive(self):
    	# function = Sleep for 500 ms and wake up.
    	# Keep Repeating function
    	# until Ctrl+C is used to kill
    	# the main thread.
        while True:
		#suspend the thread
            time.sleep(0.5)


if __name__ == "__main__":
	mainThread = Main()
	mainThread.initialize_threads()
	mainThread.keep_main_alive()
	mainThread.close_all_sockets()
