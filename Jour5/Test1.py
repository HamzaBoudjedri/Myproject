import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.opencart.com/index.php?route=account/register")
liste = driver.find_element(By.ID,'input-country')
contry = Select(liste)
contry.select_by_visible_text("Algeria")
# On peut aussi autres options de selection
time.sleep(1)
# Récuperer tous les element de la liste des options
all_option = contry.options
nombre_total_options = len(all_option)
print('le nombre total des options est' , nombre_total_options)

# Afficher la liste des options

# for element in all_option:
#     print(element.text)

for opt in all_option:
    if opt.text == "Canada":
        opt.click()
        break
time.sleep(4)