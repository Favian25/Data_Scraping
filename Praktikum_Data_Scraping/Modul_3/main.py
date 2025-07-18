from bs4 import BeautifulSoup
import requests
import fungsi

def main_scrapper(url, directory):
    fungsi.create_directory(directory)
    sumber_kode = requests.get(url)
    sumber_text = sumber_kode.text
    soup = BeautifulSoup(sumber_text, "html.parser")
    articles = soup.find_all("div", {'class':'section-post card post-list'})
    
    for article in articles:
        print("URL :" + article.a['href'])
        print("Judul :" + article.text) 
        print()
        article_format = "URL :" + article.a['href'] + "\n" + "title :" + article.text + "\n\n"
        
        if fungsi.does_file_exist(directory + "/artikel.doc") is False:
            fungsi.create_new_file(directory + "/artikel.doc")
            
        fungsi.write_to_file(directory + "/artikel.doc", article_format)
        print(article_format)
    
main_scrapper("https://bwi24jam.co.id/", "Hasil")
