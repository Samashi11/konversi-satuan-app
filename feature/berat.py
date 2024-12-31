import streamlit as st
import time

# Tambahkan gaya kustom
st.markdown("""
      <style>
         .stAppHeader, .stAppFooter {
            opacity: 0;
        }
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
            [data-testid="stBaseButton-headerNoPadding"] {
            color: #1abc9c;
          }
      </style>
  """, unsafe_allow_html=True)

# Judul aplikasi
st.markdown("<h1 class='header-title'> Aplikasi Konversi Satuan Berat </h1>", unsafe_allow_html=True)

# Deskripsi aplikasi
st.write("""
<div class='info-text'>
Aplikasi ini memungkinkan Anda untuk melakukan konversi satuan berat antara:
<ul>
<li>Kilogram (kg)</li>
<li>Gram (g)</li>
<li>Ton (T)</li>
</ul>
Masukkan nilai berat, pilih satuan asal, dan satuan tujuan untuk melihat hasil konversinya.
</div>
""", unsafe_allow_html=True)

# Input nilai
nilai = st.number_input("Masukkan nilai berat:", value=0.0, min_value=0.0)

# Pilihan satuan
satuan_dari = st.selectbox("Dari satuan:", ["Kilogram", "Gram", "Ton"])
satuan_ke = st.selectbox("Ke satuan:", ["Kilogram", "Gram", "Ton"])

# Fungsi konversi berat
def konversi_berat(nilai, dari, ke):
    if dari == "Kilogram" and ke == "Gram":
        return nilai * 1000
    elif dari == "Gram" and ke == "Kilogram":
        return nilai / 1000
    elif dari == "Kilogram" and ke == "Ton":
        return nilai / 1000
    elif dari == "Ton" and ke == "Kilogram":
        return nilai * 1000
    elif dari == "Gram" and ke == "Ton":
        return nilai / 1_000_000
    elif dari == "Ton" and ke == "Gram":
        return nilai * 1_000_000
    else:
        return nilai

# Tombol konversi
if st.button("Konversi"):
    with st.spinner("Mengonversi..."):
        time.sleep(2)  # Simulasi proses
    hasil = konversi_berat(nilai, satuan_dari, satuan_ke)
    st.markdown(
        f"<div class='info-text'><strong>Hasil:</strong> {nilai} {satuan_dari} sama dengan <strong>{hasil:.2f} {satuan_ke}</strong>.</div>",
        unsafe_allow_html=True,
    )
