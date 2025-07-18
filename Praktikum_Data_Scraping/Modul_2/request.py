from bs4 import BeautifulSoup
import requests

url = "https://www.tempo.co/"
response = requests.get(url)

# Melakukan parsing HTML menggunakan BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Menampilkan judul halaman website
print("Judul halaman:", soup.findAll("a", {'class':'article'}))

# Menampilkan semua link yang ada pada halaman
for link in soup.find_all("a"):
    print(link.get("href"))
    
# Menampilkan semua teks pada halaman
print(soup.get_text())
print("-" * 100)

url2 = 'https://www.liputan6.com/'

# mengambil konten halaman web menggunakan requests
response = requests.get(url2)

# memproses konten halaman web dengan Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# mencetak semua judul berita
for news in soup.find_all('span', class_='articles--iridescent-list--text-item__title-link-text'):
    print(news.text.strip())