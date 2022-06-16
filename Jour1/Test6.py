from selenium.webdriver.chrome import webdriver
from selenium import  webdriver
h = webdriver.Chrome()
h.get("https://login.salesforce.com/")
h.maximize_window()