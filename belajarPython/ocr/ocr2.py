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
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imshow('Input', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      cv2.imwrite('test1.jpg', frame)
      break

cap.release()
cv2.destroyAllWindows()

image = 'test1.jpg'
img = cv2.imread(image)

if img is None:
  print('Image not found')
  exit()

#filters
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
kernel = np.ones((0,0),np.uint8)
dilate = cv2.dilate(thresh, kernel, iterations= 1)
erode = cv2.erode(dilate, kernel, iterations= 1)
opening = cv2.morphologyEx(erode, cv2.MORPH_OPEN, kernel)

#simpan gambar & konversi gambar ke teks
status = cv2.imwrite('image1.jpg', opening)
text = pytesseract.image_to_string(Image.open('image1.jpg'))
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
# def get_grayscale(image):
#   return cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

# def remove_noise(image):
#   return cv2.medianBlur(image, 5)

# def thresholding(image):
#     return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# def opening(image):
#     kernel = np.ones((5,5),np.uint8)
#     return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# def canny(image):
#     return cv2.Canny(image, 100, 200)

# thresh = thresholding(gray)
# opening = opening(gray)
# canny = canny(gray)
# import random
# while decide:
#   angkaSaya = str(input("Masukkan angka anda : "));
#   angkaKomputer = str(random.randint(1, 10));
#   print('angka anda : ' + angkaSaya)
#   print('angka yang sebenarnya ' + angkaKomputer)

#   if angkaSaya == angkaKomputer : print('tebakkan benar')
#   else : print('tebakkan salah')

#   decide = print('ulang ? [y/n] : ')
#   if(decide == 'y'):
#     continue
#   else : exit

