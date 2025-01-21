import requests
import MainFungsi

def MainScrapper(url, dir):
    MainFungsi.CreateDirectory(dir)
    sourceCode = requests.get(url)
    sourceText = sourceCode.text
    print(sourceText)
    
MainScrapper("https://www.detik.com", "Hasil")