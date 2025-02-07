import cv2
import face_recognition

img = cv2.imread("Data/putin.jpeg")
rgb_im = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_en = face_recognition.face_encodings(rgb_im)[0]





cv2.imshow("Img", img)
cv2.waitKey(0)