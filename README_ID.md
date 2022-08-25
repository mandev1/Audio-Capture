# Audio Capture
Source Code of Audio Capture for Smart Speaker

## Pendahuluan
Audio capture merupakan salah satu teknik yang digunakan untuk
mendapatkan informasi dari korban dengan memanfaatkan mikrofon. Teknik ini
memanfaatkan layanan pengolahan suara yang ada di dalam smart speaker untuk
merekam suara secara diam-diam.


## Cara Kerja
Cara kerjanya adalah dengan mengaktifkan fitur mikrofon pada perangkat,
khususnya pada smart speaker yang sudah mendapatkan program ini dan dapat
merekam secara diam-diam. Program ini juga dijadikan jalur komunikasi smart
speaker menuju pelaku kejahatan untuk mengirimkan hasil pembicaraan yang sudah
direkam.

![image](https://user-images.githubusercontent.com/101856662/186625480-f2517078-69fa-4823-a7d3-4dc0d77e3299.png)

## Source Code
Program audio capture menggunakan sistem skills dan client dan diprogram
dengan menggunakan bahasa pemrograman python. Program skills bertugas untuk
menerima suara yang didengar oleh smart speaker, untuk mendapat informasi dari
pengguna. Skills ini dimasukkan ke dalam smart speaker dan didaftarkan sebagai
layanan yang tersedia untuk smart speaker. Program client digunakan untuk menerima hasil dari audio capture 
pada smart speaker.


### Client side
Program client dimasukkan dan dijalankan pada smart speaker untuk
menerima instruksi merekam, lalu hasil rekaman yang diterima dikirmkan melalui
jaringan menuju oleh CnC.

![image](https://user-images.githubusercontent.com/101856662/186627108-782a59f9-d891-4dba-85c9-b7827143e1d0.png)

### Server Side
Skills secara diam-diam mendegarkan semua pembicaraan yang terjadi di sekitar
smart speaker dan data percakapan tersebut disimpan dan dikirimkan secara berkala
ke CnC.
Setiap ada jeda pembicaraan, data rekaman sebelumnya langsung ditampung
dalam sebuah variabel dan dikirimkan ke CnC via tautan yang sudah di setting
dimasukkan ke dalam skills. Setiap selesai mengirim data pembicaraan sebelumnya,
skills terus melanjutkan tugasnya untuk merekam percakapan selanjutnya dan
dikirimkan lagi ke CnC. Cara kerja skills dijelaskan pada Gambar dibawah.

![image](https://user-images.githubusercontent.com/101856662/186626036-68364cf2-368d-401a-a6d0-ba49e5c3bb59.png)

## Hasil
### Nama Kota
![audio_capture(city)](https://user-images.githubusercontent.com/101856662/186627818-a8154a9b-7586-45a4-9887-0f943e5718c6.PNG)

### Nama Negara
![audio_capture(country)](https://user-images.githubusercontent.com/101856662/186627828-6e925903-4707-469c-b970-2a3e09e060af.PNG)

### Nomor Telepon
![audio_capture(num_phonenum)](https://user-images.githubusercontent.com/101856662/186627831-657d095a-5b53-473e-b706-1e0551a7277e.PNG)

### Nama Orang
![audio_capture(person)](https://user-images.githubusercontent.com/101856662/186627836-7afbbb14-2774-4639-816a-9496471812f5.PNG)

### Kode Pin
![audio_capture(pin)](https://user-images.githubusercontent.com/101856662/186627839-b937fd85-7806-403b-8834-370d0a9ddd95.PNG)


## Informasi
Semua Hasil Audio capture terdapat pada folder result
