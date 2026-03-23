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
2. **Data Preparation**: Cleaning, encoding, dan preprocessing data karyawan
3. **Predictive Modeling**: Membangun model machine learning untuk memprediksi attrition
4. **Business Dashboard**: Visualisasi interaktif di Metabase untuk monitoring attrition metrics
5. **Prediction Script**: Tools untuk prediksi attrition karyawan baru
6. **Actionable Recommendations**: Rekomendasi strategis berdasarkan temuan analisis

### Persiapan

**Sumber Data**: employee_data.csv (1058 records, 34 columns)

**Fitur Target**: Attrition (Binary: Yes/No)

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

**Database file**: `metabase.db.mv.db` (included dalam submission)

### Dashboard Contents

Dashboard berisi **8 visualisasi interaktif** yang menampilkan faktor-faktor attrition:

1. **Total Employees** - Ringkasan jumlah karyawan
2. **Attrition Distribution** - Perbandingan retained vs attrition
3. **Attrition by Department** - Count attrition per department
4. **Attrition by Job Role** - Count attrition per job role (sorted top)
5. **Attrition - Overtime Impact** - Count attrition filtered by overtime
6. **Attrition by Job Satisfaction** - Count attrition per satisfaction level (1-4)
7. **Attrition by Work-Life Balance** - Count attrition per WLB rating (1-4)
8. **Attrition by Environment Satisfaction** - Count attrition per environment satisfaction

### Visualisasi Dashboard

Dashboard mencakup 8 visualisasi utama:

1. **Attrition Overview**:
   - Total attrition rate (12.18% based on data = 179/1470)
   - Perbandingan jumlah karyawan retained vs attrition

2. **Attrition by Department**:
   - Sales: Highest attrition
   - HR: Medium attrition
   - R&D: Lowest attrition

3. **Attrition by Job Role**:
   - Sales Representative: HIGHEST (43.1%)
   - Research Scientist: High (26.1%)
   - Manager: Low (6.3%)

4. **Impact of Overtime**:
   - OverTime (Yes): 31.9% attrition
   - OverTime (No): 10.8% attrition

5. **Job Satisfaction Effect**:
   - Low Satisfaction: 22.4% attrition
   - High Satisfaction: Lower attrition

6. **Environment Satisfaction**:
   - Low Satisfaction: 27.3% attrition
   - High Satisfaction: 12.7% attrition

7. **Work-Life Balance Impact**:
   - Low Balance: 32.1% attrition
   - High Balance: Lower attrition

8. **Job Involvement & Attrition**:
   - Low Involvement: 40.0% attrition
   - High Involvement: 9.5% attrition

### Interpretasi Dashboard

Dashboard menunjukkan bahwa attrition di Jaya Jaya Maju dipicu oleh kombinasi faktor yang kompleks:

- **Faktor Utama**: Overtime, job satisfaction, environment satisfaction, dan work-life balance
- **Departemen Berisiko**: Sales department memiliki attrition rate tertinggi
- **Role Berisiko**: Sales Representatives paling susceptible terhadap attrition
- **Pola**: Karyawan dengan engagement dan satisfaction rendah cenderung untuk keluar
- **Overtime Critical**: Karyawan dengan overtime 3x lebih likely untuk attrition

## Conclusion

### Ringkasan Temuan Analisis

Analisis komprehensif terhadap dataset 1058 karyawan Jaya Jaya Maju mengungkap insight penting tentang faktor-faktor pemicu attrition:

#### 1. **Attrition Rate Saat Ini**

- Current attrition rate: **16.9%** (12.18% berdasarkan data)
- Melampaui target >10% yang menjadi masalah perusahaan
- 179 dari 1058 karyawan telah keluar

#### 2. **Top 5 Faktor Pemicu Attrition** (berdasarkan korelasi dan analisis)

| Ranking | Faktor                          | Impact               | Correlation |
| ------- | ------------------------------- | -------------------- | ----------- |
| 1       | Job Involvement rendah          | 40% attrition rate   | -0.150      |
| 2       | Work-Life Balance rendah        | 32.1% attrition rate | -0.059      |
| 3       | Overtime (Yes)                  | 31.9% attrition rate | Categorical |
| 4       | Environment Satisfaction rendah | 27.3% attrition rate | -0.132      |
| 5       | Job Satisfaction rendah         | 22.4% attrition rate | -0.091      |

#### 3. **Segmentasi Risiko Tinggi**

- **Sales Department**: 20.7% attrition (tertinggi dibanding departemen lain)
- **Sales Representatives**: 43.1% attrition rate (role paling berisiko)
- **Single/Unmarried**: 26.7% attrition (status marital berpengaruh)
- **Junior Levels (Level 1)**: Attrition rate lebih tinggi

#### 4. **Model Predictive Performance**

- **Model Terbaik**: Logistic Regression
- **Accuracy**: 78%
- **ROC-AUC Score**: 0.8373 (excellent predictive power)
- **Recall untuk Attrition**: 69% (dapat mendeteksi 69% karyawan yang akan keluar)

#### 5. **Faktor Protektif (Retention)**

- **Higher Job Involvement**: 9.5% attrition (vs 40% untuk low)
- **Higher Monthly Income**: Negative correlation (-0.163)
- **Longer Tenure at Company**: Negative correlation (-0.135)
- **Higher Job Level**: Negative correlation (-0.169)

### Kesimpulan Utama

Atrition di Jaya Jaya Maju bukan single-factor problem melainkan kombinasi dari:

1. **Engagement rendah** (job involvement, job satisfaction)
2. **Work quality rendah** (overtime excessive, work-life balance poor)
3. **Environmental factors** (environment satisfaction, departemen/role)
4. **Career progression** (job level, years since promotion)

Perusahaan perlu mengambil tindakan holistik yang mencakup program engagement, workload management, dan career development untuk meningkatkan retention.

### Rekomendasi Action Items

#### 1. **Prioritas URGENT: Kurangi Overtime Beban Kerja** (Potential Impact: -8-10% attrition)

- **Problem**: Karyawan dengan overtime memiliki 3x lebih tinggi attrition (31.9% vs 10.8%)
- **Action**:
  - Audit workload di Sales department dan departemen dengan overtime tinggi
  - Implementasi flexible working hours atau work-from-home
  - Tambah headcount di tim dengan overtime excessive
  - Monitoring overtime dengan target maksimal 10% karyawan per bulan
- **Timeline**: 1-3 bulan
- **Owner**: HR + Department Head

#### 2. **Tingkatkan Job Involvement dan Engagement** (Potential Impact: -10-15% attrition)

- **Problem**: Low job involvement = 40% attrition (tertinggi semua faktor)
- **Action**:
  - Program career development dan skill enhancement untuk junior staff
  - Employee recognition program (monthly awards)
  - Employee involvement dalam decision-making (suggestion boxes, town halls)
  - Mentoring program antara senior dan junior staff
  - Clear career path progression
- **Timeline**: 2-6 bulan
- **Owner**: HR + L&D Department
- **KPI**: Job involvement score improvement dari Likert 1→3+

#### 3. **Improve Work-Life Balance Initiatives** (Potential Impact: -6-8% attrition)

- **Problem**: Poor work-life balance dikaitkan dengan 32.1% attrition rate
- **Action**:
  - Establish work-life balance policy (no after-hours emails, minimum 8 hours rest)
  - Mental health support program (counseling, wellness)
  - Quarterly town hall on well-being
  - Flexible leave policy dan paid time-off
  - Gym membership atau wellness benefits
- **Timeline**: 1-2 bulan (policy), ongoing (implementation)
- **Owner**: HR + Operations
- **KPI**: Work-life balance score measurement

#### 4. **Focus Retention di Sales Department** (Potential Impact: -5-7% attrition)

- **Problem**: Sales = 20.7% attrition, Sales Rep = 43.1% (critical)
- **Action**:
  - Sales-specific incentive review (commission structure, bonuses)
  - Sales mentoring/coaching program
  - Career path clarity untuk sales career progression
  - Recognition of good performers
  - Sales support tools untuk reduce administrative burden
- **Timeline**: 1-2 bulan
- **Owner**: Sales Director + HR

#### 5. **Enhance Environment Satisfaction** (Potential Impact: -4-6% attrition)

- **Problem**: Low environment satisfaction = 27.3% attrition
- **Action**:
  - Office environment improvement (ergonomics, office comfort)
  - Team building activities
  - Department culture initiatives
  - Workspace customization
  - Open communication from management
- **Timeline**: 1-3 bulan (depending on scale)
- **Owner**: Facilities + HR

#### 6. **Implement Predictive Attrition Model** (Systemic Change)

- **Action**:
  - Use the trained ML model untuk identify at-risk employees quarterly
  - Proactive intervention untuk identified high-risk employees
  - Track model performance dan refine
  - Integrate dengan HR system untuk early warning
- **Timeline**: Ongoing
- **Owner**: HR + Data Analytics team
- **Output**: Quarterly risk reports

### KPI untuk Monitoring Progres

| KPI                       | Baseline | Target (6 bulan) | Target (12 bulan) |
| ------------------------- | -------- | ---------------- | ----------------- |
| Attrition Rate            | 16.9%    | 13-14%           | <10%              |
| Overtime headcount        | TBD      | <10%             | <5%               |
| Avg Job Involvement Score | Low      | Medium           | High/Very High    |
| Work-Life Balance Score   | Low      | Medium           | High              |
| Environment Satisfaction  | Low      | Medium           | High              |
| Sales Dept Attrition      | 20.7%    | 16-17%           | <12%              |
| Sales Rep Attrition       | 43.1%    | 30%              | <20%              |

### Investment & ROI

- **Cost of Implementation**: ~Rp 200-300 juta (initiatives + tools)
- **Cost per Attrition**: ~Rp 50-100 juta (replacement + training + lost productivity)
- **Expected Benefit**: Reduction dari 16.9% → 10% = 73 fewer attritions × Rp 75 juta = **~Rp 5.5 Billion annually saved**
- **ROI**: **15-25x dalam tahun pertama**

### Catatan Teknis

**Prediction Script Usage**:

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
    # ... tambahkan semua 33 features
}

result = predict_attrition(employee_data)
print(f"Attrition Risk: {result['prediction']} ({result['probability']:.1%})")
print(f"Risk Level: {result['risk_level']}")

# Batch prediction
df_employees = pd.read_csv('employees.csv')
results = predict_attrition(df_employees)
high_risk = results[results['attrition_probability'] > 0.7]
```

Model dapat digunakan untuk:

1. Prediksi attrition untuk new hires candidates
2. Quarterly risk assessment untuk existing employees
3. Performance monitoring dan validation
