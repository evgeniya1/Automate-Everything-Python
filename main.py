#web scraping
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

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

  driver = webdriver.Chrome(options=options) #service=service
  driver.get("http://automated.pythonanywhere.com")

  return driver


def main():
  driver = get_driver()
  element = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[1]")
  return element.text


print(main())