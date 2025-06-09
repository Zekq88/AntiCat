# AntiCat
# 🐱 Real-Time Cat Detector with Siren using YOLOv8 and Pygame

This project is a lightweight real-time object detection tool that uses [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) to detect cats via webcam and trigger an audio siren alert using `pygame`.

## 📸 Overview

- Uses YOLOv8 (Nano model) for efficient real-time detection.
- Automatically plays a siren when a cat (`class ID 15`) is detected.
- Displays live webcam feed with bounding boxes.
- Multi-threaded audio playback (non-blocking).

## 🚀 Getting Started

## 1. Clone the repository

```bash
git clone https://github.com/your-username/cat-siren-detector.git
```


## 2. Install dependencies

write this line in the terminal:
```bash
pip install ultralytics pygame
```

## 3. Requirements
* Python 3.8+

* A webcam

* Yolov8n.pt weights (automatically downloaded by Ultralytics on first run)

* An MP3 file named Silent Hill Sirens.mp3 in the same folder as your script

# 🛑 Disclaimer
### This is a fun proof-of-concept project and not intended for production use. Use responsibly and don't scare your pets too much 😸
