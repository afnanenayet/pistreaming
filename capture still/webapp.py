import picamera
import os
from time import sleep
from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    with picamera.PiCamera() as camera:
        os.remove('./static/temp.jpg')
        camera.resolution = (2592, 1944)
        camera.start_preview()
        # Camera warm-up time
        sleep(5)
        camera.capture('static/temp.jpg')
        return render_template('template.html')
        

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')