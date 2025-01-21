from bs4 import BeautifulSoup
import requests
import MainFungsi

def MainScrapper(url, dir):
    MainFungsi.CreateDirectory(dir);
    sourceCode = requests.get(url);
    sourceText = sourceCode.text;
    soup = BeautifulSoup(sourceText, "html.parser");
    artikel = soup.find_all(True, {"class":['article__box', 'article__title']});

    for dataArtikel in artikel:
        print("URL: " + dataArtikel.a.get("href"));
        print("Judul: " + dataArtikel.text);
        print();
        formatArtikel = "URL: " + dataArtikel.a.get("href") + "\n" + "Judul: " + dataArtikel.a.text;

        if MainFungsi.DoesFileExist(dir + "/artikel.txt") is False:
            MainFungsi.CreateNewFile(dir + "/artikel.txt");

        MainFungsi.WriteToFile(dir + "/artikel.txt", formatArtikel);
        print(formatArtikel);

MainScrapper("https://tekno.kompas.com/gadget", "Hasil");