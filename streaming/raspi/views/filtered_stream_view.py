from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import StreamingHttpResponse
from raspi.services.video_camera import VideoCamera
import cv2

cam = VideoCamera()

def get_thresholded(frame):
    ret, threshold = cv2.threshold(frame,127,255,cv2.THRESH_BINARY)
    return threshold

def get_laplacian(frame):
    laplacian = cv2.Laplacian(frame,cv2.CV_64F)
    return laplacian


class FilteredStreamView(View):
    def get_stream(self):
        # https://stackoverflow.com/questions/49680152/opencv-live-stream-from-camera-in-django-webpage

        while True:
            frame = cam.get_filtered_frame(get_thresholded)
            yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    def get(self, request):
        return StreamingHttpResponse(self.get_stream(), content_type='multipart/x-mixed-replace;boundary=frame')