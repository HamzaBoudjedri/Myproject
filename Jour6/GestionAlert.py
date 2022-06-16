import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
# Ouvrir le navigateur
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
# Accéder au site
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH,"//button[contains(text(),'Alert')]" ).click()
#Récuperer l'alarte
alertWindows = driver.switch_to.alert
print(alertWindows.text)

#cliquer sur le boutton Ok de l'alert (dismiss = cancel)
alertWindows.accept()


time.sleep(2)