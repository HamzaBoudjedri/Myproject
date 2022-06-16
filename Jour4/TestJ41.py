import time

from  selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#driver = webdriver.Chrome()
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window();
# Optenir l'url de la page
driver.get("https://demo.nopcommerce.com/")
url_page= driver.current_url
print(url_page)
#Optenir title de la page
titre_page = driver.title
print(titre_page)
#Optenir le code source de la page
source_page = driver.page_source
print(source_page)
time.sleep(5)
driver.quit();