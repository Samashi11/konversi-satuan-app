import streamlit as st
from PIL import Image

st.set_page_config(page_title='Konversi Satuan App')

# home = Image.open('img/sttnf.png')
# st.image(home, use_column_width=True)

page_bg_style = """
<style>
    body {
        background-image: url("img/sttnf.png"); /* Pastikan path gambar benar */
        background-color: #4DA1A9; /* Warna biru muda */
        background-size: cover; /* Memastikan latar belakang memenuhi layar */
        background-attachment: fixed; /* Latar belakang tetap saat scroll */
    }
    [data-testid="stAppViewContainer"] {
        color: black; /* Warna teks */
    }
    [data-testid="stSidebar"] {
        background-color: #074799; /* Warna biru muda transparan */
    }
    [data-testid="stNavSectionHeader"] {
        color: #ffff; /* Warna teks sidebar */
    }
    [data-testid="stSidebarNavLink"] span {
        color: #ffff; /* Warna teks sidebar */
    }
    [data-testid="stSidebarNavLink"] span span {
        color: #ffff!important; /* Warna teks sidebar */
    }
    [data-testid="stSidebarCollapseButton"] {
        color: white; /* Warna teks sidebar */
    }
</style>
"""

# Menyisipkan CSS ke aplikasi
st.markdown(page_bg_style, unsafe_allow_html=True)


home = st.Page("./feature/home.py", title="Home", icon=":material/home:")
panjang = st.Page("./feature/panjang.py", title="Panjang", icon=":material/straighten:")
berat = st.Page("./feature/berat.py", title="Berat", icon=":material/weight:")
waktu = st.Page("./feature/waktu.py", title="Waktu", icon=":material/hourglass_empty:")
suhu = st.Page("./feature/suhu.py", title="Suhu", icon=":material/device_thermostat:")

# Navigasi
pg = st.navigation(
  {
    "Menu Utama": [home],
    "Konversi": [panjang, berat, waktu, suhu],
    
  }
)

pg.run()