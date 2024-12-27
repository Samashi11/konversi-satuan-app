import streamlit as st

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