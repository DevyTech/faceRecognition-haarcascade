# Versi Python 3.10
> Gunakan python interpreter 3.10||
> Ubah pengaturan python interpreter pada ***File/Settings(Ctrl+Alt+S)/Project:Face Recognition/Python Interpreter/
> Add Interpreter/Add Local Interpreter/(pilih versi Python 3.10)***
# Install Package
### pip install --upgrade pip
> Upgrade terlebih dahulu pip
### pip install open-cv
> Install opencv untuk menyiapkan camera, mendeteksi wajah, konversi warna, menyimpan image, membuat bingkai
### pip install opencv-contrib-python
> Install opencv-contib-python untuk menggunakan Local Binary Patterns Histogram (LBPH) untuk mendeteksi wajah yang akan di training
### pip install Pillow
> Install Pillow untuk penggunaan properti Image
# Run
### run ***generateDataset_trainingData.py***
> Masukan ID dan Nama setelah itu data wajah akan direkam dan disimpan ke dalam DataSet 
> setelah itu akan melakukan training data wajah
### run ***faceRecognition.py***
> Untuk Mendekteksi Kecocokan Wajah yang sudah direkam ke dalam DataSet
