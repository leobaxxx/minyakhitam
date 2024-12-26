import streamlit as st
import pandas as pd
import plotly.express as px
import os
from PIL import Image

st.title("Kelompok Minyak Hitam")

st.write("# Tugas Kelompok Minyak Hitam")
# Judul Aplikasi
st.title("")

# File gambar default (pastikan file ini ada di direktori proyek)
image_path = "kopi.jpg"  # Ganti dengan nama file gambar Anda

try:
    # Membuka gambar menggunakan PIL
    image = Image.open(image_path)
    
    # Menampilkan gambar langsung
    st.image(image, caption="hehehehe", use_container_width=True)
    

except FileNotFoundError:
    st.error(f"Tidak dapat menemukan file gambar di path: {image_path}")
    st.write("Pastikan file gambar ada di direktori yang sama dengan file kode ini.")
    
st.write("## Pendahuluan")
st.write("kita mengambil data Ekspor Kopi karena ingin mengetahui negara indonesia mengekspor kopi ke negara luar  berapa banyak")

st.write("## Deskripsi Data")
st.write("kita mengambil data dari tahun 2000 sampai dengan 2023")

st.write("##")

# # Fungsi untuk membaca file Excel
def load_data(file):
    data = pd.read_excel(file, sheet_name=None)  # Membaca semua sheet
    return data

# Fungsi untuk merapikan data (sesuai kebutuhan dataset Anda)
def process_data(sheet):
    df = sheet.copy()
    df.columns = [str(col).strip() for col in df.columns]  # Menghilangkan spasi di nama kolom
    return df

# Header aplikasi
st.title("Analisis Ekspor Kopi")

# Memuat file Excel
data_file = "Ekspor Kopi Menurut Negara Tujuan Utama, 2000-2023.xlsx"
data = load_data(data_file)

# Menampilkan daftar sheet
data_sheets = list(data.keys())
st.sidebar.header("Filter Data")
selected_sheet = st.sidebar.selectbox("Pilih Sheet Data", data_sheets)

# Memproses data dari sheet yang dipilih
sheet_data = process_data(data[selected_sheet])
st.write(f"### Data dari Sheet: {selected_sheet}")

# Filter interaktif berdasarkan kolom (contoh: Tahun dan Negara Tujuan)
if "Tahun" in sheet_data.columns:
    tahun = st.sidebar.multiselect("Pilih Tahun", sheet_data["Tahun"].unique())
    if tahun:
        sheet_data = sheet_data[sheet_data["Tahun"].isin(tahun)]

if "Negara Tujuan" in sheet_data.columns:
    negara = st.sidebar.multiselect("Pilih Negara Tujuan", sheet_data["Negara Tujuan"].unique())
    if negara:
        sheet_data = sheet_data[sheet_data["Negara Tujuan"].isin(negara)]

# Menampilkan tabel data
st.write("### Tabel Data")
st.dataframe(sheet_data)

# Membuat visualisasi (contoh: Grafik Bar)
if "Tahun" in sheet_data.columns and "Volume Ekspor" in sheet_data.columns:
    fig = px.bar(sheet_data, x="Tahun", y="Volume Ekspor", color="Negara Tujuan", title="Volume Ekspor per Tahun")
    st.plotly_chart(fig)

# Catatan tambahan
st.write("Gunakan panel samping untuk memfilter data berdasarkan kebutuhan Anda.")

st.write("")

st.write("## Analisis")
st.write("Jepang adalah negara tujuan dengan volume ekspor signifikan, mulai dari 65.327,4 pada tahun 2000 hingga 23.471,6 pada tahun 2020")
("Singapura dan Malaysia juga menjadi negara tujuan, dengan volume ekspor yang bervariasi dari tahun ke tahun.")

st.write("## Kesimpulan")
st.write("Kopi merupakan salah satu komoditas utama yang memberikan kontribusi signifikan terhadap perekonomian nasional. Berdasarkan data ekspor kopi dari tahun 2000 hingga 2023, terdapat berbagai dinamika yang mencerminkan perubahan dalam permintaan global, kebijakan perdagangan, serta fluktuasi produksi dalam negeri. Negara-negara tujuan utama seperti Jepang, Amerika Serikat, dan negara-negara Eropa konsisten menjadi pasar terbesar bagi produk kopi nasional.")

("Namun, dalam kurun waktu tersebut, tren menunjukkan adanya diversifikasi pasar ekspor. Beberapa negara berkembang mulai menunjukkan peningkatan permintaan terhadap kopi, seiring dengan perubahan pola konsumsi masyarakat global. Hal ini membuka peluang bagi produsen kopi untuk memperluas jaringan perdagangan ke pasar-pasar non-tradisional.")

("Meskipun demikian, ekspor kopi juga menghadapi tantangan. Fluktuasi harga internasional, perubahan iklim yang memengaruhi hasil panen, serta persaingan dengan negara produsen lain menjadi faktor yang perlu diperhatikan untuk menjaga daya saing kopi nasional. Upaya peningkatan kualitas produk, sertifikasi, dan diversifikasi jenis kopi menjadi langkah penting untuk mengatasi tantangan tersebut.")

("Dengan langkah strategis dan dukungan pemerintah serta pelaku industri, prospek ekspor kopi di masa depan diharapkan dapat terus meningkat dan memberikan manfaat ekonomi yang lebih besar bagi semua pihak yang terlibat dalam rantai pasokannya.")

st.write("## Referensi / Daftar Pustaka")
st.write("https://www.bps.go.id/id/statistics-table/1/MTAxNCMx/ekspor-kopi-menurut-negara-tujuan-utama--2000-2023.html")
