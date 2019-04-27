#!/usr/bin/python
import picamera
from datetime import datetime
cam = picamera.PiCamera()
cam.vflip = True
file_name = datetime.now().strftime("%Y%m%d%H%M%S")
cam.capture('/tmp/' + file_name + '.jpg' )
cam.close()