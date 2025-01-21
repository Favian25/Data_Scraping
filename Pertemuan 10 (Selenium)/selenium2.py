from selenium import webdriver
from bs4 import BeautifulSoup

URL = 'https://id.indeed.com/jobs?';
params = {
    'q': 'fresh graduate',
    'l': 'Surabaya'
};
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.186 Safari/537.36'};
driver = webdriver.Chrome();
fullURL = f"{URL}&q={params['q']}&l={params['l']}";
driver.get(fullURL);
html = driver.page_source;

# print(html);
soup = BeautifulSoup(html, 'html.parser')
data = soup.find_all('td', {'class':'resultContent'})

#print(data);
for i in range(len(data)):
    pekerjaan = data[i].find('h2', {'class':'jobTitle'});
    perusahaan = data[i].find('div', {'class':'company_location'});
    gaji = data[i].find('ul', {'class':'heading6 tapItem-gutter'});
    print(pekerjaan);
    print(perusahaan);
    print(gaji);
