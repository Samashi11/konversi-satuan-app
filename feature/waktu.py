import streamlit as st

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
input_value = st.number_input("Masukkan nilai waktu:", min_value=0, step=0.1)

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