#!/usr/bin/python
# -*- coding: utf-8 -*-

# gosttpy
#Voice recognition library using googleSpeech API
# Created by: fito_segrera 
# www.fii.to
# 05-07-14


import urllib  # For http request / google search
import urllib2  # For doing https POST
# This library is for calling shell scripts from within python
import subprocess
# for handling JSON objects - in this case the return from google's API
import simplejson as json
import os
import ast


class gosttpy:

    # This function records voice using the microphone input, uploads
    # the .flac audio file to google Speech API transcripts that to text and
    # searches for it on google's search engine
    # The function takes 2 arguments: 
    # apiKey contains the GOOGLE SPEECH API Key
    # recognitionType contains the type of process that will be executed:
    #       'search' = Whatever the user Speaks it will be searched in google
    #      'compare' = Whatever the user Speaks will NOT be searched... 
    #                  It will be compared to the contents of an array to see if matches an specific voice command

    def voiceRecognition(self, apiKey):
        #subprocess.call(['./googleSpeech.sh'])
        #os.system("./sox -r 16000 -t alsa default voice.flac silence 1 0.1 5% 1 1.0 5%")
        print '================================'
        f = open('voice.wav')
        audioFile = f.read()
        #f.close()
        lang_code = 'en-US'
        googl_speech_url = 'https://www.google.com/speech-api/v2/recognize?output=json&lang=en-us&key=' + apiKey
        hrs = {'Content-type': 'audio/l16; rate=16000'}
        req = urllib2.Request(googl_speech_url, data=audioFile, headers=hrs)
        p = urllib2.urlopen(req)

        # -----------------------
        # For some reason the google speech API returns 2 json objects (the first one is empty)
        # and parsing with the json library was breaking the code...
        # I solved the issue writing a .txt file with the json data and deleting the first json object in the stream...
        # As follows:

        rawData = p.read()
        print 'RAW-DATA:'
        print rawData
    
        print '================================'
        print 'CLEAN-DATA:'
        
        # removes the empty "{"result":[]}" object that comes in the json string
        textFileClean = rawData.replace("""{"result":[]}""", '')
        print textFileClean
        print '================================'

        # -----------------------
        # Parsing the CLEAN JSON data:

        # Loads the converted and cleaned data as a JSON object
        data = json.loads(textFileClean)

        # Read through all the json object and store all the 'transcript' items in an array called 'allData'
        allData = []
        itemsCounter = 0
        commands = open('commands.txt', 'r').read()
        dictionary = ast.literal_eval(commands)
        
        #print 'ALL TRANSCRIPTS:'
        for items in data['result'][0]['alternative']:
            allData.append(items['transcript'])
            if allData[itemsCounter] == dictionary["light on"]:
                return dictionary["light on"]
            if allData[itemsCounter] == dictionary["light off"]:
                return dictionary["light off"]
            if allData[itemsCounter] == dictionary["open curtain"]:
                return dictionary["open curtain"]
            if allData[itemsCounter] == dictionary["close curtain"]:
                return dictionary["close curtain"]
            if allData[itemsCounter] == dictionary["open window"]:
                return dictionary["open window"]
            if allData[itemsCounter] == dictionary["close window"]:
                return dictionary["close window"]  
            if allData[itemsCounter] == dictionary["fan on"]:
                return dictionary["fan on"]
            if allData[itemsCounter] == dictionary["fan off"]:
                return dictionary["fan off"]                
            #return allData[itemsCounter]
            #print allData[itemsCounter]
            itemsCounter += 1

        # This line deletes the audio file once the operation is done
        #os.remove('voice.flac')
        #return rawData