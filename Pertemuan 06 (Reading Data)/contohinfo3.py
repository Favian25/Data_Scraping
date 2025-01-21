from bs4 import BeautifulSoup
import requests
import MainFungsi

def GetDetail(url):
    sourceCode = requests.get(url)
    sourceText = sourceCode.text
    soup = BeautifulSoup(sourceText, "html.parser")
    divEntry = soup.find("article", {"class": "post"})
    soup = BeautifulSoup(str(divEntry), "html.parser")
    paragraf = soup.find_all("p")
    print(paragraf)
    print("paragraf: ")
    MainFungsi.WriteToFile("Cerpen Islami/artikel.txt", "Paragraf: \n")
    for p in paragraf:
        if p.string is not None:
            print(p.string)
            MainFungsi.WriteToFile("Cerpen Islami/artikel.txt", p.string)

def MainScrapper(url, dir):
    MainFungsi.CreateDirectory(dir);
    sourceCode = requests.get(url);

    sourceText = sourceCode.text;
    soup = BeautifulSoup(sourceText, "html.parser");

    artikel = soup.find_all(True, {"class":"articles--iridescent-list--item articles--iridescent-list--text-item"});

    for dataArtikel in artikel:
        formatArtikel = "URL: " + dataArtikel.a.get("href") + "\n Tanggal: " + \
                        dataArtikel.time.get("datetime") + "\n Judul: " + dataArtikel.a.get("title") + "\n Waktu: " + \
                        dataArtikel.time.text + "\n";

        print(formatArtikel);

MainScrapper("https://www.liputan6.com/tekno/berita", "hasil");