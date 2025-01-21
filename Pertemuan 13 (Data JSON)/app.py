import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("base.html")

@app.route("/rates")
def Rates():
    source = requests.get('https://www.floatrates.com/daily/idr.json')
    jsonData = source.json()
    return render_template('rates.html', datas=jsonData.values())

if __name__ == "__main__":
    app.run(debug=True)