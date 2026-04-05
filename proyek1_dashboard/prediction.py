import pandas as pd
import joblib

# 1. Load Model dan List Kolom saat Training
# Penting: Model harus di-load bersamaan dengan urutan kolom aslinya
try:
    model = joblib.load('attrition_model.joblib')
    model_columns = joblib.load('model_columns.joblib') # Simpan ini saat training!
    
    print("✅ Model berhasil dimuat!")
except:
    print("❌ Model atau file kolom tidak ditemukan. Pastikan sudah di-save di Colab.")

def predict_attrition(input_data):
    """
    Fungsi untuk menerima input berupa dictionary atau DataFrame 
    dan mengembalikan prediksi.
    """
    # 2. Ubah input ke DataFrame
    df = pd.DataFrame([input_data])
    
    # 3. Preprocessing (Harus sama persis dengan di Colab!)
    # Contoh: Handling OverTime
    if 'OverTime' in df.columns:
        df['OverTime_Numeric'] = df['OverTime'].apply(lambda x: 1 if x == 'Yes' else 0)
        df = df.drop(columns=['OverTime'])
    
    # 4. One-Hot Encoding untuk kolom kategorik
    # Sesuaikan dengan kolom yang kamu pakai di proyek (Dept, JobRole, dll)
    df_encoded = pd.get_dummies(df)
    
    # 5. Alignment (PENTING: Biar kolomnya pas dengan model)
    # Tambahkan kolom yang kurang dengan isi 0, dan buang kolom yang gak ada di model
    for col in model_columns:
        if col not in df_encoded.columns:
            df_encoded[col] = 0
            
    df_final = df_encoded[model_columns]
    
    # 6. Prediksi
    prediction = model.predict(df_final)
    probability = model.predict_proba(df_final)[:, 1]
    
    return "Resign" if prediction[0] == 1 else "Stay", probability[0]

# --- CONTOH CARA TEST NYA ---
if __name__ == "__main__":
    # Contoh data karyawan baru buat ngetes
    sample_employee = {
        'Age': 25,
        'BusinessTravel': 'Travel_Frequently',
        'Department': 'Sales',
        'DistanceFromHome': 20,
        'Education': 3,
        'EducationField': 'Marketing',
        'EnvironmentSatisfaction': 1,
        'Gender': 'Male',
        'JobRole': 'Sales Representative',
        'JobSatisfaction': 1,
        'MonthlyIncome': 2500,
        'OverTime': 'Yes',
        'WorkLifeBalance': 1
    }
    
    hasil, skor = predict_attrition(sample_employee)
    print(f"\n--- Hasil Prediksi ---")
    print(f"Status: {hasil}")
    print(f"Risiko Resign: {skor:.2%}")