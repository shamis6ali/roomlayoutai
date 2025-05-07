# Just some engine planning before the actual app
# The main code can be found in streamlit_apprunner.py


from ultralytics import YOLO
import json
import cv2

# import the YOLO model and feed a sample image
model = YOLO('yolov8n.pt')
results = model('roomlayout-unsplash.jpg')

#results[0].show()

#just sample objects that are present generally
room_objects = ['chair', 'couch', 'bed', 'tv', 'window', 'door']

#iterating and extracting results
for r in results:
    for box in r.boxes:
        cls = int(box.cls[0])
        label = model.names[cls]
        if label in room_objects:
            print(f"{label}: {box.xyxy}")

#exporting the found detections to a JSON format
detections = []
for box in r.boxes:
    cls = int(box.cls[0])
    label = model.names[cls]
    if label in room_objects:
        coords = box.xyxy[0].tolist()
        detections.append({'label': label, 'bbox': coords})

with open('detections.json', 'w') as f:
    json.dump(detections, f, indent=2)

img = cv2.imread('roomlayout-unsplash.jpg')
for d in detections:
    x1, y1, x2, y2 = map(int, d['bbox'])
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.putText(img, d['label'], (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

cv2.imwrite('annotated_room.jpg', img)

