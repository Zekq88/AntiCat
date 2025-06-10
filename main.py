from ultralytics import YOLO

import threading
import pygame
import time

cat = 15
# the model of yolo
model = YOLO("yolov8n.pt")

# loads the model version
results = model.predict(source=0, stream=True, show=True, conf=0.5)

# plays the sirens
def sirens():
   # global sirenTime
    pygame.mixer.init()
    pygame.mixer.music.load("Sirens.mp3")
    pygame.mixer.music.play()

# iteration from webcam
for result in results:
    
    boxes = result.boxes
    names = result.names
   
    print("CLS baby! " + str(boxes.cls))
    # för att se alla värden
    # print(str(names).replace(",", "\n"))
    if cat in boxes.cls:
        thread = threading.Thread(target=sirens, daemon=True)
        print("\033[0;31m" "Alert: A Cat has been detected!!!")
        print("Sound the sirens!!!" + "\033[0m")
        thread.start()
        time.sleep(20)
