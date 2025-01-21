from bs4 import BeautifulSoup
import requests
import MainFungsi

def GetDetail(url):
    sourceCode = requests.get(url);
    sourceText = sourceCode.text;
    soup = BeautifulSoup(sourceText, "html.parser");
    divEntry = soup.find("article", {"class": "post"});
    soup = BeautifulSoup(str(divEntry), "html.parser");
    paragraf = soup.find_all("p");
    print(paragraf);
    print("paragraf: ")
    MainFungsi.WriteToFile("Cerpen Islami/artikel.txt", "Paragraf: \n");
    for p in paragraf:
        if p.string is not None:
            print(p.string);
            MainFungsi.WriteToFile("Cerpen Islami/artikel.txt", p.string);

def MainScrapper(url, dir):
    MainFungsi.CreateDirectory(dir);
    sourceCode = requests.get(url);
    sourceText = sourceCode.text;
    soup = BeautifulSoup(sourceText, "html.parser");
    artikel = soup.find_all("div", {"id": "content"});

    for dataArtikel in artikel:
        formatArtikel = "URL: " + dataArtikel.a.get("href") + "\n";

        if MainFungsi.DoesFileExist(dir + "/artikel.doc") is False:
            MainFungsi.CreateNewFile(dir + "/artikel.doc");

        MainFungsi.WriteToFile(dir + "/artikel.doc", formatArtikel);
        print(formatArtikel);
        GetDetail(dataArtikel.a.get("href"));

MainScrapper("https://cerpenmu.com/category/cerpen-islami-religi/", "Cerpen Islami")
