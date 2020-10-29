# main.py
# import the necessary packages
from flask import Flask, render_template, Response
from camera_flask import VideoCamera

start_record = 0
app = Flask(__name__)
#################################
@app.route('/')
def index():
    # rendering webpage
    return render_template('index.html')

def gen(camera):
    global start_record
    while True:
        #get camera frame
        frame = camera.get_frame()

        if start_record == 1:
            #print("start record", start_record)
            start_record = 0
            camera.record_video()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

##################################
@app.route('/save_video_button')
def save_video_button():
    global start_record
    data = json.loads(request.data)
    text = data.get("text", None)
    print("data ----- ", text)
    start_record = 1
    return "nothing"

##################################
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == '__main__':
    # defining server ip address and port
    app.run(host='0.0.0.0',port='5000', debug=True)