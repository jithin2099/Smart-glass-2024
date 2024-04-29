import cv2
import numpy as np
import os 

import mainfile

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
font = cv2.FONT_HERSHEY_SIMPLEX
#iniciate id counter
id = 0
# names related to ids: example ==> Marcelo: id=1,  etc
f = open("datasetnames.txt", "r")
names = f.read()
names = names.split("\n")
# Initialize and start realtime video capture
cam = cv2.VideoCapture(1)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height
# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

occurance = 0
occurance_id = "None"
occcurance_times = [i for i in range(len(names))]
id_no = 0

print(occcurance_times)
print(len(names))
print(range(len(names)))
for i in range(len(names)):
    occcurance_times[i] = 0
print(occcurance_times)

for i in range(100):
    ret, img =cam.read()
    # img = cv2.flip(img, -1) # Flip vertically
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        confidence_toprint = 100-confidence
        # Check if confidence is less them 100 ==> "0" is perfect match 
        if (confidence < 100):
            id_no = id
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
        
        if int(confidence_toprint) > 40:
            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)



        if occurance_id == "None":
            continue
        
        else:
            occcurance_times[id_no] += 1

    
    cv2.imshow('camera',img) 
    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

max_occurance = max(occcurance_times)
max_occurance_index = occcurance_times.index(max_occurance)

mainfile.speak(str(names[max_occurance_index]) +" is found in the frame")

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
f.close()
cv2.destroyAllWindows()

os.startfile("C:\\Users\\HP\\Desktop\\New Codings\\Btech main Project\\objectcounter.py")