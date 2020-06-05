#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 21:21:29 2020

@author: claire
"""
import cv2

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

  
    def __del__(self):
        self.video.release() 
        

    def get_frame(self):
        ret, frame = self.video.read()

        # DO WHAT YOU WANT WITH TENSORFLOW / KERAS AND OPENCV

        print(frame)
        ret, jpeg = cv2.imencode('.jpg', frame)

        return jpeg.tobytes()
        
     
