#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 22:03:01 2020

@author: claire
"""
 
import os 
#import pygame.midi
#import time
import numpy as np
import cv2
from keras.models import load_model

model = None

#load the model

'''
note_list = [(60,127),(50,127),(53,127),(52,127),(55,127),(72,127),(58,172)]
'''

frq_list = [261,294,330,349,392,440,494,523]
duration = 1 

def frame_to_note(frame):


    global model
    if model is None:
        model = load_model('handrecognition_model.h5')     

    gesture_id = 0
    if frame is None:
        return gesture_id

    #pygame.mixer.init() #to play sound w.o opening pygame window
    #pygame.midi.init()

    #player = pygame.midi.Output(0)
    #player.set_instrument(0)
    
    # Add frame to a input list
    X = []
    X.append(frame)
    # Cast to an array
    X = np.array(X, dtype="uint8")
    # reshape array (number of images, height, width, ?)
    X = X.reshape(1, 120, 320, 1)
    # Make predictions towards the frame
    predictions = model.predict(X) 

    # index of the max value 
    gesture_id = np.argmax(predictions[0])
    
    # if index is the range(first through the end of the note list
    if gesture_id in range(1, len(frq_list)):
        #get the note at the gesture id index
        #note = note_list[gesture_id]
        note = frq_list[gesture_id]
        print(note)
        os.system(f'play -n -c1 synth {duration} sine {note}')
        #play the note at first and 2nd 
        #player.note_on(note[0], note[1])  
        #time.sleep(1)
        #turn off note
        #player.note_off(note[0], note[1])
        print(gesture_id, frq_list[gesture_id])
    

    return gesture_id

