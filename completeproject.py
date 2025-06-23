import cv2 as cv
import tkinter as tk
from tkinter import messagebox
import time
import subprocess

def open_app(app_path):
    try:
        subprocess.Popen(app_path)
        
    except Exception as e:
        print("Error Launching: ",e)

def show_popup(title,message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo(title,message)
    root.destroy()

def authenticate_face(timeout = 5):

    cap = cv.VideoCapture(0)
    facedetect = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    recognizer = cv.face.LBPHFaceRecognizer_create()
    recognizer.read("Trainer.yml")

    if  not cap.isOpened():
        show_popup("Camera Unavailable","THE CAMERA CANNOT BE ACCESSED ")
        return False
    
    start_time = time.time()
    authenticated = False

    
    while time.time() - start_time < timeout:
        ret,frame = cap.read()

        gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        faces = facedetect.detectMultiScale(gray,1.3,5)

        for (x,y,w,h) in faces:
            serial, conf = recognizer.predict(gray[y:y+h,x:x+w])
            cv.rectangle(frame, (x,y),(x+w,y+h),(255,255,255),2)
            print(f"Detected ID: {serial}, Confidence: {conf}")
            if conf < 50:
                 authenticated = True
                 break
            
        cv.imshow("Frame",frame)
        k = cv.waitKey(1)
        if k == ord('q'):
                break
        if authenticated:
             break


    cap.release()
    cv.destroyAllWindows()

    return authenticated


def open_securely(app_path):
    if authenticate_face():
          open_app(app_path)
    else:
         show_popup("Access Denied","You do not have permission to access this application.")

if __name__ == '__main__':
     appPath = fr"C:\Users\manav\AppData\Local\Programs\Obsidian\Obsidian_original.exe"
     open_securely(appPath)

