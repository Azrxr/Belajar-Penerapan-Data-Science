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

model_dir = os.path.join(os.path.dirname(__file__), 'model')
model = joblib.load(os.path.join(model_dir, 'trained_model.pkl'))
scaler = joblib.load(os.path.join(model_dir, 'scaler.pkl'))
label_encoders = joblib.load(os.path.join(model_dir, 'label_encoders.pkl'))

try:
    df_train_ref = pd.read_csv(os.path.join(os.path.dirname(__file__), '..', 'employee_data.csv'))
    
    cols_to_drop = ['Attrition', 'EmployeeId', 'EmployeeCount']
    for col in cols_to_drop:
        if col in df_train_ref.columns:
            df_train_ref = df_train_ref.drop(col, axis=1)
            
    for col in label_encoders.keys():
        if col in df_train_ref.columns:
            df_train_ref[col] = df_train_ref[col].fillna('Unknown').astype(str)
            known_classes = set(label_encoders[col].classes_)
            df_train_ref[col] = df_train_ref[col].apply(lambda x: x if x in known_classes else label_encoders[col].classes_[0])
            df_train_ref[col] = label_encoders[col].transform(df_train_ref[col])
    
    REQUIRED_FEATURES = df_train_ref.columns.tolist()
    FEATURE_MEANS = df_train_ref.mean(numeric_only=True).to_dict()
except Exception as e:
    try:
        REQUIRED_FEATURES = scaler.feature_names_in_.tolist()
        FEATURE_MEANS = {}
    except:
        REQUIRED_FEATURES = None
        FEATURE_MEANS = {}


def predict_attrition(data):
    """
    Prediksi attrition untuk satu atau lebih karyawan.
    
    Parameters:
    -----------
    data : dict atau pd.DataFrame
        Data karyawan untuk prediksi.
    
    Returns:
    --------
    dict atau DataFrame
        Berisi prediksi (0 atau 1) dan probability
    """
    
    is_dict_input = isinstance(data, dict)
    if is_dict_input:
        df_input = pd.DataFrame([data])
    else:
        df_input = data.copy()
    
    cols_to_drop = ['Attrition', 'EmployeeId', 'EmployeeCount']
    for col in cols_to_drop:
        if col in df_input.columns:
            df_input = df_input.drop(col, axis=1)
            
    for col in label_encoders.keys():
        if col in df_input.columns:
            df_input[col] = df_input[col].fillna('Unknown').astype(str)
            known_classes = set(label_encoders[col].classes_)
            default_class = label_encoders[col].classes_[0]
            
            df_input[col] = df_input[col].apply(lambda x: x if x in known_classes else default_class)
            # Transform
            df_input[col] = label_encoders[col].transform(df_input[col])
            
    object_cols = df_input.select_dtypes(include=['object']).columns
    for col in object_cols:
        df_input[col] = pd.to_numeric(df_input[col], errors='coerce').fillna(0)
    
    if REQUIRED_FEATURES:
        for feature in REQUIRED_FEATURES:
            if feature not in df_input.columns:
                if feature in FEATURE_MEANS:
                    df_input[feature] = FEATURE_MEANS[feature]
                else:
                    df_input[feature] = 0
        
        df_input = df_input[REQUIRED_FEATURES]
    
    for col in df_input.columns:
        if df_input[col].isnull().any():
            if col in FEATURE_MEANS:
                df_input[col].fillna(FEATURE_MEANS[col], inplace=True)
            else:
                df_input[col].fillna(df_input[col].mean(), inplace=True)
    
    df_input = df_input.astype(np.float64)
    
    df_scaled = scaler.transform(df_input)
    
    predictions = model.predict(df_scaled)
    probabilities = model.predict_proba(df_scaled)[:, 1]
    
    if is_dict_input:
        return {
            'prediction': 'Yes' if predictions[0] == 1 else 'No',
            'probability': float(probabilities[0]),
            'risk_level': get_risk_level(probabilities[0])
        }
    else:
        results_df = data.copy() if isinstance(data, pd.DataFrame) else pd.DataFrame(data)
        results_df['attrition_prediction'] = ['Yes' if p == 1 else 'No' for p in predictions]
        results_df['attrition_probability'] = probabilities
        results_df['risk_level'] = [get_risk_level(p) for p in probabilities]
        return results_df


def get_risk_level(probability):
    if probability < 0.3:
        return 'Low'
    elif probability < 0.7:
        return 'Medium'
    else:
        return 'High'


def get_feature_description():
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
    print("ATTRITION PREDICTION TOOL (UPDATED & BULLETPROOF)")
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
        'TrainingTimesLastYear': 2,
        'EmployeeCount': 1,
        'EmployeeId': 9999
    }
    
    print("Contoh Prediksi untuk Seorang Karyawan:")
    print("-" * 80)
    result = predict_attrition(example_employee)
    print(f"Prediksi Attrition: {result['prediction']}")
    print(f"Probability: {result['probability']:.2%}")
    print(f"Risk Level: {result['risk_level']}")
    print()