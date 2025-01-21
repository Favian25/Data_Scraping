from bs4 import BeautifulSoup
import requests
import re
import MainFungsi

def GetDetail(url, file_path):
    try:
        sourceCode = requests.get(url)
        sourceCode.raise_for_status()
        sourceText = sourceCode.text
        soup = BeautifulSoup(sourceText, "html.parser")

        judul = soup.find("h1")
        judul_text = f"Judul: {judul.get_text(strip=True)}" if judul else "Judul: Tidak ditemukan"

        pengarang = soup.find("a", {"rel": "tag"})
        article = soup.find("article", {"class": "post"})
        
        if article:
            article_text = article.get_text(separator=" ")
            print("DEBUG - Full article text:\n", article_text)

            date_pattern = r"(\d{1,2} \w+ \d{4})"
            match = re.search(date_pattern, article_text)
            if match:
                tanggal = match.group(1)
            else:
                tanggal = "Tidak ditemukan"
        else:
            tanggal = "Tidak ditemukan"

        MainFungsi.WriteToFile(file_path, judul_text)
        MainFungsi.WriteToFile(file_path, f"Pengarang: {pengarang.get_text(strip=True) if pengarang else 'Tidak ditemukan'}")
        MainFungsi.WriteToFile(file_path, f"Tanggal: {tanggal}")
        MainFungsi.WriteToFile(file_path, "Isi Cerita:")
        
        isi_berita = article.find_all("p") if article else []
        for p in isi_berita:
            text = p.get_text(strip=True)
            if text:
                MainFungsi.WriteToFile(file_path, text)
                print(text)
        
        MainFungsi.WriteToFile(file_path, "\n" + "="*55 + "\n")
    except Exception as e:
        print(f"Terjadi kesalahan saat mengambil detail dari {url}: {e}")

def MainScrapper(url, dir):
    try:
        MainFungsi.CreateDirectory(dir)
        file_path = f"{dir}/artikel.doc"

        if not MainFungsi.DoesFileExist(file_path):
            MainFungsi.CreateNewFile(file_path)

        sourceCode = requests.get(url)
        sourceCode.raise_for_status()
        sourceText = sourceCode.text
        soup = BeautifulSoup(sourceText, "html.parser")
        artikel = soup.find_all("article", {"class": "post"})

        if not artikel:
            print("Tidak ada artikel ditemukan.")
            return

        for dataArtikel in artikel:
            link_artikel = dataArtikel.find("a").get("href")
            if link_artikel:
                formatArtikel = f"URL: {link_artikel}\n"
                MainFungsi.WriteToFile(file_path, formatArtikel)
                print(f"Scraping: {link_artikel}")
                GetDetail(link_artikel, file_path)
            else:
                print("URL artikel tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan saat mengambil dari {url}: {e}")

MainScrapper("https://cerpenmu.com/category/cerpen-islami-religi/", "Cerpen Islami")