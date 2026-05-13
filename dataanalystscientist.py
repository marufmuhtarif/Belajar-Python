import pandas as pd
import numpy as np

# 1. Membuat/Memuat Dataset (Contoh Data Penjualan)
data = {
    'Produk': ['A', 'B', 'A', 'C', 'B', 'A', 'C', np.nan],
    'Harga': [100, 150, 100, 200, 150, 100, 200, 300],
    'Jumlah': [2, 1, 3, 1, 2, 2, 1, 1],
    'Tanggal': ['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-03', 
                '2023-01-02', '2023-01-04', '2023-01-05', '2023-01-06']
}
df = pd.DataFrame(data)

# 2. Data Cleaning
# Menangani Missing Values
df['Produk'] = df['Produk'].fillna('Unknown')

# Menghapus Duplikat
df.drop_duplicates()

# Mengubah tipe data tanggal
df['Tanggal'] = pd.to_datetime(df['Tanggal'])

print("Data setelah dibersihkan:")
print(df.info())

# 3. Analisis Dasar
# Menghitung total penjualan per produk

df['Total_Penjualan'] = df['Harga'] * df['Jumlah']
pivot_table = df.groupby('Produk')['Total_Penjualan'].sum().reset_index()

print("\nTotal Penjualan per Produk:")
print(pivot_table)

# 4. Statistik Deskriptif
print("\nStatistik Deskriptif:")
print(df.describe())

import matplotlib.pyplot as plt
import seaborn as sns

# Mengatur style seaborn
sns.set(style="whitegrid")

# 5. Membuat Plot
plt.figure(figsize=(10, 6))
sns.barplot(x='Produk', y='Total_Penjualan', data=pivot_table, palette='viridis')

# Menambahkan Label
plt.title('Total Penjualan per Produk', fontsize=16)
plt.xlabel('Produk', fontsize=12)
plt.ylabel('Total Pendapatan', fontsize=12)

# Menampilkan plot
plt.show()
