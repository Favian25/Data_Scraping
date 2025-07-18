from bs4 import BeautifulSoup
import requests
import fungsi

def main_scrapper(url, directory):
    fungsi.create_directory(directory)
    sumberCode = requests.get(url)
    sumberText = sumberCode.text
    soup = BeautifulSoup(sumberText, "html.parser")
    articles = soup.find_all("div", {'class':'col-md-6 mb-4'})
    
    for article in articles:
        url = article.a['href']
        judul = article.h5.text.strip()
        meta_div = article.find("div", class_="post-meta")
        tanggal_raw = meta_div.find("i").next_sibling
        tanggal = tanggal_raw.strip()
        ringkasan = article.find("div", class_="card-text d-md-block d-none").text.strip()
        
        print("URL :", url)
        print("Judul :", judul)
        print("Tanggal :", tanggal)
        print("Ringkasan :", ringkasan)
        print()
        
        article_format = f"URL : {url}\nJudul : {judul}\nTanggal : {tanggal}\nRingkasan : {ringkasan}\n"
        
        if fungsi.does_file_exist(directory + "/artikel.doc") is False:
            fungsi.create_new_file(directory + "/artikel.doc")
            
        fungsi.write_to_file(directory + "/artikel.doc", article_format)

    
main_scrapper("https://bwi24jam.co.id/berita", "Hasil")