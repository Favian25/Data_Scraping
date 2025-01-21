from bs4 import BeautifulSoup
import requests

def Mainscrapper(url):
    sourceCode = requests.get(url)
    sourcetext = sourceCode.text
    soup = BeautifulSoup(sourcetext, 'html.parser')
    articles = soup.find_all('article', {'class': 'post'})
    
    print(articles)
    
Mainscrapper('https://cerpenmu.com/')