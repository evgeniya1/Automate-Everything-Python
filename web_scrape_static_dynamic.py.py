#web scraping
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

#for local IDE
#from selenium.webdriver.chrome.service import Service
#service = Service("path to chrome driver")


def get_driver():
  #set options to make browsing easier
  options = Options()
  options.add_argument("disable-infobar")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)  #service=service
  driver.get("http://automated.pythonanywhere.com")

  return driver


def clean_text(text):
  return float(text.split(": ")[1])


def main():
  driver = get_driver()
  time.sleep(2)
  element_static = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[1]")
  element_dynamic = driver.find_element(By.XPATH,"/html/body/div[1]/div/h1[2]")

  return element_static.text, clean_text(element_dynamic.text)


print(main())
