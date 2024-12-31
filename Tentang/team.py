import streamlit as st
import os
from PIL import Image

# Kode CSS untuk styling halaman
about_us_style = """
<style>
    body {
        background-color: #FFFFFF; /* Warna putih */
    }
    [data-testid="stAppViewContainer"] {
        padding: 20px;
    }
    h1, h2, h3 {
        color: #074799; /* Warna teks utama */
    }
    p {
        color: #333333; /* Warna teks deskripsi */
        font-size: 18px;
        line-height: 1.6;
    }
    .team-img {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    .team-img img {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        margin: 10px;
    }
    .stMain {
        background-color: #FFFFFF; /* Warna background */
    }
    .stAppHeader, .stAppFooter {
        opacity: 0;
    }
    [data-testid="stAppViewContainer"] {
        padding: 0px;
    }
    [data-testid="stBaseButton-headerNoPadding"] {
        color: orange;
    }
</style>
"""

# Menyisipkan CSS ke aplikasi
st.markdown(about_us_style, unsafe_allow_html=True)

# Judul halaman
st.title("Tentang Kami")

# Deskripsi aplikasi
st.write("""
### Apa itu Aplikasi Konversi Satuan?
Aplikasi Konversi Satuan adalah platform sederhana yang dirancang untuk mempermudah pengguna 
dalam mengonversi berbagai satuan, seperti panjang, berat, waktu, dan suhu. 
Kami berkomitmen untuk menyediakan alat yang user-friendly, interaktif, dan mudah digunakan.

### Tujuan Kami
Kami ingin membantu masyarakat dalam menyelesaikan kebutuhan sehari-hari terkait konversi satuan 
dengan cepat dan akurat. Kami percaya bahwa teknologi dapat mempermudah hidup Anda.
""")

# Foto Tim (Opsional)
st.write("### Tim Pengembang")
team_images = [
    {
        "name": "Wahyu Ahmad Yassin",
        "img_path": "img/wahyu1.png",
        "description": "Mahasiswa baru di bidang Teknik Informatika yang memiliki semangat tinggi untuk belajar dan berkembang di dunia teknologi.",
        "contact": {
            "GitHub": "https://github.com/bgwahyoe",
            "LinkedIn": "https://linkedin.com/in/wahyuahmadyassin"
        }
    },
    {
        "name": "Salman Maula As-Shidqi",
        "img_path": "img/salman.png",
        "description": "Mahasiswa baru di bidang Teknik Informatika yang memiliki semangat tinggi untuk belajar dan berkembang di dunia teknologi.",
        "contact": {
            "GitHub": "https://github.com/Samashi11",
            "LinkedIn": "https://www.linkedin.com/in/salman-shidqi-31409428b/"
        }
    },
    {
        "name": "Ferdy Pratama",
        "img_path": "img/ferdy1.jpg",
        "description": "Mahasiswa baru di bidang Teknik Informatika yang memiliki semangat tinggi untuk belajar dan berkembang di dunia teknologi.",
        "contact": {
            "GitHub": "https://github.com/ferdy",
            "LinkedIn": "https://linkedin.com/in/ferdy" 
        }
    },
    {
        "name": "Muhammad Varrel Mahardika",
        "img_path": "img/varrel1.jpg",
        "description": "Mahasiswa baru di bidang Teknik Informatika yang memiliki semangat tinggi untuk belajar dan berkembang di dunia teknologi.",
        "contact": {
            "GitHub": "https://github.com/varrel",
            "LinkedIn": "https://linkedin.com/in/varrel"
        }
    },
]

# Menampilkan foto tim dan informasi
for member in team_images:
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image(member["img_path"], caption=member["name"], use_container_width=True)
    with col2:
        st.write(f"**{member['name']}**")
        st.write(f"*{member['description']}*")
        st.write("**Contact:**")
        for platform, url in member["contact"].items():
            st.markdown(f"[{platform}]({url})")

# Informasi tambahan
st.write("""\n\n
### Hubungi Kami
Jika Anda memiliki saran, pertanyaan, atau ingin berkolaborasi, jangan ragu untuk menghubungi kami:

- Email : wahyuyassin@gmail.com
- Telepon : [+62 895 6048 49987](https://wa.me/+62895604849987) | [+62 813 1828 8133](https://wa.me/+6281318288133)
- Media Sosial : [Instagram](https://instagram.com/bg.wahyoee) | [Github](https://github.com/Samashi11/konversi-satuan-app)

Terima kasih telah menggunakan aplikasi kami!
""")
