import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# -------- LOAD TRAINED MODEL --------
MODEL_PATH = "mask_detector.h5"

print("[INFO] Loading model...")
model = load_model(MODEL_PATH)

# -------- START WEBCAM -------------
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("[ERROR] Camera not working")
    exit()

print("[INFO] Press 'q' to quit\n")

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    # Resize for model
    face = cv2.resize(frame, (224, 224))
    face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
    face = preprocess_input(face)
    face = np.expand_dims(face, axis=0)

    # -------- PREDICT --------
    (mask, withoutMask) = model.predict(face, verbose=0)[0]

    # -------- LABEL ----------
    if mask > withoutMask:
        label = f"Mask {mask*100:.2f}%"
        color = (0, 255, 0)
    else:
        label = f"No Mask {withoutMask*100:.2f}%"
        color = (0, 0, 255)

    # -------- SHOW TEXT ------
    cv2.putText(frame, label, (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    cv2.imshow("Mask Detector", frame)

    # Press q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

print("[INFO] App closed")
