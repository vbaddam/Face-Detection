import cv2


class detect():

    def __init__(self,img):
    
        self.img = img

    def detectface(self):
        image = cv2.imread(self.img)
        frontalface = cv2.CascadeClassifier('classifiers/haarcascade_frontalface_default.xml')
        imgray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        faces = frontalface.detectMultiScale(imgray,1.3,5)
        for (x,y,w,h) in faces:
            face_image = cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
            eye = cv2.CascadeClassifier('classifiers/haarcascade_eye.xml')
            eyes = face_image[y:y+h,x:x+h]
            eygray = imgray[y:y+h,x:x+h]
            eyes_ = eye.detectMultiScale(eygray,1.3,5)
            for (l,m,n,o ) in eyes_:
                cv2.rectangle(eyes,(l,m),(l+n,m+o),(255,0,0),2)
        return face_image


if __name__ == "__main__":

    print('####### Welcome to Face and eyes detection ######')
    photo = input('Enter the Jpeg file here : ')
    
    det = detect(photo)
    cv2.imshow('image',det.detectface())
    cv2.waitKey(0)
    cv2.destryAllwindows()
