# -*- coding: utf-8 -*-
"""
Spyder Editor


"""
from flask import Flask, render_template, Response
from camera import VideoCamera
import cv2
import midi_model


app = Flask(__name__)

video_stream = VideoCamera()

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        model_frame = camera.get_model_frame()
        gesture_id = midi_model.frame_to_note(model_frame)
        if(gesture_id >= 0):
            print("PLAYING NOTE : ", gesture_id)
        jpeg_frame = camera.get_jpeg_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg_frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(video_stream),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    global model

    app.run(host='127.0.0.1', debug=True,port="5000")

