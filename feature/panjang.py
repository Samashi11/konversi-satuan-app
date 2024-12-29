import streamlit as st

st.title("Konversi Satuan Panjang")
st.write(":gray[Gunakan alat ini untuk mengonversi panjang antara berbagai satuan, seperti meter, kilometer, inci, dan lainnya.]")

st.image("https://www.wahanaedukasi.latifaba.com/public/uploads/blog/blog_240201090159_satuan-panjang-adalah-tangga-satuan-cara-hitung-dan-contoh-soal.png", width=400)

# Variabel
panjang = st.number_input("Masukkan Panjang :",0)
satuan1 = st.selectbox("Dari Satuan :",["Sentimeter","Meter","Kilometer","Hektometer","Dekameter","Desimeter","Inci","Milimeter"])
satuan2 = st.selectbox("Ke Satuan :",["Sentimeter","Meter","Kilometer","Hektometer","Dekameter","Desimeter","Inci","Milimeter"])
konversi = st.button("Konversi")

# Fungsi
def konversi_panjang(panjang, satuan1, satuan2):
  if satuan1 == "Kilometer":
    if satuan2 == "Hektometer":
      return panjang * 10
    elif satuan2 == "Dekameter":
      return panjang * 100
    elif satuan2 == "Meter":
      return panjang * 1000
    elif satuan2 == "Desimeter":
      return panjang * 10000
    elif satuan2 == "Sentimeter":
      return panjang * 100000
    elif satuan2 == "Milimeter":
      return panjang * 1000000
    elif satuan2 == "Inci":
      return panjang * 39370
    else:
      return None
  elif satuan1 == "Hektometer":
    if satuan2 == "Kilometer":
      return panjang / 10
    elif satuan2 == "Dekameter":
      return panjang * 10
    elif satuan2 == "Meter":
      return panjang * 100
    elif satuan2 == "Desimeter":
      return panjang * 1000
    elif satuan2 == "Sentimeter":
      return panjang * 10000
    elif satuan2 == "Milimeter":
      return panjang * 100000
    elif satuan2 == "Inci":
      return panjang * 3937
    else:
      return None
  elif satuan1 == "Dekameter":
    if satuan2 == "Kilometer":
      return panjang / 100
    elif satuan2 == "Hektometer":
      return panjang / 10
    elif satuan2 == "Meter":
      return panjang * 10
    elif satuan2 == "Desimeter":
      return panjang * 100
    elif satuan2 == "Sentimeter":
      return panjang * 1000
    elif satuan2 == "Milimeter":
      return panjang * 10000
    elif satuan2 == "Inci":
      return panjang * 393.7
    else:
      return None
  elif satuan1 == "Meter":
    if satuan2 == "Kilometer":
      return panjang / 1000
    elif satuan2 == "Hektometer":
      return panjang / 100
    elif satuan2 == "Dekameter":
      return panjang / 10
    elif satuan2 == "Desimeter":
      return panjang * 10
    elif satuan2 == "Sentimeter":
      return panjang * 100
    elif satuan2 == "Milimeter":
      return panjang * 1000
    elif satuan2 == "Inci":
      return panjang * 39.37
    else:
      return None
  elif satuan1 == "Desimeter":
    if satuan2 == "Kilometer":
      return panjang / 10000
    elif satuan2 == "Hektometer":
      return panjang / 1000
    elif satuan2 == "Dekameter":
      return panjang / 100
    elif satuan2 == "Meter":
      return panjang / 10
    elif satuan2 == "Sentimeter":
      return panjang * 10
    elif satuan2 == "Milimeter":
      return panjang * 100
    elif satuan2 == "Inci":
      return panjang * 3.937
    else:
      return None
  elif satuan1 == "Sentimeter":
    if satuan2 == "Kilometer":
      return panjang / 100000
    elif satuan2 == "Hektometer":
      return panjang / 10000
    elif satuan2 == "Dekameter":
      return panjang / 1000
    elif satuan2 == "Meter":
      return panjang / 100
    elif satuan2 == "Desimeter":
      return panjang / 10
    elif satuan2 == "Milimeter":
      return panjang * 10
    elif satuan2 == "Inci":
      return panjang / 2.54
    else:
      return None
  elif satuan1 == "Milimeter":
    if satuan2 == "Kilometer":
      return panjang / 1000000
    elif satuan2 == "Hektometer":
      return panjang / 100000
    elif satuan2 == "Dekameter":
      return panjang / 10000
    elif satuan2 == "Meter":
      return panjang / 1000
    elif satuan2 == "Desimeter":
      return panjang / 100
    elif satuan2 == "Sentimeter":
      return panjang / 10
    elif satuan2 == "Inci":
      return panjang / 25.4
    else:
      return None
  elif satuan1 == "Inci":
    if satuan2 == "Kilometer":
      return panjang / 39370
    elif satuan2 == "Hektometer":
      return panjang / 3937
    elif satuan2 == "Dekameter":
      return panjang / 393.7
    elif satuan2 == "Meter":
      return panjang / 39.37
    elif satuan2 == "Desimeter":
      return panjang / 3.937
    elif satuan2 == "Sentimeter":
      return panjang * 2.54
    elif satuan2 == "Milimeter":
      return panjang * 25.4
    else:
      return None
  else:
    return None

# If Else
if konversi:
  hasil = konversi_panjang(panjang, satuan1, satuan2)
  if hasil is not None:
    st.write("Hasil Konversi : ", f"**{hasil:.2f}**", satuan2)
  else:
    st.write("Hasil Konversi Tidak Valid")