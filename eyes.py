import cv2
from detect import *


        
class eyes():

    
    def __init__(self,img1):
    
        self.img1 = img1

    def eye(self):
        image = cv2.imread(self.img1)
        ey = cv2.CascadeClassifier('classifiers/haarcascade_eye.xml')
        imgray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        faces = ey.detectMultiScale(imgray,1.3,5)
        for (ex,ey,ew,eh) in faces:
            eye_image = cv2.rectangle(image,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
        return eye_image


if __name__ == "__main__":
    e = eyes(detect('vasanth.jpg').detectface())
    cv2.imshow('image',e.eye())
    cv2.waitKey(0)
    cv2.destryAllwindows()


