from bs4 import BeautifulSoup
import requests
import MainFungsi

def GetDetail(url):
    sourceCode = requests.get(url)
    sourceText = sourceCode.text
    soup = BeautifulSoup(sourceText, "html.parser")
    divEntry = soup.find_all("div", {"class": "article-content-body__item-content"})
    print("Isi Berita: ")
    MainFungsi.WriteToFile("Pertemuan 7/hasil/artikel.doc", "Isi Berita:\n")
    for p in divEntry:
        if p.get_text() is not None:
            isiBerita = p.get_text().strip()
            print(isiBerita)
            MainFungsi.WriteToFile("Pertemuan 7/hasil/artikel.doc", isiBerita)

def MainScrapper(url, dir):
    MainFungsi.CreateDirectory(dir)
    sourceCode = requests.get(url)
    sourceText = sourceCode.text
    soup = BeautifulSoup(sourceText, "html.parser")
    artikel = soup.find_all(True, {"class":"post"})

    for dataArtikel in artikel:
        formatArtikel = dataArtikel.text + "\n"
        if not MainFungsi.DoesFileExist(dir + "/artikel.doc"):
            MainFungsi.CreateNewFile(dir + "/artikel.doc")

        MainFungsi.WriteToFile(dir + "/artikel.doc", formatArtikel)
        print(formatArtikel)
        # GetDetail(dataArtikel.a.get("href"))

MainScrapper("https://cerpenmu.com/category/cerpen-islami-religi/", "hasil")
