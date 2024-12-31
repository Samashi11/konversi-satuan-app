import streamlit as st

# Menambahkan CSS untuk gaya aplikasi
st.markdown("""
    <style>
        .stAppHeader, .stAppFooter {
            opacity: 0;
        }
        
        .stApp {
            background-color: #fff5f5;
        }
        .header-title {
            text-align: center;
            font-family: 'Poppins', sans-serif;
            font-size: 36px;
            font-weight: bold;
            color: #e63946;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(42, 157, 244, 0.3)
        }
        .subheader-title {
            text-align: center;
            font-family: 'Roboto', sans-serif;
            font-size: 20px;
            font-weight: 400;
            color: #7d2b2b;
            margin-bottom: 20px;
        }
        .info-section {
            font-family: 'Roboto', sans-serif;
            font-size: 16px;
            color: #7d2b2b;
            background-color: #fdecea;
            padding: 15px;
            border-left: 6px solid #e63946;
            border-radius: 8px;
            margin: 20px auto;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .category-tile {
            background-color: #ffffff;
            border-radius: 10px;
            border: 1px solid #f9d9d9;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 15px;
            text-align: center;
            transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
        }
        .category-tile:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
        }
        .icon {
            font-size: 40px;
            color: #e63946;
            margin-bottom: 10px;
        }
        .category-title {
            font-size: 18px;
            font-family: 'Poppins', sans-serif;
            font-weight: bold;
            color: #e63946;
        }
        [data-testid="stBaseButton-headerNoPadding"] {
        color: #e63946;
        }
    </style>
""", unsafe_allow_html=True)

# Judul aplikasi
st.markdown("<h1 class='header-title'>Aplikasi Konversi Satuan</h1>", unsafe_allow_html=True)
st.markdown("<p class='subheader-title'>Ubah Satuan dengan Mudah, Cepat, dan Akurat!</p>", unsafe_allow_html=True)

# Deskripsi aplikasi
st.markdown("""
<div class='info-section'>
    <p>\U0001F4CF <b>Panjang</b>: Dari meter ke kilometer, atau bahkan milimeter, semuanya tersedia!</p>
    <p>\u2696\ufe0f <b>Berat</b>: Tak perlu bingung lagi dengan kilogram, gram, hingga miligram.</p>
    <p>\u23F3 <b>Waktu</b>: Hitung jam, menit, dan detik dengan sempurna.</p>
    <p>\U0001F321\ufe0f <b>Suhu</b>: Ubah Celcius ke Fahrenheit atau Kelvin dengan akurasi tinggi.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='info-section'>
    Mulailah pengalaman konversi satuan yang mudah dan bebas ribet! Cocok untuk siswa, pekerja, atau siapa saja yang ingin hasil instan dan tepat. \U0001F31F  
    <b>Jelajahi Aplikasi ini Sekarang!</b>
</div>
""", unsafe_allow_html=True)

# Ikon dan kategori
icon = ["\U0001F4CF", "\u2696\ufe0f", "\u23F3", "\U0001F321\ufe0f"]
title1 = ["Panjang", "Berat", "Waktu", "Suhu"]
row1 = st.columns(4)

# Menampilkan ikon dan kategori dalam kolom
for i, col in enumerate(row1):
    col.markdown(f"""
        <div class='category-tile'>
            <div class='icon'>{icon[i]}</div>
            <div class='category-title'>{title1[i]}</div>
        </div>
    """, unsafe_allow_html=True)
