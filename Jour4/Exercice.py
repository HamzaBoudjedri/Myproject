#Cas de test
# lancer le lien https://www.google.ca
# saisir le mot "Selenium" dans la zone de recherche
# Cliquer sur la suggestion selenium webdriver

import time
from  selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#driver = webdriver.Chrome()
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window();
# Ouvrir le lien google.ca
driver.get("https://www.google.ca/")
#Saisir le mot recherché Selenium
mot_recherche=driver.find_element(By.NAME, "q")
mot_recherche.send_keys("Selenium")
time.sleep(5)
#Récupérer la liste des suggestions
suggestions = driver.find_elements(By.XPATH, "//form[@action='/search' and @role='search']//ul[@role='listbox']//li//span")
print(len(suggestions))
#parcourir la liste des suggestions
#Faire un clique sur l'element de la liste si egale à "selenium webdriver"
for element in suggestions:
    print(element.text)
    if element.text.__eq__('selenium webdriver'):
        element.click()
        break
time.sleep(5)
