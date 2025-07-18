from bs4 import BeautifulSoup
import requests
import fungsi

def main_scraper(url, directory):
    fungsi.create_directory(directory)
    file_path = directory + "/artikel.txt"
    
    if not fungsi.does_file_exist(file_path):
        fungsi.create_new_file(file_path)
    
    sumber_kode = requests.get(url)
    sumber_text = sumber_kode.text
    soup = BeautifulSoup(sumber_text, "html.parser")
    articles = soup.find_all("div", {'class': 'blog card h-100'})
    
    for article in articles:
        link = article.a['href']
        title = article.a.text.strip()
        
        article_format = f"URL : {link}\nTitle : {title}\n"
        fungsi.write_to_file(file_path, article_format)

        get_details(link, file_path)

def get_details(url, file_path):
    source_code = requests.get(url)
    source_text = source_code.text
    soup = BeautifulSoup(source_text, "html.parser")

    div_entry = soup.find("div", {"class": "card-text"})
    if div_entry is None:
        fungsi.write_to_file(file_path, "Tidak ada konten ditemukan.\n===============\n\n")
        return

    paragraf = div_entry.find_all("p")

    fungsi.write_to_file(file_path, "Detail Artikel:\n")

    for p in paragraf:
        text = p.get_text().strip()
        if text:
            print(text)
            fungsi.write_to_file(file_path, text)

    fungsi.write_to_file(file_path, "\n===============\n")
        
main_scraper("https://bwi24jam.co.id/kategori/detail/pariwisata", "Hasil")