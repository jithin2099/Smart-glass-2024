import cv2
import os

import mainfile

f = open('datasetnames.txt', 'r+')
names = f.read()
names = names.split("\n")
id = len(names)
f.close()

cam = cv2.VideoCapture(1)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# For each person, enter one numeric face id
face_name = input('\n Enter user name: ')
# face_id = input('\n enter user na end press <return> ==>  ')
face_id = id

g = open('datasetnames.txt', 'a')
g.write('\n'+face_name)

print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
count = 0
while(True):
    ret, img = cam.read()
    # img = cv2.flip(img, -1) # flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1
        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        cv2.putText(img, str(count), (10, 10), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)
        cv2.imshow('image', img)
    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 200: # Take 100 face sample and stop video
         break
# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()

mainfile.speak("Face Data Collection Completed, Starting Training on the new data")

os.startfile("C:\\Users\\HP\\Desktop\\New Codings\\btech main project\\trainercode_attempt1.py")