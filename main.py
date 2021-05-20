import cv2  # opencv library module
import numpy as np
# import face_recognition

face_detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")  # loading the pre-trained classifier

webcam = cv2.VideoCapture(0)  # getting video frames from webcam

while True:
    cam, img = webcam.read()  # returns flag to indicate correct frame read and the frame itself

    imgS = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # converting to grayscale image

    faces = face_detect.detectMultiScale(imgS, 1.1, 4)  # scale factor set to 1.1 and minimum neighbours to 4

    for (x1, y1, x2, y2) in faces:
        cv2.rectangle(img, (x1, y1), (x1 + x2, y1 + y2), (0, 255, 0), 2)  # BGR color used to draw rectangle around
        # detected face

    cv2.imshow("webcam", img)  # show the image
    key = cv2.waitKey(30)  # wait for key press to close screen
    if key == 27:  # ESC key to exit
        break

webcam.release()  # to close video and it's capturing device


# mark = face_recognition.load_image_file("images/elon.jpg")
# mark = cv2.cvtColor(mark, cv2.COLOR_BGR2RGB)
#
# markTest = face_recognition.load_image_file("images/mark Test.jpg")
# markTest = cv2.cvtColor(markTest, cv2.COLOR_BGR2RGB)
#
# markFacePos= face_recognition.face_locations(mark)[0]
# markFaceEncode = face_recognition.face_encodings(mark)[0]
# cv2.rectangle(mark,(markFacePos[3],markFacePos[0]),(markFacePos[1],markFacePos[2]),(150,0,150),4)
#
# markTestFacePos= face_recognition.face_locations(markTest)[0]
# markTestFaceEncode = face_recognition.face_encodings(markTest)[0]
# cv2.rectangle(markTest,(markTestFacePos[3],markTestFacePos[0]),(markTestFacePos[1],markTestFacePos[2]),(150,0,150),4)


# faceDis= face_recognition.face_distance([markfaceEncode],markTestfaceEncode)
# Match1 = face_recognition.compare_faces([markFaceEncode], imgSfaceEncode[0])
#   cv2.putText(mark,f'{Match1}',(50,50),cv2.FONT_HERSHEY_DUPLEX,1,(150,0,0),2)
#
#   Match2 = face_recognition.compare_faces([markTestFaceEncode], imgSfaceEncode[0])
#   cv2.putText(markTest,f'{Match2}',(50,50),cv2.FONT_HERSHEY_DUPLEX,1,(150,0,0),2)


# print(Match)
# cv2.imshow("Mark", mark)
# cv2.imshow("Mark Test", markTest)
# cv2.waitKey(0)
