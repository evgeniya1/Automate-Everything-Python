from bs4 import BeautifulSoup
import requests


def get_currency(in_currency, out_currency):
  url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
  content = requests.get(url).text
  soup = BeautifulSoup(content, "html.parser")
  rate_text = soup.find("span", class_="ccOutputRslt").get_text()
  rate = float(rate_text.split(' ')[0])
  return rate


current_rate = get_currency("USD", "RUB")

print(current_rate)
