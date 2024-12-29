import streamlit as st

# Menambahkan gaya CSS dengan warna oranye
st.markdown("""
      <style>
          .stApp {
              background-color: #fff7e6;
          }
          .header-title {
              color: #ff7f0e;
              text-align: center;
              font-family: 'Poppins', sans-serif;
              font-size: 36px;
              font-weight: bold;
              text-shadow: 2px 2px 4px rgba(255, 127, 14, 0.3);
          }
          .info-text {
              color: #4d2800;
              font-family: 'Roboto', sans-serif;
              padding: 20px;
              background-color: #ffe6cc;
              border-left: 6px solid #ff7f0e;
              border-radius: 10px;
              margin: 20px auto;
              max-width: 650px;
              line-height: 1.6;
          }
          .info-text ul {
              list-style-type: square;
              padding-left: 20px;
          }
          .info-text li {
              margin: 8px 0;
              padding: 5px;
              color: #b35900;
              font-weight: bold;
          }
          .stButton>button {
              color: white;
              background-color: #ff7f0e;
              border: none;
              border-radius: 8px;
              padding: 12px 20px;
              font-size: 18px;
              font-weight: bold;
              font-family: 'Poppins', sans-serif;
              transition: all 0.3s ease-in-out;
              box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
          }
          .stButton>button:hover {
              background-color: #e66900;
              box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
              transform: translateY(-2px);
          }
          .stNumberInput input, .stSelectbox select {
              border: 2px solid #ff7f0e;
              border-radius: 5px;
              padding: 8px;
              font-size: 16px;
              font-family: 'Roboto', sans-serif;
          }
          .stNumberInput input:focus, .stSelectbox select:focus {
              outline: none;
              border-color: #e66900;
              box-shadow: 0 0 5px rgba(255, 127, 14, 0.4);
          }
      </style>
  """, unsafe_allow_html=True)

# Judul aplikasi
st.markdown("<h1 class='header-title'> Aplikasi Konversi Satuan Panjang </h1>", unsafe_allow_html=True)

# Deskripsi aplikasi
st.write("""
<div class='info-text'>
Aplikasi ini memungkinkan Anda untuk melakukan konversi satuan panjang antara:
<ul>
<li>Kilometer</li>
<li>Meter</li>
<li>Sentimeter</li>
<li>Milimeter</li>
<li>Inci</li>
</ul>
Masukkan nilai panjang, pilih satuan asal, dan satuan tujuan untuk melihat hasil konversinya.
</div>
""", unsafe_allow_html=True)

# Definisi kelas untuk konversi panjang
class LengthConverter:
    # Faktor konversi antar satuan panjang (ke meter)
    conversion_factors = {
          "Kilometer": 1000,
          "Hektometer": 100,
          "Dekameter": 10,
          "Meter": 1,
          "Desimeter": 0.1,
          "Sentimeter": 0.01,
          "Milimeter": 0.001,
          "Inci": 0.0254,
      }


    def __init__(self, value, from_unit, to_unit):
        self.value = value
        self.from_unit = from_unit
        self.to_unit = to_unit

    def convert(self):
        # Konversi ke meter
        value_in_meters = self.value * self.conversion_factors[self.from_unit]
        # Konversi dari meter ke satuan tujuan
        result = value_in_meters / self.conversion_factors[self.to_unit]
        return result

# Input nilai
nilai = st.number_input("Masukkan nilai panjang:", 0.0)

# Pilihan satuan
satuan_dari = st.selectbox("Dari Satuan :", ["Sentimeter", "Meter", "Kilometer", "Hektometer", "Dekameter", "Desimeter", "Inci", "Milimeter"])
satuan_ke = st.selectbox("Ke Satuan :", ["Sentimeter", "Meter", "Kilometer", "Hektometer", "Dekameter", "Desimeter", "Inci", "Milimeter"])


# Tombol konversi
if st.button("Konversi"):
    # Membuat objek LengthConverter
    converter = LengthConverter(nilai, satuan_dari, satuan_ke)
    # Menghitung hasil konversi
    hasil = converter.convert()
    # Menampilkan hasil dengan gaya khusus
    st.markdown(f"""
        <div style="
            padding: 15px;
            margin-top: 20px;
            background-color: #ffe6cc;
            border: 2px solid #ff7f0e;
            border-radius: 10px;
            font-family: 'Roboto', sans-serif;
            color: #b35900;
            font-size: 18px;
            font-weight: bold;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            text-align: center;
        ">
            🎉 Hasil Konversi: <span style="color: #ff7f0e;">{hasil:.2f} {satuan_ke}</span>
        </div>
    """, unsafe_allow_html=True)
