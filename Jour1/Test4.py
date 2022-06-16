from selenium import  webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager


# 1) Ouvrir le navigateur(chrome/firefox/Edge)
driver = webdriver.Chrome();
# 2) Naviguer vers l'url
driver.get("https://login.salesforce.com/")
driver.maximize_window()
# 3) Entrer username (Admin)
driver.find_element(By.ID, "username").send_keys("Hamza")
# 4) Entrer password (admin123)
driver.find_element(By.ID, "password").send_keys("admin123")
# 5) Cliquer sur le bouton Login
driver.find_element(By.ID, "Login").click()
# 6) recuperer le titre de la page(titre actuel)
act_title =  driver.title
# 7) Verifier le titre de la page: OrangeHRM  (attendu)
exp_title = "Connexion | Salesforce"
if act_title == exp_title:
    print("Le test Login  est passed")
else:
    print("Le test Login  est failed")
time.sleep(4)
# 8) Fermer le navigateur
driver.close()