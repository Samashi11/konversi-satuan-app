import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Konversi Satuan App')

# Navigasi Sidebar
with st.sidebar:
  selected = option_menu(
    menu_title="Aplikasi \n Konversi Satuan",
    options=["Home", "Panjang", "Berat","Waktu", "Suhu"],
    icons=["house-fill","rulers","box-fill","hourglass-split","thermometer-half"],
    menu_icon="option",
    default_index=0
  )

if selected == "Home":
  st.title("Aplikasi Konversi Satuan")
  st.subheader("Ubah Satuan dengan Mudah, Cepat, dan Akurat!")
  st.write("Ingin menghitung panjang, berat, waktu, atau suhu dengan praktis? Aplikasi Konversi Satuan adalah solusi tepat untuk kebutuhan Anda! Dengan antarmuka yang intuitif dan ramah pengguna, Anda dapat mengonversi satuan hanya dalam hitungan detik.")
  multi = '''
  \U0001F4CF **Panjang** : Dari meter ke kilometer, atau bahkan milimeter, semuanya tersedia!  
  \u2696\ufe0f **Berat** : Tak perlu bingung lagi dengan kilogram, gram, hingga miligram.  
  \u23F3 **Waktu** : Hitung jam, menit, dan detik dengan sempurna.  
  \U0001F321\ufe0f **Suhu** : Ubah Celcius ke Fahrenheit atau Kelvin dengan akurasi tinggi.
  '''
  st.markdown(multi)
  multi1 = '''
  Mulailah pengalaman konversi satuan yang mudah dan bebas ribet! Cocok untuk siswa, pekerja, atau siapa saja yang ingin hasil instan dan tepat. \U0001F31F  
  **Jelajahi Aplikasi ini Sekarang!**
  '''
  st.markdown(multi1)

  icon = ["\U0001F4CF","\u2696\ufe0f","\u23F3","\U0001F321\ufe0f"]
  title1 = ["Panjang","Berat","Waktu","Suhu"]
  row1 = st.columns(4)

  for i, col in enumerate(row1):
    tile = col.container(height=180)
    tile.title(icon[i])
    tile.subheader(title1[i])

if selected == "Panjang":
  st.title("Konversi Satuan Panjang")
  st.write(":gray[Gunakan alat ini untuk mengonversi panjang antara berbagai satuan, seperti meter, kilometer, inci, dan lainnya.]")

  st.image("https://www.wahanaedukasi.latifaba.com/public/uploads/blog/blog_240201090159_satuan-panjang-adalah-tangga-satuan-cara-hitung-dan-contoh-soal.png", width=400)

  panjang = st.number_input("Masukkan Panjang :",0)
  satuan1 = st.selectbox("Dari Satuan :",["Sentimeter","Meter","Kilometer","Hektometer","Dekameter","Desimeter","Inci","Milimeter"])
  satuan2 = st.selectbox("Ke Satuan :",["Sentimeter","Meter","Kilometer","Hektometer","Dekameter","Desimeter","Inci","Milimeter"])
  konversi = st.button("Konversi")

  if konversi:
    if satuan1 == "Meter" and satuan2 == "Kilometer":
      hasil = panjang / 1000
      st.write("Hasil Konversi : ", f"**{hasil}**", satuan2)
    elif satuan1 == "Meter" and satuan2 == "Inci":
      hasil = panjang * 39.37
      st.write("Hasil Konversi : ",f"**{hasil}**", satuan2)
    elif satuan1 == "Kilometer" and satuan2 == "Meter":
      hasil = panjang * 1000
      st.write("Hasil Konversi : ", f"**{hasil}**", satuan2)
    elif satuan1 == "Kilometer" and satuan2 == "Inci":
      hasil = panjang * 39370
      st.write("Hasil Konversi : ", f"**{hasil}**", satuan2)
    elif satuan1 == "Inci" and satuan2 == "Meter":
      hasil = panjang / 39.37
      st.write("Hasil Konversi : ", f"**{hasil}**", satuan2)
    elif satuan1 == "Inci" and satuan2 == "Kilometer":
      hasil = panjang / 39370
      st.write("Hasil Konversi : ", f"**{hasil}**", satuan2)
    elif satuan1 == "Sentimeter" and satuan2 == "Meter":
      hasil = panjang / 100
      st.write("Hasil Konversi : ", f"**{hasil}**", satuan2)
    elif satuan1 == "Sentimeter" and satuan2 == "Kilometer":
      hasil = panjang / 100000
      st.write("Hasil Konversi : ", f"**{hasil}**", satuan2)
    elif satuan1 == "Sentimeter" and satuan2 == "Inci":
      hasil = panjang / 2.54
      st.write("Hasil Konversi : ", f"**{hasil}**", satuan2)
    elif satuan1 == "Inci" and satuan2 == "Sentimeter":
      hasil = panjang * 2.54
      st.write("Hasil Konversi : ", f"**{hasil}**", satuan2)
    elif satuan1 == "Kilometer" and satuan2 == "Sentimeter":
      hasil = panjang * 100000
      st.write("Hasil Konversi : ", f"**{hasil}**", satuan2)
    elif satuan1 == "Meter" and satuan2 == "Sentimeter":
      hasil = panjang * 100
      st.write("Hasil Konversi : ", f"**{hasil}**", satuan2)
    elif satuan1 == "Hektometer" and satuan2 == "Meter":
      hasil = panjang * 100
      st.write("Hasil Konversi : ", f"**{hasil}**", satuan2)
    elif satuan1 == "Hektometer" and satuan2 == "Kilometer":
      hasil = panjang / 10
      st.write("Hasil Konversi : ", f"**{hasil}**", satuan2)
    elif satuan1 == "Dekameter" and satuan2 == "Meter":
      hasil = panjang * 10
      st.write("Hasil Konversi : ", f"**{hasil}**", satuan2)
    elif satuan1 == "Dekameter" and satuan2 == "Kilometer":
      hasil = panjang / 100
      st.write("Hasil Konversi : ", f"**{hasil}**", satuan2)
    elif satuan1 == "Desimeter" and satuan2 == "Meter":
      hasil = panjang * 10
      st.write("Hasil Konversi : ", f"**{hasil}**", satuan2)
    elif satuan1 == "Desimeter" and satuan2 == "Kilometer":
      hasil = panjang / 100
      st.write("Hasil Konversi : ", f"**{hasil}**", satuan2)
    elif satuan1 == "Milimeter" and satuan2 == "Meter":
      hasil = panjang / 1000
      st.write("Hasil Konversi : ", f"**{hasil}**", satuan2)
    elif satuan1 == "Milimeter" and satuan2 == "Kilometer":
      hasil = panjang / 1000000
      st.write("Hasil Konversi : ", f"**{hasil}**", satuan2)
    else:
      st.write("Hasil Konversi Tidak Valid")





if selected == "Berat":
  st.title("Konversi Satuan Berat")
  st.markdown("""
  Aplikasi ini memungkinkan Anda untuk melakukan konversi satuan berat antara:
  - Kilogram (Kg)
  - Gram (G)
  - Ton (T)
  """)
  # st.write(":gray[Gunakan alat ini untuk mengonversi panjang antara berbagai satuan, seperti meter, kilometer, inci, dan lainnya.]")

  st.image("https://i.ytimg.com/vi/RgqQzWkJrx8/maxresdefault.jpg", width=400)

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
        return nilai / 1000000
      elif dari == "Ton" and ke == "Gram":
        return nilai * 1000000
      else:
        return nilai


  # Input nilai
  nilai = st.number_input("Masukkan nilai berat:", min_value=0.0)

  # Pilihan satuan
  satuan_dari = st.selectbox("Dari satuan:", ["Kilogram", "Gram", "Ton"])
  satuan_ke = st.selectbox("Ke satuan:", ["Kilogram", "Gram", "Ton"])

  # Tombol konversi
  if st.button("Konversi"):
      hasil = konversi_berat(nilai, satuan_dari, satuan_ke)
      st.success(f"Hasil: {hasil} {satuan_ke}")




if selected == "Waktu":
  st.title("Konversi Satuan Waktu")
  st.write(":gray[Aplikasi ini memungkinkan Anda mengonversi suhu antara Celsius, Fahrenheit, Kelvin, Reaumur, dan Rankine.]")


if selected == "Suhu":
  st.title("Konversi Satuan Suhu")
  st.write(":gray[Aplikasi ini memungkinkan Anda mengonversi suhu antara Celsius, Fahrenheit, Kelvin, Reaumur, dan Rankine.]")

  import streamlit as st

  def convert_temperature(value, from_unit, to_unit):
    """Fungsi untuk mengonversi suhu dari satu unit ke unit lain."""
    if from_unit == to_unit:
        return value
    
    # Konversi ke Celsius sebagai titik tengah
    if from_unit == "Celsius":
        celsius = value
    elif from_unit == "Fahrenheit":
        celsius = (value - 32) * 5/9
    elif from_unit == "Kelvin":
        celsius = value - 273.15
    elif from_unit == "Reaumur":
        celsius = value * 5/4
    elif from_unit == "Rankine":
        celsius = (value - 491.67) * 5/9
    else:
        return None  # Tidak valid
    
    # Konversi dari Celsius ke unit tujuan
    if to_unit == "Celsius":
        return celsius
    elif to_unit == "Fahrenheit":
        return (celsius * 9/5) + 32
    elif to_unit == "Kelvin":
        return celsius + 273.15
    elif to_unit == "Reaumur":
        return celsius * 4/5
    elif to_unit == "Rankine":
        return (celsius + 273.15) * 9/5
    else:
        return None

  # Input
  value = st.number_input("Masukkan nilai suhu:", value=0.0)
  from_unit = st.selectbox("Dari satuan:", ["Celsius", "Fahrenheit", "Kelvin", "Reaumur", "Rankine"])

  # Pilihan mode
  mode = st.radio("Pilih mode konversi:", ["Konversi ke unit tertentu", "Konversi ke semua unit"])

  if mode == "Konversi ke unit tertentu":
      to_unit = st.selectbox("Ke satuan:", ["Celsius", "Fahrenheit", "Kelvin", "Reaumur", "Rankine"])
      if st.button("Konversi"):
          result = convert_temperature(value, from_unit, to_unit)
          if result is not None:
              st.write(f"**{value} {from_unit}** sama dengan **{result:.2f} {to_unit}**.")
          else:
              st.error("Konversi tidak valid!")

  elif mode == "Konversi ke semua unit":
      if st.button("Konversi Semua"):
          units = ["Celsius", "Fahrenheit", "Kelvin", "Reaumur", "Rankine"]
          results = {}
          for unit in units:
              if unit != from_unit:
                  result = convert_temperature(value, from_unit, unit)
                  results[unit] = result
          
          st.write(f"**{value} {from_unit}** dikonversi menjadi:")
          for unit, result in results.items():
              st.write(f"- {result:.2f} {unit}")



