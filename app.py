from flask import Flask,render_template,Response
import tensorflow as tf
import cv2
import numpy as np
import os
from playsound import playsound


app=Flask(__name__)

cv2_base_dir = os.path.dirname(os.path.abspath(cv2.__file__))
haar_face_model = os.path.join(cv2_base_dir, 'data/haarcascade_frontalface_default.xml')
haar_eyes_model = os.path.join(cv2_base_dir, 'data/haarcascade_eye.xml')
model=tf.keras.models.load_model('model.h5')

# alarm_sound=False


def generate_frames():

    camera=cv2.VideoCapture(0)
    while True:
        ## read the camera frame
        success,frame=camera.read()
        if not success:
            break
        else:

            detector=cv2.CascadeClassifier(haar_face_model)
            eye_cascade = cv2.CascadeClassifier(haar_eyes_model)
            faces=detector.detectMultiScale(frame,1.1,7)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
             #Draw the rectangle around each face
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
                for (ex, ey, ew, eh) in eyes:
                    # text = str(model.predict(frame[ey:ey+eh,ex:ex+ew]))
                    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 0, 255), 2)
                    final_image = cv2.resize(roi_color, (224,224))
                    final_image = np.expand_dims (final_image,axis =0) ## need fourth dimension
                    final_image= final_image/255.0
                    Predictions = model.predict(final_image)
                    if (np.round(Predictions)>0):
                        text = "Awake"
                        # alarm_sound=False
                    else:
                        text = "Drowsy"
                        # alarm_sound=True
                        # playsound('./alarm/alarm.wav')

                origin = (x,y)
                # text = drowsiness_model(frame,eyes,model)
                cv2.putText(frame, text, origin , fontFace = cv2.FONT_HERSHEY_COMPLEX, fontScale = 2, color = (0,255,0))
                ret, buffer = cv2.imencode('.jpg', frame)

                if cv2.waitKey(100) == ord('q'):
                    break

            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


# Routes
@app.route('/')
def index():
    return render_template('feed.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=True)
