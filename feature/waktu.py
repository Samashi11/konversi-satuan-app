import streamlit as st

# Menambahkan gaya CSS dengan warna biru
st.markdown("""
      <style>
          .stApp {
              background-color: #f4faff;
          }
          .header-title {
              color: #2a9df4;
              text-align: center;
              font-family: 'Poppins', sans-serif;
              font-size: 36px;
              font-weight: bold;
              text-shadow: 2px 2px 4px rgba(42, 157, 244, 0.3);
          }
          .info-text {
              color: #1b263b;
              font-family: 'Roboto', sans-serif;
              padding: 20px;
              background-color: #e3f2fd;
              border-left: 6px solid #2a9df4;
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
              color: #064789;
              font-weight: bold;
          }
          .stButton>button {
              color: white;
              background-color: #2a9df4;
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
              background-color: #1b7fcc;
              box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
              transform: translateY(-2px);
          }
          .stNumberInput input, .stSelectbox select {
              border: 2px solid #2a9df4;
              border-radius: 5px;
              padding: 8px;
              font-size: 16px;
              font-family: 'Roboto', sans-serif;
          }
          .stNumberInput input:focus, .stSelectbox select:focus {
              outline: none;
              border-color: #1b7fcc;
              box-shadow: 0 0 5px rgba(42, 157, 244, 0.4);
          }
      </style>
  """, unsafe_allow_html=True)


# Judul aplikasi
st.markdown("<h1 class='header-title'> Aplikasi Konversi Satuan Waktu </h1>", unsafe_allow_html=True)

# Deskripsi aplikasi
st.write("""
<div class='info-text'>
Aplikasi ini memungkinkan Anda untuk melakukan konversi satuan waktu antara:
<ul>
<li>Jam (Hour)</li>
<li>Menit (Minute)</li>
<li>Detik (Second)</li>
<li>Milidetik (Millisecond)</li>
<li>Mikrodetik (Microsecond)</li>
</ul>
Masukkan nilai waktu, pilih satuan asal, dan satuan tujuan untuk melihat hasil konversinya.
</div>
""", unsafe_allow_html=True)

# Definisi kelas untuk konversi waktu
class TimeConverter:
    # Faktor konversi antar satuan waktu
    conversion_factors = {
        "Jam": 3600,
        "Menit": 60,
        "Detik": 1,
        "Milidetik": 0.001,
        "Mikrodetik": 0.000001,
    }

    def __init__(self, value, from_unit, to_unit):
        self.value = value
        self.from_unit = from_unit
        self.to_unit = to_unit

    def convert(self):
        # Konversi ke detik
        value_in_seconds = self.value * self.conversion_factors[self.from_unit]
        # Konversi dari detik ke satuan tujuan
        result = value_in_seconds / self.conversion_factors[self.to_unit]
        return result

# Input nilai
nilai = st.number_input("Masukkan nilai waktu:", 0.0)

# Pilihan satuan
satuan_dari = st.selectbox("Dari satuan:", ["Jam", "Menit", "Detik", "Milidetik", "Mikrodetik"])
satuan_ke = st.selectbox("Ke satuan:", ["Jam", "Menit", "Detik", "Milidetik", "Mikrodetik"])

# Tombol konversi
# Tombol konversi
if st.button("Konversi"):
    # Membuat objek TimeConverter
    converter = TimeConverter(nilai, satuan_dari, satuan_ke)
    # Menghitung hasil konversi
    hasil = converter.convert()
    # Menampilkan hasil dengan gaya khusus
    st.markdown(f"""
        <div style="
            padding: 15px;
            margin-top: 20px;
            background-color: #e3f2fd;
            border: 2px solid #2a9df4;
            border-radius: 10px;
            font-family: 'Roboto', sans-serif;
            color: #064789;
            font-size: 18px;
            font-weight: bold;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            text-align: center;
        ">
            🎉 Hasil Konversi: <span style="color: #2a9df4;">{hasil:.2f} {satuan_ke}</span>
        </div>
    """, unsafe_allow_html=True)
