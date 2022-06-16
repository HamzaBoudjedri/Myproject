#Test Case
#----------------
# 1) Ouvrir le navigateur(chrome/firefox/Edge)
# 2) Naviguer vers l'url https://login.salesforce.com/## 3) Entrer username (Admin)
# 4) Entrer password (admin123)
# 5) Cliquer sur le bouton Login
# 6) recuperer le titre de la page(titre actuel)
# 7) Verifier le titre de la page: Login | SalesForce  (attendu)
# 8) Fermer le navigateur
import chromedriver_binary
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By
#service_obj = Service("F:\\Formation SQL\\Session3\\webdriver\\chromedriver.exe")
# 1) Ouvrir le navigateur(chrome/firefox/Edge)
#driver = webdriver.Chrome(service=service_obj)
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://login.salesforce.com/")
driver.maximize_window()
driver.find_element(By.ID, "username").send_keys("Admin")
driver.find_element(By.ID, "password").send_keys("admin123")
driver.find_element(By.ID, "Login").click()
act_title =  driver.title
print(act_title)
exp_title = "Connexion | Salesforce"
exp_msg_error=driver.find_element(By.ID,"error").text
print("le message d'erreur est: " + exp_msg_error)
if act_title == exp_title:
    print("Le test Login  est passed")
    print("le titre de la page est : "+act_title)
else:
    print("Le test Login  est failed")
time.sleep(4)
