import numpy as np
import cv2
import os.path

video_capture = cv2.VideoCapture(0)
fps = int(video_capture.get(cv2.CAP_PROP_FPS))
recordFrame = int(fps)*5
numframe = 0

frame_width = int(video_capture.get(3))
frame_height = int(video_capture.get(4))

size = (frame_width, frame_height)
out = None

while(True):
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Display the resulting frame
    cv2.imshow('frame',gray)

    if numframe != 0 and numframe != recordFrame:
        numframe += 1
        print(numframe)
        # write the flipped frame
        out.write(frame)
    elif numframe == recordFrame:
        numframe = 0
        out.release()

    wKew = cv2.waitKey(1) & 0xFF

    if wKew == ord('q'):
        break
    elif wKew == ord('s'):
        if os.path.exists('faces/tmp/output.mp4') != True:
            #global out
            #forcc = cv2.VideoWriter_fourcc(*'MJPG')
            #out = cv2.VideoWriter('faces/tmp/output.mp4', forcc, fps, size)
            forcc = cv2.VideoWriter_fourcc('m','p','4','v')
            out = cv2.VideoWriter('faces/tmp/output.mp4', forcc, fps, size)
        #name_file = input()
        numframe = 1


# When everything done, release the capture
video_capture.release()
cv2.destroyAllWindows()