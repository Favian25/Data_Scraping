import pandas as pd
import requests

# # membuat series dari list
# daftar_nilai = [10, 20, 30, 40]
# my_series = pd.Series(daftar_nilai)
# print(my_series)

# # membuat series dari dictionary
# my_dict = {'a': 100, 'b': 200, 'c': 300}
# my_series = pd.Series(my_dict)
# print(my_series)


# url = 'https://referensi.data.kemdikbud.go.id/pendidikan/yayasan'
# response = requests.get(url)
# tables = pd.read_html(response.text)

# data_table = tables[0]
# print(data_table)


# # definisikan URL website
# url = 'https://www.w3schools.com/html/html_tables.asp'

# # Menentukan header dan index kolom
# header_row = 0
# index_col = 0

# # Menentukan nama tabel yang ingin dibaca
# table_name = "Contact"

# # Membaca tabel data dari halaman web dan mengembalikan DataFrame
# df_list = pd.read_html(url, header=header_row,
# index_col=index_col, match=table_name)

# # Mengambil DataFrame pertama dari list hasil bacaan
# df = df_list[0]

# # Menampilkan DataFrame sebelum sorting dan filtering
# print("Sebelum sorting dan filtering:")
# print(df)
# print("-" * 55)

# # Sorting DataFrame berdasarkan kolom "Country"
# df_sorted = df.sort_values("Country")

# # Filtering DataFrame hanya dengan data dari "Germany"
# df_filtered = df[df["Country"] == "Germany"]

# # Menampilkan DataFrame setelah sorting dan filtering
# print("Setelah sorting dan filtering:")
# print(df_sorted)
# print("-" * 55)
# print(df_filtered)

# # Menyimpan DataFrame ke dalam file CSV
# df.to_csv("data.csv", index=False)
# # Menyimpan DataFrame ke dalam file Excel
# df.to_excel("data.xlsx", index=False)

url = 'https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data#covid-19-pandemic-data'

header_row = 0
index_col = 0
skiprows = 0

attrs = {'class': 'wikitable'}
df_list = pd.read_html(url, header=header_row,
index_col=index_col, skiprows=skiprows, attrs=attrs)

df = df_list[0]
print("Kolom:", df.columns)

df = df[df["Cases"].str.replace(',', '').str.isnumeric()]
df["Cases"] = pd.to_numeric(df["Cases"].str.replace(',', ''), errors='coerce')
df["Deaths"] = pd.to_numeric(df["Deaths"].str.replace(',', ''), errors='coerce')
df = df.assign(Jumlah=df["Cases"] * df["Deaths"])

print("\nSebelum sorting dan filtering:")
print(df)

df_sorted = df.sort_values("Location")
df_filtered = df[df["Location"] == "Indonesia"]

df_sorted.to_csv("data.csv", index=False)
df_sorted.to_excel("data.xlsx", index=False)

print("\nSetelah sorting dan filtering:")
print(df_sorted)
print(df_filtered)

df["Kasus+Kematian"] = df["Cases"] + df["Deaths"]
df["Fatality Rate (%)"] = (df["Deaths"] / df["Cases"]) * 100
df.to_excel("data_tugas.xlsx", index=False)

print("\nData dengan kolom tambahan:")
print(df[["Location", "Cases", "Deaths", "Kasus+Kematian", "Fatality Rate (%)"]])