# Proyek Analisis Data E-Commerce

Proyek ini bertujuan untuk menganalisis data transaksi e-commerce guna memahami pola pembelian pelanggan, tren penjualan, dan metode pembayaran yang paling sering digunakan.

## Struktur Folder
eCommerceDataset
├───dashboard
│ ├───data
│ │ ├───customers_dataset.csv
│ │ ├───geolocation_dataset.csv
│ │ ├───order_items_dataset.csv
│ │ ├───order_payments_dataset.csv
│ │ ├───order_reviews_dataset.csv
│ │ ├───orders_dataset.csv
│ │ ├───product_category_name_translation.csv
│ │ ├───products_dataset.csv
│ │ ├───sellers_dataset.csv
│ ├───dashboard.py
├───notebook.ipynb
├───requirements.txt
├───README.md
└───url.txt
---

## Instalasi dan Cara Menjalankan

    ### 1️ Clone Repository  
    Jika proyek ini berada di GitHub, clone repository-nya:  
    ```sh
    git clone https://github.com/username/proyek-analisis-data.git
    cd proyek-analisis-data

    ### 2 Buat Virtual Environment (Opsional) 
    Untuk menghindari konflik dependensi, buat virtual environment:

    python -m venv env
    source env/bin/activate  # Mac/Linux
    env\Scripts\activate  # Windows

    ### 3 Install Dependencies
    Pastikan semua library yang diperlukan telah terinstall dengan menjalankan perintah berikut:
    
    pip install -r requirements.txt

    ### 4 Jalankan Notebook
    Buka Jupyter Notebook atau Google Colab, lalu jalankan notebook.ipynb untuk melakukan analisis data:

    jupyter notebook

    ### 5 Menjalankan Dashboard (Streamlit)
    Untuk melihat dashboard interaktif, jalankan perintah berikut:

    streamlit run dashboard.py

## Fitur Dashboard
1. Analisis Tren Penjualan
2. Top 10 Produk Terlaris
3. Distribusi Nilai Pembayaran
4. Analisis Geospasial

## Dataset yang Digunakan
Proyek ini menggunakan dataset transaksi e-commerce, yang terdiri dari beberapa file CSV:

1. orders_dataset.csv → Data pesanan
2. order_items_dataset.csv → Detail item dalam pesanan
3. order_payments_dataset.csv → Data pembayaran
5. customers_dataset.csv → Data pelanggan
6. products_dataset.csv → Data produk
7. sellers_dataset.csv → Data penjual
8. geolocation_dataset.csv → Data lokasi
9. order_reviews_dataset.csv → Data ulasan pelanggan
10. product_category_name_translation.csv → Data kategori produk

## Link Dashboard


## Kontributor
Elyzia Janara | Data Analyst