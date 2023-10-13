from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://google.com")

from selenium.webdriver.common.by import By

google_text = driver.find_element(By.CLASS_NAME, "MV3Tnb").text

print(google_text)

