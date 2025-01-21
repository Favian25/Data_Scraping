import requests
from bs4 import BeautifulSoup

htmlDoc = requests.get('https://www.detik.com/jatim/berita/indeks')
soup = BeautifulSoup(htmlDoc.text, 'html.parser')

populerArea = soup.find(attrs={'class':'grid-row list-content'})

titles = populerArea.find_all(attrs={'class':'media__title'})
images = populerArea.find_all(attrs={'class':'media__image'})
# images = populerArea.find_all(attrs={'class':'list-content__item'})

for image in images:
    print(image.find('a').find('img'))
    # print(image.find('div', {'class':'media__date'})find('span')['title'])