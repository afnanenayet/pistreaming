import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (2592, 1944)
    camera.start_preview()
    # Camera warm-up time
    time.sleep(5)
    camera.capture('temp.jpg')