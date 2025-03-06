import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")

# --- Load Dataset ---
@st.cache_data
def load_data():
    df_orders = pd.read_csv("dashboard/data/orders_dataset.csv", parse_dates=["order_purchase_timestamp"])
    df_order_items = pd.read_csv("dashboard/data/order_items_dataset.csv")
    df_payments = pd.read_csv("dashboard/data/order_payments_dataset.csv")
    df_reviews = pd.read_csv("dashboard/data/order_reviews_dataset.csv")
    df_customers = pd.read_csv("dashboard/data/customers_dataset.csv")
    df_geolocation = pd.read_csv("dashboard/data/geolocation_dataset.csv")
    return df_orders, df_order_items, df_payments, df_reviews, df_customers, df_geolocation

df_orders, df_order_items, df_payments, df_reviews, df_customers, df_geolocation = load_data()

# --- Filter Tahun & Bulan ---
df_orders = df_orders.dropna(subset=['order_purchase_timestamp'])
year = st.sidebar.selectbox("Pilih Tahun", sorted(df_orders['order_purchase_timestamp'].dt.year.unique(), reverse=True))
month = st.sidebar.selectbox("Pilih Bulan", sorted(df_orders[df_orders['order_purchase_timestamp'].dt.year == year]['order_purchase_timestamp'].dt.month.unique()))

# Filter Data
filtered_orders = df_orders[(df_orders['order_purchase_timestamp'].dt.year == year) & 
                            (df_orders['order_purchase_timestamp'].dt.month == month)]
filtered_order_items = df_order_items[df_order_items['order_id'].isin(filtered_orders['order_id'])]

# --- 📌 KPI Ringkasan ---
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
    st.metric("💵 Rata-rata Pembayaran", f"Rp {avg_payment:,.0f}")

# --- 📈 Tren Penjualan Per Hari ---
st.subheader("📈 Tren Penjualan Per Hari")
sales_per_day = filtered_orders.groupby(filtered_orders['order_purchase_timestamp'].dt.date)['order_id'].count()

fig, ax = plt.subplots(figsize=(10, 5))
sales_per_day.plot(kind="line", marker="o", color="b", ax=ax)
ax.set_xlabel("Tanggal")
ax.set_ylabel("Jumlah Order")
ax.set_title(f"Tren Penjualan {month}/{year}")
st.pyplot(fig)

# --- 🏆 Produk Terlaris ---
st.subheader("🏆 10 Produk Terlaris")
top_products = filtered_order_items['product_id'].value_counts().head(10)

fig, ax = plt.subplots(figsize=(10, 5))
top_products.plot(kind="bar", color="skyblue", ax=ax)
ax.set_xlabel("Product ID")
ax.set_ylabel("Jumlah Terjual")
ax.set_title("Top 10 Produk Terlaris")
st.pyplot(fig)

# --- 💰 Distribusi Nilai Pembayaran ---
st.subheader("💰 Distribusi Nilai Pembayaran")
filtered_payments = df_payments[df_payments['order_id'].isin(filtered_orders['order_id'])]

fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(x=filtered_payments["payment_value"], ax=ax)
ax.set_title("Distribusi Pembayaran")
st.pyplot(fig)

# --- 🌟 Distribusi Skor Review ---
st.subheader("🌟 Distribusi Skor Review")
filtered_reviews = df_reviews[df_reviews['order_id'].isin(filtered_orders['order_id'])]

fig, ax = plt.subplots(figsize=(8, 5))
filtered_reviews["review_score"].value_counts().sort_index().plot(kind="bar", color="orange", ax=ax)
ax.set_title("Distribusi Skor Review")
ax.set_xlabel("Rating")
ax.set_ylabel("Jumlah Ulasan")
st.pyplot(fig)


