from ultralytics import YOLO

model = YOLO("")

results = results = model.train(
    data="",
    split="train",
    batch = 8,
    epochs=10,
    imgsz=640,
    device="mps",
    save_dir="model_result",
)
