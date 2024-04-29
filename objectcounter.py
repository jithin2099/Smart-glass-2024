import cv2
from ultralytics import YOLO
import cvzone
import numpy as np
import pandas as pd
from collections import Counter  # Import Counter from collections module
# import glob
import os
from subprocess import call

model = YOLO("yolov8n.pt")


detection = 0

my_file = open("coco.names", "r")
data = my_file.read()
class_list = data.split("\n")

cap = cv2.VideoCapture(1)
thres = 0.45

cap.set(3,1280)
cap.set(4,720)
cap.set(10,70)


def object(img):
    results = model.predict(img)
    a = results[0].boxes.data
    px = pd.DataFrame(a).astype("float")
    object_classes = []

    for index, row in px.iterrows():
        x1=int(row[0])
        y1=int(row[1])
        x2=int(row[2])
        y2=int(row[3])
        d=int(row[5])
        c=class_list[d]
        obj_class = class_list[d]
        object_classes.append(obj_class)
        cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
        cvzone.putTextRect(img, f'{obj_class}', (x2, y2), 1, 1)

    return object_classes

def count_objects_in_image(object_classes):
    counter = Counter(object_classes)
    print("Object Count in Image:")
    for obj, count in counter.items():
        print(f"{obj}: {count}")

        if obj == 'person':
            detection = 1

    if detection == 1:
        detection = 0
        cap.release()
        cv2.destroyAllWindows
        os.startfile("C:\\Users\\HP\\Desktop\\New Codings\\Btech main Project\\recognizer_attempt2.py")

# path = r'C:\\Users\\HP\\Desktop\\New Codings\\Btech main Project\\street images\\sreejith.jpg'
# for file in glob.glob(path):
#     img = cv2.imread(file)
#     img = cv2.resize(img, (1020, 500))
#     object_classes = object(img)
#     count_objects_in_image(object_classes)
#     cv2.imshow("img", img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

while True:
    ret, img = cap.read()
    # img = cv2.resize(img, (1020, 500))

    object_classes = object(img)
    count_objects_in_image(object_classes)

    cv2.imshow("img", img)
    if (cv2.waitKey(30) == 27):
        print("Exiting Program...")
        break
cap.release()
cv2.destroyAllWindows

