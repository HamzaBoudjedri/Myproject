import time

from  selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#driver = webdriver.Chrome()
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window();
# Optenir l'url de la page
driver.get("https://demo.nopcommerce.com/")
driver.get("https://www.google.com")
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.refresh()
time.sleep(3)