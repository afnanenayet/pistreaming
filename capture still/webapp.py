from flask import Flask
import picamera

app = Flask(__name__)

@app.route('/')
def index():
    with picamera.PiCamera() as camera:
        camera.resolution = (2592, 1944)
        camera.start_preview()
        # Camera warm-up time
        time.sleep(5)
        camera.capture('temp.jpg')
        return render_template('temp.jpg')
        

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')