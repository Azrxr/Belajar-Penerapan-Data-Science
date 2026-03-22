# Ketentuan Submission

## Pengantar
Selamat! Akhirnya Anda telah sampai di Proyek Pertama dari kelas ini. Sejauh ini, Anda telah mengerjakan beberapa studi kasus tentang data science yang umum dijumpai di industri. Good job!

Nah, untuk dapat lanjut ke modul berikutnya, Anda harus mengirimkan submission Proyek Pertama: Menyelesaikan Permasalahan departemen Human Resources (HR). Pada proyek pertama ini, Anda perlu membuat business dashboard untuk membantu departemen HR. Agar lebih memahami proyek ini, mari simak background story dari proyek ini terlebih dahulu.

Peringatan! 
Skenario dalam proyek ini hanyalah fiktif belaka. Apabila terdapat kesamaan nama tokoh, perusahaan, ataupun produk, itu adalah kebetulan semata dan tidak ada unsur kesengajaan.

### Background
Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. 

Walaupun telah menjadi menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%.

Untuk mencegah hal ini semakin parah, manajer departemen HR ingin meminta bantuan Anda mengidentifikasi berbagai faktor yang mempengaruhi tingginya attrition rate tersebut. Selain itu, ia juga meminta Anda untuk membuat business dashboard untuk membantunya memonitori berbagai faktor tersebut. Selain itu, mereka juga telah menyediakan dataset yang dapat Anda unduh melalui tautan berikut: employee_data.csv.

Apakah Anda siap menjawab tantangan tersebut? Tentunya siap dong!

## Kriteria
Terdapat 3 kriteria utama yang harus Anda penuhi dalam mengerjakan proyek submission pertama ini.

Kriteria 1: Menggunakan Templat Proyek yang Telah Disediakan
Pada submission ini, Anda harus menjalankan proyek data science menggunakan template proyek yang telah disediakan. Templat ini dapat Anda unduh melalui tautan berikut: template proyek pertama. Jangan lupa untuk melengkapi dokumen Markdown (.md).

Kriteria 2: Menjalankan Seluruh Proses dalam Proyek Data Science
Mirip seperti berbagai studi kasus sebelumnya, Anda harus melakukan seluruh proses dalam proyek data science mulai dari business understanding sampai deployment (cukup dijalankan di local). Semua tahapan tersebut harus terdokumentasi dengan rapi sesuai dengan template proyek yang telah disediakan. Perlu diingat, tahap modeling, evaluation, dan deployment hanya dilakukan jika Anda membuat model machine learning. Selain itu, pastikan untuk menyertakan kesimpulan atau conclusion pada berkas Markdown (.md) sebagai jawaban dari permasalahan yang dihadapi departemen HR.

Kriteria 3: Membuat Minimal Satu Business Dashboard
Pada proyek ini, Anda diminta untuk membuat minimal satu business dashboard untuk membantu departemen HR dalam memahami data dan memonitor berbagai faktor yang mempengaruhi tingginya attrition rate. Pada prosesnya, Anda dapat menggunakan metabase sebagai tool utama. Pastikan untuk menyertakan username dan password pada berkas Markdown (.md). Sebagai alternatif, Anda dapat menggunakan email “root@mail.com” dan password “root123”. Setelah selesai membuat dashboard, Anda perlu mengekspor dashboard beserta database instance dari container metabase. Hal ini dapat Anda lakukan dengan menjalankan perintah berikut (perintah di bawah ini mengasumsi nama container yang Anda buat adalah metabase).

```
docker cp metabase:/metabase.db/metabase.db.mv.db ./
```
Sebagai alternatif, Anda juga dapat menggunakan berbagai tools lain seperti tableau public ataupun looker studio. Jika menggunakan kedua tools tersebut, pastikan Anda menyertakan link untuk mengakses dashboard yang telah dibuat.

Perlu diingat, bahwa dashboard yang Anda buat dianggap tidak valid jika hanya menampilkan data dalam bentuk tabel tanpa adanya visualisasi data yang mudah dipahami. Selain itu, dashboard tersebut dianggap tidak valid jika tidak menampilkan faktor yang mempengaruhi tingginya attrition rate. Selain itu, pastikan juga dashboard yang Anda buat dapat diakses oleh reviewer (jika menggunakan tableau public ataupun looker studio). 

## Penilaian
Submission Anda akan dinilai oleh Reviewer guna menentukan kebenaran submission yang dikerjakan. Supaya bisa lulus dari kelas ini, proyek Anda mesti memenuhi seluruh kriteria yang ada. Apabila ada ketentuan dalam kriteria yang belum terpenuhi, proyek Anda akan kami tolak.

Submission Anda akan dinilai oleh Reviewer dengan penilaian bintang berskala 1-5. Untuk mendapatkan nilai tinggi, Anda bisa menerapkan beberapa saran berikut:

1. Membuat video singkat (maksimal 5 menit). Video tersebut harus menjelaskan beberapa poin berikut.
2. Menjelaskan business dashboard yang telah dibuat.
    - Menjelaskan kesimpulan atau conclusion dari dashboard tersebut.
    - Memberikan beberapa rekomendasi action items untuk yang dapat diikuti oleh perusahaan untuk mencapai target mereka.
3. Membuat visualisasi data yang baik dan efektif dengan menerapkan prinsip desain dan integritas.
4. Membuat model machine learning untuk membantu departemen HR. Pastikan Anda membuat script Python sederhana untuk menjalankan proses prediksi.
5. Berikut adalah detail penilaian submission.

rating-default-1
Semua ketentuan wajib terpenuhi, tetapi terdapat indikasi kecurangan atau plagiasi dalam mengerjakan submission.

rating-default-2
Semua ketentuan wajib terpenuhi, tetapi tidak menerapkan saran sama sekali.

rating-default-3
Semua ketentuan wajib terpenuhi dan menerapkan minimal 1 saran di atas.

rating-default-4
Semua ketentuan wajib terpenuhi dan menerapkan minimal 2 saran di atas.

rating-default-5
Semua ketentuan wajib terpenuhi dan menerapkan semua saran di atas.

Catatan:

Jika submission Anda ditolak maka tidak ada penilaian. Kriteria penilaian bintang di atas hanya berlaku jika submission Anda lulus.

## Lainnya

### Tips
Berikut beberapa tips yang perlu Anda perhatikan.

Berikut merupakan beberapa cheat sheet yang dapat membantu Anda dalam mengerjakan proyek ini.
- [Pandas cheat sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [Matplotlib cheat sheet](https://matplotlib.org/cheatsheets/_images/cheatsheets-1.png)
- [Seaborn cheat sheet](https://www.kaggle.com/code/themlphdstudent/cheat-sheet-seaborn-charts)
- [Tableau cheat sheet](https://towardsdatascience.com/the-ultimate-cheat-sheet-on-tableau-charts-642bca94dde5)
- [The Ultimate Guide to Google Looker Studio 2023](https://bymarketers.co/the-ultimate-guide-to-google-data-studio/)
- [Metabase documentation](https://www.metabase.com/docs/latest/)
Berikut merupakan panduan dalam pembuatan berkas markdown (.md): Github Guides: Mastering Markdown.


### Ketentuan Pengiriman Submission
Berikut merupakan beberapa poin yang perlu diperhatikan ketika mengirimkan submission.

1. Berkas submission yang dikirim merupakan folder proyek submission akhir dalam format ZIP. Ia mengandung beberapa berkas seperti berikut.
    - Berkas Jupyter Notebook atau Colab Notebook (.ipynb). Pastikan berkas notebook tersebut sudah dijalankan.
    - Berkas requirements.txt yang berisi berbagai library yang digunakan dalam proses analisis data. Berikut contoh berkas requirements yang digunakan pada proyek latihan: contoh_requirements.txt.
    - Berkas Markdown (.md) yang berisi dokumentasi proyek dan action items (optional).
    - Screenshot business dashboard yang telah dibuat dengan nama: <username_dicoding>-dashboard. Screenshot yang dilampirkan berupa file image dengan format JPG/JPEG atau PNG.
    - Menyertakan seluruh kebutuhan (dependencies) untuk menjalankan proyek data science, seperti model (jika menerapkan saran keempat), module, Dockerfile, dll.
    - Berkas metabase.db.mv.db.
2. Jika menerapkan saran pertama, lampirkan video singkat Anda pada folder submission dengan nama: <username_dicoding>-video. Pastikan video tersebut memiliki ukuran yang masuk akal.
3. Jika Anda menerapkan saran kedua, lengkapi bagian Rekomendasi Action Items pada berkas Markdown (.md).
4. Apabila Anda menerapkan saran keempat, lampirkan berkas model yang telah Anda latih. Jangan lupa sertakan juga script Python untuk menjalankan proses prediksi beserta cara penggunaannya yang ditulis pada berkas Markdown (.md).


### Format Berkas Submission
Berkas submission yang dikirimkan merupakan sebuah folder yang disimpan dalam bentuk ZIP. Folder berisi beberapa berkas seperti berikut.

- Berkas Jupyter Notebook atau Colab Notebook (.ipynb).
- Berkas requirements.txt.
- Berkas Markdown (.md).
- Berkas metabase.db.mv.db jika membuat dashboard dengan metabase.
- Screenshot business dashboard: <username_dicoding>-dashboard.
- Video singkat jika menerapkan saran pertama.
- Berkas Python (.py) jika menerapkan saran keempat.
- Berkas model machine learning jika menerapkan saran keempat.
- Berikut merupakan struktur direktori submission yang kami sarankan.

submission
├───model
├───notebook.ipynb
├───prediction.py
├───README.md
├───<username_dicoding>-dashboard
├───<username_dicoding>-video
├───metabase.db.mv.db
└───requirements.txt


Submission Anda akan Ditolak bila
Kriteria wajib tidak terpenuhi.
Ketentuan berkas submission tidak terpenuhi.
Melakukan kecurangan seperti tindakan plagiarisme.


Forum Diskusi
Jika mengalami kesulitan, Anda bisa menanyakan langsung ke forum diskusi https://www.dicoding.com/academies/590/discussions. 

Ketentuan Proses Review
Beberapa hal yang perlu Anda ketahui mengenai proses review:

Tim Reviewer akan mengulas submission Anda dalam waktu selambatnya 3 (tiga) hari kerja (tidak termasuk Sabtu, Minggu, dan hari libur nasional).
Tidak disarankan untuk melakukan submit berkali-kali karena akan memperlama proses penilaian.
Anda akan mendapatkan notifikasi hasil review submission via email. Status submission juga bisa dilihat dengan mengecek di halaman submission