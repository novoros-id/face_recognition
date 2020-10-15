# main.py
# import the necessary packages
from flask import Flask, render_template, Response
from camera_flask import VideoCamera

app = Flask(__name__)
#################################
@app.route('/')
def index():
    # rendering webpage
    return render_template('index.html')
def gen(camera):
    while True:
        #get camera frame
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

##################################
#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    print ("Hello")
    return "nothing"

##################################
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == '__main__':
    # defining server ip address and port
    app.run(host='0.0.0.0',port='5000', debug=True)