from ultralytics import YOLO

model = YOLO("")
results = model.track(source=1, show=True)
