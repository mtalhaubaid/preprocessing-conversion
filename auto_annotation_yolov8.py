import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from ultralytics import YOLO

# Load your YOLO detection model
model = YOLO(r"C:\Users\ASDF\Downloads\best.pt")

# Perform predictions on your dataset (this will output bounding boxes)
results = model.predict(source=r'E:\dukto\data_set_weapon', conf=0.25, iou=0.45, imgsz=640,batch=64, save=True, save_txt=True, show=True)