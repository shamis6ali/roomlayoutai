import streamlit as st
from PIL import Image
from ultralytics import YOLO
import json, cv2
import numpy as np

model = YOLO('yolov8n.pt')
room_objects = ['chair', 'couch', 'bed', 'tv', 'window', 'door']  #needs to change add support for more objects

st.title("RoomLayoutAI - Layout Detection from Room Photos")

uploaded_file = st.file_uploader("Upload a room image", type=['jpg', 'png'])
if uploaded_file:
    image = Image.open(uploaded_file).convert('RGB')
    image_np = np.array(image)
    results = model(image_np)
    detections = []

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]
            if label in room_objects:
                coords = list(map(int, box.xyxy[0].tolist()))
                detections.append({'label': label, 'bbox': coords})
                cv2.rectangle(image_np, (coords[0], coords[1]), (coords[2], coords[3]), (0,255,0), 2)
                cv2.putText(image_np, label, (coords[0], coords[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)

    st.image(image_np, caption="Detected Layout", use_column_width=True)
    st.download_button("Download JSON", json.dumps(detections, indent=2), file_name="layout.json")
