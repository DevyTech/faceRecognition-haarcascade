import cv2,os

cameraId = 1 # Set id camera yang digunakan
video = cv2.VideoCapture(cameraId, cv2.CAP_DSHOW) # inisialisasi Video Webcam

# Deteksi Wajah dengan metode 'haarcascade'
deteksiWajah = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('training.xml')

# path = 'DataSet'
# className = ['Unknown']
# listImg = os.listdir(path)
# for cls in listImg:
#     className.append(os.path.split(cls)[-1].split('.')[0])
# print(listImg)
# print(className)

while True:
    sukses, frame = video.read()  # Membaca Frame Video
    konversiWarna = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Konversi Warna ke Abu-abu
    lokasiWajah = deteksiWajah.detectMultiScale(konversiWarna, 1.3, 5)  # Mendeteksi Wajah
    for (x, y, w, h) in lokasiWajah:
        # Membuat Bingkai
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        id, conf = recognizer.predict(konversiWarna[y:y+h, x:x+w])
        confText = "{0}%".format(round(100 - conf)) # Jika nilai confidence dibawah 50% maka kecocokan Wajah bernilai True
        cv2.putText(frame, 'Face ID'+str(id), (x + 6, y - 6), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0),2) # Memasukan Text Nama
        cv2.putText(frame, str(confText), (x + 6, y + h - 7), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 2) # Memasukan Text confidence
    cv2.imshow("Face Recognation", frame)
    key = cv2.waitKey(1)
    if key == ord('s'):
        break
video.release()
cv2.destroyAllWindows()