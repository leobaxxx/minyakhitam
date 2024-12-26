import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

# Judul Aplikasi
st.title("Kelompok Minyak Hitam")

st.write("# Tugas Kelompok Minyak Hitam")

# File gambar default (pastikan file ini ada di direktori proyek)
image_path = "kopi.jpg"  # Ganti dengan nama file gambar Anda

try:
    # Membuka gambar menggunakan PIL
    image = Image.open(image_path)

    # Menampilkan gambar langsung
    st.image(image, caption="hehehehe", use_column_width=True)

except FileNotFoundError:
    st.error(f"Tidak dapat menemukan file gambar di path: {image_path}")
    st.write("Pastikan file gambar ada di direktori yang sama dengan file kode ini.")

st.write("## Pendahuluan")
st.write("Kita mengambil data ekspor kopi karena ingin mengetahui seberapa banyak Indonesia mengekspor kopi ke luar negeri.")

st.write("## Deskripsi Data")
st.write("Data yang digunakan adalah data ekspor kopi dari tahun 2000 hingga 2023.")

# Fungsi untuk membaca file CSV
def load_data(file):
    data = pd.read_csv(file)
    return data

# Fungsi untuk merapikan data (sesuai kebutuhan dataset Anda)
def process_data(df):
    df.columns = [str(col).strip() for col in df.columns]  # Menghilangkan spasi di nama kolom
    return df

# Header aplikasi
st.title("Analisis Ekspor Kopi")

# Memuat file CSV
data_file = "kopi.csv"

try:
    data = load_data(data_file)
    data = process_data(data)

    # Menampilkan data
    st.sidebar.header("Filter Data")

    # Filter interaktif berdasarkan kolom (contoh: Tahun dan Negara Tujuan)
    if "Tahun" in data.columns:
        tahun = st.sidebar.multiselect("Pilih Tahun", sorted(data["Tahun"].unique()))
        if tahun:
            data = data[data["Tahun"].isin(tahun)]

    if "Negara Tujuan" in data.columns:
        negara = st.sidebar.multiselect("Pilih Negara Tujuan", sorted(data["Negara Tujuan"].unique()))
        if negara:
            data = data[data["Negara Tujuan"].isin(negara)]

    # Menampilkan tabel data
    st.write("### Tabel Data")
    st.dataframe(data)

    # Membuat visualisasi (contoh: Grafik Bar)
    if "Tahun" in data.columns and "Volume Ekspor" in data.columns:
        fig = px.bar(data, x="Tahun", y="Volume Ekspor", color="Negara Tujuan", title="Volume Ekspor per Tahun")
        st.plotly_chart(fig)

    # Analisis
    st.write("## Analisis")
    st.write("Jepang adalah negara tujuan dengan volume ekspor signifikan, mulai dari 65.327,4 pada tahun 2000 hingga 23.471,6 pada tahun 2020.")
    st.write("Singapura dan Malaysia juga menjadi negara tujuan, dengan volume ekspor yang bervariasi dari tahun ke tahun.")

    # Kesimpulan
    st.write("## Kesimpulan")
    st.write("Kopi merupakan salah satu komoditas utama yang memberikan kontribusi signifikan terhadap perekonomian nasional. Berdasarkan data ekspor kopi dari tahun 2000 hingga 2023, terdapat berbagai dinamika yang mencerminkan perubahan dalam permintaan global, kebijakan perdagangan, serta fluktuasi produksi dalam negeri.")
    st.write("Dengan langkah strategis dan dukungan pemerintah serta pelaku industri, prospek ekspor kopi di masa depan diharapkan dapat terus meningkat.")

    # Referensi
    st.write("## Referensi / Daftar Pustaka")
    st.write("https://www.bps.go.id/id/statistics-table/1/MTAxNCMx/ekspor-kopi-menurut-negara-tujuan-utama--2000-2023.html")

except FileNotFoundError:
    st.error(f"Tidak dapat menemukan file data di path: {data_file}")
    st.write("Pastikan file CSV tersedia di direktori yang sama dengan file kode ini.")