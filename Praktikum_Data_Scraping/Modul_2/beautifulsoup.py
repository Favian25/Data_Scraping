from bs4 import BeautifulSoup
import os

html = """
        <div>Ini adalah paragraf pertama div</div>
        <p>Ini adalah paragraf dengan sintag p</p>
        <div class='bold'>Ini adalah paragraf kedua div</div>"""

soup = BeautifulSoup(html, "html.parser")

print(soup.div)
print(soup.find_all("div"))
print(soup.find_all("div")[1])
print(soup.find_all("div", {'class' :'bold'}))
