import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

folder = "images"
images = []
imagesNames = []
imgList = os.listdir(folder)
print(imgList)

for each in imgList:
    oneImg = cv2.imread(f'{folder}/{each}')
    images.append(oneImg)
    imagesNames.append(os.path.splitext(each)[0])
print(imagesNames)


def Encodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def Attendance(name):
    with open("Attendance.csv", 'r+') as file:
        attendanceList = file.readlines()
        students = []
        for each in attendanceList:
            format = each.split(',')
            students.append(format[0])

        if name not in students:
            now = datetime.now()
            attendanceTime = now.strftime('%H:%M:%S')
            file.writelines(f'\n{name},{attendanceTime}')


encodingImageList = Encodings(images)
print("Encoding complete");

cap = cv2.VideoCapture(0);

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.20, 0.20)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    curFrameLoc = face_recognition.face_locations(imgS)
    curFrameEncoding = face_recognition.face_encodings(imgS)

    for (encodeFace, faceLoc) in zip(curFrameEncoding, curFrameLoc):
        check = face_recognition.compare_faces(encodingImageList, encodeFace)
        faceDis = face_recognition.face_distance(encodingImageList, encodeFace)
        # print(faceDis)

        checkIndex = np.argmin(faceDis)

        if check[checkIndex]:
            name = imagesNames[checkIndex].upper()
            print(name)

            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 5, x2 * 5, y2 * 5, x1 * 5
            cv2.rectangle(img, (x1, y1), (x2, y2), (155, 55, 50), 2)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_ITALIC, 1, (255, 0, 155), 2);

            Attendance(name)

        cv2.imshow("webcam", img)
        cv2.waitKey(1)
