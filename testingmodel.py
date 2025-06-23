import cv2 as cv

cap = cv.VideoCapture(0)
facedetect = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read("Trainer.yml")

name_list = ["","Manav"]

while cap.isOpened():
    ret,frame = cap.read()
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
          
        serial, conf = recognizer.predict(gray[y:y+h,x:x+w])
        if conf < 50:
            cv.putText(frame,name_list[serial],(x,y-40),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
            cv.rectangle(frame, (x,y),(x+w,y+h),(255,255,255),1)
        else:
            cv.putText(frame,"Unknown",(x,y-40),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
            cv.rectangle(frame, (x,y),(x+w,y+h),(255,255,255),1)

    cv.imshow("FRAME",frame)
    k = cv.waitKey(1)
    
    if k == ord('q'):
         break
    
cap.release()
cv.destroyAllWindows()