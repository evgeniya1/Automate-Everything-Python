#web scraping
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime as dt
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

  driver = webdriver.Chrome(options=options)  #service=service ##local ide
  driver.get("http://automated.pythonanywhere.com/login/")

  return driver


def clean_text(text):
  return float(text.split(": ")[1])


def write_file(text):
  filename = dt.now().strftime('%Y-%m-%d.%H-%M-%S')
  print(f"\n*** write {filename}.txt ***\n")
  with open(f"{filename}.txt", "w") as file:
    file.write(text)


def main():

  driver = get_driver()
  driver.find_element(by=By.ID, value="id_username").send_keys("automated")
  time.sleep(2)
  driver.find_element(by=By.ID,
                      value="id_password").send_keys("automatedautomated",
                                                     Keys.RETURN)
  print(driver.current_url)
  time.sleep(2)

  ##click to HOME
  driver.find_element(by=By.XPATH, value="/html/body/nav/div/a").click()
  print(driver.current_url)
  time.sleep(2)

  for i in range(2):
    ## get dynamic number reading
    element_dynamic = driver.find_element(By.XPATH,
                                          value="/html/body/div[1]/div/h1[2]")
    #"/html/body/div/h1[2]/div" - from dashboard page
    temperature = str(clean_text(element_dynamic.text))
    write_file(temperature)
    time.sleep(2)


if __name__ == "__main__":
  main()
