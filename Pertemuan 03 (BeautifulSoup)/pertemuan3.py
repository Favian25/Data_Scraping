from bs4 import BeautifulSoup
import os
import requests

isiHTML = "<div>Ini isi div</div>";
soup = BeautifulSoup(isiHTML, "html.parser");
print(soup.div.text);

isiHTML = "<div>Ini adalah dokumen div</div><p>Ini adalah paragraf halaman luar</p>";
soup = BeautifulSoup(isiHTML, "html.parser");
print(soup.p.text);

isiHTML = """
        <div>Ini adalah paragraf div ke-1</div>
        <p>Ini adalah paragraf dengan syntaks p</p>
        <div>Ini adalah paragraf div ke-2</div>
        """;

soup = BeautifulSoup(isiHTML, "html.parser");
print(soup);
print(soup.div);
print(soup.findAll("div"));
print(soup.findAll("div")[1]);
print(soup.findAll("div", {'class':'bold'}));
print(soup.findAll("P", {'id', 'para'}));

isiHTML = """
        <div id='d1' class='wide'>
            <p id='p1'>Isi paragraf 1</p>
            <img src=""/>
            <a id='a1'></a>
        </div>
        <div id='d2' class='small'>
            <p id='p2'>Isi Paragraf 2</p>
            <img src=""/>
            <a id='a2'></a>
        </div>
        """;

soup = BeautifulSoup(isiHTML, "html.parser");
print(soup.findAll("div", {'id':'d2'})[0].p);

url = "https://www.wikipedia.org";
response = requests.get(url);

if response.status_code == 200:
    pageContent = response.content;

