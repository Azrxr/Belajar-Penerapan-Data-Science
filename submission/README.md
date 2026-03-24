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

Proyek ini mengimplementasikan seluruh tahapan data science untuk mengidentifikasi faktor penyebab attrition dan membangun sistem prediksi, termasuk:

- Exploratory Data Analysis (EDA) untuk memahami pola attrition
- Data Preparation dengan cleaning dan preprocessing
- Pembuatan Machine Learning Model untuk prediksi attrition
- Business Dashboard interaktif di Metabase
- Script prediksi untuk identifikasi karyawan berisiko

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

### Ringkasan Temuan

Analisis 1058 karyawan Jaya Jaya Maju menunjukkan attrition rate saat ini **16.9%**, melampaui standar 10%. Faktor utama pemicu attrition:

1. **Beban Kerja Berlebih**: Karyawan yang lembur (OverTime=Yes) menunjukkan attrition signifikan lebih tinggi
2. **Departemen Berisiko**: R&D dan Sales menjadi penyumbang attrition terbesar
3. **Work-Life Balance**: Karyawan dengan skor WLB rendah (1-2) memiliki kecenderungan attrition tinggi
4. **Job Role**: Laboratory Technician dan Sales Executive adalah posisi paling rentan

Model machine learning (Logistic Regression) mencapai accuracy **78%** dan ROC-AUC **0.8373**, dapat diandalkan untuk identifikasi karyawan berisiko tinggi.

### Rekomendasi Action Items

1. **Manajemen Beban Kerja** (1-3 bulan)
   - Audit target kerja di R&D dan Sales
   - Implementasikan batas jam lembur maksimal per minggu
   - Tambah personel di divisi dengan beban kerja tinggi

2. **Peningkatan Work-Life Balance** (3-6 bulan)
   - Sistem jam kerja fleksibel atau hybrid-working
   - Program kesehatan mental dan kesejahteraan karyawan
   - Revitalisasi lingkungan kerja

3. **Early Warning System**
   - Gunakan `prediction.py` untuk evaluasi kuartalan
   - Lakukan stay-interview untuk karyawan berisiko tinggi sebelum mereka pergi
