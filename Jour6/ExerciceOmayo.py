import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
# Ouvrir le navigateur
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
# Accéder au site
driver.get("http://omayo.blogspot.com/")
# Récupérer la liste des voitures
liste = driver.find_element(By.ID,'multiselect1')
voiture = Select(liste)
# Faire une selection multiple
voiture.select_by_visible_text("Volvo")
voiture.select_by_visible_text("Swift")
voiture.select_by_visible_text("Hyundai")
# Récupérer la liste des documents
Listedoc = driver.find_element(By.ID,'drop1')
documets = Select(Listedoc)
all_options = documets.options
# Calculer le nombre des documents
total_options = len(all_options)
#afficher le nombre des documents
print(total_options)
time.sleep(2)
Listedoc.click()
for element in all_options:
    if element.text.__eq__('doc 1'):
        element.click()
        break
time.sleep(2)
#Faire une déselection
voiture.deselect_all()
time.sleep(3)
