from bs4 import BeautifulSoup
import requests
import MainFungsi

def MainScrapper(url, dir):
    MainFungsi.CreateDirectory(dir);
    sourceCode = requests.get(url);
    sourceText = sourceCode.text;
    soup = BeautifulSoup(sourceText, "html.parser");
    artikel1 = soup.find_all("h3", {"class":"article__title articletitle__medium"})
    artikel2= soup.find_all(True, {"class":['article__box', 'article__title']});
    
    for dataArtikel1 in artikel1:
        print("URL:" + dataArtikel1.a.get("href"));
        print("Judul:" + dataArtikel1.text);
        
    for dataArtikel2 in artikel2:
        print("URL:" + dataArtikel2.a.get("href"));
        print("Judul:" + dataArtikel2.text);

MainScrapper("https://tekno.kompas.com/gadget", "Hasil");