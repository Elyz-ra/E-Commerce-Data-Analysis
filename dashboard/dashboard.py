import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")

# --- Load Dataset ---
@st.cache_data
def load_data():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(BASE_DIR, "..", "data")

    df_orders = pd.read_csv(os.path.join(DATA_DIR, "orders_dataset.csv"), parse_dates=["order_purchase_timestamp"])
    df_order_items = pd.read_csv(os.path.join(DATA_DIR, "order_items_dataset.csv"))
    df_payments = pd.read_csv(os.path.join(DATA_DIR, "order_payments_dataset.csv"))
    df_reviews = pd.read_csv(os.path.join(DATA_DIR, "order_reviews_dataset.csv"))
    df_customers = pd.read_csv(os.path.join(DATA_DIR, "customers_dataset.csv"))
    df_geolocation = pd.read_csv(os.path.join(DATA_DIR, "geolocation_dataset.csv"))

    return df_orders, df_order_items, df_payments, df_reviews, df_customers, df_geolocation

df_orders, df_order_items, df_payments, df_reviews, df_customers, df_geolocation = load_data()

# --- Filter Tahun & Bulan ---
df_orders = df_orders.dropna(subset=['order_purchase_timestamp'])
year = st.sidebar.selectbox("Pilih Tahun", sorted(df_orders['order_purchase_timestamp'].dt.year.unique(), reverse=True))

available_months = sorted(df_orders[df_orders['order_purchase_timestamp'].dt.year == year]['order_purchase_timestamp'].dt.month.unique())

if len(available_months) > 0:
    month = st.sidebar.selectbox("Pilih Bulan", available_months)
else:
    st.warning("Tidak ada data untuk tahun ini.")
    st.stop()

# Filter Data
filtered_orders = df_orders[(df_orders['order_purchase_timestamp'].dt.year == year) & 
                            (df_orders['order_purchase_timestamp'].dt.month == month)]
filtered_order_items = df_order_items[df_order_items['order_id'].isin(filtered_orders['order_id'])]

# --- KPI Ringkasan ---
st.title("📊 E-Commerce Dashboard")
st.write(f"**Analisis Penjualan - {month}/{year}**")

col1, col2, col3 = st.columns(3)
with col1:
    total_orders = filtered_orders.shape[0]
    st.metric("📦 Total Order", total_orders)

with col2:
    total_revenue = df_payments[df_payments['order_id'].isin(filtered_orders['order_id'])]['payment_value'].sum()
    st.metric("💰 Total Revenue", f"Rp {total_revenue:,.0f}")

with col3:
    avg_payment = df_payments[df_payments['order_id'].isin(filtered_orders['order_id'])]['payment_value'].mean()
    avg_payment = avg_payment if not pd.isna(avg_payment) else 0
    st.metric("💵 Rata-rata Pembayaran", f"Rp {avg_payment:,.0f}")

# --- Plot Data ---
st.subheader("📈 Tren Penjualan Per Hari")
sales_per_day = filtered_orders.groupby(filtered_orders['order_purchase_timestamp'].dt.date)['order_id'].count()
fig, ax = plt.subplots(figsize=(10, 5))
sales_per_day.plot(kind="line", marker="o", color="b", ax=ax)
ax.set_xlabel("Tanggal")
ax.set_ylabel("Jumlah Order")
ax.set_title(f"Tren Penjualan {month}/{year}")
st.pyplot(fig)
