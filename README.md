
# RoomLayoutAI

RoomLayoutAI is a lightweight computer vision app that detects and labels furniture and structural elements in room photos using YOLOv8. It allows users to visualize layout structure and download detection results in JSON format, perfect for renovation planning and design automation.

## 🚀 Features

- 📸 Upload a room photo (JPG/PNG)
- 🧠 Detect objects like chairs, beds, TVs, couches, etc.
- 📦 Export layout data in structured JSON
- 🖼️ View annotated layout directly in the browser
- Built with **YOLOv8**, **OpenCV**, and **Streamlit**

## 🛠️ Tech Stack

- Python 3.10+
- [YOLOv8 (Ultralytics)](https://github.com/ultralytics/ultralytics)
- Picture Link: https://unsplash.com/photos/living-room-L7EwHkq1B2s
- OpenCV
- Streamlit

## 🖥️ Setup

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/RoomLayoutAI.git
cd RoomLayoutAI
```

### 2. Create and activate conda environment

```bash
conda create -n roomlayoutai python=3.10 -y
conda activate roomlayoutai
conda install -c conda-forge opencv streamlit -y
pip install ultralytics
```

### 3. Run the app

```bash
streamlit run streamlit_apprunner.py
```

## 📁 Project Structure

```
RoomLayoutAI/
├── engine.py                # Sample detection and JSON export script
├── streamlit_apprunner.py  # Streamlit front-end
├── detections.json         # Sample output (generated)
├── annotated_room.jpg      # Sample image with annotations (generated)
```

## 📷 Example

Upload an image like this:

![Room Example](./sample-room.jpg)

…and see this output:

![Detected Layout](./annotated_room.jpg)

## 📥 Output Format

Downloadable `layout.json`:
```json
[
  {"label": "bed", "bbox": [50, 90, 400, 300]},
  {"label": "tv", "bbox": [420, 80, 600, 250]}
]
```

## 🔍 TODO

- [ ] Add more object types (`sink`, `toilet`, `table`, etc.)
- [ ] Deploy on Streamlit Cloud
- [ ] Add confidence threshold slider

---

## 👨‍💻 Author

**Shamis Ali**  
[LinkedIn](https://linkedin.com/in/shamis-06-ali)

---

## 📄 License

MIT License
