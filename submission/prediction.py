"""
Script untuk prediksi attrition karyawan menggunakan trained model.
Gunakan script ini untuk memprediksi apakah seorang karyawan akan keluar dari perusahaan.
"""

import pandas as pd
import numpy as np
import joblib
import os
import sys
import warnings
warnings.filterwarnings('ignore')

# Load model dan scaler
model_dir = os.path.join(os.path.dirname(__file__), 'model')
model = joblib.load(os.path.join(model_dir, 'trained_model.pkl'))
scaler = joblib.load(os.path.join(model_dir, 'scaler.pkl'))
label_encoders = joblib.load(os.path.join(model_dir, 'label_encoders.pkl'))

# Load training data untuk reference feature names dan means
try:
    df_train_ref = pd.read_csv(os.path.join(os.path.dirname(__file__), '..', 'employee_data.csv'))
    # Encode training reference data
    for col in label_encoders.keys():
        if col in df_train_ref.columns:
            df_train_ref[col] = label_encoders[col].transform(df_train_ref[col].astype(str))
    if 'Attrition' in df_train_ref.columns:
        df_train_ref = df_train_ref.drop('Attrition', axis=1)
    if 'EmployeeId' in df_train_ref.columns:
        df_train_ref = df_train_ref.drop('EmployeeId', axis=1)
    
    REQUIRED_FEATURES = df_train_ref.columns.tolist()
    FEATURE_MEANS = df_train_ref.mean(numeric_only=True).to_dict()
except:
    # Fallback jika gagal load training data
    REQUIRED_FEATURES = None
    FEATURE_MEANS = {}


def predict_attrition(data):
    """
    Prediksi attrition untuk satu atau lebih karyawan.
    
    Parameters:
    -----------
    data : dict atau pd.DataFrame
        Data karyawan untuk prediksi.
        Untuk single prediction: dict dengan columns sebagai keys
        Untuk multiple predictions: DataFrame
    
    Returns:
    --------
    dict atau DataFrame
        Berisi prediksi (0 atau 1) dan probability
    
    Examples:
    ---------
    # Single prediction - minimal features
    employee_data = {
        'Age': 35,
        'MonthlyIncome': 5000,
        'Department': 'Sales',
        'OverTime': 'Yes',
        'JobSatisfaction': 2,
        'WorkLifeBalance': 2,
        'YearsAtCompany': 3,
    }
    result = predict_attrition(employee_data)
    print(result)
    
    # Multiple predictions dari CSV
    df_employees = pd.read_csv('employees.csv')
    results = predict_attrition(df_employees)
    """
    
    # Convert ke DataFrame jika dict
    is_dict_input = isinstance(data, dict)
    if is_dict_input:
        df_input = pd.DataFrame([data])
    else:
        df_input = data.copy()
    
    # Encode categorical variables menggunakan label encoders
    categorical_features = ['Gender', 'Department', 'JobRole', 'MaritalStatus', 'OverTime',
                           'BusinessTravel', 'EducationField']
    
    for col in categorical_features:
        if col in df_input.columns and col in label_encoders:
            try:
                df_input[col] = label_encoders[col].transform(df_input[col].astype(str))
            except Exception as e:
                pass  # Silently fail jika ada issue encoding
    
    # Drop columns yang tidak digunakan
    if 'EmployeeId' in df_input.columns:
        df_input = df_input.drop('EmployeeId', axis=1)
    if 'Attrition' in df_input.columns:
        df_input = df_input.drop('Attrition', axis=1)
    
    # Ensure semua required features ada
    # Jika REQUIRED_FEATURES berhasil di-load, align features
    if REQUIRED_FEATURES:
        for feature in REQUIRED_FEATURES:
            if feature not in df_input.columns:
                # Fill dengan mean dari training data jika ada
                if feature in FEATURE_MEANS:
                    df_input[feature] = FEATURE_MEANS[feature]
                else:
                    df_input[feature] = 0
        
        # Keep hanya required features dalam urutan yang sama
        df_input = df_input[REQUIRED_FEATURES]
    
    # Handle missing values dengan mean dari training
    for col in df_input.columns:
        if df_input[col].isnull().any():
            if col in FEATURE_MEANS:
                df_input[col].fillna(FEATURE_MEANS[col], inplace=True)
            else:
                df_input[col].fillna(df_input[col].mean(), inplace=True)
    
    # Ensure numeric dtype
    df_input = df_input.astype(np.float64)
    
    # Scaling features
    df_scaled = scaler.transform(df_input)
    
    # Predict
    predictions = model.predict(df_scaled)
    probabilities = model.predict_proba(df_scaled)[:, 1]
    
    # Prepare results
    if isinstance(data, dict):
        return {
            'prediction': 'Yes' if predictions[0] == 1 else 'No',
            'probability': float(probabilities[0]),
            'risk_level': get_risk_level(probabilities[0])
        }
    else:
        results_df = df_input.copy() if isinstance(data, pd.DataFrame) else data.copy()
        results_df['attrition_prediction'] = ['Yes' if p == 1 else 'No' for p in predictions]
        results_df['attrition_probability'] = probabilities
        results_df['risk_level'] = [get_risk_level(p) for p in probabilities]
        return results_df


def get_risk_level(probability):
    """
    Kategori risiko berdasarkan probability.
    
    Parameters:
    -----------
    probability : float
        Probability attrition (0-1)
    
    Returns:
    --------
    str
        Kategori risiko: 'Low', 'Medium', 'High'
    """
    if probability < 0.3:
        return 'Low'
    elif probability < 0.7:
        return 'Medium'
    else:
        return 'High'


def get_feature_description():
    """
    Deskripsi fitur yang diperlukan untuk prediksi.
    
    Returns:
    --------
    dict
        Mapping nama feature dengan deskripsinya
    """
    features = {
        'Age': 'Umur karyawan (tahun)',
        'MonthlyIncome': 'Pendapatan bulanan (Rp)',
        'Department': 'Departemen (HR, R&D, Sales)',
        'OverTime': 'Overtime (Yes/No)',
        'JobSatisfaction': 'Kepuasan pekerjaan (1-4, Low-Very High)',
        'EnvironmentSatisfaction': 'Kepuasan lingkungan kerja (1-4)',
        'WorkLifeBalance': 'Work-life balance (1-4)',
        'YearsAtCompany': 'Tahun di perusahaan',
        'YearsInCurrentRole': 'Tahun di posisi saat ini',
        'JobRole': 'Job role (Sales Executive, Research Scientist, dll)',
        'Gender': 'Jenis kelamin (Male/Female)',
        'MaritalStatus': 'Status pernikahan (Single, Married, Divorced)',
        'TotalWorkingYears': 'Total tahun pengalaman kerja',
        'JobLevel': 'Level pekerjaan (1-5)',
        'StockOptionLevel': 'Level opsi saham (0-4)',
        'YearsWithCurrManager': 'Tahun dengan manager saat ini',
        'DistanceFromHome': 'Jarak dari rumah ke kantor (km)'
    }
    return features


if __name__ == "__main__":
    print("=" * 80)
    print("ATTRITION PREDICTION TOOL")
    print("=" * 80)
    print()
    
    # Example usage
    example_employee = {
        'Age': 35,
        'MonthlyIncome': 4500,
        'Department': 'Sales',
        'OverTime': 'Yes',
        'JobSatisfaction': 1,
        'EnvironmentSatisfaction': 2,
        'WorkLifeBalance': 2,
        'YearsAtCompany': 2,
        'YearsInCurrentRole': 1,
        'TotalWorkingYears': 8,
        'JobLevel': 1,
        'JobRole': 'Sales Representative',
        'Gender': 'Male',
        'MaritalStatus': 'Single',
        'StockOptionLevel': 0,
        'YearsWithCurrManager': 2,
        'DistanceFromHome': 10,
        'BusinessTravel': 'Travel_Frequently',
        'EducationField': 'Marketing',
        'Education': 3,
        'HourlyRate': 65,
        'DailyRate': 450,
        'MonthlyRate': 15000,
        'PercentSalaryHike': 11,
        'PerformanceRating': 3,
        'RelationshipSatisfaction': 1,
        'StandardHours': 80,
        'TrainingTimesLastYear': 2
    }
    
    print("Contoh Prediksi untuk Seorang Karyawan:")
    print("-" * 80)
    result = predict_attrition(example_employee)
    print(f"Prediksi Attrition: {result['prediction']}")
    print(f"Probability: {result['probability']:.2%}")
    print(f"Risk Level: {result['risk_level']}")
    print()
    
    print("Feature yang Diperlukan:")
    print("-" * 80)
    features = get_feature_description()
    for i, (feature, description) in enumerate(features.items(), 1):
        print(f"{i}. {feature}: {description}")
    print()
    
    print("Untuk menggunakan script ini:")
    print("1. Dari Python: from prediction import predict_attrition")
    print("2. Buat dictionary dengan data karyawan")
    print("3. Panggil: result = predict_attrition(employee_data)")
    print()
