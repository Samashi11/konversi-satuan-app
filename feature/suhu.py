import streamlit as st

st.markdown("""
    <style>
        .stApp {
            background-color: #e8f6ff;
        }
        .header-title {
            color: #1abc9c;
            text-align: center;
            font-family: 'Arial Black', sans-serif;
            text-shadow: 2px 2px 4px #b3e5fc;
        }
        .info-text {
            color: #34495e;
            font-family: 'Verdana', sans-serif;
            padding: 15px;
            background-color: #dff9fb;
            border: 3px solid #1abc9c;
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
            background-color: #1abc9c;
            color: white;
            border-radius: 10px;
            font-weight: bold;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        }
        .stButton>button {
            color: white;
            background-color: #1abc9c;
            border: none;
            border-radius: 5px;
            padding: 10px;
            font-size: 16px;
            font-weight: bold;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        }
        .stButton>button:hover {
            background-color: #16a085;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
        }
        .stNumberInput input {
            border: 2px solid #1abc9c;
            border-radius: 5px;
        }
        .stSelectbox select {
            border: 2px solid #1abc9c;
            border-radius: 5px;
        }
        .stRadio>div {
            background-color: #dff9fb;
            padding: 10px;
            border: 2px solid #1abc9c;
            border-radius: 10px;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
            margin-bottom: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# Judul aplikasi
st.markdown("<h1 class='header-title'> Aplikasi Konversi Satuan Suhu </h1>", unsafe_allow_html=True)

# Deskripsi aplikasi
st.write("""
<div class='info-text'>
Aplikasi ini memungkinkan Anda untuk melakukan konversi satuan suhu antara:
<ul>
<li>Celsius</li>
<li>Fahrenheit</li>
<li>Kelvin</li>
<li>Reaumur</li>
<li>Rankine</li>
</ul>
Masukkan nilai suhu, pilih satuan asal, dan satuan tujuan untuk melihat hasil konversinya.
</div>
""", unsafe_allow_html=True)

# Input nilai
nilai = st.number_input("Masukkan nilai suhu:", 0.0)

# Pilihan satuan
satuan_dari = st.selectbox("Dari satuan:", ["Celsius", "Fahrenheit", "Kelvin", "Reaumur", "Rankine"])

# Pilihan mode
mode = st.radio("Pilih mode konversi:", ["Konversi ke unit tertentu", "Konversi ke semua unit"])

def konversi_suhu(nilai, dari, ke):
    if dari == ke:
        return nilai

    # Konversi ke Celsius sebagai titik tengah
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

    # Konversi dari Celsius ke unit tujuan
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

if mode == "Konversi ke unit tertentu":
    satuan_ke = st.selectbox("Ke satuan:", ["Celsius", "Fahrenheit", "Kelvin", "Reaumur", "Rankine"])
    if st.button("Konversi"):
        hasil = konversi_suhu(nilai, satuan_dari, satuan_ke)
        st.success(f"Hasil: {hasil:.2f} {satuan_ke}")

elif mode == "Konversi ke semua unit":
    if st.button("Konversi Semua"):
        satuan = ["Celsius", "Fahrenheit", "Kelvin", "Reaumur", "Rankine"]
        hasil_konversi = {}
        for satuan_ke in satuan:
            if satuan_ke != satuan_dari:
                hasil_konversi[satuan_ke] = konversi_suhu(nilai, satuan_dari, satuan_ke)

        st.write("Hasil konversi:")
        for satuan_ke, hasil in hasil_konversi.items():
            st.write(f"- {hasil:.2f} {satuan_ke}")
