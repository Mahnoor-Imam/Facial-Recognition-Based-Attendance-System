# Facial Recognition Based Attendance System

## Facial Recognition System
A facial recognition system is a technology capable of matching a human face from a digital image or a video frame against a database of faces and works by pinpointing and measuring facial features from a given image.

## Phases
1.	Face Detection
2.	Data Gathering
3.	Training the Recognizer
4.	Face Recognition
5.	Attendance System Integration

## Methodology
OpenCV is a multi-platform library that allows us to create real-time computer vision applications. It mainly focuses on image processing, video recording and analysis, including features such as face and object detection.

### Face detection
The first thing we do is to use the dlib package to detect faces in images or video streams. Now that we know the exact location/coordinates of the face, we delete this face for further processing.

### Feature extraction
Now that the face has been cropped from the image, we use HOG to extract 128 features from it. In this case, face mosaic will be used to extract facial features. The neural network takes the face image as input and generates a vector representing the most important attributes of the face. This vector is called an embedding in machine learning, which is why we call it a face embedding. Use these functions to calculate face distance. When the test image is displayed in openCV, it compares its facial distance with the distance existing in the database. Then the person with the smallest distance is recognized as the person in the picture.


## Tools Used
* PyCharm IDE
* OpenCV Library
* GitHub Version Control
