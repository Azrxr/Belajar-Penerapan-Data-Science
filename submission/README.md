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

**Cakupan Proyek**

Proyek ini mencakup:

1. **Exploratory Data Analysis (EDA)**: Analisis mendalam tentang faktor-faktor yang berkorelasi dengan attrition
2. **Data Preparation**: Cleaning, handling missing values, encoding kategori, dan preprocessing data
3. **Predictive Modeling**: Membangun model machine learning untuk memprediksi probabilitas attrition
4. **Business Dashboard**: Visualisasi interaktif di Metabase untuk memonitor faktor penyebab attrition
5. **Prediction Script**: Script Python siap pakai untuk prediksi karyawan baru
6. **Actionable Recommendations**: Rekomendasi strategis berdasarkan temuan analisis

### Persiapan

**Sumber Data**: [employee_data.csv](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee) (1058 records, 34 columns)

**Fitur Target**: Attrition (Binary: Yes/No atau True/False)

**Setup Environment**:

```bash
# Create conda environment
conda create -n dicoding-ml python=3.10

# Install dependencies
pip install -r requirements.txt
```

## Business Dashboard

### Akses Metabase Dashboard

**Metabase credentials untuk reviewer:**

- **URL**: `http://localhost:3000`
- **Email**: `root@mail.com`
- **Password**: `root123`

**Database file**: `metabase.db.mv.db` (terlampir dalam submission)

### Dashboard Contents

Dashboard berisi **8 visualisasi interaktif** yang menampilkan analisis karyawan berdasarkan data bersih:

1. **Total Employees** - Ringkasan total karyawan perusahaan (1,058 Karyawan)
2. **Attrition Distribution** - Persentase karyawan yang keluar (true/16.9%) vs bertahan (false/83.1%)
3. **Attrition by Department** - Analisis jumlah attrition per departemen
4. **Attrition by Job Role** - Distribusi attrition berdasarkan peran kerja/jabatan
5. **Attrition - Overtime Impact** - Perbandingan attrition antara karyawan lembur (true) vs tidak lembur (false)
6. **Attrition by Job Satisfaction** - Hubungan kepuasan kerja (1 - Low s/d 4 - Very High) dengan attrition
7. **Attrition by Work-Life Balance** - Dampak work-life balance (1 - Bad s/d 4 - Best) terhadap attrition
8. **Attrition by Environment Satisfaction** - Hubungan kenyamanan lingkungan kerja dengan attrition

### Interpretasi Dashboard

Berdasarkan dashboard yang telah dibuat, tingginya attrition di Jaya Jaya Maju dipengaruhi oleh beberapa faktor kritis:

- **Tingkat Attrition Saat Ini (16.9%)**: Melebihi batas toleransi perusahaan (>10%).
- **Overtime Berbahaya**: Pekerja yang lembur (OverTime = true) memiliki jumlah attrition yang lebih tinggi dibandingkan yang tidak lembur, mengindikasikan kelelahan (burnout).
- **Departemen Rawan**: Departemen Research & Development dan Sales menyumbang angka attrition terbesar. Pada tingkat jabatan, Laboratory Technician, Sales Executive, dan Research Scientist paling banyak keluar.
- **Kepuasan dan Work-Life Balance**: Pekerja dengan nilai WLB dan Kepuasan yang berada di tingkat tengah hingga rendah (1 dan 2) memiliki kecenderungan tinggi untuk keluar perusahaan.

## Conclusion

### Ringkasan Temuan Analisis

Analisis komprehensif terhadap dataset 1058 karyawan Jaya Jaya Maju mengungkap insight penting tentang faktor-faktor pemicu attrition:

#### 1. **Attrition Rate Saat Ini**

Current attrition rate: **16.9%** (Berdasarkan data: 179 karyawan keluar dari total 1058 karyawan).

Melampaui batas aman perusahaan, sehingga butuh intervensi segera.

#### 2. **Segmentasi Risiko Tinggi**

- **Sales Department & R&D**: Merupakan penyumbang angka keluar terbesar secara kuantitas.
- **Role Berisiko Tinggi**: Laboratory Technician dan Sales Executive adalah posisi paling rentan.
- **Faktor Kesejahteraan**: Work-Life Balance yang buruk dan kewajiban OverTime sangat mendorong keinginan karyawan untuk meninggalkan perusahaan.

#### 3. **Model Predictive Performance**

- **Model Terbaik**: Logistic Regression
- **Accuracy**: 78%
- **ROC-AUC Score**: 0.8373 (Excellent predictive power)
- Model ini dapat diandalkan oleh HR untuk memprediksi secara dini siapa saja yang berisiko keluar di masa depan.

### Kesimpulan Utama

Attrition di Jaya Jaya Maju bukan sekadar masalah kompensasi, melainkan isu struktural yang berkaitan erat dengan beban kerja berlebih (OverTime) dan kurangnya Work-Life Balance. Karyawan di level eksekusi (seperti teknisi dan sales) menjadi korban utama dari sistem kerja yang kurang seimbang ini.

### Rekomendasi Action Items

#### 1. **Prioritas URGENT: Manajemen Beban Kerja & Lembur**

- **Problem**: Karyawan dengan lembur menyumbang jumlah attrition terbanyak.
- **Action**:
  - Audit ulang target kerja harian, khususnya di departemen R&D dan Sales.
  - Implementasikan kebijakan batas maksimal jam lembur per minggu.
  - Tambah jumlah personel di divisi dengan rasio beban kerja tertinggi (contoh: Laboratory Technician).
- **Timeline**: 1-3 bulan
- **Owner**: HR + Department Head

#### 2. **Tingkatkan Work-Life Balance & Kepuasan Lingkungan**

- **Problem**: Karyawan dengan skor Work-Life Balance 1 (Bad) hingga 3 (Better) banyak yang mengalami attrition.
- **Action**:
  - Implementasi jam kerja fleksibel (flexi-time) atau model hybrid-working.
  - Program dukungan kesehatan mental dan kesejahteraan karyawan.
  - Revitalisasi lingkungan kerja agar lebih nyaman dan kolaboratif.
- **Timeline**: 3-6 bulan
- **Owner**: HR + Operations

#### 3. **Implementasi Sistem Prediksi (Early Warning System)**

- **Action**: Gunakan script machine learning (prediction.py) yang telah dibuat untuk mengevaluasi karyawan secara kuartalan. Lakukan wawancara retensi (stay-interview) khusus untuk karyawan yang terdeteksi "Beresiko Tinggi" oleh model sebelum mereka benar-benar keluar.

### Catatan Teknis (Prediction Script Usage)

Untuk memprediksi status attrition karyawan baru atau yang sedang dievaluasi, jalankan script berikut:

```python
from prediction import predict_attrition

# Single employee prediction
employee_data = {
    'Age': 35,
    'MonthlyIncome': 5000,
    'Department': 'Sales',
    'OverTime': 'Yes',
    'JobSatisfaction': 2,
    'WorkLifeBalance': 2,
    'YearsAtCompany': 3,
    'EmployeeNumber': 1001,
    'DistanceFromHome': 10,
    'EnvironmentSatisfaction': 2,
    'Gender': 'Male',
    'JobRole': 'Sales Representative',
    # ... (tambahkan parameter pendukung lainnya)
}

result = predict_attrition(employee_data)
print(f"Attrition Risk: {result['prediction']} ({result['probability']:.1%})")
print(f"Risk Level: {result['risk_level']}")
```
