#!/usr/bin/python

import os

class gpio:
	
	def digitalWrite(self, pin, state):
		os.system('echo -n '+state+' > /sys/class/gpio/gpio'+pin+'/value')

	def analogRead(self, pin):
		data = open('/sys/bus/iio/devices/iio:device0/in_voltage'+pin+'_raw')	
		value = data.read()
		data.close()
		return value

	def playAudio(self, fileName):
		os.system('aplay '+fileName)