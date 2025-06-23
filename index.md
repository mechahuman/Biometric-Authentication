# Face Recognition-based Secure Application Access

This project is a complete face recognition pipeline that allows secure access to a desktop application using facial authentication. It includes data collection, model training, testing, and implementation with a GUI-based authentication system.

---

## Key Features

- **Real-Time Face Detection:** Uses OpenCV's Haar Cascade for efficient face detection through a webcam.
- **Local Face Dataset Collection:** Automatically captures and stores over 500 facial samples per user.
- **Face Recognition with LBPH:** Implements LBPH (Local Binary Pattern Histogram) for accurate facial recognition.
- **User Authentication:** Grants or denies access based on model prediction and confidence score.
- **Application Integration:** Automatically launches a secure application (like Obsidian) upon successful authentication.
- **Tkinter GUI Feedback:** Provides real-time popup alerts for success or failure in authentication.

---

## Project Structure and File Overview

### `collectdata.py`

- **Purpose:** Captures facial images of a user via webcam and stores them in a local dataset.
- **How it works:**
  - Prompts the user for a unique ID.
  - Uses OpenCV's Haar Cascade Classifier to detect faces.
  - Captures and stores 500+ grayscale face images into the `datasets/` folder in the format: `User.<ID>.<image_number>.jpg`.
- **Dependencies:** OpenCV (`cv2`)

---

### `trainingdata.py`

- **Purpose:** Trains a facial recognition model using the Local Binary Pattern Histogram (LBPH) algorithm.
- **How it works:**
  - Loads all `.jpg` images from the `datasets/` folder.
  - Extracts face data and corresponding user IDs.
  - Trains the LBPH face recognizer on the extracted data.
  - Stores the trained model in a `Trainer.yml` file.
- **Dependencies:** OpenCV, NumPy, PIL (Python Imaging Library)

---

### `testingmodel.py`

- **Purpose:** Tests the trained model in real-time.
- **How it works:**
  - Loads the LBPH model from `Trainer.yml`.
  - Captures webcam video and detects faces.
  - Predicts the user ID for detected faces.
  - Displays the recognized user’s name if the confidence score is acceptable; otherwise labels them as "Unknown".
  - Allows live validation of the model accuracy.
- **Dependencies:** OpenCV

---

### `completeproject.py`

- **Purpose:** Implements the complete system, integrating real-time facial recognition with GUI-based secure access control.
- **How it works:**
  - Loads the LBPH model and initializes webcam for authentication.
  - Uses a 5-second window to detect and recognize a registered face.
  - If authentication succeeds (confidence < 50), the specified application (e.g., Obsidian) is launched.
  - If the face is not recognized, access is denied with a popup message.
- **GUI Elements:** Tkinter for message popups.
- **Dependencies:** OpenCV, Tkinter, subprocess, time

---

## Project Flow

1. **Data Collection** (`collectdata.py`):
   - Capture face images of the user and store them for training.

2. **Model Training** (`trainingdata.py`):
   - Train a model using the images captured in step 1.

3. **Model Testing** (`testingmodel.py`):
   - Verify the model by testing it with real-time face inputs.

4. **Final Deployment** (`completeproject.py`):
   - Use the trained model to grant or deny access to a desktop application.

---

## Requirements

- Python 3.x
- OpenCV (`opencv-python`, `opencv-contrib-python`)
- PIL (`Pillow`)
- NumPy

Install all dependencies using:

```bash
pip install opencv-python opencv-contrib-python Pillow numpy
```

---

## Credits

- **Developer:** [Manav Bhavsar](https://mechahuman.github.io/)  
- **Libraries:** OpenCV, Tkinter, Pillow, NumPy  
- **Face Detection Model:** [Haar Cascade - OpenCV](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)  
- **Tutorial Reference:** Face data collection, training, and testing were adapted from a tutorial by [KNOWLEDGE DOCTOR](https://www.youtube.com/watch?v=LKPB8YM8awk)  
- **Inspiration:** Biometric-based secure access systems
