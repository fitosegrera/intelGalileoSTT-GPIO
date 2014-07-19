#!/usr/bin/python
# -*- coding: utf-8 -*-

from gostt import gosttpy # From the file gostt.py import the class gosttpy 
from gpio import gpio
import subprocess
import time
import os
import subprocess, signal
import ast

galileo = gpio()
voiceCommand = gosttpy()

#----------------------------------------
#Infinite loop for reading the sensors
analog0Val = 0;
analog1Val = 0;
analog2Val = 0;
analog3Val = 0;

state = 0
stateMotion = 0
stateRecording = 0
stateAutoMode = 1
stateCurtain = 0
stateCurtain1 = 0
stateCurtainOC = 0
stateFan = 0
stateFan1 = 0
stateFanOnOff = 0

while state == 0:

	analog0Val = int(galileo.analogRead("0"))
	#print 'SENSOR 0: ' + analog0Val
	analog1Val = int(galileo.analogRead("1"))
	#print 'SENSOR 1: ' + analog1Val
	analog2Val = galileo.analogRead("2")
	#print 'SENSOR 2: ' + analog2Val
	analog3Val = galileo.analogRead("3")
	#print 'SENSOR 3: ' + analog3Val

	analog2ValInt = int(analog2Val)
	#arecordid = os.system('pgrep arecord')
	p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
	out, err = p.communicate()
	#----------------------------------------
	#Sensor Thresholds...
	gasThresh = 2000
	lightThresh = 900
	lightThresh1 = 800
	motionThresh = 1
	babyThresh = 1500

	'''
	#Evaluation of sensor states:
	#1.GAS-SENSOR and trigger for FAN
	if analog0Val > gasThresh:
		galileo.digitalWrite("26","0")
		#Read and play audio file
		galileo.playAudio("005.wav")
	else:
		galileo.digitalWrite("26","1")

	if analog1Val > lightThresh:
		galileo.digitalWrite("24","0")
		time.sleep(0.8)
		galileo.digitalWrite("24","1")
	'''
	def readButton():
		data = open('/www/pages/a.txt')	
		value = data.read()
		data.close()
		print value
		return value

	'''
	voiceButton = readButton()
	if voiceButton == "1":
		if stateMotion == 0:
			print "RECORDING..."
			os.system('arecord -f S16_LE -c 1 -r 16000 voice.wav &')
			stateMotion = 1
			stateRecording = 1
	'''		
	if analog2ValInt < 100:
		if stateMotion == 0:
			print "RECORDING..."
			os.system('arecord -f S16_LE -c 1 -r 16000 voice.wav &')
			stateMotion = 1
			stateRecording = 1

	else:
		stateMotion = 0
		if stateRecording == 1:
			#print arecordid
			#os.system('kill -9 arecord')
			for line in out.splitlines():
				if 'arecord' in line:
					pid = int(line.split(None, 1)[0])
					os.kill(pid, signal.SIGKILL)
			#print "NO!!!!"
			stateRecording = 0
			#subprocess.call('exit 1')
			#state = 0

			# Google API key for voice recognition
			#apiKey = 'AIzaSyDT34UUHcNJ6lDTkj4EegMMpDn3FHaTSwY'
			apiKey = 'AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw'  # Google API key for
			# voice recognition
			returnedValue = voiceCommand.voiceRecognition(apiKey)
			#print returnedValue
			
			commands = open('commands.txt', 'r').read()
			#commands = {'light on': 'XXXXX', 'light off': 'YYYYY'}
			dictionary = ast.literal_eval(commands)

			if returnedValue == dictionary["light on"]:
				galileo.digitalWrite("32","0")
			if returnedValue == dictionary["light off"]:
				galileo.digitalWrite("32", "1")
			if returnedValue == "open curtain":
				galileo.digitalWrite("27", "0")
				time.sleep(0.8)
				galileo.digitalWrite("27", "1")
				stateCurtainOC = 1
			if returnedValue == "close curtain":
				galileo.digitalWrite("24", "0")
				time.sleep(0.8)
				galileo.digitalWrite("24", "1")
				stateCurtainOC = 0
			if returnedValue == "open window":
				galileo.digitalWrite("17", "0")
				time.sleep(0.6)
				galileo.digitalWrite("17", "1")
			if returnedValue == "close window":
				galileo.digitalWrite("28", "0")
				time.sleep(0.6)
				galileo.digitalWrite("28", "1")
			if returnedValue == "fan on":
				galileo.digitalWrite("26", "0")
			if returnedValue == "fan off":	
				galileo.digitalWrite("26", "1")	

	#------------------------------------------
		
	#Curtain STATES
	if stateAutoMode == 1:
		if analog1Val > lightThresh:
			if stateCurtain == 0:
				if stateCurtainOC == 1:
					galileo.digitalWrite("24", "0")
					time.sleep(0.8)
					galileo.digitalWrite("24", "1")
					stateCurtain = 1
					stateCurtainOC = 0
					#stateCurtain1 = 0
		else:
			stateCurtain = 0
		if analog1Val < lightThresh1:
			if stateCurtainOC == 0:
				if stateCurtain1 == 0:
					galileo.digitalWrite("27", "0")
					time.sleep(0.8)
					galileo.digitalWrite("27", "1")	
					stateCurtain1 = 1
					stateCurtainOC = 1
					#stateCurtain = 0
		else:
			stateCurtain1 = 0
		#------------------------------------------	
			
		#Fan STATES
		if analog0Val > gasThresh:
			if stateFan == 0:
				if stateFanOnOff == 1:
					galileo.digitalWrite("26", "0")
					stateFan = 1
					stateFanOnOff = 0
					galileo.playAudio('005.wav')
					#stateCurtain1 = 0
		else:
			stateFan = 0
		if analog0Val < gasThresh:
			if stateFanOnOff == 0:
				if stateFan1 == 0:
					galileo.digitalWrite("26", "1")
					stateFan1 = 1
					stateFanOnOff = 1
					#stateCurtain = 0
		else:
			stateFan1 = 0					


