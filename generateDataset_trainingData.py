# upload package
import cv2,os
import numpy as np
from PIL import Image

# ======================================================================================================================
# GENERATE DATASET
# ======================================================================================================================
cameraId = 1 # Set id camera yang digunakan
video = cv2.VideoCapture(cameraId, cv2.CAP_DSHOW) # inisialisasi Video Webcam

# Deteksi Wajah dengan metode 'haarcascade'
deteksiWajah = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Menentukan ID & Nama & Nomor Gambar
id = input('Masukan ID : ')
nama = input('Masukan Nama : ')
index_img = 0

# Memulai Pengulangan
while True:
    index_img += 1 # Menambahkan nilai index_img sebanyak 1
    sukses, frame = video.read() # Membaca Frame Video
    konversiWarna = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Konversi Warna ke Abu-abu
    lokasiWajah = deteksiWajah.detectMultiScale(konversiWarna,1.3,5) # Mendeteksi Wajah
    # Menyimpan koordinat wajah ke dalam variabel x,y,w,h
    for(x,y,w,h) in lokasiWajah:
        # Menyimpan file Gambar
        cv2.imwrite('DataSet/'+str(nama)+'.'+str(id)+'.'+str(index_img)+'.jpg', konversiWarna[y:y+h,x:x+w])
        # Membuat Bingkai
        cv2.rectangle(frame, (x,y),(x+w,y+h), (0,255,0),2)
    # Menampilkan Webcam
    cv2.imshow('Generate DataSet',frame)
    # Mengakhiri Pengulangan
    if(index_img==30):
        break
# Menutup Webcam dan Aktivasi dari OpenCv
video.release()
cv2.destroyAllWindows()
print('Generate DataSet Success!!')

# ======================================================================================================================
# TRAINING DATA
# ======================================================================================================================
def getImageWithLabels(path):
    ImagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    faceSamples = []
    faceIDs = []
    for Imagepath in ImagePaths:
        PILImage = Image.open(Imagepath).convert('L') # Konversi ke Abu-abu
        imageNp = np.array(PILImage, 'uint8')
        ID = int(os.path.split(Imagepath)[-1].split('.')[1])
        face = deteksiWajah.detectMultiScale(imageNp)
        for (x,y,w,h) in face:
            faceSamples.append(imageNp[y:y + h, x:x + w])
            faceIDs.append(ID)
    return faceSamples, faceIDs
faces, IDs = getImageWithLabels('DataSet')
Facerecognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histogram

Facerecognizer.train(faces, np.array(IDs))
Facerecognizer.save('training.xml')
print(format(len(np.unique(IDs))),'Faces Training Success!!')