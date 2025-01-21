from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/detik-popular")
def DetikPopular():
    htmlDoc = requests.get("https://www.bola.com/tag/bolacom")
    soup = BeautifulSoup(htmlDoc.text, "html.parser")
    popularArea = soup.find(attrs={'class': 'articles--iridescent-list'})

    images = popularArea.find_all(attrs={'class': 'articles--iridescent-list--item articles--iridescent-list--text-item'})

    return render_template("populer.html", gambar=images)

if __name__ == "__main__":
    app.run(debug=True)