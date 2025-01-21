import requests
from bs4 import BeautifulSoup

def GetTotalPages():
    url = 'https://www.opencodez.com'
    res = requests.get(url)

    with open('res.html', 'w+', encoding='utf-8') as outfile:
        outfile.write(res.text)

    soup = BeautifulSoup(res.text, 'html.parser')
    pagination = soup.find_all('div', 'pagination')
    print(pagination)

GetTotalPages()
