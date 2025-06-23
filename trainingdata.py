import cv2 as cv
import numpy as np
from PIL import Image
import os

recognizer = cv.face.LBPHFaceRecognizer_create()

path = 'datasets'

def getImageID(path):
    imagePath = [os.path.join(path,f) for f in os.listdir(path)]
    faces = []
    ids = []
    for imagepaths in imagePath:
        faceImage = Image.open(imagepaths).convert('L')
        faceNP = np.array(faceImage)
        Id = (os.path.split(imagepaths)[-1].split(".")[1])
        Id = int(Id)
        faces.append(faceNP)
        ids.append(Id)
        cv.imshow('Training',faceNP)
        cv.waitKey(1)
    return ids, faces

IDs, facedata = getImageID(path)
recognizer.train(facedata, np.array(IDs))
recognizer.write("Trainer.yml")
cv.destroyAllWindows()
print("Training Completed.....")

