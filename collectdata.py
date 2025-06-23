import cv2 as cv

cap = cv.VideoCapture(0)
facedetect = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
count = 0
id = input("Enter your id: ")

while cap.isOpened():
    ret,frame = cap.read()
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
          count += 1
          cv.imwrite('datasets/User.'+str(id)+'.'+str(count)+'.jpg',gray[y:y+h,x:x+w])
          cv.rectangle(frame, (x,y),(x+w,y+h),(255,255,255),1)

    cv.imshow("FRAME",frame)
    k = cv.waitKey(1)
    if count>500:
        break
    
cap.release()
cv.destroyAllWindows()
print("DATASET COLLECTED SUCCESSFULLY.......")