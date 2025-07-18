from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    url = 'https://www.liputan6.com/news'
    data = main_scrapper(url)
    return render_template('index.html', articles=data)

def main_scrapper(url):
    sumber_code = requests.get(url)
    sumber_text = sumber_code.text
    soup = BeautifulSoup(sumber_text, 'html.parser')
    articles = soup.find_all('article', attrs={'class': 'articles--iridescent-list--item'})

    hasil = []

    for item in articles:
        title_tag = item.find('h4', class_='articles--iridescent-list--text-item__title')
        a_tag = title_tag.find('a') if title_tag else None
        img_tag = item.find('img')
        img_url = img_tag.get('data-src') if img_tag else None

        if a_tag:
            hasil.append({
                'title': a_tag.get('title'),
                'url': a_tag.get('href'),
                'img': img_url
            })

    return hasil

if __name__ == '__main__':
    app.run(debug=True)