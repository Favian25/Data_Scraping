from bs4 import BeautifulSoup
import requests

def Mainscrapper(url):
    sourceCode = requests.get(url)
    sourcetext = sourceCode.text
    soup = BeautifulSoup(sourcetext, 'html.parser')
    articles = soup.find_all('article', {'class': 'post'})
    
    for article in articles:
        articlesFormat = "URL:" + article.a.get("href") + "\n" + "Judul: " + article.getText() + "\n"
        print(articlesFormat)
    
Mainscrapper('https://cerpenmu.com/')