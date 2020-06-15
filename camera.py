#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 21:21:29 2020

@author: claire
"""
import cv2
import pygame.midi
#import time
import numpy as np


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(1)

  
    def __del__(self):
        self.video.release() 
        

    def get_jpeg_frame(self):
        ret, frame = self.video.read()

        # DO WHAT YOU WANT WITH TENSORFLOW / KERAS AND OPENCV

        print(frame)
        ret, jpeg = cv2.imencode('.jpg', frame)

        return jpeg.tobytes()
        

    def get_model_frame(self):
        ret, frame = self.video.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        frame = cv2.resize(frame, (320, 120))
        return frame
     
