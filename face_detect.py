import cv2
import sys

# Pass img and cascade names as cli arguments
image_path = sys.argv[1]
casc_path = sys.argv[2]

# create the cascade and initilize with the face cascade
face_cascade = cv2.CascadeClassifier(casc_path)

# read and convert image to grayscale
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(30, 30),  flags = cv2.CASCADE_SCALE_IMAGE)

print("Found {0} faces!".format(len(faces)))

# Draw rect around faces
for x, y, w, h in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)