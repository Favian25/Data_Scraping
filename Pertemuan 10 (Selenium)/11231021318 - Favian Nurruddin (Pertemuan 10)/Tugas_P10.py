from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

URL = 'https://www.tokopedia.com/search?st=product&q=kopi+banyuwangi'

options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.186 Safari/537.36")

driver = webdriver.Chrome(options=options)
driver.get(URL)

time.sleep(20)

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

data = soup.find_all('div', {'class': 'css-5wh65g'})

for item in data:
    nama_produk = item.find('span', {'class': '_0T8-iGxMpV6NEsYEhwkqEg=='})
    harga_produk = item.find('div', {'class': '_67d6E1xDKIzw+i2D2L0tjw=='})
    penjual = item.find('span', {'class': 'T0rpy-LEwYNQifsgB-3SQw=='})

    if nama_produk and harga_produk and penjual:
        print(f"Nama Produk : {nama_produk.text.strip() if nama_produk else 'Tidak tersedia'}")
        print(f"Harga Produk: {harga_produk.text.strip() if harga_produk else 'Tidak tersedia'}")
        print(f"Nama Penjual: {penjual.text.strip() if penjual else 'Tidak tersedia'}")
        print("-" * 50)

driver.quit()