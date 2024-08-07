import joblib
import pandas as pd
import os
# Modeli yükledim
model_path = 'company/models/model.pkl'
model = joblib.load(model_path)

# Manuel numaralandırma eşlemeleri yaptım
konum_mapping = {
    'Ankara': 1,
    'İstanbul': 2,
    'İzmir': 3,
    'Antalya': 4,
    'Bursa': 5
}

bolum_mapping = {
    'Yazılım Mühendisliği': 1,
    'Adli Bilişim Mühendisliği': 2,
    'Yapay Zeka ve Veri Mühendisliği': 3,
    'Bilgisayar Mühendisliği': 4,
    'Elektrik Elektronik Mühendisliği': 5,
    'Makine Mühendisliği': 6
}

ingilizce_seviyesi_mapping = {
    'A1': 1,
    'A2': 2,
    'B1': 3,
    'B2': 4,
    'C1': 5,
    'C2': 6
}

def predict_company(student_data):
    # Verileri encode ediyor
    student_data[0] = konum_mapping[student_data[0]]
    student_data[1] = bolum_mapping[student_data[1]]
    student_data[4] = ingilizce_seviyesi_mapping[student_data[4]]
    
    df = pd.DataFrame([student_data], columns=["Konum", "Bolum", "Sinif", "Transkript", "IngilizceSeviyesi"])
    prediction = model.predict(df)
    return prediction[0]

def get_company_info(company_id):
    try:
        # CSV dosyasının tam yolunu belirtiyoruz.
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        csv_file_path = os.path.join(base_dir, 'company', 'company_data.csv')
        df = pd.read_csv(csv_file_path, sep=',', encoding='ISO-8859-1')
        company_info = df[df['SirketId'] == company_id].to_dict(orient='records')
        if company_info:
            return company_info[0]
        else:
            return {}
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return {}



