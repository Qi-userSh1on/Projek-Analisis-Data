import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='dark')

st.write(
    """
    # Proyek Analisis Data
    By: Qianna Vassaputri MS-08
    """
)

# Pertanyaan ke-1
st.write("***1. Musim manakah yang memiliki peningkatan pada penyewaan sepeda?***")

day_df = pd.read_csv('day.csv')
hour_df = pd.read_csv('hour.csv')

byseason = hour_df.groupby("season")["cnt"].sum().sort_values(ascending=False).reset_index()

colors = ["#645CAA", "#A084CA", "#BFACE0", "#EBC7E8"]

plt.figure(figsize=(10, 5))
sns.barplot(y="cnt", x="season", data=byseason, palette=colors)
plt.title("Pengguna Sepeda Berdasarkan Musim", loc="center", fontsize=15)
plt.ylabel("Total Pengguna")
plt.xlabel("Musim")
plt.ticklabel_format(style='plain', axis='y')

st.pyplot(plt.gcf())

# Pertanyaan ke-2
st.write("***2. Bagaimana rata-rata penurunan penyewaan sepeda dalam tiap minggu?***")

day_df = pd.read_csv('day.csv')
day_df["dteday"] = pd.to_datetime(day_df["dteday"], errors='coerce')

day_df["weekday"] = day_df["dteday"].dt.weekday

# Rata-rata penyewaan per-hari dalam per-minggu
weekday_avg = day_df.groupby("weekday")["cnt"].mean()

plt.figure(figsize=(10, 5))
plt.plot(weekday_avg.index, weekday_avg.values, marker="o", linestyle="-", color="#4d4686", alpha=0.6)
plt.xlabel("Hari dalam Seminggu (0 = Senin, 6 = Minggu)")
plt.ylabel("Rata-rata Penyewaan")
plt.title("Rata-rata Penyewaan Sepeda per Hari dalam Seminggu")
plt.grid(True)
plt.legend(["Hari dalam Seminggu (0 = Senin, 6 = Minggu)"])

st.pyplot(plt.gcf())