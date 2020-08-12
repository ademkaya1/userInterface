import cv2
import numpy as np
from PyQt5 import QtWidgets
import time
from patientRegister import *
from modelTrain import *



from PyQt5 import *


import warnings
warnings.filterwarnings("ignore")
face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")



def face_extractor(img, size=0.5):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is ():
        return img, []
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        roi = img[y:y + h, x:x + w]
        roi = cv2.resize(roi, (200, 200))
    return img, roi


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    image, face = face_extractor(frame)
    try:
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        results = model.predict(face)
        if results[1] < 500:
            confidence = int(100 * (1 - (results[1]) / 400))
            display_string = 'DOGRULAMA ORANI ' + str(confidence) + '%'
            cv2.putText(image, display_string, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 120, 150), 2)
        if confidence > 89:
            cv2.putText(image, "GIRIS BASARILI", (200, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow("Face Recognition", image)

            window = QtWidgets.QMainWindow()
            ui = Ui_hasta_kayit_window()
            ui.setupUi(window)
            window.show()

            break


        else:
            cv2.putText(image, "ORTAMIN AYDINLIK OLDUGUNA EMIN OLUNUZ", (100, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow("Face Recognition", image)

    except:
        cv2.putText(image, "YUZ BULUNAMADI", (220, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        cv2.putText(image, "GIRIS YAPILAMADI", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow("Face Recognition", image)
    # if cv2.waitKey(1) == 13:
    #     cap.release()
    #     break
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
