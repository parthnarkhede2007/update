import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_me = "img" +str (number)
        cv2.imwrite = time.time()
        start_time = time.time()
        result = False

    return img_me()
    cv2.imwrite(img_name,frames)
    print("take_snapshot")
