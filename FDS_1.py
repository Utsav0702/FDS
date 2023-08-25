import cv2
import numpy as np

# Load the pre-trained Haarcascades face detection model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Open a video capture stream (you can also use cv2.VideoCapture(0) for webcam)
video_capture = cv2.VideoCapture('My Video.mp4')


while True:
    # Read a frame from the video stream
    ret, frame = video_capture.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the result
    cv2.imshow('Face Detection', frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture
video_capture.release()
cv2.destroyAllWindows()

def recognize_face(face):
    # Placeholder for face recognition
    
    return "Person Detected"

# Loop through detected faces and recognize them
for (x, y, w, h) in faces:
    face = frame[y:y+h, x:x+w]
    recognized_person = recognize_face(face)
    cv2.putText(frame, recognized_person, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# Release the video capture and close windows
video_capture.release()
cv2.destroyAllWindows()
