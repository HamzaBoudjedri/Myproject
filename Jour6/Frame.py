import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
# Accéder au site
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.switch_to.frame("packageListFrame")
time.sleep(2)
driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()

driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")
#driver.find_element(By.LINK_TEXT,"WebDriver").click()
driver.find_element(By.XPATH,"/html/body/main/div/section[1]/ul/li[14]/a/span").click()
time.sleep(2)
driver.quit()