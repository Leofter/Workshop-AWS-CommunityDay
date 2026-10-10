import cv2
import os

cap = cv2.VideoCapture("")

output_folder = ""
os.makedirs(output_folder, exist_ok=True)

frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_name = os.path.join(output_folder, f"frame_{frame_count}.jpg")

    cv2.imwrite(frame_name, frame)
    frame_count += 1

cap.release()
print("Finalizado")
