from bs4 import BeautifulSoup
import requests

def scrape_antaranews():
    url = 'https://www.antaranews.com/ekonomi'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    main_title = soup.find('h1', class_='border_section')
    print("Judul Utama: ", main_title.text.strip())

    titles = soup.find_all('h2', class_='post_title post_title_medium')
    for title in titles:
        print("Judul Artikel:", title.text.strip())

    links = soup.find_all('a')
    for link in links:
        print("Link Artikel:", link.get('href'))

    dates = soup.find_all('span', class_='text-secondary')
    for date in dates:
        print("Tanggal Artikel:", date.text.strip())

    contents = soup.find_all('p')
    for content in contents:
        print("Isi Artikel:", content.text.strip())

scrape_antaranews()