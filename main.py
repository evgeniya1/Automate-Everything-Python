from flask import Flask, jsonify

from bs4 import BeautifulSoup
import requests


def get_currency(in_currency, out_currency):
  url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
  content = requests.get(url).text
  soup = BeautifulSoup(content, "html.parser")
  rate_text = soup.find("span", class_="ccOutputRslt").get_text()
  rate = float(rate_text.split(' ')[0])
  return rate


app = Flask(__name__)


@app.route('/')
def home():
  return "<h1>Currency Rate API</h1> <p> Example URL: /api/v1/usd-eur</p>"


@app.route('/api/v1/<in_currency>-<out_currency>')
def api(in_currency, out_currency):

  rate = get_currency(in_currency, out_currency)

  rate_dict = {
      'input_currency': in_currency,
      'out_currency': out_currency,
      'rate': rate
  }

  return jsonify(rate_dict)


app.run(host="0.0.0.0")
