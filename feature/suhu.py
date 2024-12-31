import streamlit as st
import time  # Menambahkan modul time untuk menggunakan sleep

st.markdown("""
    <style>
        .stAppHeader, .stAppFooter {
            opacity: 0;
        }
        .stApp {
            background-color: #f4e1ff; /* Latar belakang ungu muda */
        }
        .header-title {
            color: #6a0dad;
            text-align: center;
            font-family: 'Arial Black', sans-serif;
            text-shadow: 2px 2px 4px #dab6fc;
        }
        .info-text {
            color: #4b0082;
            font-family: 'Verdana', sans-serif;
            padding: 15px;
            background-color: #e6ccff;
            border: 3px solid #6a0dad;
            border-radius: 15px;
            box-shadow: 3px 3px 8px rgba(0,0,0,0.1);
            margin: 20px auto;
            max-width: 600px;
        }
        .info-text ul {
            list-style-type: none;
            padding: 0;
        }
        .info-text li {
            margin: 10px 0;
            padding: 5px 10px;
            background-color: #6a0dad;
            color: white;
            border-radius: 10px;
            font-weight: bold;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        }
        .stButton>button {
            color: white;
            background-color: #6a0dad;
            border: none;
            border-radius: 5px;
            padding: 10px;
            font-size: 16px;
            font-weight: bold;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        }
        .stButton>button:hover {
            background-color: #4b0082;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
        }
        .stNumberInput input {
            border: 2px solid #6a0dad;
            border-radius: 5px;
        }
        .stSelectbox select {
            border: 2px solid #6a0dad;
            border-radius: 5px;
        }
        .stRadio div[data-baseweb="radio"] > label {
            color: #4b0082;
            font-family: 'Verdana', sans-serif;
            font-weight: bold;
        }
        [data-testid="stBaseButton-headerNoPadding"] {
        color: #6a0dad;
        }
    </style>
""", unsafe_allow_html=True)

# Judul aplikasi
st.markdown("<h1 class='header-title'> Aplikasi Konversi Satuan Suhu </h1>", unsafe_allow_html=True)

# Deskripsi aplikasi
st.write("""
<div class='info-text'>
Aplikasi ini memungkinkan Anda untuk mengonversi suhu antara:
<ul>
<li>Celsius (°C)</li>
<li>Fahrenheit (°F)</li>
<li>Kelvin (K)</li>
<li>Reaumur (°Re)</li>
<li>Rankine (°Ra)</li>
</ul>
Masukkan nilai suhu, pilih satuan asal, dan satuan tujuan untuk melihat hasil konversinya.
</div>
""", unsafe_allow_html=True)

# Input nilai
nilai = st.number_input("Masukkan nilai suhu:", 0.0)

# Pilihan satuan
satuan_dari = st.selectbox("Dari satuan:", ["Celsius", "Fahrenheit", "Kelvin", "Reaumur", "Rankine"])
mode = st.radio("Pilih mode konversi:", ["Konversi ke unit tertentu", "Konversi ke semua unit"])

# Fungsi konversi suhu
def konversi_suhu(nilai, dari, ke):
    if dari == ke:
        return nilai
    if dari == "Celsius":
        celsius = nilai
    elif dari == "Fahrenheit":
        celsius = (nilai - 32) * 5/9
    elif dari == "Kelvin":
        celsius = nilai - 273.15
    elif dari == "Reaumur":
        celsius = nilai * 5/4
    elif dari == "Rankine":
        celsius = (nilai - 491.67) * 5/9
    else:
        return None

    if ke == "Celsius":
        return celsius
    elif ke == "Fahrenheit":
        return (celsius * 9/5) + 32
    elif ke == "Kelvin":
        return celsius + 273.15
    elif ke == "Reaumur":
        return celsius * 4/5
    elif ke == "Rankine":
        return (celsius + 273.15) * 9/5
    else:
        return None

# Tombol konversi
if mode == "Konversi ke unit tertentu":
    satuan_ke = st.selectbox("Ke satuan:", ["Celsius", "Fahrenheit", "Kelvin", "Reaumur", "Rankine"])
    if st.button("Konversi"):
        with st.spinner("Menghitung konversi..."):
            time.sleep(2)  # Menambahkan jeda 2 detik untuk simulasi
            hasil = konversi_suhu(nilai, satuan_dari, satuan_ke)
            st.success(f"Hasil: {hasil:.2f} {satuan_ke}")
elif mode == "Konversi ke semua unit":
    if st.button("Konversi Semua"):
        with st.spinner("Menghitung konversi ke semua unit..."):
            time.sleep(2)  # Menambahkan jeda 2 detik untuk simulasi
            satuan_ke_semua = ["Celsius", "Fahrenheit", "Kelvin", "Reaumur", "Rankine"]
            hasil_semua = {}
            for satuan_ke in satuan_ke_semua:
                if satuan_ke != satuan_dari:
                    hasil_semua[satuan_ke] = konversi_suhu(nilai, satuan_dari, satuan_ke)
            st.write("Hasil konversi:")
            for satuan, hasil in hasil_semua.items():
                st.write(f"- {satuan}: {hasil:.2f}")
