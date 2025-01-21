from bs4 import BeautifulSoup
import requests

def Mainscrapper(url):
    sourceCode = requests.get(url)
    sourcetext = sourceCode.text
    soup = BeautifulSoup(sourcetext, 'html.parser')
    articles = soup.find_all('article', {'class': 'post'})
    
    listCerpen = []
    for article in articles:
        url = article.a.get("href")
        title = article.a.get("title")
        deskripsi = article.find('blockquote')
        print(title)
        
        articleFormat = {
            'url': url,
            'title': title,
            'deskripsi': deskripsi
        }
        listCerpen.append(articleFormat)
        print(listCerpen)
            
Mainscrapper('https://cerpenmu.com/')