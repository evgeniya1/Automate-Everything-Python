from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QComboBox

from bs4 import BeautifulSoup
import requests


def get_currency(in_currency, out_currency):
  url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
  content = requests.get(url).text
  soup = BeautifulSoup(content, "html.parser")
  rate_text = soup.find("span", class_="ccOutputRslt").get_text()
  rate = float(rate_text.split(' ')[0])
  return rate


def show_currency():
  input_text = text.text()
  in_cur = in_combo.currentText()
  out_cur = out_combo.currentText()

  output = round(
      float(input_text) *
      get_currency(in_currency=in_cur, out_currency=out_cur), 2)
  message = f"{input_text} {in_cur} is {output} {out_cur}"
  output_label.setText(message)


app = QApplication([])
window = QWidget()
window.setWindowTitle("Currency Converter")

layout = QVBoxLayout()

currencies = ['USD', 'EUR', 'INR', "RUB"]

in_combo = QComboBox()
in_combo.addItems(currencies)
layout.addWidget(in_combo)

out_combo = QComboBox()
out_combo.addItems(currencies)
layout.addWidget(out_combo)

text = QLineEdit()
layout.addWidget(text)

btn = QPushButton('Convert')
layout.addWidget(btn)

btn.clicked.connect(show_currency)

output_label = QLabel("")
layout.addWidget(output_label)

window.setLayout(layout)
window.show()

app.exec()
