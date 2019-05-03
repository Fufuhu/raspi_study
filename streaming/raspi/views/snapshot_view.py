from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import HttpResponse

from raspi.services.video_camera import VideoCamera
from uuid import uuid4
from streaming.settings import CAMERA_IMAGE_DIRECTORY

cam = VideoCamera()

class SnapView(View):

    def get(self, request):
        image = cam.get_frame()

        filename = str(uuid4()) + '.jpg'
        print(filename)
        full_path = CAMERA_IMAGE_DIRECTORY + '/' + filename

        # ファイルの書き込み???
        with open(full_path, "wb") as fout:
            fout.write(image)

        return HttpResponse(image, content_type="image/jpeg")