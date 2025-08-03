import joblib
import pandas as pd
import os
from src.predict import predict_from_input
from src.model import train_model

def get_input(prompt, dtype=int, choices=None, required=True, min_val=None, max_val=None):
    while True:
        try:
            value = input(prompt).strip()
            if required and not value:
                print("❌ Input wajib diisi.")
                continue
            value = dtype(value)
            if choices and value not in choices:
                print(f"❌ Pilihan tidak valid. Pilih salah satu: {choices}")
                continue
            if min_val is not None and value < min_val:
                print(f"❌ Nilai minimal adalah {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"❌ Nilai maksimal adalah {max_val}")
                continue
            return value
        except ValueError:
            print("❌ Input harus berupa angka yang valid.")

def main():
    print("="*60)
    print("PREDIKSI RISIKO DIABETES BERDASARKAN KESEHATAN")
    print("Silakan isi data Anda dengan jujur untuk hasil terbaik.")
    print("="*60)

    input_data = {}

    # GEJALA DAN RIWAYAT KESEHATAN
    print("\n1. Gejala dan Riwayat Kesehatan")
    input_data['HighBP'] = get_input("   1.1 Tekanan darah tinggi? (0=Tdk, 1=Ya): ", choices=[0, 1])
    input_data['HighChol'] = get_input("   1.2 Kolesterol tinggi? (0=Tdk, 1=Ya): ", choices=[0, 1])
    input_data['CholCheck'] = get_input("   1.3 Pernah cek kolesterol? (0=Tdk, 1=Ya): ", choices=[0, 1])
    input_data['Smoker'] = get_input("   1.4 Merokok? (0=Tdk, 1=Ya): ", choices=[0, 1])
    input_data['Stroke'] = get_input("   1.5 Pernah stroke? (0=Tdk, 1=Ya): ", choices=[0, 1])
    input_data['HeartDiseaseorAttack'] = get_input("   1.6 Serangan jantung sebelumnya? (0=Tdk, 1=Ya): ", choices=[0, 1])

    # GAYA HIDUP
    print("\n2. Gaya Hidup & Pola Makan")
    input_data['PhysActivity'] = get_input("   2.1 Aktivitas fisik rutin? (0=Tdk, 1=Ya): ", choices=[0, 1])
    input_data['Fruits'] = get_input("   2.2 Konsumsi buah rutin? (0=Tdk, 1=Ya): ", choices=[0, 1])
    input_data['Veggies'] = get_input("   2.3 Konsumsi sayur rutin? (0=Tdk, 1=Ya): ", choices=[0, 1])
    input_data['HvyAlcoholConsump'] = get_input("   2.4 Konsumsi alkohol berlebihan? (0=Tdk, 1=Ya): ", choices=[0, 1])

    # DATA BMI
    print("\n3. Berat Badan & Tinggi Badan")
    berat = get_input("   3.1 Berat badan (kg): ", dtype=float, min_val=1)
    tinggi = get_input("   3.2 Tinggi badan (cm): ", dtype=float, min_val=1)
    input_data['BMI'] = round(berat / ((tinggi / 100) ** 2), 2)
    print(f"   ➤ BMI Anda adalah: {input_data['BMI']}")

    # AKSES KESEHATAN
    print("\n4. Akses & Penilaian Kesehatan")
    input_data['AnyHealthcare'] = get_input("   4.1 Punya akses layanan kesehatan? (0=Tdk, 1=Ya): ", choices=[0, 1])
    input_data['NoDocbcCost'] = get_input("   4.2 Pernah tidak ke dokter karena biaya? (0=Tdk, 1=Ya): ", choices=[0, 1])
    input_data['GenHlth'] = get_input("   4.3 Penilaian kesehatan umum (1=Sgt Baik - 5=Sgt Buruk): ", choices=[1, 2, 3, 4, 5])
    input_data['MentHlth'] = get_input("   4.4 Hari stres (0-30): ", min_val=0, max_val=30)
    input_data['PhysHlth'] = get_input("   4.5 Hari sakit fisik (0-30): ", min_val=0, max_val=30)
    input_data['DiffWalk'] = get_input("   4.6 Sulit berjalan jauh? (0=Tdk, 1=Ya): ", choices=[0, 1])

    # DEMOGRAFI
    print("\n5. Data Demografis")
    input_data['Sex'] = get_input("   5.1 Jenis kelamin (0=Perempuan, 1=Laki-laki): ", choices=[0, 1])
    input_data['Age'] = get_input("   5.2 Usia (18 - 100 tahun): ", min_val=18, max_val=100)
    input_data['Education'] = get_input("   5.3 Pendidikan (1=SMP↓ - 6=Sarjana): ", choices=[1, 2, 3, 4, 5, 6])
    input_data['Income'] = get_input("   5.4 Penghasilan (1=Terendah - 8=Tertinggi): ", choices=[1, 2, 3, 4, 5, 6, 7, 8])
    
    print("\nTerima kasih telah mengisi data Anda! Berikut adalah ringkasan input Anda:")
    
    # Load model
    model_path = "model/diabetes_model.pkl"
    if not os.path.exists(model_path):
        print("🔧 Model belum dilatih. Melatih model terlebih dahulu...")
        model, _ = train_model()
    else:
        model = joblib.load(model_path)

    # Predict
    hasil = predict_from_input(model, list(input_data.values()))
    print("\n📊 Hasil Prediksi:")
    print("✅ Berisiko Diabetes" if hasil == 1 else "❎ Tidak Berisiko Diabetes")

if __name__ == "__main__":
    main()
