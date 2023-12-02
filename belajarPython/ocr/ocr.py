import cv2
from PIL import Image
import numpy as np
import pytesseract

#camera & capture
cap = cv2.VideoCapture(0)
if not (cap.isOpened()):
  print("camera can't opened")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=1, fy=1, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    kernel = np.ones((0,0),np.uint8)
    dilate = cv2.dilate(thresh, kernel, iterations= 1)
    erode = cv2.erode(dilate, kernel, iterations= 1)
    opening = cv2.morphologyEx(erode, cv2.MORPH_OPEN, kernel)
    cv2.imshow('Input', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      gambar = cv2.imwrite('test1.jpg', opening)
      break

cap.release()
cv2.destroyAllWindows()

#simpan gambar & konversi gambar ke teks
text = pytesseract.image_to_string(Image.open('test1.jpg'))
print(text)

#insert to database
import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", 
password = "", database = "python_db")

mycursor = mydb.cursor()
sql = "INSERT INTO `plat_nomor` (`nomor_plat`) VALUES (%s)"
val = (text,)
mycursor.execute(sql, val)
mydb.commit()
print("data ditambahkan")