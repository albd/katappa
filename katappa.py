import RPi.GPIO as GPIO
import subprocess
from time import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN, GPIO.PUD_UP)
epoch = time()
state = 0

while 1:
	if GPIO.input(4) == False:
		epoch = time()	
		state = 0
	else:
		if (time() - epoch) > 300:
			if state == 0:
				state = 5
				subprocess.call(["sh","/home/pi/katappa/send_door_close_reminder"])



