import requests
from bs4 import BeautifulSoup

url = 'https://dongengceritarakyat.com'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
datax = soup.find_all('img')

print(datax)