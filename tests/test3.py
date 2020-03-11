import signal
from time import sleep

finish = False

def signal_handler(signal, frame):
	global finish
	finish = True

signal.signal(signal.SIGINT, signal_handler)

while (True):
	if finish:
		break
	print("1")
	sleep(2)
	print("2")
	sleep(2)
	print("3")
	sleep(2)
	print("finished...")