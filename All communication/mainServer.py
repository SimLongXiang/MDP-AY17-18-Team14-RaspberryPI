import sys
import time
import Queue
import threading

from pc_communication import *


__author__ = 'Sim Long Siang'

class Main(threading.Thread):
    
    def __init__(self):
	threading.Thread.__init__(self)

	self.pc_thread = PcAPI()

	# Initialize the connections
	self.pc_thread.init_pc_comm()
	time.sleep(1)	# wait for 1 secs before starting


# PC Functions

    def writePC(self, msg_to_pc):
	"""
	Write to PC. Invoke write_to_PC()
	"""
        self.pc_thread.write_to_PC(msg_to_pc)
	#print "WritePC: Sent to PC: %s" % msg_to_pc

    def readPC(self):
	"""
	Read from PC. Invoke read_from_PC() and send 
	data according to header
	"""
	print ("Inside readPC")
	while True:
            read_pc_msg = self.pc_thread.read_from_PC()
            print (read_pc_msg)
            # Check header for destination and strip out first char
	    
            if(read_pc_msg[0].lower() == '0'):		# send to all
                #self.writeBT(read_pc_msg[1:])		# strip the header
                #self.writeSR(read_pc_msg[1:])	
		print ("text received from PC: %s" % read_pc_msg[1:])

	    elif(read_pc_msg[0].lower() == '1'):	# send to arduino
		#self.writeSR(read_pc_msg[1:])		# strip the header
		print ("value received from PC: %s" % read_pc_msg[1:])

	    elif(read_pc_msg[0].lower() == '2'):	# send to andriod
		#self.writeBT(read_pc_msg[1:])		# strip the header
		print ("value received from PC: %s" % read_pc_msg[1:])


	    else:
		print ("incorrect header received from PC: [%s]" % read_pc_msg[0])
	    #	time.sleep(1)
	    



    def initialize_threads(self):

        # PC read and write thread
	rt_pc = threading.Thread(target = self.readPC, name = "pc_read_thread")
	print "created rt_pc"
	wt_pc = threading.Thread(target = self.writePC, args = ("",), name = "pc_write_thread")
	print "created wt_pc"

	# Set threads as daemons
	rt_pc.daemon = True
	wt_pc.daemon = True
	print ("All threads initialized successfully")

	# Start Threads
        rt_pc.start()
	wt_pc.start()

	print "Starting rt and wt threads"


    def close_all_sockets(self):
	"""
	Close all sockets
	"""
	pc_thread.close_all_pc_sockets()
	print "end threads"

    def keep_main_alive(self):
	"""
	function = Sleep for 500 ms and wake up.
	Keep Repeating function 
	until Ctrl+C is used to kill
	the main thread.
	"""
	while True:
	    #suspend the thread  
	    time.sleep(0.5)


if __name__ == "__main__":
	mainThread = Main()
	mainThread.initialize_threads()
	mainThread.keep_main_alive()
	mainThread.close_all_sockets()	
