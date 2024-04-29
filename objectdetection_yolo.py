import cv2
from ultralytics import YOLO
import supervision as sv


model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(1)
thres = 0.45

cap.set(3,1280)
cap.set(4,720)
cap.set(10,70)


def main():

    box_annotator = sv.BoxAnnotator(
        thickness=2,
        text_thickness=2,
        text_scale=1
    )

    while True:
        ret, frames = cap.read()

        result = model(frames)[0]
        detections = sv.Detections.from_ultralytics(result)

        frames = box_annotator.annotate(scene=frames, detections=detections)

        cv2.imshow("YOLO Out", frames)
        if (cv2.waitKey(30) == 27):
            print("Exiting Program...")
            break
    cap.release()
    cv2.destroyAllWindows


if __name__ == "__main__":
    print("Execcuting...")
    main()