from selenium import webdriver

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
print(html);
