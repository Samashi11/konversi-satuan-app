import streamlit as st

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