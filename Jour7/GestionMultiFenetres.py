import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
# Accéder au site
driver.get("https://opensource-demo.orangehrmlive.com/")
#
pageParenteId = driver.current_window_handle
print(pageParenteId)
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()

# Recupérer tous les Id des fenetres
listeDesIdsFenetres = driver.window_handles
pageParenteId = listeDesIdsFenetres[0]
pageFilsId = listeDesIdsFenetres [1]

print("id de page parent", pageParenteId)
print("id de page fils", pageFilsId)

# Récupéer l'url de la page fils, il faut switcher

driver.switch_to.window(pageFilsId)
url1 = driver.current_url
title1 = driver.title
print(url1)

# 2éme Approche

for winId in listeDesIdsFenetres:
    driver.switch_to.window(winId)
    if driver.title == title1:
        driver.close()

time.sleep(2)
driver.quit()