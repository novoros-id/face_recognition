# main.py
# import the necessary packages
from flask import Flask, render_template, Response
from camera_flask import VideoCamera

#start_record = 0
name_new_guest = "--"
app = Flask(__name__)
#################################
@app.route('/')
def index():
    # rendering webpage
    return render_template('index.html')

def gen(camera):
    global name_new_guest
    while True:
        #get camera frame
        frame = camera.get_frame()

        if name_new_guest != "--":
            #print("start record", start_record)
            camera.record_video(name_new_guest)
            name_new_guest = "--"

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

##################################

@app.route('/process_data/<data_>', methods=['GET','POST'])
def doit(data_):
    global name_new_guest
    print ("press button - ",str(data_))
    name_new_guest = str(data_)
    return "0"

##################################
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == '__main__':
    # defining server ip address and port
    app.run(host='0.0.0.0',port='5000', debug=True)