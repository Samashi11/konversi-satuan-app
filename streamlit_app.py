import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Konversi Satuan App')

st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background: linear-gradient(90deg, #a1c4fd, #c2e9fb); /* Warna gradien biru muda */
        animation: gradientAnimation 5s ease infinite;
        background-size: 200% 200%; /* Memastikan animasi terlihat */
    }

    @keyframes gradientAnimation {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.image("img/sttnf.png", width=150)
st.sidebar.markdown("")

# Navigasi Sidebar
with st.sidebar:
  selected = option_menu(
    menu_title="Aplikasi \n Konversi Satuan",
    options=["Home", "Panjang", "Berat","Waktu", "Suhu"],
    icons=["house-fill","rulers","box-fill","hourglass-split","thermometer-half"],
    menu_icon="cast",
    default_index=0,
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

  def konversi_panjang(panjang, satuan1, satuan2):
    if satuan1 == "Sentimeter":
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
    elif satuan1 == "Kilometer":
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
    elif satuan1 == "Inci":
      if satuan2 == "Kilometer":
        return panjang / 39370
      elif satuan2 == "Hektometer":
        return panjang / 393.7
      elif satuan2 == "Dekameter":
        return panjang / 39.37
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
    elif satuan1 == "Hektometer":
      if satuan2 == "Sentimeter":
        return panjang * 10000
      elif satuan2 == "Meter":
        return panjang * 100
      elif satuan2 == "Kilometer":
        return panjang / 10
      elif satuan2 == "Inci":
        return panjang * 393.7
      elif satuan2 == "Dekameter":
        return panjang * 10
      elif satuan2 == "Desimeter":
        return panjang * 10
      elif satuan2 == "Milimeter":
        return panjang * 10000
      else:
        return None
    elif satuan1 == "Dekameter":
      if satuan2 == "Sentimeter":
        return panjang * 1000
      elif satuan2 == "Meter":
        return panjang * 10
      elif satuan2 == "Kilometer":
        return panjang / 100
      elif satuan2 == "Inci":
        return panjang * 39.37
      elif satuan2 == "Hektometer":
        return panjang / 10
      elif satuan2 == "Desimeter":
        return panjang / 10
      elif satuan2 == "Milimeter":
        return panjang * 1000
      else:
        return None
    elif satuan1 == "Desimeter":
      if satuan2 == "Sentimeter":
        return panjang * 10
      elif satuan2 == "Meter":
        return panjang / 10
      elif satuan2 == "Kilometer":
        return panjang / 10000
      elif satuan2 == "Inci":
        return panjang * 3.937
      elif satuan2 == "Hektometer":
        return panjang / 100
      elif satuan2 == "Dekameter":
        return panjang / 10
      elif satuan2 == "Milimeter":
        return panjang * 10
      else:
        return None
    elif satuan1 == "Milimeter":
      if satuan2 == "Sentimeter":
        return panjang * 10
      elif satuan2 == "Meter":
        return panjang / 1000
      elif satuan2 == "Kilometer":
        return panjang / 1000000
      elif satuan2 == "Inci":
        return panjang / 25.4
      elif satuan2 == "Hektometer":
        return panjang / 10000
      elif satuan2 == "Dekameter":
        return panjang / 1000
      elif satuan2 == "Desimeter":
        return panjang / 10
      else:
        return None
    else:
      return None


  if konversi:
    hasil = konversi_panjang(panjang, satuan1, satuan2)
    if hasil is not None:
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
  # Judul aplikasi
  st.title("Konversi Satuan Waktu")

  # Gambar waktu
  st.image("img/konversi_waktu.png", width=400)

  # Deskripsi aplikasi
  st.write("""
  ### Deskripsi Aplikasi:
  Aplikasi ini membantu Anda mengonversi nilai waktu dari satu satuan ke satuan lainnya, 
  seperti dari Jam ke Menit, Menit ke Detik, atau bahkan hingga Milidetik dan Mikrodetik. 
  Berikut langkah-langkah menggunakan aplikasi ini:
  1. **Masukkan nilai waktu** yang ingin Anda konversi (contoh: 2 untuk 2 Jam).
  2. **Pilih satuan asal** dari nilai waktu yang Anda masukkan (contoh: Jam).
  3. **Pilih satuan tujuan** untuk mengonversi waktu ke satuan yang diinginkan (contoh: Menit).
  4. Klik tombol **Konversi** untuk melihat hasilnya.
  5. Aplikasi akan menampilkan hasil konversi dan informasi tambahan untuk membantu Anda memahami proses konversi.
  """)

  # Input nilai waktu
  input_value = st.number_input("Masukkan nilai waktu:", min_value=0.0, step=0.1)

  # Pilihan satuan asal dan tujuan
  st.write("### Pilih konversi waktu:")
  options = ["Jam", "Menit", "Detik", "Milidetik", "Mikrodetik"]
  from_unit = st.selectbox("Dari (satuan asal):", options)
  to_unit = st.selectbox("Ke (satuan tujuan):", options)

  # Tombol konversi
  if st.button("Konversi"):
      # Inisialisasi variabel untuk hasil konversi
      result = 0.0
      
      # Konversi waktu menggunakan if-elif
      if from_unit == "Jam":
          if to_unit == "Menit":
              result = input_value * 60
          elif to_unit == "Detik":
              result = input_value * 3600
          elif to_unit == "Milidetik":
              result = input_value * 3600000
          elif to_unit == "Mikrodetik":
              result = input_value * 3600000000
          else:
              result = input_value  # Jika sama satuan, hasil sama dengan input
      elif from_unit == "Menit":
          if to_unit == "Jam":
              result = input_value / 60
          elif to_unit == "Detik":
              result = input_value * 60
          elif to_unit == "Milidetik":
              result = input_value * 60000
          elif to_unit == "Mikrodetik":
              result = input_value * 60000000
          else:
              result = input_value
      elif from_unit == "Detik":
          if to_unit == "Jam":
              result = input_value / 3600
          elif to_unit == "Menit":
              result = input_value / 60
          elif to_unit == "Milidetik":
              result = input_value * 1000
          elif to_unit == "Mikrodetik":
              result = input_value * 1000000
          else:
              result = input_value
      elif from_unit == "Milidetik":
          if to_unit == "Jam":
              result = input_value / 3600000
          elif to_unit == "Menit":
              result = input_value / 60000
          elif to_unit == "Detik":
              result = input_value / 1000
          elif to_unit == "Mikrodetik":
              result = input_value * 1000
          else:
              result = input_value
      elif from_unit == "Mikrodetik":
          if to_unit == "Jam":
              result = input_value / 3600000000
          elif to_unit == "Menit":
              result = input_value / 60000000
          elif to_unit == "Detik":
              result = input_value / 1000000
          elif to_unit == "Milidetik":
              result = input_value / 1000
          else:
              result = input_value

      # Tampilkan hasil
      st.write("### Hasil Konversi:")
      st.success(f"{input_value} {from_unit} sama dengan **{result:.2f} {to_unit}**")



if selected == "Suhu":
  st.title("Konversi Satuan Suhu")
  st.image("img/konversi_suhu.jpg", width=400)
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



