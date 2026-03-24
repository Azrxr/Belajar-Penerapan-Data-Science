# Proyek Akhir: Solusi Analisis Attrition Karyawan - Jaya Jaya Maju

## Business Understanding

### Latar Belakang

**Jaya Jaya Maju** adalah perusahaan multinasional yang didirikan tahun 2000 dengan lebih dari 1000 karyawan tersebar di seluruh nusantara. Meskipun telah menjadi perusahaan besar, perusahaan masih menghadapi tantangan signifikan dalam manajemen karyawan.

### Permasalahan Bisnis

- **Attrition Rate Tinggi**: Tingkat attrition karyawan mencapai lebih dari 10%, yang menunjukkan tingginya turnover (perputaran) karyawan
- **Dampak Negatif**: Attrition tinggi mengakibatkan:
  - Biaya replacement dan training yang tinggi
  - Hilangnya institutional knowledge
  - Penurunan produktivitas
  - Menurunnya moral tim yang tersisa
- **Kebutuhan Identifikasi**: Perlunya identifikasi faktor-faktor yang mempengaruhi attrition untuk implementasi strategi retensi

### Cakupan Proyek

Proyek ini akan menganalisis data karyawan untuk menemukan pola attrition dan membangun Business Dashboard interaktif. Dashboard tersebut dibuat untuk menjawab daftar pertanyaan bisnis berikut:

- Berapa persentase attrition rate perusahaan saat ini?
- Departemen dan peran (Job Role) mana yang menyumbang angka attrition tertinggi?
- Apakah beban kerja seperti lembur (OverTime) berdampak langsung terhadap keputusan karyawan untuk keluar?
- Bagaimana pengaruh tingkat kesejahteraan karyawan (Job Satisfaction, Environment Satisfaction, & Work-Life Balance) terhadap tingkat attrition?

### Persiapan

**Sumber data**: [employee_data.csv](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee) (1058 karyawan dengan 34 fitur)

**Setup environment**:

```bash
# Buat conda environment
conda create -n dicoding-ml python=3.10

# Aktifkan environment
conda activate dicoding-ml

# Install dependencies
pip install -r requirements.txt

# Jalankan notebook
jupyter notebook notebook.ipynb
```

## Business Dashboard

Dashboard Metabase dengan 8 visualisasi interaktif menampilkan faktor-faktor penyebab attrition:

1. **Total Employees** - Ringkasan total karyawan perusahaan
2. **Attrition Distribution** - Distribusi karyawan keluar vs bertahan
3. **Attrition by Department** - Analisis per departemen
4. **Attrition by Job Role** - Distribusi berdasarkan jabatan
5. **Attrition - Overtime Impact** - Dampak lembur pada attrition
6. **Attrition by Job Satisfaction** - Hubungan kepuasan kerja dengan attrition
7. **Attrition by Work-Life Balance** - Dampak work-life balance pada attrition
8. **Attrition by Environment Satisfaction** - Hubungan kenyamanan lingkungan kerja dengan attrition

**Cara akses**:

- URL: `http://localhost:3000`
- Email: `root@mail.com`
- Password: `root123`
- Database: `metabase.db.mv.db` (include dalam submission)

## Conclusion

Berdasarkan analisis data, disimpulkan bahwa:
- Attrition rate saat ini mencapai 16.9%, jauh melampaui batas toleransi perusahaan (10%).
- Faktor beban kerja sangat kritis: Karyawan yang diwajibkan lembur (OverTime=Yes) memiliki jumlah attrition yang paling tinggi.
- Departemen R&D dan Sales (khususnya Laboratory Technician dan Sales Executive) adalah kelompok paling rentan untuk keluar.
- Skor kesejahteraan (WLB dan Environment Satisfaction) yang rendah berkontribusi besar pada keputusan karyawan untuk resign.

Model Machine Learning (Logistic Regression) yang dibangun berhasil mencapai akurasi 78% dengan ROC-AUC 0.8373, membuktikan bahwa model ini layak digunakan untuk memprediksi probabilitas keluarnya karyawan.

### Rekomendasi Action Items

Berikut adalah beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan tingginya attrition:
- Action item 1: Melakukan audit beban kerja dan menerapkan kebijakan batas jam lembur maksimal per minggu, khususnya di departemen Sales dan R&D.
- Action item 2: Mengimplementasikan sistem jam kerja fleksibel (flexi-time) atau hybrid-working untuk meningkatkan skor Work-Life Balance karyawan.
- Action item 3: Menggunakan script prediksi ML (prediction.py) secara kuartalan untuk mendeteksi dini karyawan yang berisiko keluar, lalu melakukan stay-interview sebelum mereka benar-benar pergi.
