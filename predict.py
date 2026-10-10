from ultralytics import YOLO

model = YOLO('')
image_path = ''

result = model.track(source= image_path, save=True, save_dir='predict_save')