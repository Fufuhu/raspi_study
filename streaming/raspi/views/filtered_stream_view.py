from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import StreamingHttpResponse
import time
import cv2
import threading

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture('http://hoge:hoge@192.168.1.98:8080/?action=stream') 
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        ret, threshold = cv2.threshold(image,127,255,cv2.THRESH_BINARY)

        # ret, jpeg = cv2.imencode('.jpg', image)
        ret, jpeg = cv2.imencode('.jpg', threshold)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

cam = VideoCamera()

class FilteredStreamView(View):
    def get_stream(self):
        # https://stackoverflow.com/questions/49680152/opencv-live-stream-from-camera-in-django-webpage

        while True:
            frame = cam.get_frame()
            yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    def get(self, request):
        return StreamingHttpResponse(self.get_stream(), content_type='multipart/x-mixed-replace;boundary=frame')