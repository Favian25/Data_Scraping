import requests
from bs4 import BeautifulSoup
import MainFungsi

def MainScrapper(url, dir):
    MainFungsi.CreateDirectory(dir)
    sourceCode = requests.get(url)
    sourceText = sourceCode.text
    #print(sourceText)
    soup = BeautifulSoup(sourceText, "html.parser")
    artikel = soup.find_all("div", {'class':'media media--image-radius block-link'})
    for isiArtikel in artikel:
        print(isiArtikel.a.get("href"))
        print(isiArtikel)
    
MainScrapper("https://www.detik.com", "Hasil")